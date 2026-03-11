# Gestion des caractères spéciaux dans les recherches

**URL:** https://community.simplicite.io/t/4553

## Question
### Request description

*----description of the request----*
Nous constatons que si un caractère spécial est stocké dans un champ texte d'une table, alors cela perturbe le bon fonctionnement de l'application. Deux cas d'usage identifiés :
=> soit la recherche plante l'IHM et seule un rafraichissement de la page peut rétablir la situation mais la recherche reste impossible
=> soit la recherche peut se faire mais tous les enregistrements dont au moins un champ contient un caractère spécial n'apparaissent pas dans le résultat de la recherche.

Y a-t-il un contournement ou une piste de solution ?

### Steps to reproduce
chaine de caractère qui peut poser un pb MSCTOTO si elle est stockée dans un champ d'une table

**Nota : le caractère peut ne pas être vu à l'oeil nu entre MSC et TOTO en mode graphique**

### Technical information

[details="Instance /health"]

[Platform]
Status=OK
Version=4.0.P24
BuiltOn=2020-03-09 21:18 (revision 52f72387225102f2eaa20dad7acd604e2792760d)
Encoding=UTF-8
EndpointIP=172.18.0.2
EndpointURL=http://e2951d995dd7:8080
TimeZone=GMT+01:00
SystemDate=2022-03-18 16:06:58

[Application]
ApplicationVersion=4.0
ContextPath=
ContextURL=http://istdsimp.ansm-intra.fr:8080
ActiveSessions=89
TotalUsers=747
EnabledUsers=572
LastLoginDate=

[Server]
ServerInfo=Apache Tomcat/9.0.31
ServerType=WEB
User=root

[OS]
Name=Linux
Architecture=amd64
Version=5.3.18-24.52-default
SystemEncoding=UTF-8

[Disk]
DiskFree=199409
DiskUsable=197421
DiskTotal=255989

[JavaVM]
Version=13.0.2
Vendor=N/A
VMName=OpenJDK 64-Bit Server VM
VMVersion=13.0.2+8
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.11 2019 05 30
HeapFree=2615226
HeapSize=5169152
HeapMaxSize=8388608
TotalFreeSize=5834682

[Cache]
GrantCache=4127
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=2996
ObjectCacheMax=10000
ObjectCacheRatio=29
ProcessCache=2
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=4
ProductName=Oracle
ProductVersion=Oracle Database 18c Standard Edition 2 Release 18.0.0.0.0 - Production
Version 18.3.0.0.0
DriverName=Oracle JDBC driver
DriverVersion=19.3.0.0.0
DBDate=2022-03-18 16:06:58
DBDateOffset=0
DBPatchLevel=P24;52f72387225102f2eaa20dad7acd604e2792760d
UsingBLOBs=true

[Healthcheck]
Date=2022-03-18 16:06:58
ElapsedTime=32


[/details]

[details="Simplicité logs"]
N/A => Rien dans les logs
[/details]

[details="Browser logs"]
N/A => Rien dans les logs
[/details]

[details="Other relevant information"]
N/A 
[/details]

## Answer
Bonjour Hafid, 

Dans ce cas il faudra implémenter dans un hook de validation des données une fonction qui retire ces caractères de contrôle. Par exemple : https://stackoverflow.com/questions/14028716/how-to-remove-control-characters-from-java-string
