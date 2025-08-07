# Restitution du contenu d'un bloc dans une action avec attribut

**URL:** https://community.simplicite.io/t/7276

## Question
### Request description

Suspicion anomalie : Le contenu d'un champ bloc note n'est pas restitué dans une action pop up avec attributs

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

Sur la base de la démo

1. Ajouter le champ "demoPrdComments" dans l'action DEMO_INCSTOCK
2. Sur un produit, saisir un commentaire
3. Lancer l'action "Augmenter le stock"
4. Le commentaire n'est pas visible

### Technical information

[details="Instance /health"]
[Platform]
Status=OK
Version=5.3.23
BuiltOn=2023-11-24 15:38
Git=5.3/b849931f89c40ba4f13af0f3dc9da5761f63381f
Encoding=UTF-8
EndpointIP=127.0.0.1
EndpointURL=http://partenor.simplicite.io:11248
TimeZone=Europe/Paris
SystemDate=2023-12-01 18:43:47

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://demo5.partenor.simplicite.io
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-12-01 18:39:22

[Server]
ServerInfo=Apache Tomcat/9.0.83
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.99.1.el7.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=25344
DiskUsable=21187
DiskTotal=100701

[JavaVM]
Version=17.0.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.1+12
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=226873
HeapSize=410624
HeapMaxSize=524288
TotalFreeSize=340537

[Cache]
ObjectCache=379
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=379
ProcessCacheMax=10000
ProcessCacheRatio=3
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
ProductName=MySQL
ProductVersion=5.5.68-MariaDB
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-8.2.0 (Revision: 06a1f724497fd81c6a659131fda822c9e5085b6c)
DBDate=2023-12-01 18:43:47
DBDateOffset=0
DBPatchLevel=5;P03;6f1cec3ddb7615b1340daf5a9becaab3
UsingBLOBs=true

[Healthcheck]
Date=2023-12-01 18:43:47
ElapsedTime=8
---paste the content of your-instance.com/health---
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
Le block note s'affiche bien quand c'est un JSON d'activités :

![image|604x500](upload://uc7jEIG2QDPDETLvBx6DV3OgJ8W.png)

Par contre l'ancien rendering textuel remonte l'historique dans la "old value" du champ ajax (la valeur courante sert pour saisir juste une note).

La old value sera désormais remontée dans le popup de confirmation pour que la UI puisse l'afficher.

Ce sera poussé en 5.3.24
