# Le paramétrage "Liens navigables" n'est pas pris en compte lors de l'affichage pillbox

**URL:** https://community.simplicite.io/t/7686

## Question
### Request description

Bonjour,

Au niveau du paramétrage d'un objet métier, quand je mets "Liens navigables = non", les liens ne sont plus présents dans l'affichage liste et formulaire mais sont toujours présents pour l'affichage pillbox.


### Steps to reproduce

A partir du module de Démo :

1. J'ai créé un objet "DemoCountry" lié à l'objet DemoClient par une relation n-n :

![image|556x499](upload://khOl8Cu8AIfwRBlQA0H1U4XIPnH.png)

2. Au niveau de la table d'association "DemoCouCli", j'ai mis "Liens navigables = non" :

![image|690x323](upload://ftCfJJCTFnw1P7P49Hvj95scCU5.png)

3. Au niveau de la relation d'objet "demoCoucliCliId" dans "DemoClient" j'ai mis "Présentation = Pillbox" :

![image|690x308](upload://7Vqlyqa1oZ066s7ltp8zdhm9M29.png)

4. Dans le formulaire de DemoClient, le lien au niveau des pays est présent. Si je clique sur un pays j'arrive sur le formulaire de celui-ci (DemoCountry) au lieu de rester sur le formulaire où je suis (DemoClient) :

![image|690x185](upload://5MvKDbvVEa9n6zolj3eYiK6lt7E.png)

![image|690x235](upload://rGkmA8ry3RfxoLMf06zZkSo2CF2.png)


![Simplicite_v53_pillbox_lien_navigable_non|video](upload://9q3swgCOpDSOhrVbeIwIqg9SsXB.mp4)

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.27
BuiltOn=2024-01-31 11:28
Git=5.3/0666d5e9ba5ff03705a1491771d7c40b3e049660
Encoding=UTF-8
EndpointIP=172.20.0.3
EndpointURL=http://3fc8d2f3173b:8080
TimeZone=UTC
SystemDate=2024-02-06 13:46:45

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://10.24.160.176:5380
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2024-02-06 13:23:52

[Server]
ServerInfo=Apache Tomcat/9.0.85
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.105.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.10
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.10+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=238409
HeapSize=516096
HeapMaxSize=2007040
TotalFreeSize=1729353

[Cache]
ObjectCache=486
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=486
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.13 (Debian 13.13-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.1
DBDate=2024-02-06 13:46:45
DBDateOffset=0
DBPatchLevel=5;P03;5c8058e37783405af29741d24f91d541
UsingBLOBs=true

[Healthcheck]
Date=2024-02-06 13:46:45
ElapsedTime=9


```
[/details]

## Answer
Reproduit, 
en fait le flag était testé globalement sur l'objet et non pas par record, du coup suivant la navigation le followLink était présent ou pas dans les méta-data.

Il va falloir tester le followLink pour chaque item de la pillbox, car on peut très bien rendre navigable certains items et pas d'autres par hook `canFollowLink`.

On prépare ça pour la 5.3.29.
