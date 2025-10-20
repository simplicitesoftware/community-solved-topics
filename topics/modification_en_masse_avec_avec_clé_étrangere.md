# Modification en masse avec avec clé étrangere

**URL:** https://community.simplicite.io/t/10486

## Question
### Request description

Suspicion Anomalie : Lors de la modification en masse d’un objet que l’on veut associer à un autre objet avec une clé étrangère, les données non clé fonctionnelle sont supprimées.

### Steps to reproduce

1. Créer un référentiel sur la demo puis mettre à jour le paramétrage de produit comme l’exemple ci dessous :

![image|690x374](upload://uBnPcj89wfh310lckheSHKj8Iw3.png)

1. Depuis Fournisseur, faire une mise à jour en masse en modifiant la technologie et enregistrer.

### Technical information

[details="Instance /health" open]
```text
[Platform]
Status=OK
Version=6.2.14
BuiltOn=2025-07-31 15:05
Git=6.2/285e27aae1fe529c1a4afc33b026a6d5f04a3552
Encoding=UTF-8
EndpointIP=127.0.0.1
EndpointURL=http://XXXXXXXXXXXXXXXX.simplicite.io:20068
TimeZone=Europe/Paris
SystemDate=2025-08-08 14:46:58

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://XXXXXXXXXXX.XXXXXXXXXXX.simplicite.io
ActiveSessions=1
TotalUsers=10
EnabledUsers=8
LastLoginDate=2025-08-08 14:44:12

[Server]
ServerInfo=Apache Tomcat/9.0.107
ServerType=WEB
ServerDevMode=true
ServerCompiler=true
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=5.14.0-570.17.1.el9_6.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=49849
DiskUsable=49849
DiskTotal=101109

[JavaVM]
Version=21.0.7
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.7+6-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=44164
HeapSize=290816
HeapMaxSize=524288
TotalFreeSize=277636

[Cache]
ObjectCache=418
ObjectCacheMax=10000
ObjectCacheRatio=4
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
ProductVersion=13.20
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.7
DBDate=2025-08-08 14:46:58
DBDateOffset=0
DBPatchLevel=6;P02;56a2df3887f754ccf1ded39d8fd8bffe;14
UsingBLOBs=true

[Healthcheck]
Date=2025-08-08 14:46:58
ElapsedTime=17

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

**Built on** 2025-07-31 15:05

[/details]

## Answer
Ce sera corrigé en 6.2.15.
Il y avait bien un problème de rechargement de chaque ligne à mettre à jour en back.
