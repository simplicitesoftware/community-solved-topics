# Redirection vers objet externe dans parseAuth

**URL:** https://community.simplicite.io/t/5842

## Question
### Request description

Bonjour,

Est-il possible de rediriger un utilisateur vers un objet externe publique si dans le parseAuth on ne trouve pas de login pour l'utilisateur ?


### Steps to reproduce


1. L'utilisateur se connecte via un SSO OpenIdConnect.
2. Dans parseAuth, je récupère le login envoyé par le SSO et je vérifie si un compte existe dans l'application avec ce login.
3. Si le login existe, l'utilisateur accède à l'application.
4. Si le login n'existe pas, j'aimerai rediriger l'utilisateur vers un objet externe publique avec un message lui indiquant de contacter l'administrateur.

Pour customAuth je peux le faire avec la méthode sendRedirect() de HttpServletResponse, mais pour parseAuth je n'ai pas trouvé d'équivalent. Est-ce que je dois le faire dans un autre hook ?

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=4.0.P25
BuiltOn=2022-11-10 00:35 (revision c04f307ce401ed97b3fd1ab3e21c2d43d05f9894)
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2023-02-06 15:45:15

[Application]
ApplicationVersion=4.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=5
EnabledUsers=4
LastLoginDate=

[Server]
ServerInfo=Apache Tomcat/9.0.68
ServerType=WEB
User=root

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.59.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[Disk]
DiskFree=21998
DiskUsable=21998
DiskTotal=30702

[JavaVM]
Version=17.0.5
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.5+8
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=194684
HeapSize=508928
HeapMaxSize=2097152
TotalFreeSize=1782908

[Cache]
GrantCache=22
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=254
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=2
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.9 (Debian 13.9-1.pgdg110+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.5.0
DBDate=2023-02-06 15:45:15
DBDateOffset=0
DBPatchLevel=4.0;P25;572ca2253ecf00be6c90c8dd7259db11
UsingBLOBs=true

[Healthcheck]
Date=2023-02-06 15:45:16
ElapsedTime=168
```
[/details]

## Answer
Bonjour Florent, 

Je ne sais pas si un tel mécanisme est possible. 
En revanche tu peux peut-être contourner en retournant le login d'un user "générique" dans le `parseAuth` si le compte n'existe pas. Ce login de user "générique" aurait comme page d'accueil ton ton objet externe indiquant de contacter l'admin.
