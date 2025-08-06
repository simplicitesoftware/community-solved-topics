# Webservice - Authorization avec un contenu Bearer + token (token non Simplicité)

**URL:** https://community.simplicite.io/t/7994

## Question
### Request description

Bonjour,
Dans le cadre de la mise œuvre d'un webservice "habilitation public" permettant la création d'un user, nous avons dans l'entête une entrée Authorization avec un contenu Bearer +token (le token est non Simplicité). Nativement, le socle essaie de valider le token via JWT. Comment peut-on bypasser cette vérification ? la validation du token se faisant par un système spécifique au client.

Utilisation de la class : RESTServiceExternalObject

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.31
BuiltOn=2024-03-15 13:56
Git=5.3/0ccf142afa4e52dbd9ac3d0e72cb527a5ca11e22
Encoding=UTF-8
EndpointIP=10.105.64.27
EndpointURL=http://alpha:8080/simplicite
TimeZone=Europe/Paris
SystemDate=2024-03-29 09:53:54

[Application]
ApplicationVersion=0.2
ContextPath=/simplicite
ContextURL=https://alpha.fr/simplicite
ActiveSessions=2
TotalUsers=16
EnabledUsers=14
LastLoginDate=2024-03-29 09:52:05

[Server]
ServerInfo=Apache Tomcat/9.0.62.redhat-00017
ServerType=WEB
ServerActiveSessions=0
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=4.18.0-513.18.1.el8_9.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=2977
DiskUsable=2977
DiskTotal=3062

[JavaVM]
Version=17.0.9
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.9+9-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=801977
HeapSize=1048576
HeapMaxSize=2097152
TotalFreeSize=1850553

[Cache]
ObjectCache=419
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=419
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=1
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=14.10
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.1
DBDate=2024-03-29 09:53:54
DBDateOffset=0
DBPatchLevel=5;P03;504b3d3f35216ae713e5bf5df2855321
UsingBLOBs=true

[Healthcheck]
Date=2024-03-29 09:53:54
ElapsedTime=7
```
[/details]

[details="Simplicité logs"]
```text
2024-03-29 09:54:24,556|SIMPLICITE|ERROR||http://alpha:8080/simplicite|/simplicite|ERROR|system|com.simplicite.webapp.servlets.api.ExternalObjectServlet|service||Event: Authentication error: Invalid token
2024-03-29 09:54:24,555|SIMPLICITE|ERROR||http://alpha:8080/simplicite|/simplicite|ECORED0001|system|com.simplicite.webapp.tools.ServletTool|validateJWTToken||Error Unable to process JWT token: The token was expected to have 3 parts, but got 0.
```
[/details]

## Answer
Ca ressemble de plus en plus à un endpoint token info  OpenIDConnect

Il faut donc juste parametrer l'URL de ce endpoint sur ton provider + les mappings et pas besoin d'implementer quoi que ce soit de specifique

Cf.[ Generic OpenIDConnect provider settings](https://docs.simplicite.io/docs/authentication/oauth2#openidconnect)
