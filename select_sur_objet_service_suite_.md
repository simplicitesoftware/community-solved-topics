# Select sur Objet service (suite)

**URL:** https://community.simplicite.io/t/10095

## Question
### Request description

Bonjour,

Après avoir migré en 6.2, je rencontre toujours des soucis avec l'utilisation d'une action en ligne sur objet Service. Cela fait suite à [ce ticket](https://community.simplicite.io/t/utilisation-des-valeurs-dune-ligne-dun-objet-service-dans-une-action/9469/14).

Mon problème est qu'à l'appel de l'action, les valeurs de mon instance d'objet sont ceux de la dernière ligne de la liste, et non celle sur laquelle j'ai cliqué.

Exemple :
Je clique sur l'action pour l'**IRN-79643**, mais les valeurs utilisées sont celles de l'**IRN-79648**.

![image|634x500](upload://3a3zrc9BoEfgl79zTwAFYNKdu9C.png)

J'ai essayé de surcharger le selectService pour valoriser correctement la ligne, mais cela génère une erreur : **il semble que dans la variable passée rowId, j'ai le nom de l'action au lieu du rowId.**

```
	@Override
	public boolean selectService(String rowId, boolean copy) {
		AppLog.info("selectService " + rowId + " IRN " + getFieldValue("rciSnaIrn"), getGrant());
		setValues(getCurrentList().get(Integer.parseInt(rowId)));
		return true;
	}
```
Les logs :

```
2025-06-04 08:34:42,754|SIMPLICITE|INFO||http://simplicite-dev-5fc8c64d94-t584s:8080||INFO|testRespApp|com.simplicite.objects.RCIB.RciSnowApplication|selectService||Event: selectService createApp IRN IRN-79648
2025-06-04 08:34:42,754|SIMPLICITE|ERROR||http://simplicite-dev-5fc8c64d94-t584s:8080||ECORED0001|system|com.simplicite.util.engine.ObjectDirect|select||Error RciSnowApplication
java.lang.NumberFormatException: For input string: "createApp"
```

Ma question est la suivante : comment récupérer les valeurs de la bonne ligne dans mon action, sans devoir réappeler mon API inutilement ?

Mon code ci-dessous

```
	@Override
	public boolean selectService(String rowId, boolean copy) {
		AppLog.info("selectService " + rowId + " IRN " + getFieldValue("rciSnaIrn"), getGrant());
		setValues(getCurrentList().get(Integer.parseInt(rowId)));
		return true;
	}
	
	@Override
	public long countService() {
		
		String apiFilters = formatFilters();
		long snowCount = RciSnow.countSnowAppWithLimit(null, apiFilters, getGrant());
		getGrant().setParameter("RCI_SNOW_COUNT",snowCount);
		return snowCount;
	}

	@Override
	public List<String[]> searchService(boolean pagine) {

		AppLog.info("Entering searchService pagine " + pagine + "getSearchLimit() " + Integer.toString(getMaxRows()) + " getCurrentPage() " + Integer.toString(getCurrentPage()), getGrant());

		List<String[]> snowApps = new ArrayList<>();

		try
		{
			String apiFilters = formatFilters(), appExistsFilter = "";
			
			String limit = "", page = "";
			
			if (getField("rciSnaAppExists").isFiltered())
				appExistsFilter = getFieldFilter("rciSnaAppExists");
			
			if (appExistsFilter.isEmpty())
			{
				limit = Integer.toString(getMaxRows());
				page = Integer.toString(getCurrentPage());
				//setLimit(true);
			}
			else
			{
				limit = getGrant().getParameter("RCI_SNOW_COUNT");
				page = "0";
				//setLimit(false);
			}
			
			String res = RciSnow.reqSnowAppWithLimit(null, limit, page, apiFilters, getGrant());
			
			if (res != null)
			{
				JSONObject resJSON = new JSONObject(res);
				
				if (resJSON != null && resJSON.getJSONArray("result") != null && resJSON.getJSONArray("result").length() > 0)
				{

					JSONArray appsJSON = resJSON.getJSONArray("result");
					AppLog.info(getClass(), "appsJSON : ", appsJSON.length() + " " + appsJSON.toString(), getGrant());
					
					String key = "";
				    String snaField = "";
				    String snowField = "";
					
					for (int j = 0 ; j < appsJSON.length() ; j++)
					{
						JSONObject appJSON = appsJSON.getJSONObject(j);
						AppLog.info(getClass(), "appJSON : ", Integer.toString(j) + " " +  appJSON.toString(), getGrant());
						AppLog.info(getClass(), "IRN : ", appJSON.getString("name") + "size " + getFields().size(), getGrant());

						String[] snowApp = new String[getFields().size()];
						
						String irn = appJSON.getString("name");
						snowApp[getFieldIndex("rciSnaIrn")] = irn;
						
						Boolean appExists = appExists(irn);
						snowApp[getFieldIndex("rciSnaAppExists")] = Boolean.toString(appExists);
						snowApp[0] = Integer.toString(j + 1);
						AppLog.info(getClass(), "snowApp rowid 1 : ", snowApp[0], getGrant());
						if (appExistsFilter.isEmpty() || ((appExistsFilter.equals("1") && appExists) || (appExistsFilter.equals("0") && !appExists)))
						{
							for (Map.Entry<String, String> entry : RciSnow.CMDB_EAR_FIELDS.entrySet()) {
											
							    key = entry.getKey();
							    snaField = "rciSna" + key;
							    snowField = entry.getValue();
							    
							    if (getField(snaField, false) != null)
							    	snowApp[getFieldIndex(snaField)] = RciSnow.cmdbToEar(snowField, appJSON);
							}
													AppLog.info(getClass(), "snowApp rowid 2 : ", snowApp[0], getGrant());

							snowApps.add(snowApp);
							AppLog.info(getClass(), "snowApps : ", snowApps.get(0)[0], getGrant());
						}

					}
				}
			}
			
			
		}
		catch (Exception e) {
			AppLog.error(e, getGrant());
		}

		return snowApps;
	}
```

Et la version

[Platform]
Status=OK
Version=6.2.10
BuiltOn=2025-05-23 10:17
Git=6.2/db71f45b7b47f1aea2d669dc5b22c5369ec75d92

Merci d'avance pour votre aide !
Emmanuelle

## Answer
- il faut faire un setCurrentList dans le searchServicepour garder la page en mémoire et s'en servir dans le selectService par défaut
- debugger l'intégralité du contenu des tableaux issus du search ?
- est-ce conforme à la définition de l'objet : custom rowID ? attributs ?
- c'est quoi `createApp` au juste ? une donnée, un nom d'action (du coup mal nommée) ?...
