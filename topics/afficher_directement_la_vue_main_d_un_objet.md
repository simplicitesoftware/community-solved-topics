# Afficher directement la vue "main" d'un objet

**URL:** https://community.simplicite.io/t/10477

## Question
### Bonjour

*Lorsque je me connecte à une application et que j’arrive sur une page, il est nécessaire que je clique encore sur l’objet pour avoir la liste :*

A la connexion :

![image|690x128](upload://cLgSNIz3hdV76lXHxLmlTzs3yNo.png)

et je dois encore cliquer sur Employeurs frontaliers v2.0 pour afficher la liste :

![image|690x222](upload://51MPj6GmIk8BiG874LOczGb66rD.png)

c’est sûrement qu’une question de config, mais comment est-ce que je fais pour arriver directement sur cette liste (avec le panel de la recherche)? ou n'est-ce pas possible?

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.12
BuiltOn=2025-06-27 18:57
Git=6.2/52d763856412a8eb1564748d6d391f60e1b9c921
Encoding=UTF-8
EndpointIP=172.31.255.7
EndpointURL=http://b084fcfeaf4f:8080
TimeZone=Europe/Zurich
SystemDate=2025-08-06 14:33:52

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://app1-test.domaine.ch
ActiveSessions=2
TotalUsers=8
EnabledUsers=6
LastLoginDate=2025-08-06 14:33:41

[Server]
ServerInfo=Apache Tomcat/9.0.106
ServerType=WEB
ServerDevMode=false
ServerCompiler=true
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=4.18.0-553.56.1.el8_10.x86_64
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.7
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.7+6-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=149839
HeapSize=380160
HeapMaxSize=380160
TotalFreeSize=149839

[Cache]
ObjectCache=457
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=7
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=16.8
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.7
DBDate=2025-08-06 14:33:52
DBDateOffset=0
DBPatchLevel=6;P02;070eeaa53c5b6fd9eacbce674cd833d7;12
UsingBLOBs=true

[Healthcheck]
Date=2025-08-06 14:33:52
ElapsedTime=895
```

[/details]


Merci pour votre aide

Fabrice

## Answer
Bonjour,

C'est effectivement voulu car la recherche dockée a besoin de tout l'écran et non d'une zone de vue/accueil. Si on avait 2 listes sur son accueil, on ne pourrait pas avoir 2 recherches à gauche...

Une instance `home` de page d'accueil ne peut faire que des recherches en liste ou en dialog.

Le fonctionnement de la recherche a été entièrement revu en 6.3 avec la possibilité notamment d'ajouter un template de recherche (en haut ou à gauche de la liste, et non de la page).

[cf release note](https://docs.simplicite.io/versions/release-notes/v6-3#enhanced-list-search-ux)

En attendant si vous voulez absolument une recherche dockée à gauche, il faudra ouvrir la liste de l'instance Main en pleine page. Donc la page d'accueil devra contenir un simple bout de code javascript qui `$ui.displayList(null,"MonObject")`, par défaut ça ouvrira la liste main = instance `the_ajax_MonObject`.
