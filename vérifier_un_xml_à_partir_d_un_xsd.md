# Vérifier un XML à partir d'un XSD

**URL:** https://community.simplicite.io/t/5559

## Question
Bonjour,

Existe t'il une méthode pour vérifier l'intégrité d'un fichier XML à l'aide d'un fichier XSD ?

J'ai trouvé la classe https://docs.simplicite.io/5/javadoc/com/simplicite/util/tools/XSDTool.html

Mais je n'ai pas trouvé de méthode spécifique.

Si jamais vous avez un exemple, je suis preneur.

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.1.54
BuiltOn=2022-10-31 15:49
Git=5.1/06cc2793ebaaa50ddf3f3dee2251b397d7bdc09b
Encoding=UTF-8
EndpointIP=10.144.21.118
EndpointURL=http://mla-api-6ff6c94c9-gccmk:8080
TimeZone=Europe/Paris
SystemDate=2022-11-30 15:52:27

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=https://api-mla.gke.ope.gcp.renault.com
ActiveSessions=50
TotalUsers=477
EnabledUsers=476
LastLoginDate=2022-11-30 15:50:08

[Server]
ServerInfo=Apache Tomcat/9.0.68
ServerType=WEB
ServerActiveSessions=51

[OS]
Name=Linux
Architecture=amd64
Version=5.10.133+
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.5
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.5+8
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=1669888
HeapSize=2785280
HeapMaxSize=14262272
TotalFreeSize=13146880

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=3586
ObjectCacheMax=10000
ObjectCacheRatio=35
ProcessCache=16
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.13
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.5.0
DBDate=2022-11-30 15:52:27
DBDateOffset=0
DBPatchLevel=5;P01;1aa3e07e98e9b46a7bb1f2d6d409c032
UsingBLOBs=true

[Healthcheck]
Date=2022-11-30 15:52:27
ElapsedTime=10

```
[/details]

## Answer
Bonjour,

Oui rien de spécifique à Simplicité.

Votre parser va nécessairement implémenter le XSD attendu, donc ça ne sert à priori à rien de faire un check avant. Sinon vous pouvez surement l'implémenter via des Validator simplement en java avant d'importer, sinon l'import générera des exceptions.

https://stackoverflow.com/questions/15732/how-to-validate-an-xml-file-against-an-xsd-file
