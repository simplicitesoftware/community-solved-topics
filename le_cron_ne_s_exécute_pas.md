# Le CRON ne s'exécute pas

**URL:** https://community.simplicite.io/t/10426

## Question
### Cron ne s'exécute pas

*----J'ai créé une cron expression pour une exécution toutes les 5 minutes (le temps de vérifier que tout est fonctionnel) mais le cron ne s'exécute pas. 
- ça fonctionne si j'exécute la tâche manuellement
- j'ai créé un user spécialement pour le CRON et il est dans le groupe LAUSANNEUSERRI_ADMIN

![image|523x339](upload://jwQGUsRi2BRmZhEqqwgXTrTdRRm.png)


Malgré tout le user semble ne pas être autorisé et je ne vois pas ce qui manque:
[details="LOGS"]
```[Platform]
2025-07-30 13:40:00,005|SIMPLICITE|ERROR||http://b819bf7edd50:8080||ECORECM001|system|com.simplicite.util.CronJob|initJobStandalone||Error creating new job for object LsnUsersBo method LsnuAc_migration
    java.lang.Exception: Job user user_migration not granted for action LsnuAc_migration on object LsnUsersBo
```
[/details]
----*
![image|690x163](upload://8u5KMOfzGXmRGa6spl2kwO3A5XY.png)
 

### Technical information

[details="Instance /health"]
```[Platform]
Status=OK
Version=6.2.12
BuiltOn=2025-06-27 18:57
Git=6.2/52d763856412a8eb1564748d6d391f60e1b9c921
Encoding=UTF-8
EndpointIP=172.31.255.6
EndpointURL=http://b819bf7edd50:8080
TimeZone=Europe/Zurich
SystemDate=2025-07-30 13:16:25

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://serveur....
ActiveSessions=2
TotalUsers=7
EnabledUsers=5
LastLoginDate=2025-07-30 09:11:20

[Server]
ServerInfo=Apache Tomcat/9.0.106
ServerType=WEB
ServerDevMode=false
ServerCompiler=true
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=4.18.0-553.56.1.el8_10.x86_64
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.7
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.7+6-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=124012
HeapSize=380160
HeapMaxSize=380160
TotalFreeSize=124012

[Cache]
ObjectCache=125
ObjectCacheMax=10000
ObjectCacheRatio=1
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=1
VendorName=hsqldb
ProductName=HSQL Database Engine
ProductVersion=2.7.4
DriverName=HSQL Database Engine Driver
DriverVersion=2.7.4
DBDate=2025-07-30 13:16:25.400095+2:00
DBDateOffset=0
DBPatchLevel=6;P02;070eeaa53c5b6fd9eacbce674cd833d7;12
UsingBLOBs=false

[Healthcheck]
Date=2025-07-30 13:16:25
ElapsedTime=5---
```
[/details]


Merci d'avance pour tout indice qui me permet sur la voie :slight_smile:

 Fabrice

## Answer
Bonjour, 

Avez vous rechargé la table des CRON?

![Portal_DEV_-_Cron_table|690x223](upload://6nh1hF2KQqJePmBtcMkWNSP6tvX.png)
