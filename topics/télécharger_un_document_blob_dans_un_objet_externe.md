# Télécharger un Document (BLOB) dans un objet externe

**URL:** https://community.simplicite.io/t/5336

## Question
Bonjour,

J'essaye d'obtenir le lien (URL) permettant de télécharger un BLOB, pour l'intégrer dans le HTML d'un objet externe. J'ai l'ID du document en question.

Le but est de créer un lien permettant de télécharger le document depuis l'HTML d'un objet externe, en résumé, reproduire l'action du bouton download ci après, mais de façon dynamique :

![image|317x77](upload://24hu9B0tWPASBhns5WKvoqo4jr4.png)

Merci d'avance pour votre aide.

Benoît

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.1.44
BuiltOn=2022-05-10 18:36
Git=5.1/a51516647c95b8cab51e136ca72a2a5e5c30e27c
Encoding=UTF-8
EndpointIP=172.20.179.51
EndpointURL=http://xxx
TimeZone=Europe/Paris
SystemDate=2022-10-04 15:57:42

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=https://xxx
ActiveSessions=4
TotalUsers=35
EnabledUsers=16
LastLoginDate=2022-10-04 15:18:31

[Server]
ServerInfo=Apache Tomcat/9.0.62
ServerType=WEB
ServerActiveSessions=5

[OS]
Name=Linux
Architecture=amd64
Version=5.10.133+
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.3+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=322920
HeapSize=888832
HeapMaxSize=7131136
TotalFreeSize=6565224

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=402
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.16
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.3.5
DBDate=2022-10-04 15:57:42
DBDateOffset=0
DBPatchLevel=5;P01;94dfa153d22f9e8ecd37b949c00b442c
UsingBLOBs=true

[Healthcheck]
Date=2022-10-04 15:57:42
ElapsedTime=9

```
[/details]

## Answer
`cdisp` permet de dire si le content disposition de la réponse sera :

- "inline" = le navigateur essaie d'afficher le document (constante `HTTPTool.DISP_INLINE`).
- ou "attachment" = le navigateur propose le download du document (constante `HTTPTool.DISP_ATTACHMENT`)

`cache` permet de dire si la réponse de l'URL du document contiendra des headers qui autorisent le navigateur à conserver le document dans son cache (ça a typiquement du sens pour les documents de type image, HTML ou PDF), sinon la réponse dira au navigateur de ne pas conserver le document
