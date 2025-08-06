# PreSearchIndex non pris en compte

**URL:** https://community.simplicite.io/t/8949

## Question
### Request description

Bonjour, ce sujet fait suite à ce [topic](https://community.simplicite.io/t/indexcore-searchindex-avec-caracteres-speciaux/8735/21?u=jordanso) sur lequel j'ai zappé de rebondir. 
Pour répondre à François, non je n'ai malheureusement pas la possibilité de faire une montée de version de MySql.

Cependant, j'avais réussi à gérer les différents PlatformHooks grâce à des paramétres. (cf https://community.simplicite.io/t/orchestration-multi-platformhooks/8792/8?u=jordanso)

Depuis hier alors que rien n'a changé (à ma connaissance), cela ne fonctionne plus. Les modifications faite sur le texte en input n'était plus "pris en compte" pour la recherche.
Pour débugger, j'ai fusionné mes platformhooks pour n'en garder qu'un mais le comportement reste le même. 

Méthode :
```
@Override
	public String preSearchIndex(Grant g, java.lang.String search) {
		AppLog.error("Called !1", null, g);
		String modifiedSearch = handleSpecialCharInPhraseSearch(search);
		AppLog.error("return value is : "+ modifiedSearch, null, g);
		return modifiedSearch;
	}
```
On peut constater dans les logs ci-dessous que la substitution n'est pas faite. Donc on tombre dans l'erreur de syntaxe ( wildcard et les guillements) de MySql 5. 
[details="Simplicité logs"]
```text
2024-10-24 09:08:52,605|SIMPLICITE|ERROR||http://bca-68521-app-86c7c4546f-pmk2l:8080||ECOREDB001|system|com.simplicite.util.engine.GrantManager|query||Error SQL query: SELECT idx_key, idx_object, idx_row_id, idx_ukey, idx_all, MATCH (idx_ukey, idx_all) AGAINST ('"NOM PRENOM NOM" *' IN BOOLEAN MODE) AS score FROM m_index WHERE MATCH (idx_ukey, idx_all) AGAINST ('"NOM PRENOM NOM" *' IN BOOLEAN MODE) AND idx_object in ('BCSIAppPerson') ORDER BY score desc, idx_ukey LIMIT 0,100000
    java.sql.SQLSyntaxErrorException: syntax error, unexpected $end, expecting FTS_TERM or FTS_NUMB or '*'
     at com.mysql.cj.jdbc.exceptions.SQLError.createSQLException(SQLError.java:112)
     at com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping.translateException(SQLExceptionsMapping.java:114)
     at com.mysql.cj.jdbc.ClientPreparedStatement.executeInternal(ClientPreparedStatement.java:987)
     at com.mysql.cj.jdbc.ClientPreparedStatement.executeQuery(ClientPreparedStatement.java:1055)
     at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:123)
     at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:123)
     at com.simplicite.util.engine.DBAccess.query(DBAccess.java:661)
     at com.simplicite.util.engine.DBAccess.query(DBAccess.java:509)
     at com.simplicite.util.engine.GrantDirect.query(GrantDirect.java:89)
     at com.simplicite.util.Grant.query(Grant.java:1086)
     at com.simplicite.util.Grant.query(Grant.java:1039)
     at com.simplicite.util.tools.IndexSQLTool.doSearchMySQL(IndexSQLTool.java:711)
     at com.simplicite.util.tools.IndexSQLTool.doSearch(IndexSQLTool.java:597)
     at com.simplicite.util.tools.IndexSQLTool.search(IndexSQLTool.java:568)
     at com.simplicite.util.tools.IndexCore.searchIndex(IndexCore.java:140)
     at com.simplicite.util.tools.IndexCore.searchIndex(IndexCore.java:91)
     ...
2024-10-24 09:08:52,551|SIMPLICITE|ERROR||http://bca-68521-app-86c7c4546f-pmk2l:8080||ERROR|p125801|com.simplicite.commons.RenaultGroup.PlatformHooks|preSearchIndex||Evénement: return value is : +NOM +PRENOM
2024-10-24 09:08:52,551|SIMPLICITE|ERROR||http://bca-68521-app-86c7c4546f-pmk2l:8080||ERROR|p125801|com.simplicite.commons.RenaultGroup.PlatformHooks|preSearchIndex||Evénement: Called !1
```
[/details]

Auriez-vous une idée de la root cause ou une idée de debug supplémentaire sur ce cas? 

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.45
BuiltOn=2024-08-18 13:52
Git=5.3/afbdc085b6d18cb2051762fd69ca60a5a234e042
Encoding=UTF-8
EndpointIP=100.88.79.109
EndpointURL=http://bca-68521-app-86c7c4546f-pmk2l:8080
TimeZone=Europe/Paris
SystemDate=2024-10-24 09:23:49

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://bcsi-app.ext.gke2.int.gcp.renault.com
ActiveSessions=1
TotalUsers=9014
EnabledUsers=1204
LastLoginDate=2024-10-24 09:20:05

[Server]
ServerInfo=Apache Tomcat/9.0.93
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=6.1.100+
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.12
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.12+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=265695
HeapSize=604160
HeapMaxSize=2068480
TotalFreeSize=1730015

[Cache]
ObjectCache=395
ObjectCacheMax=50000
ObjectCacheRatio=0
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
DBDate=2024-10-24 07:23:49
DBDateOffset=-7200
DBPatchLevel=5;P03;a4067bb64c54435ec5a9b948a3aa16b9;45
UsingBLOBs=true

[Healthcheck]
Date=2024-10-24 09:23:49
ElapsedTime=22
```
[/details]

## Answer
Bonjour,

Un test élémentaire montre qu'on passe bien par ce hook en 5.3 :

```java
package com.simplicite.commons.Application;

import java.util.*;
import com.simplicite.util.*;
import com.simplicite.bpm.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;

/**
 * Platform Hooks
 */
public class PlatformHooks extends com.simplicite.util.engine.PlatformHooksInterface {
	
	@Override
	public String preSearchIndex(Grant g, java.lang.String search) {
		AppLog.info("Called !1", g);
		return "texte a trouver";
	}
}
```
Recherche globale "test" :

![image|690x314](upload://jUoxd5gSBx3gBlZEEjf3NxwaQjS.png)

- Vérifiez si vous implémentez bien la bonne interface
- Vider le cache et redémarrer votre instance/tomcat. Vos changements de hooks ou classes n'ont peut être pas été bien rechargés dans le class loader.
- Ajoutez des logs dans les autres PlatformHooks pour voir si c'est la méthode ou toute la classe qui est ignorée.
- Comment s'appelle l'objet shared script ? il faut qu'il commence par "PlatformHooks" pour être chargé et appelé comme tel.

On va livrer dans la prochaine 5.3 l'évolution sur les caractères spéciaux pour ne plus leur ajouter de wildcard.
