# Keycloack - Langue par défaut

**URL:** https://community.simplicite.io/t/7941

## Question
### Request description
Bonjour,

Peut-on positionner la langue par défaut de l'utilisateur (usr_lang) lors de la création d'un compte à la volée par keycloack ? par défaut elle est positionnée en Anglais.
Si oui, comment ?
Si non, peut-on prévoir une évolution ?

Je ne récupère pas la langue dans la trame 

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.31
BuiltOn=2024-03-15 13:56
Git=5.3/0ccf142afa4e52dbd9ac3d0e72cb527a5ca11e22
Encoding=UTF-8
EndpointIP=10.144.28.217
EndpointURL=http://SW51634:8080
TimeZone=Europe/Paris
SystemDate=2024-03-18 16:56:44

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://XXXXXXXXXXXXX
ActiveSessions=2
TotalUsers=28
EnabledUsers=23
LastLoginDate=2024-03-18 16:55:36

[Server]
ServerInfo=Apache Tomcat/9.0.80
ServerType=WEB
ServerActiveSessions=3
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Windows Server 2022
Architecture=amd64
Version=10.0
SystemEncoding=UTF-8

[Disk]
DiskFree=286756
DiskUsable=286756
DiskTotal=562466

[JavaVM]
Version=17.0.3.1
Vendor=Oracle Corporation
VMName=Java HotSpot(TM) 64-Bit Server VM
VMVersion=17.0.3.1+2-LTS-6
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=1510727
HeapSize=2097152
HeapMaxSize=4194304
TotalFreeSize=3607879

[Cache]
ObjectCache=456
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=456
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
VendorName=mysql
ProductName=MySQL
ProductVersion=5.5.68-MariaDB
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-8.1.0 (Revision: 7b6f9a337afe6ccb41823df485bf848ca7952b09)
DBDate=2024-03-18 16:56:44
DBDateOffset=0
DBPatchLevel=5;P03;504b3d3f35216ae713e5bf5df2855321
UsingBLOBs=true

[Healthcheck]
Date=2024-03-18 16:56:44
ElapsedTime=31

```
[/details]

## Answer
Bonjour,

Vous pouvez surcharger la valeur par défaut du champ `usr_lang`.
Si vous utilisez un objet utilisateur héritier de SimpleUser, vous pouvez aussi valoriser ce champ dans le hook `preCreate`.
