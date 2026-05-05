# Recherches prédéfinies non autorisée

**URL:** https://community.simplicite.io/t/12177

## Question
### Bonjour, 

J'ai activé la recherche prédéfinie dans la définition de mes objets et les utilisateurs ont bien des droits CRUD sur les objets mais lorsque que ils souhaitent créer un recherche prédéfinie, l'erreur suivante apparait "L'accès à cette fonction vous est interdite."

Nous sommes récemment passés à la version 6.3.7 (auparavant en 6.3.5). Il me semble que cela fonctionnait avant.

Cordialement, 

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.3.7
Variant=light
BuiltOn=2026-04-03 09:45
Git=6.3/3f01baa9ac25b9b349f607f8d913f3984ec7c924
Encoding=UTF-8
EndpointIP=10.40.55.46
EndpointURL=http://xxx/maindev
TimeZone=Europe/Paris
SystemDate=2026-05-04 14:55:41

[Application]
ApplicationVersion=1.0.0
ContextPath=/maindev
ContextURL=https://xxx/maindev
ActiveSessions=2
TotalUsers=25
EnabledUsers=23
LastLoginDate=2026-05-04 14:53:10

[Server]
ServerInfo=Apache Tomcat/9.0.108
ServerType=WEB
ServerDevMode=true
ServerCompiler=true
ServerActiveSessions=0
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=5.14.0-570.60.1.el9_6.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=6483
DiskUsable=6483
DiskTotal=12224

[JavaVM]
Version=21.0.9
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.9+10-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=495327
HeapSize=1482752
HeapMaxSize=1482752
TotalFreeSize=495327

[Cache]
ObjectCache=144
ObjectCacheMax=10000
ObjectCacheRatio=1
ProcessCache=1
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=16.9
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.10
DBDate=2026-05-04 14:55:41
DBDateOffset=0
DBPatchLevel=6;P03;ec60a897be456b54a0334ce46619a1a4;7
UsingBLOBs=true

[Healthcheck]
Date=2026-05-04 14:55:42
ElapsedTime=268

```

[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```

[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```

[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*

[/details]

## Answer
Effectivement, il y a eu dernièrement un renforcement des contrôles d'accès via la nouvelle API `BusinessObject` qui permet d'utiliser les objets plus simplement via une interface "builder", en cours de documentation. 

Le contrôle ne tenait pas bien compte du `withAllAccess()` temporaire afin d'autoriser l'utilisateur à utiliser l'objet `Research` même s'il n'en a pas les droits via ses responsabilités.

Ce sera livré en 6.3.9.
