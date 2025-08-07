# Erreur SQL étrange

**URL:** https://community.simplicite.io/t/4956

## Question
Simplicité 5.1.44

Bonjour, suite a des tests jmeter executés par le client nous observons une erreur SQL un peu surprenante qui revient régulièrement. Nous ne savons pas trop comment la reproduire ni en identifier là cause, peut être qu'elle vous parle à vous. A priori c'est causé des par des erreur 504 mais on dirait une requête SQL générée par simplicité :

`Error SQL query: jdbc/simplicite: select t.row_id, t.utk_usr_id, t_utk_usr_id.usr_login, t.utk_token, t.utk_refreshtoken, t.utk_type, t.utk_provider, t.utk_clientid, t.utk_creationdate, t.utk_expirydate, t.utk_data from m_user_token t left outer join m_user t_utk_usr_id on (t.utk_usr_id=t_utk_usr_id.row_id) where ( t.utk_token <html t.utk_token >   t.utk_token <head t.utk_token ><title t.utk_token >504 Gateway Time-out t.utk_token </title t.utk_token ></head t.utk_token >   t.utk_token <body t.utk_token >   t.utk_token <center t.utk_token ><h1 t.utk_token >504 Gateway Time-out t.utk_token </h1 t.utk_token ></center t.utk_token >   t.utk_token </body t.utk_token >   t.utk_token </html t.utk_token >) and (t.utk_type='API') order by t.utk_provider asc, t.row_id asc`


```
org.postgresql.util.PSQLException: ERROR: syntax error at or near \"t\"\n  Position: 302at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2675) ~[postgresql-42.3.5.jar:42.3.5]
at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2365) ~[postgresql-42.3.5.jar:42.3.5]
at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:355) ~[postgresql-42.3.5.jar:42.3.5]
at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:490) ~[postgresql-42.3.5.jar:42.3.5]
at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:408) ~[postgresql-42.3.5.jar:42.3.5]
at org.postgresql.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:167) ~[postgresql-42.3.5.jar:42.3.5]
at org.postgresql.jdbc.PgPreparedStatement.executeQuery(PgPreparedStatement.java:119) ~[postgresql-42.3.5.jar:42.3.5]
at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:121) ~[tomcat-dbcp.jar:9.0.62]
at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:121) ~[tomcat-dbcp.jar:9.0.62]
at com.simplicite.util.engine.DBAccess.query(DBAccess.java:622) ~[classes/:?]
at com.simplicite.util.engine.ObjectManager.search(ObjectManager.java:401) ~[classes/:?]
at com.simplicite.util.engine.ObjectManager.search(ObjectManager.java:307) ~[classes/:?]
at com.simplicite.util.engine.ObjectDirect.search(ObjectDirect.java:302) ~[classes/:?]
at com.simplicite.util.ObjectDB.search(ObjectDB.java:877) ~[classes/:?]
at com.simplicite.util.ObjectDB.search(ObjectDB.java:854) ~[classes/:?]
at com.simplicite.objects.System.UserToken.selectFromToken(UserToken.java:128) ~[classes/:?]
at com.simplicite.webapp.tools.ServletTool.getAPIGrant(ServletTool.java:2371) ~[classes/:?]
at com.simplicite.webapp.servlets.api.RESTServlet.initService(RESTServlet.java:41) ~[classes/:?]
at com.simplicite.webapp.servlets.AbstractRESTServlet.getWebServicesFactory(AbstractRESTServlet.java:79) ~[classes/:?]
at com.simplicite.webapp.servlets.AbstractRESTServlet.service(AbstractRESTServlet.java:331) ~[classes/:?]
at javax.servlet.http.HttpServlet.service(HttpServlet.java:764) ~[servlet-api.jar:4.0.FR]
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227) ~[catalina.jar:9.0.62]
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162) ~[catalina.jar:9.0.62]
at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53) ~[tomcat-websocket.jar:9.0.62]
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189) ~[catalina.jar:9.0.62]
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162) ~[catalina.jar:9.0.62]
at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:86) ~[classes/:?]
at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37) ~[classes/:?]
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189) ~[catalina.jar:9.0.62]
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162) ~[catalina.jar:9.0.62]
at com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter(HTTPHeadersFilter.java:39) ~[classes/:?]
at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37) ~[classes/:?]
at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189) ~[catalina.jar:9.0.62]
at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162) ~[catalina.jar:9.0.62]
at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:183) ~[catalina.jar:9.0.62]
at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97) ~[catalina.jar:9.0.62]
at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:541) ~[catalina.jar:9.0.62]
at com.simplicite.tomcat.valves.APISessionValve.invoke(APISessionValve.java:230) ~[simplicite-valves-1.5.9.jar:?]
at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:135) ~[catalina.jar:9.0.62]
at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92) ~[catalina.jar:9.0.62]
at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687) ~[catalina.jar:9.0.62]
at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78) ~[catalina.jar:9.0.62]
at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:360) ~[catalina.jar:9.0.62]
at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:399) ~[tomcat-coyote.jar:9.0.62]
at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65) ~[tomcat-coyote.jar:9.0.62]
at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:890) ~[tomcat-coyote.jar:9.0.62]
at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1743) ~[tomcat-coyote.jar:9.0.62]
at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49) ~[tomcat-coyote.jar:9.0.62]
at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191) ~[tomcat-util.jar:9.0.62]
at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659) ~[tomcat-util.jar:9.0.62]
at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61) ~[tomcat-util.jar:9.0.62]
at java.lang.Thread.run(Thread.java:833) ~[?:?]\n
```

## Answer
**Rectification**: En regardant votre stacktrace je vois qu'on est dans les couches API, donc pas dans le contexte d'une session UI...

Cela dit, là aussi la manière dont sont fait les appels API et la manière dont est configuré le endpoint API peut avoir des conséquences très significatives sur les performances et, donc, sur la capacité de montée en charge dans un contexte d'appels en masse.

- dans tous les cas il faut respecter une séquence d'appel du type login API pour obtenir un token + appel(s) API avec le token tant que celui-ci est valide (ou logout explicite API avec le token pour le flusher).
- le coût machine du login/logout est important donc pour avoir de bonnes performances, notamment sous forte charge il faut éviter des logiques d'appel "unitaire" login+appel+logout et privilégier une logique de réutilisation du token
- si vous utilisez un user technique unique pour de nombreux appels en // il est **impératif** d'activer le pooling d'objets API
- si les données accédées sont souvent les mêmes activer le data caching peut être une bonne chose
- etc.

Bref, sans plus d'infos sur votre besoin et sur ce que vous testez il est impossible pour nous de vous conseiller sur ce qu'il conviendrait de faire idéalement dans votre contexte particulier.

PS: en 5.2 le endpoint API a été fortement refactoré et enrichi (notamment vis à vis de l'usage de tokens d'IdPs externes et les accès public), si vous avez un usage massif des APIs une migration en 5.2 ne peut être que bénéfique.
