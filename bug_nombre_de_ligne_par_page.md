# Bug nombre de ligne par page

**URL:** https://community.simplicite.io/t/9938

## Question
Bonjour,

On a réalisé une migration de la 5.3 à la 6.1 (on va migrer en 6.2 prochainement) et depuis cette migration, on possède un bug d'affichage sur le nombre de ligne par page qui affiche le même choix en doublon.  

[grid]
![image|608x111](upload://ufMKldcHT30cKtpa4XwYJQE3gAU.png)
![image|587x109](upload://kR8rDBme5YMHNLm2wwIy1xui7gu.png)
[/grid]

J'ai appris via ce post que le min/max était défini sur le formulaire user, puis en vérifiant les données utilisateurs, les paramètres sont bien présents et l'user possède bien ce min/max par défaut (20 et 50). Par conséquent - le problème est ailleurs. 

[quote="scampano, post:2, topic:2318"]
Il y a uniquement un min et un max défini sur le formulaire user. Vous pouvez donc:

* changer la valeur par défaut pour les Fields usr_minrows et usr_maxrows pour avoir 5 et 50 par exemple, mais pas de valeurs intermédiaires
[/quote]

Par contre, en réalisant une surcharge sur une classe métier pour les champs obo_minrows et obo_maxrows, on retrouve bien le comportement attendu et il n'y a plus ce problème. 

On dirait que les champs usr_minrows et usr_maxrows ne sont plus du tout valorisé. Est-ce possible que la migration a réalisé une régression ?

Le bug est présent sur l'ensemble des objets métiers de l'application et des objets métiers Simplicité (Domaines, Attributs, etc). Et on ne réalise aucune modification dans le preCreate. 

[quote="scampano, post:2, topic:2318"]
si vous gérez les utilisateurs avec un héritier du user, forcer ces valeurs dans le preCreate.
[/quote]

Je reste entièrement disponible pour plus d'info.

Merci d'avance pour votre aide et belle journée !!

[details="Health check"]
[Platform]
Status=OK
Version=6.1.25
BuiltOn=2025-03-19 09:22
Git=6.1/58e447d66b47ae2064aad08dfe90962467b28091
Encoding=UTF-8
EndpointIP=127.0.0.1
EndpointURL=https://dev-sim:10593/forpro
TimeZone=Europe/Paris
SystemDate=2025-05-15 09:22:07

[Application]
ApplicationVersion=1.0.0
ContextPath=/forpro
ContextURL=https://dev.bretagne.bzh/forpro
ActiveSessions=1
TotalUsers=40
EnabledUsers=38
LastLoginDate=2025-05-15 08:43:38

[Server]
ServerInfo=Apache Tomcat/9.0.102
ServerType=WEB
ServerActiveSessions=0
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1062.9.1.el7.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=7257
DiskUsable=4837
DiskTotal=57303

[JavaVM]
Version=11.0.6
Vendor=Oracle Corporation
VMName=OpenJDK 64-Bit Server VM
VMVersion=11.0.6+10-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=263023
HeapSize=422912
HeapMaxSize=524288
TotalFreeSize=364399

[Cache]
ObjectCache=361
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
VendorName=mysql
ProductName=MySQL
ProductVersion=5.5.5-10.2.9-MariaDB-10.2.9+maria~stretch
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-9.2.0 (Revision: a3909bfeb62d5a517ab444bb88ba7ecf26100297)
DBDate=2025-05-15 09:22:07
DBDateOffset=0
DBPatchLevel=6;P01;447d63ac17211349eca5a5d0b5eab9ff;25
UsingBLOBs=true

[Healthcheck]
Date=2025-05-15 09:22:07
ElapsedTime=221
[/details]

## Answer
Ok, tiens nous au courant.

C'est sûr que la UI pourrait retirer ce selectbox si min=max rows, on n'a jamais rencontré ce cas d'usage mais ça fait sens en terme d'UX.

Sinon pour voir dans tout le code du/des modules, via la UI c'est compliqué d'ouvrir tous les fichiers, il faut :
- soit les cloner dans un IDE et utiliser sa fonction de recherche
- soit chercher dans un export en fichier texte (xml ou json), le code est exporté dans des blocks CDATA.

Il y a peut-être un setMinRow/seMaxRows quelque part.
