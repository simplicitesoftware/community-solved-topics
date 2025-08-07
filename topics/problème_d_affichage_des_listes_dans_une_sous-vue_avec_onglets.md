# Problème d'affichage des listes dans une sous-vue avec onglets

**URL:** https://community.simplicite.io/t/8099

## Question
### Request description

Bonjour,

Dans une vue de type "Page d'accueil" j'ai une partie qui permet d'afficher plusieurs onglets affichant des listes pré-filtrées. Parmis ces onglets j'ai un onglet qui permet d'afficher une sous-vue qui contient d'autres onglets affichant des listes pré-filtrées également.

Quand cette sous-vue est le dernier onglet il n'y a pas de problèmes d'affichage mais quand ce n'est pas le cas plusieurs problèmes d'affichages sont présents.

### Steps to reproduce

A partir du module de démo :

1. J'ai fait une copie de la vue "DemoHome" de type "Accueil de domaine" pour pouvoir l'utiliser en tant que page d'accueil. La nouvelle vue s'appelle "DemoHome2" :

![image|690x339](upload://xlsJ6xy4LHF2y59Ph424lJmRQe3.png)

2. J'ai créé une vue simple "DemoSousVue" :

![image|690x339](upload://3KB2VP228r0539YdFJWm6XCyCyf.png)

3. Dans la vue DemoHome2 j'ai ajouté la vue "DemoSousVue" en tant que sous-vue à la position 6 des zones de vue :

![image|690x339](upload://wBTBRHlePE0M7ZrKJ9Elkr7ESlM.png)

![image|690x180](upload://lH6KCSpxj8rVZVyyxgNlmUzIzL1.png)

4. J'ai défini la nouvelle vue DemoHome2 comme page d'accueil du groupe DEMO_ADMIN :

![image|690x339](upload://qX97GRWdlInkTnEs8Xr2xd3VQLw.png)

5. Quand je me connecte avec un utilisateur qui a la responsabilité "DEMO_ADMIN" je constate le comportement suivant :

Le compteur au niveau des onglets s'affiche pour les onglets avant ma sous-vue, mais pas pour ceux après la sous-vue :

![image|690x268](upload://8oI3Uvaiw1iligWacXK4CvIL1Qo.png)

Quand je clique sur l'onglet "Commandes validées" la liste ne s'affiche pas, mais si je clique sur l'onglet "Sous vue" puis sur "Commandes validées" la liste s'affiche :

![Simplicite_v6_ano_sous_vue_1|video](upload://fbulOX5HUGhk2LxPAks92Y4QfHV.mp4)

Quand je rafraichis la page, puis clique sur l'onglet "Sous vue" puis clique sur le bouton "home" les onglets de la sous vue ne sont pas les bons :

![Simplicite_v6_ano_sous_vue_2|video](upload://450BGr5QsTG8S1mds2if2WZ4zmh.mp4)

Quand je rafraichis la page, puis clique sur l'onglet "Commandes validées", puis clique sur le bouton "home" le chargement de la liste reste bloqué :

![Simplicite_v6_ano_sous_vue_3|video](upload://kIPoEkirMK6WMzqmEfSgt2dZyVp.mp4)

Si la sous-vue est le dernier onglet il n'y a pas de problèmes :

![Simplicite_v6_ano_sous_vue_4|video](upload://hvtNOlIK2qlnz7u1xlV9BEpd0XK.mp4)


### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.0.8
BuiltOn=2024-04-17 16:36
Git=6.0/3d30e00e74681f385b873d9afd3c3cbfd2e87a6f
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2024-04-23 08:44:18

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2024-04-23 08:43:58

[Server]
ServerInfo=Apache Tomcat/9.0.88
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=5.15.0-101-generic
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.2
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.2+13-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=140216
HeapSize=434176
HeapMaxSize=2033664
TotalFreeSize=1739704

[Cache]
ObjectCache=200
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=200
ProcessCacheMax=10000
ProcessCacheRatio=2
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=13.14 (Debian 13.14-1.pgdg120+2)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.3
DBDate=2024-04-23 08:44:18
DBDateOffset=0
DBPatchLevel=6;P00;9df481001c41ebbaca0695b412d83ec2;8
UsingBLOBs=true

[Healthcheck]
Date=2024-04-23 08:44:18
ElapsedTime=6
```
[/details]

## Answer
En l'état les onglets se mélangent sans savoir pourquoi, surement un défaut de bootstrap qui s'emmêle les pinceaux tant que les tabs ne sont pas affichés, tout est bien isolé/synchronisé côté Simplicité.

On a revu/contourné le process de chargement pour que la sous-vue soit chargée après les onglets de la vue parente.

A voir si cela corrige ton cas à partir de la 5.3.37 / 6.0.10 à venir.
