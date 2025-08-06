# Monitoring, non visibilité du détail des Threads

**URL:** https://community.simplicite.io/t/5407

## Question
Bonjour,

En essayant de débugger des Threads au statut "BLOCKED", j'ai remarqué que sur nos instances, nous n'avons pas le détail des Threads sur l'écran de monitoring :

![image|690x388](upload://dZ7zyBcn6c0uWgw0ZMsPjiuWT0Y.png)

Alors que je n'ai pas de problème avec les instances SIM :

![image|690x388](upload://3FqG3ugWR7pAfygv1XfUdm9GXJ9.png)

Je ne suis pas expert de ces écrans, mais ce comportement est il normal ? Y a t'il un paramètre permettant de cacher ce tableau (qui aurait été caché par erreur ?) ?

Merci d'avance pour votre aide,

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
EndpointIP=172.20.49.108
EndpointURL=http://mla-api-99bc6f697-rvzqn:8080
TimeZone=Europe/Paris
SystemDate=2022-10-24 11:45:33

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=https://api-mla.gke.ope.gcp.renault.com
ActiveSessions=58
TotalUsers=432
EnabledUsers=431
LastLoginDate=2022-10-24 11:30:51

[Server]
ServerInfo=Apache Tomcat/9.0.62
ServerType=WEB
ServerActiveSessions=58

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
HeapFree=639719
HeapSize=1966080
HeapMaxSize=14262272
TotalFreeSize=12935911

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=4696
ObjectCacheMax=10000
ObjectCacheRatio=46
ProcessCache=15
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.13
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.3.5
DBDate=2022-10-24 11:45:33
DBDateOffset=0
DBPatchLevel=5;P01;94dfa153d22f9e8ecd37b949c00b442c
UsingBLOBs=true

[Healthcheck]
Date=2022-10-24 11:45:33
ElapsedTime=13

```
[/details]

## Answer
Suite à analyse, le problème se produit avec un utilisateur en français, pas en anglais.
C'est juste une erreur dans le template du composant en version française qui positionnait mal la table à remplir. Ce sera corrigé au prochain build.

En attendant, passez votre user en anglais pour voir la table des threads.
