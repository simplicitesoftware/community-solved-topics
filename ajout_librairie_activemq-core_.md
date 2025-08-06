# Ajout librairie (activemq-core)

**URL:** https://community.simplicite.io/t/5625

## Question
Bonjour,

Nous voudrions nous assurer de la compatibilité de cette librairie

> activemq-core

avec la pile technologie sous-jacente (principalement la version Java et les dépendances éventuelles à d’autres librairies présentes dans Simplicité).

https://mvnrepository.com/artifact/org.apache.activemq/activemq-core/5.7.0

Merci d'avance pour votre aide.

Benoît

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.1.52
BuiltOn=2022-10-14 15:38
Git=5.1/c6fb125e7bd075a3ba4950ff2d54caff53d171ca
Encoding=UTF-8
EndpointIP=172.20.177.46
EndpointURL=http://mla-api-7d48f57d5-2v8hm:8080
TimeZone=Europe/Paris
SystemDate=2022-12-15 15:43:47

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=https://api-mlasdb.gke.dev.gcp.renault.com
ActiveSessions=0
TotalUsers=4
EnabledUsers=3
LastLoginDate=2022-12-15 15:25:00

[Server]
ServerInfo=Apache Tomcat/9.0.68
ServerType=WEB
ServerActiveSessions=8

[OS]
Name=Linux
Architecture=amd64
Version=5.10.133+
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.4.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.4.1+1
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=472678
HeapSize=753664
HeapMaxSize=7131136
TotalFreeSize=6850150

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=14
ObjectCacheMax=10000
ObjectCacheRatio=0
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.16
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.5.0
DBDate=2022-12-15 15:43:47
DBDateOffset=0
DBPatchLevel=5;P01;1aa3e07e98e9b46a7bb1f2d6d409c032
UsingBLOBs=true

[Healthcheck]
Date=2022-12-15 15:43:47
ElapsedTime=15

```
[/details]

## Answer
Voici l'impact quand on ajoute cette dépendance sur une 5.1 à jour (5.1.55):

![image|690x261](upload://79t3r0Yal1qXGlDhzyBrXLP1BsL.png)

A priori pas de conflit avec les libs déjà embarquées, juste quelques libs additionelles.

Pour rappel voici le process nominal pour builder une image Docker custom avec des dépendances Maven additionnelles: https://community.simplicite.io/t/add-custom-maven-asssited-dependencies-to-your-custom-images/4669
