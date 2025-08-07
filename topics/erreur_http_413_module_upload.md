# Erreur HTTP 413 module upload

**URL:** https://community.simplicite.io/t/7066

## Question
### Request description
Bonjour, 

Notre équipe rencontre le problème suivante sur une instance simplicité hébergée sur un serveur client.

Nous avons consulté les sujets concernant cette erreur sur le forum, mais nous n'avons pas trouvé de solution. 

Pouvez-vous nous guider svp ? 

*A l'import d'un module dépassant une certaine taille erreur d'upload*

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1. Dans le menu Module >Module : X
2. Choisir un fichier zip ou xml
3. Sauvegarder
Une erreur 413 est générée sur le front. 
La variable max size :MAX_UPLOAD_SIZE= 100

### Technical information



[details="Simplicité logs"]
2023-10-20 15:27:59,659|SIMPLICITE|WARN||http://frparintres01.groupe.active:8080||WARN|system|com.simplicite.webapp.servlets.ui.DefaultServlet|service||Event: /events is not requested with websocket protocol. The request is ignored.
[/details]

Détails du /health de la plateformev : 

[Platform]
Status=OK
Version=5.3.16
BuiltOn=2023-09-29 15:24
Git=5.3/ada6e86492cace177cb57b570853c82fab936aab
Encoding=UTF-8
EndpointIP=10.105.30.31
EndpointURL=localhost:8080
TimeZone=GMT+02:00
SystemDate=2023-10-20 15:34:41

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=localhost
ActiveSessions=2
TotalUsers=3
EnabledUsers=1
LastLoginDate=2023-10-20 15:32:13

[Server]
ServerInfo=Apache Tomcat/9.0.80
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=4.18.0-477.27.1.el8_8.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=2977
DiskUsable=2977
DiskTotal=3062

[JavaVM]
Version=17.0.8
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.8+7-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=296650
HeapSize=557056
HeapMaxSize=1964032
TotalFreeSize=1703626

[Cache]
ObjectCache=646
ObjectCacheMax=10000
ObjectCacheRatio=6
ProcessCache=646
ProcessCacheMax=10000
ProcessCacheRatio=6
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=1
ProductName=HSQL Database Engine
ProductVersion=2.7.1
DriverName=HSQL Database Engine Driver
DriverVersion=2.7.1
DBDate=2023-10-20 15:34:41.802987+2:00
DBDateOffset=0
DBPatchLevel=5;P03;eae816e5089006449212ca1f2a1fc9f4
UsingBLOBs=false

[Healthcheck]
Date=2023-10-20 15:34:41
ElapsedTime=3

Merci d'avance.

## Answer
Bonjorur Thomas, 

Tu devrais pouvoir accéder aux logs générés par l'import du module dans Exploitation > Supervision imports. 
Si dans le fichier de logs il y a des erreurs, il faut corriger le module à la source afin de les éviter au prochain import.
