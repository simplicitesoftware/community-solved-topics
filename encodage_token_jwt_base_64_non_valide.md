# Encodage Token JWT base 64 non valide

**URL:** https://community.simplicite.io/t/6985

## Question
Bonjour,

Nous avons récemment migré de version 5.2.34 vers la 5.3.16. Nous rencontrons une erreur dans les Logs simplicité concernant la validité du token pour l'interconnexion des différentes briques de notre application.

Nous utilisons un token simplicité JWT avec la configuration suivante :

USERTOKENS_DURATION : 90d
USERTOKENS_ISSUER : Simplicite
USERTOKENS_MODE : jwt
USERTOKENS_SIGNATURE_SECRET : (renseigné)
USERTOKENS_URL_PARAM :_x_simplicite_authorization_
USE_USERTOKENS : yes

Le token expire début 2024 donc pas de soucis là dessus.
![image|690x115](upload://kkprsUYbag4O5AkzOxgUJNri6YY.png)

Nous avons déjà redémarré nos services plusieurs fois, mais le problème est récurrent, dès le démarrage de simplicité. 
Nos autres briques de l'application récupèrent correctement le token, donc ce n'est pas une histoire d'endpoint, Avez vous une idée sur le problème ?

Merci

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.16
BuiltOn=2023-09-29 15:24
Git=5.3/ada6e86492cace177cb57b570853c82fab936aab
Encoding=UTF-8
EndpointIP=169.254.129.5
EndpointURL=http://47081107d0b9:8080
TimeZone=UTC
SystemDate=2023-10-06 10:31:14

[Application]
ApplicationVersion=2.4.102
ContextPath=
ContextURL=https://agent-recette.ladom.fr
ActiveSessions=2
TotalUsers=14
EnabledUsers=10
LastLoginDate=2023-10-06 10:14:57

[Server]
ServerInfo=Apache Tomcat/9.0.80
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=5.15.116.1-1.cm2
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.8.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.8.1+1
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=160722
HeapSize=549888
HeapMaxSize=1673216
TotalFreeSize=1284050

[Cache]
ObjectCache=781
ObjectCacheMax=10000
ObjectCacheRatio=7
ProcessCache=781
ProcessCacheMax=10000
ProcessCacheRatio=7
APIGrantCache=1
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.11
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.6.0
DBDate=2023-10-06 10:31:14
DBDateOffset=0
DBPatchLevel=5;P03;eae816e5089006449212ca1f2a1fc9f4
UsingBLOBs=false

[Healthcheck]
Date=2023-10-06 10:31:14
ElapsedTime=35

```
[/details]

[details="Simplicité logs"]
```text
2023-10-06 12:28:26,194|SIMPLICITE|ERROR||http://47081107d0b9:8080||ECORED0001|system|com.simplicite.webapp.tools.ServletTool|validateJWTToken||Error Unable to process JWT token: The input is not a valid base 64 encoded string.
2023-10-06 12:28:17,846|SIMPLICITE|ERROR||http://47081107d0b9:8080||ECORED0001|system|com.simplicite.webapp.tools.ServletTool|validateJWTToken||Error Unable to process JWT token: The input is not a valid base 64 encoded string.
2023-10-06 12:28:17,825|SIMPLICITE|ERROR||http://47081107d0b9:8080||ECORED0001|system|com.simplicite.webapp.tools.ServletTool|validateJWTToken||Error Unable to process JWT token: The input is not a valid base 64 encoded string.
2023-10-06 12:28:06,299|SIMPLICITE|ERROR||http://47081107d0b9:8080||ECORED0001|system|com.simplicite.webapp.tools.ServletTool|validateJWTToken||Error Unable to process JWT token: The input is not a valid base 64 encoded string.
```
[/details]

## Answer
Il n'y a pas de différence de code entre la 5.2 à jour et la 5.3 à jour sur la servlet sur `/api/login`.

Pour mémoire exemples d'utilisation:

![image|690x297](upload://kLmoQa5ktKB1lCl4CxBtnM7NP74.png)

La prise en compte du header `Accept: application/json` a été backporté de 5.3 en 5.2 (dans le cadre de la révision 5.2.39) il y a plus de 6 mois. Cela n'a affectivement pas été indiqué dans la release note (c'est désormais ajouté) mais les appels à `/login` n'étaient pas sensés se faire jusque là avec ce header puisque la manière nominale d'obtenir du JSON sur `/login` était le paramètre d'URL `?format=json`.
