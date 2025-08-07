# Git push depuis simplicité ne pousse que vers master

**URL:** https://community.simplicite.io/t/6333

## Question
Bonjour,

J'ai récemment intégré à simplicité un repo gitlab pour stocker notre avancement : 

![image|653x378, 75%](upload://cfws3VWuXfELlgSD8dc3cl7nvHu.png)

Sur ce repo j'ai 2 branches, une master et une develop, et je voudrais utiliser cette dernière, comme en témoigne la capture ci-dessus.
Cependant lorsque je clique sur "push", la branche qui est mise à jour sur le serveur gitlab est celle de master.
![image|690x74](upload://xIaUYZKfoSwK3YtLqHdf6I0F6gq.png)
Depuis mon environnement de travail, la branche develop est pourtant bien accessible et modifiable.
Le fait que le serveur git local utilise "master" écrase t-il la configuration dans les paramètres?

Également, depuis mon IDE InteliJ, lorsque je push vers le serveur localhost gitlab, celui-ci push également vers le serveur gitlab distant. Est-il possible d'empêcher ce double push et d'avoir un comportement comme suit:

* modifications locales
* push vers http://localhost:8080/git/ladnext
* vérification manuelle des fichiers commités (coup d’œil)
* appuyer sur push -> modifications envoyées sur la branche develop ou master ( spécifié dans paramètres) du serveur gitlab distant

Bien Cordialement,

Clément

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.2.34
BuiltOn=2023-03-13 16:54
Git=5.2/8cf8688af7cd3e007a96621540535e34c4f3abf2
Encoding=UTF-8
EndpointIP=172.18.0.6
EndpointURL=http://5bd05640b444:8080
TimeZone=UTC
SystemDate=2023-05-04 13:57:41

[Application]
ApplicationVersion=2.4.6
ContextPath=
ContextURL=http://localhost:8080
ActiveSessions=1
TotalUsers=13
EnabledUsers=10
LastLoginDate=2023-05-04 13:51:48

[Server]
ServerInfo=Apache Tomcat/9.0.73
ServerType=WEB
ServerActiveSessions=4
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=5.10.102.1-microsoft-standard-WSL2
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.6
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.6+10
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=252081
HeapSize=753664
HeapMaxSize=6529024
TotalFreeSize=6027441

[Cache]
ObjectCache=393
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.6 (Debian 13.6-1.pgdg110+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.5.4
DBDate=2023-05-04 13:57:41
DBDateOffset=0
DBPatchLevel=5;P02;14f8034ce5a285931ca480a5451ce96e
UsingBLOBs=true

[Healthcheck]
Date=2023-05-04 13:57:42
ElapsedTime=121


```
[/details]

## Answer
cf. https://docs.simplicite.io/documentation/02-integration/git-repositories.md#branch

Le "branch" n'est pas au bon endroit dans le JSON
