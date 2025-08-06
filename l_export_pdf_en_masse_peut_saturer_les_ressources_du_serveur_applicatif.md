# L'export PDF en masse peut saturer les ressources du serveur applicatif

**URL:** https://community.simplicite.io/t/7600

## Question
### Request description

Bonjour,

Nous constatons lors de l'export en masse PDF standard d'un nombre très important de lignes (+30 000 par exemple) que les ressources CPU et mémoire peuvent être saturé rapidement à la différence de l'export Excel.

Comme pour l'export Excel, est-il possible de mettre en place des mécanismes afin d'optimiser l'utilisation des ressources serveurs afin d'éviter un fort ralentissement qui peut rendre l'application inutilisable ? ou mettre en place des contrôles, des "garde-fous" pour éviter cette situation ?

J'ai vu en v6 qu'on pourra choisir les exports standard qu'on souhaite garder au niveau d'un objet métier, est-ce qu'il sera possible d'autoriser un type d'export pour des utilisateurs appertenant à un certain groupe et l'interdire pour les autres par exemple ?


https://community.simplicite.io/t/xxl-publications/6017

### Steps to reproduce

Avec le module de Démo, j'ai créé plus de 60 000 commandes.

1. Je lance l'export en masse de la totalité des commandes au format PDF :

![image|690x182](upload://mtqvikPfYtvWxIwJsDFlRtiWVAi.png)

Au début de l'export ça semble aller, dans mon cas max heap reste vers 50% et heap reste en dessous de 50% :

![image|690x301](upload://iMH1xnOJYRXgWvOIGhop3hbWnji.png)

2. Mais une fois que le toast d'export affiche la totalité des lignes exportés, max heap monte à 100% et heap est très proche de 100% :

![image|269x85](upload://dVjgbgkiYgM9YJ1hRP9ujf6pR8H.png)

![image|690x290](upload://vG9PON4crO52DOqNdy5dZYJaMzs.png)

![image|690x85](upload://yWnqxVrngXpwBGL9QQF3Wh04fM9.png)

Avec le module de démo l'application reste utilisable dans le cas décrit (je n'ai pas poussé mes tests plus loin pour voir les limites) mais sur des applications où on fait le même test avec un objet plus complexe qui a plus de 200 attributs d'objets avec des champs raportés provenant d'une dizaines d'objets liés l'application ralentit énormément et n'est plus utilisable.

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.26
BuiltOn=2024-01-17 18:40
Git=5.3/e677e6d52927d1cb8aca6330c82c5616dc62ca90
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2024-01-26 10:47:23

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=2
TotalUsers=7
EnabledUsers=5
LastLoginDate=2024-01-26 10:46:25

[Server]
ServerInfo=Apache Tomcat/9.0.85
ServerType=WEB
ServerActiveSessions=3
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.105.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.9
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.9+9
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=422818
HeapSize=1048576
HeapMaxSize=2007040
TotalFreeSize=1381282

[Cache]
ObjectCache=388
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=388
ProcessCacheMax=10000
ProcessCacheRatio=3
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.13 (Debian 13.13-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.1
DBDate=2024-01-26 10:47:23
DBDateOffset=0
DBPatchLevel=5;P03;4aca705f0c03390774341693f64d5c3d
UsingBLOBs=true

[Healthcheck]
Date=2024-01-26 10:47:23
ElapsedTime=8
```
[/details]

## Answer
Bonjour,

Certains exports ont pu être optimisés
- car leurs API supportent la bufferisation/serialisation en garantissant un usage du heap paramétrable
- les "search" de simplicité sont également paginés pour ne pas monter tout l'objet (table+joins) en mémoire.

Le cas des export PDF reste le vilain canard qui n'a pas pu évoluer vers ce genre d'interface car utilise encore `iText` qui est en fin de vie, tout le PDF est en mémoire avant d'être exporté en fichier. 

On prévoit de passer sur `PdfBox` en V6, cette lib possède des `MemoryUsageSetting` qui permetteeont à priori de maitriser l'espace mémoire utilisé (mais pas forcement la CPU).

Exporter "la base de données" via la UI posera toujours des problèmes de perfs et d'écologie.
Il convient de revoir ces process si c'est récurent, afin de faire des exports "off" en back (batch sql...) et les mettre à disposition quelque part pour l'utilisateur. Passer par du TP/usage UI n'est pas forcement adapté.

En V6, le champ export (yes/no) devient un ENUM multiple. Il est donc possible de changer les valeurs possibles pour un groupe donné dans le postLoad de l'objet.

`obj.setExportMedias("CSV;PDF;XLS;ZIP")`

ou avec le hook plus précis par mode / media / rowId :

```
/**
 * Is requested export allowed?
 * @param mode ObjectXML.MODE_* full | form | list | pref
 * @param media ServletTool.MEDIA_*
 * @param rowId Optional ID (form export)
 * @return Error to denied export, Warning to confirm on UI or null to allow export
 */
public String isExportAllowed(String mode, String media, String rowId)`
```
