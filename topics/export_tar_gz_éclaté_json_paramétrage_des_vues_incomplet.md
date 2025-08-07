# Export tar.gz éclaté json : paramétrage des vues incomplet

**URL:** https://community.simplicite.io/t/8501

## Question
### Request description

Bonjour,

Lorsqu'on fait un export tar.gz éclaté (json) d'un module une partie du paramétrage des vues n'est pas exporté, le contenu de l'onglet "Page d'accueil".

### Steps to reproduce

A partir du module de Demo :

1. Modifier le paramétrage de la vue DemoAdminHome afin de compléter tous les champs de l'onglet "Page d'accueil" :

![image|690x171](upload://2rmnaQiijMx4Aq4M3doVofVzi6p.png)

2. Faire un export tar.gz éclaté du module Demo.
3. Quand on regarde le contenu du fichier DemoAdminHome.json présent dans l'archive on constate qu'il manque le paramétrage de l'onglet "Page d'accueil" dont le thème :

![image|558x232](upload://291HPsZL2CBxmMhP5eI30mr4eXL.png)

**Remarque**
Je voulais essayer avec la dernière version 6.0.16 mais quand j'utilise ce tag j'ai une version 6.1.0 à la place ...

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.0.15
BuiltOn=2024-07-05 18:31
Git=6.0/6fe341ff46405c844ad3c1bf573339ed56073a16
Encoding=UTF-8
EndpointIP=
EndpointURL=http://c32800e69eea:8080
TimeZone=UTC
SystemDate=2024-07-15 17:12:35

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2024-07-15 17:03:56

[Server]
ServerInfo=Apache Tomcat/9.0.90
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=5.15.0-113-generic
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.3+9-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=145717
HeapSize=402432
HeapMaxSize=2033664
TotalFreeSize=1776949

[Cache]
ObjectCache=657
ObjectCacheMax=10000
ObjectCacheRatio=6
ProcessCache=6
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=13.15 (Debian 13.15-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.3
DBDate=2024-07-15 17:12:35
DBDateOffset=0
DBPatchLevel=6;P00;b58ecfbaa6f45a96bdc206655ecd3d19;15
UsingBLOBs=true

[Healthcheck]
Date=2024-07-15 17:12:35
ElapsedTime=7

```
[/details]

## Answer
Effectivement, il me semble plus propre d'utiliser des instances batch (prefix `eai_`) dans le cas du treeview qui est utilisé pour sérialiser le module en JSON (éclaté en répertoires ou non).

Si l'instance de l'objet racine de l'arbre est un Module batch, tout l'arbre le sera.
On va faire ça rapidement.
