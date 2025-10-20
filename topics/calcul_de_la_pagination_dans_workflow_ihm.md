# Calcul de la pagination dans workflow IHM

**URL:** https://community.simplicite.io/t/10485

## Question
### Request description

Suspicion d’anomalie dans le calcul de la  pagination des worklfows IHM

### Steps to reproduce

1. Avec un utilisateur dont la Taille minimale des listes : 5 et Taille maximale des listes : 10, faire une selection dans un workflow IHM sur un objet de 27 occurences

2. La pagination est incohérente dans le workflow IHM :

![image|690x477](upload://ixHAawDKJmCefbukaYzAn52tTkc.png)

### Technical information

[details="Instance /health" open]
```text
Platform]
Status=OK
Version=6.2.14
BuiltOn=2025-07-31 15:05
Git=6.2/285e27aae1fe529c1a4afc33b026a6d5f04a3552
Encoding=UTF-8
EndpointIP=127.0.0.1
EndpointURL=https://XXXXXXXX.simplicite.io:20103
TimeZone=Europe/Paris
SystemDate=2025-08-08 14:38:19

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://XXXXXXXX.XXXXXXXXX.simplicite.io
ActiveSessions=2
TotalUsers=10
EnabledUsers=8
LastLoginDate=2025-08-08 14:36:05

[Server]
ServerInfo=Apache Tomcat/9.0.107
ServerType=WEB
ServerDevMode=true
ServerCompiler=true
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=5.14.0-570.17.1.el9_6.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=49850
DiskUsable=49850
DiskTotal=101109

[JavaVM]
Version=21.0.7
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.7+6-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=329235
HeapSize=524288
HeapMaxSize=524288
TotalFreeSize=329235

[Cache]
ObjectCache=317
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=2
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
VendorName=mysql
ProductName=MySQL
ProductVersion=5.5.5-10.5.27-MariaDB
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-9.4.0 (Revision: d680767849154c8e136dfc3d8a0ae4d9fefd1fb7)
DBDate=2025-08-08 14:38:19
DBDateOffset=0
DBPatchLevel=6;P02;56a2df3887f754ccf1ded39d8fd8bffe;14
UsingBLOBs=true

[Healthcheck]
Date=2025-08-08 14:38:19
ElapsedTime=11
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

[details="Other relevant information" open]
**Simplicité version** 6.2.14

**Built on**2025-07-31 15:05

[details]

[/details]

[/details]

## Answer
Reproduit, on va corriger en 6.2.15
les compteurs de pagination étaient envoyés comme des string dans le JSON.
par exemple maxpage+1 affichait "91" et pas 10.
