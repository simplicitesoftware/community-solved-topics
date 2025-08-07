# Equivalent BEGIN TRANSACTION COMMIT ROLLBACK dans un ObjectDB

**URL:** https://community.simplicite.io/t/5360

## Question
Bonjour,

Nous avons un besoin métier nécessitant de n'envoyer qu'une seule requête sql à la base, pour faire plusieurs Update/Create.

Existe-t-il un équivalent de BEGIN TRANSACTION avec les ObjectDB ?

Le but serait de ne pas tout remplacer par du sql basique, dans le but de conserver la surcouche de Simplicité (Hook, etc).

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.1.44
BuiltOn=2022-05-10 18:36
Git=5.1/a51516647c95b8cab51e136ca72a2a5e5c30e27c
Encoding=UTF-8
EndpointIP=172.20.49.136
EndpointURL=http://mla-api-58df44d898-rcj89:8080
TimeZone=Europe/Paris
SystemDate=2022-10-11 11:00:24

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=https://api-mla.gke.ope.gcp.renault.com
ActiveSessions=68
TotalUsers=420
EnabledUsers=419
LastLoginDate=2022-10-11 10:53:01

[Server]
ServerInfo=Apache Tomcat/9.0.62
ServerType=WEB
ServerActiveSessions=72

[OS]
Name=Linux
Architecture=amd64
Version=5.10.123+
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.3+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=2940982
HeapSize=6258688
HeapMaxSize=14262272
TotalFreeSize=10944566

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=5672
ObjectCacheMax=10000
ObjectCacheRatio=56
ProcessCache=2
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.13
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.3.5
DBDate=2022-10-11 11:00:24
DBDateOffset=0
DBPatchLevel=5;P01;94dfa153d22f9e8ecd37b949c00b442c
UsingBLOBs=true

[Healthcheck]
Date=2022-10-11 11:00:25
ElapsedTime=17

```
[/details]

## Answer
Bonjour,

- Vous serez forcement en auto-commit sur une base HSQLDB ou avec des tables MyISAM sur mySQL. Sinon il faut vous assurer que votre base/driver jdbc n'est pas configuré en auto-commit
- Les déploiements en EJB = la transaction est gérée par le serveur d'appli / EJB transaction support
- Les déploiements en webapp seule avec tomcat (nos images sim/docker) = accès direct via driver SQL. Les objectDB sont pilotés par le paramètre **DIRECT_TRANSACTION**

  - Il vaut "no" par défaut = toutes les mises à jour sont en auto-commit, dans ce cas il faut gérer le rollback applicatif par des "update" inverses dans un catch
  - Le passer à "yes" = tout objet qui fait un create/update/save/delete arme une transaction, et tous les hooks enfants (postSave...) utiliseront cette transaction (dans un même thread, si on utilise un autre thread genre on appelle une action asynchrone ça sortira de la transaction).
Ce n'est pas le mode par défaut car si certaines transactions sont longues, le commited read en lecture bloquera pas mal d'utilisateurs si c'est une action synchrone/UI.

- Pour faire une simple transaction par code en laissant le paramètre global à "no" et en restant dans le thread de session :

```java
Grant g = getGrant();
try {
	g.beginTransaction();

	// ....
	obj1.save();
	obj2.save();
	// postSave... hooks can include other updates in the same transaction
	obj3.delete();
	// ....

	if (error)
		g.rollbackTransaction();
	else
		g.commitTransaction();
}
catch (Exception e) {
	g.rollbackTransaction();
}
```

**Attention** 
- ces verbes ne feront rien si la base est en auto-commit
- si votre transaction est longue et bloque les accès en lecture, il y aura aussi à vérifier les timeout configurés côté base (long transaction, taille max des locks, mode de verrouillage page/row...).
- Perso, je préfère toujours laisser le système fluide / auto-commit / sans passer par les DBA... en gérant les erreurs par des "update" qui annulent applicativement les choses ou par job/cron de nettoyage asynchrone.
