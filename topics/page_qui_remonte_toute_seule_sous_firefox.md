# Page qui remonte toute seule sous Firefox

**URL:** https://community.simplicite.io/t/7118

## Question
Continuing the discussion from [Page qui remonte toute seule en haut quand on clique sur un onglet (suite)](https://community.simplicite.io/t/page-qui-remonte-toute-seule-en-haut-quand-on-clique-sur-un-onglet-suite/7090):

Bonjour,

J'ai fais quelques tests avec Simplicité v5.3.21, le problème est bien corrigé sous Chrome mais avec Firefox j'ai toujours le même comportement.

Firefox v119.0 :
![Simplicite_v53_onglets_page_qui_remonte_firefox|video](upload://41MFIzAdO5Nqi914ISdvblEZfbF.mp4)


Chrome v119.0.6045.106 :

![Simplicite_v53_onglets_page_qui_remonte_chrome|video](upload://31GeZVCEBFgkdiy0VeMeMHkgYOt.mp4)



### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.21
BuiltOn=2023-10-31 16:10
Git=5.3/bb90c9e36cac89047e7261a2e795738a0f242ac9
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2023-11-02 09:05:29

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-11-02 09:05:20

[Server]
ServerInfo=Apache Tomcat/9.0.82
ServerType=WEB
ServerActiveSessions=3
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.99.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=11.0.21
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=11.0.21+9
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=198516
HeapSize=547840
HeapMaxSize=2007040
TotalFreeSize=1657716

[Cache]
ObjectCache=302
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=302
ProcessCacheMax=10000
ProcessCacheRatio=3
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.12 (Debian 13.12-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.6.0
DBDate=2023-11-02 09:05:29
DBDateOffset=0
DBPatchLevel=5;P03;cc9a4948608f47a3e683c21feab11078
UsingBLOBs=true

[Healthcheck]
Date=2023-11-02 09:05:29
ElapsedTime=12
```
[/details]

## Answer
Ce sera corrigé en 5.3.22.

Firefox ne scrolle pas forcement, il reste là où est le focus pour le rendre visible à l'utilisateur. Chrome met le scroll là où on lui dit même si le focus est sur un champ non visible...

Pour corriger, le focus restera sur le `<a href>` du tab clické pour ne pas remonter sur le focus précédent, par défaut le premier champ du formulaire.
