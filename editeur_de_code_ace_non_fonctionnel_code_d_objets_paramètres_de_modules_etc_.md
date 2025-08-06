# Editeur de code ACE non fonctionnel (code d'objets, paramètres de modules, etc...)

**URL:** https://community.simplicite.io/t/8236

## Question
### Request description

L'éditeur ACE est inutilisable du fait d'un décalage entre le code/texte présenté avec celui qui semble chargé dans la vue. Le positionnement du curseur avec la souris "à l'écran" ne correspond pas à la position du curseur "dans le texte".

Il semble que ce soit induit par le style `font-family: var(--simplicite-font-mono), monospace;`... Lorsque je le supprime de la propriété `style` de la balise `div.ace_editor` l'affichage est "recalé".

![image|690x340](upload://7bN4uGbhjgO52rM8QhBa5KEnEoR.png)

![image|690x241](upload://84yCn3XMHfmuP0JalkCSC6OxCMT.png)

![image|690x199](upload://c2huVT4R1J6Zu83mrKhVtDJAOfd.png)

*This request concerns an **up-to-date** Simplicité instance (6.0.11)*

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.0.11
BuiltOn=2024-05-17 10:55
Git=6.0/5c12bbcfdbd43fb72989ef086352a6fa1f44540b
Encoding=UTF-8
EndpointIP=100.88.197.187
EndpointURL=http://p01-74196-addimports-687664477c-8kppf:8080
TimeZone=Europe/Paris
SystemDate=2024-05-23 19:24:18

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://p01-74196-addimports.ext.gke2.dev.gcp.renault.com
ActiveSessions=0
TotalUsers=11
EnabledUsers=8
LastLoginDate=2024-05-23 19:02:16

[Server]
ServerInfo=Apache Tomcat/9.0.89
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=6.1.58+
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.3+9-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=382430
HeapSize=587776
HeapMaxSize=651264
TotalFreeSize=445918

[Cache]
ObjectCache=206
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=206
ProcessCacheMax=10000
ProcessCacheRatio=2
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=15.5
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.3
DBDate=2024-05-23 19:24:18
DBDateOffset=0
DBPatchLevel=6;P00;83a04f7a199f0ef90f9d0607b45ee306;11
UsingBLOBs=true

[Healthcheck]
Date=2024-05-23 19:24:18
ElapsedTime=18
```
[/details]

## Answer
Je me répond à moi-même, après un reboot inopiné (k8s) de mon instance, il semble que le pb ait disparu. Je pense qu'il devait y avoir un problème avec quelques styles customs qui trainaient depuis la v4 et que j'ai entre-temps supprimés.
