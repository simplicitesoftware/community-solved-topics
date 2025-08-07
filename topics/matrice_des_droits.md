# Matrice des droits

**URL:** https://community.simplicite.io/t/5363

## Question
Bonjour,

J'aurais voulu savoir s'il existe un moyen natif pour récupérer la matrice de droits ?

C'est à dire pouvoir visualiser quel utilisateur à quel droit sur quel objet, etc.

Si cela n'est pas possible nativement, si jamais vous avez une requête SQL permettant de le faire je suis preneur :slight_smile:.

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
SystemDate=2022-10-12 12:02:13

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=https://api-mla.gke.ope.gcp.renault.com
ActiveSessions=56
TotalUsers=420
EnabledUsers=419
LastLoginDate=2022-10-12 11:58:17

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
HeapFree=1448620
HeapSize=2662400
HeapMaxSize=14262272
TotalFreeSize=13048492

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=3539
ObjectCacheMax=10000
ObjectCacheRatio=35
ProcessCache=30
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.13
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.3.5
DBDate=2022-10-12 12:02:13
DBDateOffset=0
DBPatchLevel=5;P01;94dfa153d22f9e8ecd37b949c00b442c
UsingBLOBs=true

[Healthcheck]
Date=2022-10-12 12:02:13
ElapsedTime=17

```
[/details]

## Answer
Bonjour,

Vous pouvez utiliser le tableau croisé des habilitations :

![Simplicité®|690x313](upload://rwWjf4djgAzrIEoqIeupytjLr1E.jpeg)

![Cursor_and_Simplicité®|690x470](upload://ySySoe25A8E72WkGyY2f8uUCMVn.jpeg)
