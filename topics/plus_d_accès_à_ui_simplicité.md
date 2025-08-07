# Plus d'accès à UI simplicité

**URL:** https://community.simplicite.io/t/3320

## Question
Bonjour,
suite changement de configuration DOC_DB en mettant valeur remplacée c:/dbdoc je n'ai plus d'accès à l'ui, j'ai l'erreur :
2021-05-17 16:27:34,956 INFO [com.simplicite.util.Grant] SIMPLICITE|http://2f05d3f34fba:8080||ICORED0001|public|com.simplicite.util.Grant|init||Info: public connected, session ID: 3352A87725548C5654C23608DAE7057B, timeout: 5 min , user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0
2021-05-17 16:26:35,902 ERROR [com.simplicite.webapp.servlets.ui.ResourceServlet] SIMPLICITE|http://2f05d3f34fba:8080||ERROR|designer|com.simplicite.webapp.servlets.ui.ResourceServlet|doGet||Evénement: Resource not found: missing file in {
     "code": "MAIN",
     "cached": true,
     "id": "260",
     "type": "HTML",
     "doc_id": "2281"
    }
    com.simplicite.util.exceptions.NotFoundException: missing file in {
     "code": "MAIN",
     "cached": true,
     "id": "260",
     "type": "HTML",
     "doc_id": "2281"
    }
     at com.simplicite.webapp.WebServicesFactory.streamResource(WebServicesFactory.java:2707)
     at com.simplicite.webapp.servlets.ui.ResourceServlet.doGet(ResourceServlet.java:55)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:626)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:733)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:86)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter(HTTPHeadersFilter.java:39)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:188)
     at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97)
     at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:542)
     at com.simplicite.tomcat.valves.APISessionValve.invoke(APISessionValve.java:192)
     at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:143)
     at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
     at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
     at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78)
     at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:357)
     at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:374)
     at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
     at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:893)
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1707)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1130)
     at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:630)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:831)
2021-05-17 16:26:35,897 ERROR [com.simplicite.webapp.servlets.ui.ResourceServlet] 

Pouvez m'indiquer ce que je dois faire et d'ou vient l'erreur ?
Thierry

## Answer
C'est une base mariadb, local. Je voulais éviter d'installer un client maria et j'esperais avoir accès via un endpoint. 
La commande io avec la mise à null de sys_value2 à régler mon pb.
A la base j'ai juste mis une valeur remplacée sur un dossier qui n'existait pas.

curl -u designer:simplicite --form service=sqlscript --form file=@update_null_doc_dir.sql --form log=true  http://localhost:81/io
Merci
