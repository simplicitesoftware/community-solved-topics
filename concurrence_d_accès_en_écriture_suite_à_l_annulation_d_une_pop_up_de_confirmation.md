# Concurrence d'accès en écriture suite à l'annulation d'une pop up de confirmation

**URL:** https://community.simplicite.io/t/7255

## Question
### Request description

Suspicion d'anomalie : Concurrence d'accès en écriture suite à l'annulation d'une pop up de confirmation.

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

Cas reproduit depuis la demo - Simplicité dernière version
utilisateur : designer

1. Sur le formulaire d'un produit en update, modifier le nom 
2. sans sauvegarder, cliquer sur augmenter le stock puis "Annuler"
3. sans sauvegarder, cliquer sur augmenter le stock
4. affichage du message bloquant  "Mise à jour impossible, la donnée a été déjà modifiée par ..."

Le message (4) ne devrait pas remonter.

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.23
BuiltOn=2023-11-24 15:38
Git=5.3/b849931f89c40ba4f13af0f3dc9da5761f63381f
Encoding=UTF-8
EndpointIP=127.0.0.1
EndpointURL=http://partenor.simplicite.io:11248
TimeZone=Europe/Paris
SystemDate=2023-11-28 15:19:53

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://demo5.partenor.simplicite.io
ActiveSessions=2
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-11-28 15:09:13

[Server]
ServerInfo=Apache Tomcat/9.0.83
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.99.1.el7.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=25676
DiskUsable=21519
DiskTotal=100701

[JavaVM]
Version=17.0.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.1+12
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=187888
HeapSize=403456
HeapMaxSize=524288
TotalFreeSize=308720

[Cache]
ObjectCache=444
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=444
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
ProductName=MySQL
ProductVersion=5.5.68-MariaDB
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-8.2.0 (Revision: 06a1f724497fd81c6a659131fda822c9e5085b6c)
DBDate=2023-11-28 15:19:53
DBDateOffset=0
DBPatchLevel=5;P03;6f1cec3ddb7615b1340daf5a9becaab3
UsingBLOBs=true

[Healthcheck]
Date=2023-11-28 15:19:53
ElapsedTime=9

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
Ce sera corrigé en 5.3.24

En cas d'auto-save suite à une modification de formulaire avant d'ouverture d'un dialogue de confirmation, l'annulation de l'action par l'utilisateur provoquera un rechargement du formulaire, ce qui synchronisera le timestamp en front.
