# Page qui remonte toute seule en haut quand on clique sur un onglet (suite)

**URL:** https://community.simplicite.io/t/7090

## Question
### Request description

Bonjour, 

J'ai l'impression que la correction pour l'anomalie suivante a été perdue dans les dernières versions (5.3.19 et 5.3.20).

https://community.simplicite.io/t/page-qui-remonte-toute-seule-en-haut-quand-on-clique-sur-un-onglet/6963?u=florentgn

### Steps to reproduce

Avec le module de Démo.
J'ouvre le formulaire d'un produit et je fais "Etendre" pour agrandir le formulaire.
Je clique sur un sous-onglet, la page remonte toute seule.

![ESAT_Simplicite_v5320_bug_focus_sous_onglets|video](upload://qall1TSQB9iJ1OClCFcnKvaYcRD.mp4)

(Si on clique sur une des lignes dans un sous-onglet puis sur fermer le problème n'est plus présent, on peut naviguer dans les sous-onglet sans que la page remonte tout en haut)

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.20
BuiltOn=2023-10-20 15:28
Git=5.3/316518d3b8cad1f41089f82fc87e17ce4144e2b1
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2023-10-27 14:14:40

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=2
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-10-27 14:11:14

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
Version=17.0.8.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.8.1+1
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=609394
HeapSize=898048
HeapMaxSize=2007040
TotalFreeSize=1718386

[Cache]
ObjectCache=366
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=366
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
DBDate=2023-10-27 14:14:40
DBDateOffset=0
DBPatchLevel=5;P03;ebb0d618d628fe2a22a3ce46072e998b
UsingBLOBs=true

[Healthcheck]
Date=2023-10-27 14:14:40
ElapsedTime=11

```
[/details]

## Answer
En 5.3.21, le scrolltop maintenu sera celui avant fermeture de l'onglet courant.
Ca évitera de "trop" remonter dans le formulaire, même si le nouvel onglet a moins de contenu.

En 5.3, il se peut que le scroll-y soit remis avant que tous les composants asynchrones soient chargés (ex temps de remontée d'une image...).

En V6, les Promises ont permis d'avoir un "onload" final, avec une position verticale qui sera plus précise.
