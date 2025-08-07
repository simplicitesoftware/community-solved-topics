# Group By avec template de liste

**URL:** https://community.simplicite.io/t/8434

## Question
### Request description

Bonjour,
Je rouvre un ticket suite à mes tests liés au topic https://community.simplicite.io/t/group-by-avec-un-template-de-liste-perte-de-rendering-des-enum/8353.

Les listes présentées avec un template s'affichent mal lorsqu'on ajoute un Group By et qu'on plie puis déplie une section.

### Steps to reproduce

1. Si j'arrive sur la page et que tous les éléments sont dépliés, c'est OK
![image|690x368, 75%](upload://eMZ4N94yMc1oBy3vQia2KaUQHbE.png)

2. Mais si je ferme une section et que je la rouvre, seul le header est affiché et pas les éléments de la liste (ici ma section ORD_1)
![image|690x341, 75%](upload://lbuKzF3f88jYT00BK66EsGzDgjO.png)

Merci par avance.
Maxime

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.1.0-beta
BuiltOn=2024-07-01 11:00
Git=6.1/80ee293b8d321eeb0c4998473013038e7f3244d6
Encoding=UTF-8
EndpointIP=172.22.0.8
EndpointURL=
TimeZone=UTC
SystemDate=2024-07-02 12:29:35

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=3
EnabledUsers=1
LastLoginDate=2024-07-02 12:17:06

[Server]
ServerInfo=Apache Tomcat/9.0.89
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.114.2.el7.x86_64
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.3+9-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=263500
HeapSize=386048
HeapMaxSize=2007040
TotalFreeSize=1884492

[Cache]
ObjectCache=331
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=331
ProcessCacheMax=10000
ProcessCacheRatio=3
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=14.12 (Debian 14.12-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.3
DBDate=2024-07-02 12:29:35
DBDateOffset=0
DBPatchLevel=6;P01c;dd6af46c64e2d06532fbd02a716b883c;0-beta
UsingBLOBs=true

[Healthcheck]
Date=2024-07-02 12:29:35
ElapsedTime=242

```
[/details]

## Answer
Ok merci, problème reproduit quand une liste groupée avec template de ligne se trouve dans une area parente, le selector jQuery remonte un peu trop et se trompe d'area.
On va gérer ça.

ce sera livré d'ici demain en 6.1.0 RC
