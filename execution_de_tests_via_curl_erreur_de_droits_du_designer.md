# Execution de tests via curl : erreur de droits du designer

**URL:** https://community.simplicite.io/t/4546

## Question
### Request description
Bonjour,

je voulais executé les tests via curl mais j'ai une erreur de droits.
Commande :

`curl -s -u designer:simplicite --form service=unittests --form object=DateUtilsTests "http://localhost:8080/io"
Non autorisé: DateUtilsTests`

Depuis l'UI le designer peut lancé les tests dont celui là.

![image|690x39](upload://m7f3iOXx9IyL4nJIZmR3xHoul4F.png)
![image|690x391](upload://2VTSGKrMaZZdGwJ8P6jAmmRT3lj.png)
![image|690x287](upload://ddos4CQ9S27NZfBKj9LjIVZCCYU.png)
![image|690x312](upload://ogVCqAAWEZdQ6isQCEldDLKYKhC.png)
![image|690x252](upload://560Nu38DFJu5pUu9f6fPLgp9A9v.png)

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.31
BuiltOn=2022-02-27 16:25
Git=release/8a0f5eefbf9cdfa38659c61d6f565c6883887cee
Encoding=UTF-8
EndpointIP=172.18.0.4
EndpointURL=http://6392e59b2ec5:8080
TimeZone=UTC
SystemDate=2022-03-17 16:33:57

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=http://localhost:8080
ActiveSessions=2
TotalUsers=11
EnabledUsers=9
LastLoginDate=2022-03-17 16:26:07

[Server]
ServerInfo=Apache Tomcat/9.0.58
ServerType=WEB
ServerActiveSessions=3

[OS]
Name=Linux
Architecture=amd64
Version=5.10.76-linuxkit
DockerImageName=centos7
SystemEncoding=UTF-8

[Disk]
DiskFree=54084
DiskUsable=50791
DiskTotal=64250

[JavaVM]
Version=17.0.2
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.2+8
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=99013
HeapSize=328704
HeapMaxSize=509952
TotalFreeSize=280261
```
[/details]

[details="Simplicité logs"]
```text
2022-03-17 16:26:07,324|SIMPLICITE|ERROR||http://6392e59b2ec5:8080||ECORED0001|designer|com.simplicite.util.engine.IntegrationDirect|runUnitTests||Erreur Non autorisé: DateUtilsTests
2022-03-17 16:26:07,323|SIMPLICITE|INFO||http://6392e59b2ec5:8080||INFO|designer|com.simplicite.webapp.servlets.IOServlet|doPost||Evénement: I/O service UNITTESTS...
2022-03-17 16:26:07,226|SIMPLICITE|INFO||http://6392e59b2ec5:8080||ICORED0001|public|com.simplicite.util.Grant|init||Info: public connected, session ID: 9C60532837C6648903B2BCFE4523D414, timeout: 5 min , user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
```
[/details]

Merci pour votre aide
Thierry

## Answer
cf. https://docs.simplicite.io/documentation/02-integration/io-commandline.md#unittests

On parle ici d'un "shared code" de type "unit tests", pas des tests unitaires d'un objet métier.

Donc il faut utiliser `--form test=<test shared code name>` et pas `--form object=<business object name>`
