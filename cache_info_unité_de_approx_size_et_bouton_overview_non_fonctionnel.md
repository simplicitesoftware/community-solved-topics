# Cache info : Unité de approx size et bouton Overview non fonctionnel

**URL:** https://community.simplicite.io/t/5875

## Question
Bonjour,

Je voudrais savoir quelle est l'unité de la colonne "Approx. size" (en rouge) dans l'objet "Cache info".

![image|690x152](upload://xHPwAMsZ7plIQ8eC3EdcRf0Usvi.png)

Le bouton "Overview" (en jaune) ne marche pas, voici les logs :

> 2023-02-14 09:21:04,987|SIMPLICITE|WARN||http://xxx:8080||WARN|system|com.simplicite.webapp.servlets.ui.JSONServlet|service||Event: Service error
>     java.lang.ClassCastException: class java.math.BigDecimal cannot be cast to class java.lang.String (java.math.BigDecimal and java.lang.String are in module java.base of loader 'bootstrap')
>      at com.simplicite.util.Crosstab$NodeLine.toJSON(Crosstab.java:2876)
>      at com.simplicite.util.Crosstab.toJSONTree(Crosstab.java:1978)
>      at com.simplicite.webapp.tools.JSONServletTool.crosstab(JSONServletTool.java:1894)
>      at com.simplicite.webapp.ObjectJson.crosstab(ObjectJson.java:866)
>      at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:682)
>      at com.simplicite.webapp.servlets.AbstractJSONServlet.service(AbstractJSONServlet.java:102)
>      at javax.servlet.http.HttpServlet.service(HttpServlet.java:779)
>      at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
>      at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
>      at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
>      at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
>      at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
>      at com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter(HTTPHeadersFilter.java:39)
>      at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
>      at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
>      at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
>      at com.simplicite.webapp.filters.AuthMethodFilter.doFilter(AuthMethodFilter.java:220)
>      at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
>      at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
>      at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
>      at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:62)
>      at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
>      at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
>      at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
>      at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:163)
>      at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97)
>      at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:541)
>      at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:135)
>      at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
>      at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
>      at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78)
>      at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:360)
>      at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:399)
>      at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
>      at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:891)
>      at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1784)
>      at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
>      at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
>      at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
>      at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
>      at java.base/java.lang.Thread.run(Thread.java:833)

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.31
BuiltOn=2023-02-09 18:48
Git=5.2/c905191298e741a96e312df877eaabbf42360fc4
Encoding=UTF-8
EndpointIP=10.144.56.75
EndpointURL=http://xxx:8080
TimeZone=Europe/Paris
SystemDate=2023-02-14 09:24:03

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=https://xxx
ActiveSessions=1
TotalUsers=60
EnabledUsers=15
LastLoginDate=2023-02-14 08:34:02

[Server]
ServerInfo=Apache Tomcat/9.0.71
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=5.10.147+
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.6
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.6+10
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=114091
HeapSize=589824
HeapMaxSize=7131136
TotalFreeSize=6655403

[Cache]
ObjectCache=216
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=1
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.16
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.5.3
DBDate=2023-02-14 09:24:03
DBDateOffset=0
DBPatchLevel=5;P02;6f509d25dbd7ab102ca546d83ef68fc8
UsingBLOBs=true

[Healthcheck]
Date=2023-02-14 09:24:03
ElapsedTime=12

```
[/details]

## Answer
Bonjour,

Il y a effectivement une erreur de cast suite au passage en BigDecimal du tableau croisé.
On va corriger.

La taille est un calcul via

> `SizeOfTool.getObjectSize(Object obj, boolean fast)`

qui donne la taille de l'objet sérialisé si `fast = true` ce qui reste une **approximation** en Bytes. 

PS Le caclul de la "vraie" taille mémoire est complexe en Java si fast = false (parcours recursif par reflexion du contenu de l'objet... plus utilisé car trop long à faire sur tous les objets en cache).
