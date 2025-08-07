# ObjectDB.search ne remontent pas d'enregistrement

**URL:** https://community.simplicite.io/t/8842

## Question
### Request description

Bonjour, 
je tente de parcourir tous les enregistrements d'un objet en utilisant la méthode search de `ObjectDB` pour y effectuer un `validateAndSave()` de `BusinessObjectTool`.(Reprise de données)

Quand je teste, la taille de la liste est toujours 0 alors que `object.getCount()` me retourne le nombre attendu.

Je me suis basé sur [la doc](https://docs.simplicite.io/docs/core/basic-code-examples#searching). Je me demande si mon implémentation contient une erreur qui m'échappe ?

```
ObjectDB object = g.getTmpObject(item);
synchronized (object.getLock()) {
	object.resetFilters();
	List<String[]> recordList = object.search(false);
	AppLog.info("recordList.size total records = "+recordList.size(), g);
	AppLog.info("getCount total records = "+ object.getCount(), g);
	}
```

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.45
BuiltOn=2024-08-18 13:52
Git=5.3/afbdc085b6d18cb2051762fd69ca60a5a234e042
Encoding=UTF-8
EndpointIP=100.88.206.32
EndpointURL=http://bca-68521-app-5cf7bf84d4-7wtqz:8080
TimeZone=Europe/Paris
SystemDate=2024-10-04 15:02:16

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://bcsi-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=2
TotalUsers=8733
EnabledUsers=1443
LastLoginDate=2024-10-04 15:00:00

[Server]
ServerInfo=Apache Tomcat/9.0.93
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=6.1.90+
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.12
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.12+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=435825
HeapSize=1077248
HeapMaxSize=1581056
TotalFreeSize=939633

[Cache]
ObjectCache=316
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=1
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
VendorName=mysql
ProductName=MySQL
ProductVersion=5.7.44-google-log
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-9.0.0 (Revision: e0e8e3461e5257ba4aa19e6b3614a2685b298947)
DBDate=2024-10-04 13:02:16
DBDateOffset=-7200
DBPatchLevel=5;P03;a4067bb64c54435ec5a9b948a3aa16b9;45
UsingBLOBs=true

[Healthcheck]
Date=2024-10-04 15:02:16
ElapsedTime=24
```
[/details]

[details="Simplicité logs"]
```text
Event: getCount total records = 493
Event :recordList.size total records = 0
```
[/details]

## Answer
Effectivement en 5.3, la méthode lambda ne prend pas de pageNum en second paramètre.
Ca a été ajouté en V6 pour savoir calculer un row index global = 
`maxRowsPerPage * pageNum + rows index`

On va préciser la documentation pour la 5.3 :

```java
int maxRowsPerPage = 50;
object.search(true, maxRowsPerPage, (rows) -> {
	for (String[] row : rows) {
		o.setValues(row, true);
		// ...
	}
});
```

https://docs.simplicite.io/docs/core/basic-code-examples#java-7
