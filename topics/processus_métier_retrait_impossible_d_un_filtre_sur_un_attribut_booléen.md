# Processus métier : Retrait impossible d'un filtre sur un attribut booléen

**URL:** https://community.simplicite.io/t/8569

## Question
### Request description

Bonjour, 

Dans un processus métier, lors d'une sélection d'objet, il est impossible de retirer un filtre sur un champ de type booléen.

### Steps to reproduce

J'ai placé dans un premier temps le booléen Important à non. Si je clique sur la flèche ou sur la valeur vide, le filtre ne se retire pas, sa valeur retourne par défaut à non.
Je précise que mon attribut n'est pas obligatoire.
![image|690x172, 75%](upload://zTZ7BIilf9wvbRhGKdzkHMa9fh7.png)

Merci à vous.

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.1.0-beta
BuiltOn=2024-07-01 11:00
Git=6.1/80ee293b8d321eeb0c4998473013038e7f3244d6
Encoding=UTF-8
EndpointIP=172.22.0.11
EndpointURL=http://b79c39be8e32:8080
TimeZone=UTC
SystemDate=2024-07-31 09:39:43

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2024-07-31 09:29:28

[Server]
ServerInfo=Apache Tomcat/9.0.89
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=4.18.0-553.8.1.el8_10.x86_64
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=21.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.3+9-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=77937
HeapSize=301056
HeapMaxSize=1996800
TotalFreeSize=1773681

[Cache]
ObjectCache=463
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=463
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=14.12 (Debian 14.12-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.3
DBDate=2024-07-31 09:39:43
DBDateOffset=0
DBPatchLevel=6;P01c;dd6af46c64e2d06532fbd02a716b883c;0-beta
UsingBLOBs=true

[Healthcheck]
Date=2024-07-31 09:39:44
ElapsedTime=756

```
[/details]

## Answer
Le problème a été reproduit et sera corrigé en 6.1.2.

Le back ne gérait pas bien le filtre "%" envoyé par le front sur un booléen, et le considérait comme false, alors que cette valeur indique "pas de filtre".
