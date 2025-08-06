# Récapitulatif incorrect lorsqu'une même activité revient plusieurs fois dans un processus métier

**URL:** https://community.simplicite.io/t/7258

## Question
### Request description

Bonjour,

A la différence de la v4, en v5 on a un récapitulatif des choix réalisé dans un processus métier ce qui est très pratique. Les informations sont correctes sauf dans le cas où une même activité revient plusieurs fois. Si c'est le cas le récapitulatif affiche les informations de la dernière activité réalisée.

### Steps to reproduce

Avec le module de Démo, on peut reproduire ce comportement avec le processus de création d'un nouvel utilisateur et l'activité "Choix d'un groupe".

![Simplicite_v53_recapitulatif_processus_incorrect|video](upload://zdRGtNzGjJW8dK9CvoEq3toNdFo.mp4)

Dans mon exemple, la première activité "Choix d'un groupe" devrait afficher "ADMIN" au lieu de "APP_ADMIN" dans le récapitulatif et la seconde activité "Choix d'un groupe" devrait afficher "APP_ADMIN" (c'est bien le cas).

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.23
BuiltOn=2023-11-24 15:38
Git=5.3/b849931f89c40ba4f13af0f3dc9da5761f63381f
Encoding=UTF-8
EndpointIP=172.24.0.3
EndpointURL=http://60d9135f14f0:8080
TimeZone=UTC
SystemDate=2023-11-29 07:58:39

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://10.24.160.176:5380
ActiveSessions=1
TotalUsers=8
EnabledUsers=5
LastLoginDate=2023-11-29 07:46:06

[Server]
ServerInfo=Apache Tomcat/9.0.83
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.102.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.9
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.9+9
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=141508
HeapSize=331776
HeapMaxSize=2007040
TotalFreeSize=1816772

[Cache]
ObjectCache=401
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=401
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.13 (Debian 13.13-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.0
DBDate=2023-11-29 07:58:39
DBDateOffset=0
DBPatchLevel=5;P03;6f1cec3ddb7615b1340daf5a9becaab3
UsingBLOBs=true

[Healthcheck]
Date=2023-11-29 07:58:39
ElapsedTime=10
```
[/details]

## Answer
Ce sera corrigé en 5.3.24

Le chemin de navigation clonera les données de chaque étape traversée.

Dans un screenflow, on pourra maintenant utiliser les API du ProcessRoad via `getProcessRoad()` pour avoir l'historique des ActivityFile : avec data + usage info distincts, donc même si l'activité a été traversée plusieurs fois
