# Comment insérer un TreeView dans le menu principal de l'utilisateur?

**URL:** https://community.simplicite.io/t/5341

## Question
### Request description

*Depuis la 4.0.PL9 il est possible d'ajouter des treeviews dans le menu principal. Je n'arrive néanmoins plus à le faire... en 5.2.17.*

### Steps to reproduce

*J'aimerai bien les connaître ;)*


### Technical information

[details="Instance /health"]
```
[Platform]
Status=OK
Version=5.2.17
BuiltOn=2022-10-01 11:59
Git=5.2/6d655b0fcf7b83d640303aac4c1f210c5fa3bd29
Encoding=UTF-8
EndpointIP=21.1.8.21
EndpointURL=http://16745c31bed2:8080
TimeZone=Europe/Paris
SystemDate=2022-10-05 14:15:09

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://bca.dok.intra.renault.fr
ActiveSessions=23
TotalUsers=9495
EnabledUsers=1929
LastLoginDate=2022-10-05 14:14:41

[Server]
ServerInfo=Apache Tomcat/9.0.67
ServerType=WEB
ServerActiveSessions=23
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.76.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.4.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.4.1+1
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=906860
HeapSize=3250176
HeapMaxSize=5068160
TotalFreeSize=2724844

[Cache]
ObjectCache=1075
ObjectCacheMax=10000
ObjectCacheRatio=10
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=97
APIGrantCacheMax=1000
APIGrantRatio=9

[Database]
Vendor=2
ProductName=MySQL
ProductVersion=5.6.39-log
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-java-8.0.30 (Revision: 1de2fe873fe26189564c030a343885011412976a)
DBDate=2022-10-05 14:15:09
DBDateOffset=0
DBPatchLevel=5;P02;5d9f06ab96b2d154bec456ed317d8bf0
UsingBLOBs=true

[Healthcheck]
Date=2022-10-05 14:15:09
ElapsedTime=20
```
[/details]

[details="Simplicité logs"]
```
NA
```
[/details]

[details="Browser logs"]
```
NA
```
[/details]

[details="Other relevant information"]
*NA*
[/details]

## Answer
Bonjour Bruno,

Pour le treeview dans le menu, il faut, sur le noeud racine de votre arbre:

1. décocher l'option "Docker tree on left side"
2. cocher l'option "Add tree to main menu"


[details="Voir screenshot"]

![treeview_menu|690x436](upload://hdCQtTyvQ5pYVlibZfn3VNgZPDE.gif)
[/details]
