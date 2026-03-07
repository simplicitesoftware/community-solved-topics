# Erreur 404 mode-simplicite.js

**URL:** https://community.simplicite.io/t/11740

## Question
### Request description

Bonjour,

Quand on navigue dans Simplicité on constate qu'il y a des tentatives de récupération de la ressource mode-simplicite.js qui n'est pas trouvée.

### Steps to reproduce

A partir d'une instance Simplicité vierge :

1. Se connecter avec le compte designer.
2. Aller dans Settings > System parameters
3. Cliquer sur le libellé de la colonne "Code" pour accéder au paramétrage de l'attribut.

![image|690x220](upload://hyylnSwiYovqw8iGgTn3EmitKe6.png)

4. Ouvrir DevTools. L'erreur suivante est présente dans les logs :

![image|689x57](upload://d0bJxejkwItIHaqJGqROP5YlUzN.png)

5. Dans les logs back, l'erreur suivante est présente :

![image|690x48](upload://nV658ezItO2nsxAMQoir5fuIFcA.png)


### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.3.5
BuiltOn=2026-02-20 11:40
Git=6.3/76da9078f28d66b8cde26eb7f8bed398338adb46
Encoding=UTF-8
EndpointIP=
EndpointURL=http://5713a06299a3:8080
TimeZone=Europe/Paris
SystemDate=2026-03-06 14:08:13

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=http://localhost:8083
ActiveSessions=2
TotalUsers=3
EnabledUsers=1
LastLoginDate=2026-03-06 14:06:11

[Server]
ServerInfo=Apache Tomcat/9.0.115
ServerType=WEB
ServerDevMode=true
ServerCompiler=true
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=6.12.54-linuxkit
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.10
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.10+7-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=36028
HeapSize=241664
HeapMaxSize=503808
TotalFreeSize=298172

[Cache]
ObjectCache=211
ObjectCacheMax=10000
ObjectCacheRatio=2
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
ProductVersion=15.12 (Debian 15.12-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.10
DBDate=2026-03-06 14:08:13
DBDateOffset=0
DBPatchLevel=6;P03;51af22b13838925e31430a969bd336ba;5
UsingBLOBs=true

[Healthcheck]
Date=2026-03-06 14:08:13
ElapsedTime=105

```
[/details]

## Answer
Merci pour ce signalement, c'était effectivement un raté de backport depuis la 7.0.
Ce sera résolu dans la prochaine révision 6.3.6
