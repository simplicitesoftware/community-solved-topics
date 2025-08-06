# Focus incorrect lorsqu'on a plusieurs listes dans un formulaire

**URL:** https://community.simplicite.io/t/6961

## Question
### Request description

Bonjour,

Au niveau d'un formulaire qui contient deux vues listes par exemple, quand on clique sur "Modifier la liste" (ou créer en liste) le focus ne se positionne pas sur la bonne liste. Si on le fait sur la première le focus est sur la seconde et inversemment.

### Steps to reproduce

Avec le module de démo :

1. J'ai déplacé dans le formulaire de l'objet "Clients" la vue "Commandes du client" qui était en bas du formulaire tout en haut :

![image|690x477](upload://d3WKICXns69DNFquk9LodRo0oKd.png)


2. En bas j'ai toujours la vue "Contacts du client" :

![image|690x476](upload://yESMfd6vtKXT58F3cxhSUGYfZCs.png)


3. Vidéo qui montre le comportement constaté :

![Simplicite_v53_bug_focus_listes|video](upload://snIqDIfl7810Il6LU99wLhgRZKT.mp4)


### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.16
BuiltOn=2023-09-29 15:24
Git=5.3/ada6e86492cace177cb57b570853c82fab936aab
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2023-10-02 07:40:42

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-10-02 07:32:37

[Server]
ServerInfo=Apache Tomcat/9.0.80
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.95.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.8.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.8.1+1
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=361135
HeapSize=736256
HeapMaxSize=2007040
TotalFreeSize=1631919

[Cache]
ObjectCache=475
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=475
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.12 (Debian 13.12-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.6.0
DBDate=2023-10-02 07:40:42
DBDateOffset=0
DBPatchLevel=5;P03;eae816e5089006449212ca1f2a1fc9f4
UsingBLOBs=true

[Healthcheck]
Date=2023-10-02 07:40:42
ElapsedTime=9
```
[/details]

## Answer
Reproduit,
L'erreur vient du fait que le focus revient sur le bouton "editer la liste".
Il est présent sur 2 listes éditables. Quand on clique sur le premier, la liste en édition perd ce bouton, et c'est l'autre qui prend le focus...

La mise en place des auto-focus n'est pas évidente, on a ajouté les cas passants, on doit maintenant s'occuper des "sauf si". On a revu l'algo pour ne pas se tromper de container en 5.3.17.
