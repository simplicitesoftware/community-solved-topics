# Keycloack erreur Invalid client or Invalid client credentials

**URL:** https://community.simplicite.io/t/7918

## Question
### Request description

Bonjour,

A quoi correspond l'erreur 
2024-03-13 10:33:06,808|SIMPLICITE|ERROR||http://SW51649:8080||ERROR|system|com.simplicite.webapp.servlets.OAuth2Servlet|doGet||Evénement: **Invalid client or Invalid client credentials**
com.simplicite.util.exceptions.AuthenticationException: Invalid client or Invalid client credentials

On me confirme que mon client et que mon secret sont bons.

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.24
BuiltOn=2023-12-07 15:59
Git=5.3/29fe55f389cbc517e57851b84b9146b315b93982
Encoding=UTF-8
EndpointIP=10.24.7.102
EndpointURL=http://SW51649:8080
TimeZone=Europe/Paris
SystemDate=2024-03-13 11:25:41

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://XXXXXXXXXX
ActiveSessions=2
TotalUsers=14
EnabledUsers=12
LastLoginDate=2024-03-13 11:25:20

[Server]
ServerInfo=Apache Tomcat/9.0.80
ServerType=WEB
ServerActiveSessions=3
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Windows Server 2022
Architecture=amd64
Version=10.0
SystemEncoding=UTF-8

[Disk]
DiskFree=293635
DiskUsable=293635
DiskTotal=562466

[JavaVM]
Version=17.0.3.1
Vendor=Oracle Corporation
VMName=Java HotSpot(TM) 64-Bit Server VM
VMVersion=17.0.3.1+2-LTS-6
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=1621603
HeapSize=2097152
HeapMaxSize=4194304
TotalFreeSize=3718755

[Cache]
ObjectCache=454
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=454
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
ProductName=MySQL
ProductVersion=5.5.68-MariaDB
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-8.1.0 (Revision: 7b6f9a337afe6ccb41823df485bf848ca7952b09)
DBDate=2024-03-13 11:25:41
DBDateOffset=0
DBPatchLevel=5;P03;6f1cec3ddb7615b1340daf5a9becaab3
UsingBLOBs=true

[Healthcheck]
Date=2024-03-13 11:25:42
ElapsedTime=156

```
[/details]

[details="Simplicité logs"]
```text
2024-03-13 10:33:06,808|SIMPLICITE|ERROR||http://SW51649:8080||ERROR|system|com.simplicite.webapp.servlets.OAuth2Servlet|doGet||Evénement: Invalid client or Invalid client credentials
com.simplicite.util.exceptions.AuthenticationException: Invalid client or Invalid client credentials
	at com.simplicite.webapp.servlets.OAuth2Servlet.callback(OAuth2Servlet.java:922)
	at com.simplicite.webapp.servlets.OAuth2Servlet.doGet(OAuth2Servlet.java:1135)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:529)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:623)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:209)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:153)
	at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:51)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:178)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:153)
	at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:68)
	at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:178)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:153)
	at com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter(HTTPHeadersFilter.java:39)
	at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:178)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:153)
	at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:156)
	at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:90)
	at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:481)
	at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:130)
	at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:93)
	at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:670)
	at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:74)
	at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:343)
	at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:390)
	at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:63)
	at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:926)
	at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1790)
	at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:52)
	at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
	at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
	at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
	at java.base/java.lang.Thread.run(Thread.java:833)

```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Ce message n'est pas un message généré par Simplicité, c'est le message reçu de l'IdP lors de l'appel au endpoint token info.

Il y a 2 modes possibles pour passer les credentials à ce endpoint, cf. https://docs.simplicite.io/docs/authentication/oauth2#openidconnect => setting `client_credentials_mode`, vous ne devez pas utiliser le bon mode vs la manière dont votre votre IdP est configuré.

De manière générale, pour y voir plus clair sur ce qu'il se passe pendant la séquence d'ident/authent il faut activer le log event `DAUTHSC001`. ATTENTION: à désactiver **impérativement** une fois que tout fonctionne.
