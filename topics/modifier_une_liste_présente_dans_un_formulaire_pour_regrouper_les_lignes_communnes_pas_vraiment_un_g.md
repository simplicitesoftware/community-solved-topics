# Modifier une liste présente dans un formulaire pour regrouper les lignes communnes. (pas vraiment un group by)

**URL:** https://community.simplicite.io/t/5326

## Question
Bonjour,

Je requiers un peu d'assistance dans le développement d'une évolution sur STD pour l'ANSM.
Il me semble que vous avez participé au développement de cette application.
Il s'agit d'ailleur d'une feature abandonnée suite à des comportements non voulus de cette évolution.

Le modèle est le suivant:
Un objet dossier comporte, entre autre, des codes de modification et des étapes.
Une étape d'un dossier contient des pièces justificatives elles mêmes liées aux codes de modifications associées au dossier de cette étape.

La demande:
Il faudrait que les PJ communes à plusieurs codes de modification d'un même dossier soient regroupés entre elles, puis que les autres PJ soient regroupées par leur code de modification.

Mon idée de départ:

1. Lors de l'initList des PJ, regarder le parent pour confirmer que je suis bien dans l'objet étape.
Récuperer le dossier et donc les différents  codes de modifications:
   Les parcourirs et récupérer les PJ communnes.
   Les retirer de la list de base
Et c'est là ou je sèche un peu, comment je pourrais faire niveau front? il faut que je créer une autre vue que je rajoute dans le template de l'étape? et si oui de quelle manière je dois la peupler avec les PJ que j'ai isolé? Ou je peux modifier d'une autre manière celle déja présente dans le template d'étape pour afficher les PJ comme je l'entend (le client semble attendre cette solution)?

J'espère avoir été clair, je reste à disposotion pour plus de précisions et je suis ouvert à toutes suggestions.

Cordialement,
Guillaume.

### Technical information

[details="Instance /health"]

[Platform]
Status=OK
Version=5.1.30
BuiltOn=2022-02-22 17:20
Git=release/131ccaa2f66a6b8c713377febeda0f5ec566f3de
Encoding=UTF-8
EndpointIP=172.22.0.3
EndpointURL=http://e454eed0ce9c:8080
TimeZone=Europe/Paris
SystemDate=2022-09-30 11:12:11

[Application]
ApplicationVersion=2.0.0
ContextPath=
ContextURL=http://10.24.160.175:823
ActiveSessions=1
TotalUsers=10
EnabledUsers=9
LastLoginDate=2022-09-30 10:15:31

[Server]
ServerInfo=Apache Tomcat/9.0.58
ServerType=WEB
ServerActiveSessions=4

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.76.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[Disk]
DiskFree=8745
DiskUsable=3609
DiskTotal=100663

[JavaVM]
Version=17.0.2
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.2+8
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=115110
HeapSize=362496
HeapMaxSize=2007040
TotalFreeSize=1759654

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=29
ObjectCacheMax=10000
ObjectCacheRatio=0
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=4
ProductName=Oracle
ProductVersion=Oracle Database 18c Express Edition Release 18.0.0.0.0 - Production
Version 18.4.0.0.0
DriverName=Oracle JDBC driver
DriverVersion=21.1.0.0.0
DBDate=2022-09-30 09:12:11
DBDateOffset=-7200
DBPatchLevel=5;P01;3912ca6c44bd2eba0e0b0ca850d8e290
UsingBLOBs=true

[Healthcheck]
Date=2022-09-30 11:12:11
ElapsedTime=14


[/details]

## Answer
Bonjour, 

Cette fonctionnalité a déjà été implémentée mais n'est pas stable / optimisée / testée.
Elle se situe dans la méthode `createJustifsOfCm(String cmId, String dossId)` de l'objet `StdCodeModifDoss` et donc a été commentée mais l'algo reste disponible.

Lorsqu'un code de modification est associé à un dossier, la liste des pj est générée automatiquement au niveau de l'étape de recevabilité. Si deux codes de modification partagent la même pj, au niveau de la liste des pj, les noms des codes de modification sont concténés. 

Il y a également un bout de code appelé par le `postDelete()` mais qui a subi le même traitement.
