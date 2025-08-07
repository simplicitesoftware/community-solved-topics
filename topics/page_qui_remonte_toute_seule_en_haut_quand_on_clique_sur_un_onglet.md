# Page qui remonte toute seule en haut quand on clique sur un onglet

**URL:** https://community.simplicite.io/t/6963

## Question
### Request description

Bonjour,

Quand on est sur un formulaire assez long où on doit scroller pour aller voir les onglets en bas du formulaire, si on clique sur un onglet pour afficher son contenu la page remonte toute seule en haut (focus sur le premier champ du formulaire). On doit alors scroller de nouveau tout en bas pour consulter le contenu de l'onglet.

Ce comportement n'est pas présent quand on utilise le fil d'ariane car le focus n'est pas positionné sur le premier champ.


### Steps to reproduce

Avec le module de démo.

1. J'ouvre le formulaire d'un produit.
2. Je clique sur "Etendre" pour augmenter la longueur du formulaire.
3. Je clique sur l'onglet "Commandes".
4. Le formulaire remonte automatiquement au niveau du premier champ du formulaire qui a conservé le focus.

Sur les petits formulaires ça ne pose pas trop de problèmes, mais on a des formulaires assez long sur certaines applications où ce comportement rend la navigation moins agréable puisqu'on doit systématiquement retourner en bas de la page quand on navigue entre plusieurs sous-onglets.

Vidéo :

![Simplicite_v53_onglets_page_qui_remonte|video](upload://is6E3e3e5ldIuoJpALH55e9HFBp.mp4)

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
SystemDate=2023-10-02 09:14:40

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-10-02 09:02:05

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
HeapFree=216592
HeapSize=501760
HeapMaxSize=2007040
TotalFreeSize=1721872

[Cache]
ObjectCache=262
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=262
ProcessCacheMax=10000
ProcessCacheRatio=2
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.12 (Debian 13.12-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.6.0
DBDate=2023-10-02 09:14:40
DBDateOffset=0
DBPatchLevel=5;P03;eae816e5089006449212ca1f2a1fc9f4
UsingBLOBs=true

[Healthcheck]
Date=2023-10-02 09:14:40
ElapsedTime=10
```
[/details]

## Answer
Ce sera corrigé en 5.3.17
le scroll-y forcé, une fois le formulaire rechargé, repassera après la prise de focus mise en place dernièrement.
