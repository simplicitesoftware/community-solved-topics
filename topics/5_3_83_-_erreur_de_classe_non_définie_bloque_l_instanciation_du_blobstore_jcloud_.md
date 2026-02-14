# 5.3.83 - erreur de classe non définie bloque l’instanciation du blobStore (jcloud)

**URL:** https://community.simplicite.io/t/11572

## Question
### Request description

*Suite à l’upgrade en 5.3.83, j’ai une régression sur la connectivité à nos bockets GCS via la lib intégrée jcloud.* Une erreur de classe non définie bloque l’instanciation du blobStore hébergeant la connexion à la bucket.

Le même code fonctionnait avant l’upgrade (il s’agit d’un traitement d’export quotidien).

```
2026-02-10 22:08:28,865|SIMPLICITE|ERROR||http://bca-68521-cron-7f476dcbfd-9g54r:8080||ERROR|system|com.simplicite.util.ObjectHooks|postLoad||Event: Implementation error in the postLoad hook of object GcsTransit
    java.lang.NoClassDefFoundError: Could not initialize class com.google.inject.Scopes
     at com.google.inject.internal.InjectorShell$RootModule.configure(InjectorShell.java:340)
     at com.google.inject.spi.Elements$RecordingBinder.install(Elements.java:426)
     at com.google.inject.spi.Elements.getElements(Elements.java:113)
     at com.google.inject.internal.InjectorShell$Builder.build(InjectorShell.java:160)
     at com.google.inject.internal.InternalInjectorCreator.build(InternalInjectorCreator.java:107)
     at com.google.inject.Guice.createInjector(Guice.java:87)
     at org.jclouds.ContextBuilder.buildInjector(ContextBuilder.java:412)
     at org.jclouds.ContextBuilder.buildInjector(ContextBuilder.java:329)
     at org.jclouds.ContextBuilder.buildView(ContextBuilder.java:622)
     at org.jclouds.ContextBuilder.buildView(ContextBuilder.java:602)
     at com.simplicite.objects.RenaultGCS.GcsDocument.postLoad(GcsDocument.java:80)

```

### Voici le code en question :

```
public class GcsDocument extends ObjectService {
	private static final long serialVersionUID = 1L;

	protected transient JSONObject config = null;

	private BlobStoreContext blobStoreContext = null;
	protected BlobStore blobStore = null;
	private ApiMetadata apiMetadata = null;
	private Supplier<Credentials> credentialSupplier = null;

	public static final Map<String, ApiMetadata> allApis = Maps.uniqueIndex(Apis.viewableAs(BlobStoreContext.class), Apis.idFunction());
	public static final Map<String, ProviderMetadata> appProviders = Maps.uniqueIndex(Providers.viewableAs(BlobStoreContext.class), Providers.idFunction());
	public static final Set<String> allKeys = ImmutableSet.copyOf(Iterables.concat(appProviders.keySet(), allApis.keySet()));

	@Override
	public void postLoad() {
		try {
			if (this.config == null) {
				try {
					this.config = merge(
						new JSONObject()
							.put("provider", "google-cloud-storage")
							.put("bucket", rlog(getGrant().getParameter("GCS_BUCKET_NAME", System.getenv("GCS_BUCKET_NAME")), "postLoad", "GCS_BUCKET_NAME as bucket", this, 1))
							.put("identity", rlog(new JSONObject(getGrant().getParameter("GCS_BUCKET_CREDENTIALS", System.getenv("GCS_BUCKET_CREDENTIALS"))).getString("client_email"), "postLoad", "GCS_BUCKET_CREDENTIALS.client_email as identity", this, 1))
							.put("credentials", rlog(getGrant().getParameter("GCS_BUCKET_CREDENTIALS", System.getenv("GCS_BUCKET_CREDENTIALS")), "postLoad", "GCS_BUCKET_CREDENTIALS as credentials", this, 1)),
						new JSONObject(rlog(this.getSearchSpec(), "postLoad", "getSearchSpec", this, 1))
					);
					this.credentialSupplier = new GoogleCredentialsFromJson(this.config.getString("credentials"));
					// Properties overrides = new Properties();
					this.blobStoreContext = ContextBuilder.newBuilder(this.config.getString("provider"))
						.credentials(this.config.getString("identity"), credentialSupplier.get().credential)
						.buildView(BlobStoreContext.class);
					this.apiMetadata = this.blobStoreContext.unwrap().getProviderMetadata().getApiMetadata();
					this.blobStore = this.blobStoreContext.getBlobStore();
				}
				catch (Exception e) {
					this.config = null;
					this.blobStoreContext = null;
					this.blobStore = null;
					throw e;
				}
			}
			this.setLimit(false);
			this.setSearchLimit((int)this.getLimit());
		}
		catch (Exception e) {
			AppLog.error("EXCEPTION CAUGHT while loading google-cloud-storage service configuration", (Throwable)e, this.getGrant());
		}
		try {
			ByteSource payload = ByteSource.wrap("".getBytes(Charsets.UTF_8));
			Blob blob = this.blobStore.blobBuilder(this.config.getString("root")).payload(payload).contentLength(payload.size()).build();
			this.blobStore.putBlob(this.config.getString("bucket"), blob);
		} catch (IOException e) {
			error("postLoad", "Cannot create ROOT FOLDER "+this.config.getString("root"), e, this);
		}
	}
...
```

/health

```
[Platform]
Status=OK
Version=5.3.83
BuiltOn=2026-02-06 10:26
Git=5.3/462dc56d02def0b3529e9311c484fa229e1a3c01
Encoding=UTF-8
EndpointIP=100.88.18.238
EndpointURL=http://bca-68521-cron-7f476dcbfd-9g54r:8080
TimeZone=Europe/Paris
SystemDate=2026-02-10 22:18:23
```

## Answer
La 5.3.84 est releasée (le tag temporaire `5-preview` a été supprimé)
