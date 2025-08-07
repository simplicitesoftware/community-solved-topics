# Session already invalidated

**URL:** https://community.simplicite.io/t/4877

## Question
Simplicité 5.1.43

Bonjour, depuis une semaine environ,  les logs nous pondent cette stack régulièrement sans en connaitre la cause et a priori sans anomalie induite. Nous n'avons pas de step pour reproduire cette stack. Cela peut il provenir de récente corrections de votre part ? 

Merci d'avance


```
2022-05-18 07:44:54,616|SIMPLICITE|ERROR||http://ip-172-18-12-2.eu-west-3.compute.internal:8080||ERROR|system|com.simplicite.webapp.servlets.ui.MainPublicServlet|service||Event: [1]
    java.lang.IllegalStateException: invalidate: Session already invalidated
     at org.apache.catalina.session.StandardSession.invalidate(StandardSession.java:1233)
     at org.apache.catalina.session.StandardSessionFacade.invalidate(StandardSessionFacade.java:170)
     at com.simplicite.webapp.servlets.ui.MainPublicServlet.service(MainPublicServlet.java:348)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:764)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter(HTTPHeadersFilter.java:39)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:86)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:183)
     at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97)
     at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:541)
     at com.simplicite.tomcat.valves.APISessionValve.invoke(APISessionValve.java:242)
     at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:135)
     at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
     at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
     at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78)
     at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:360)
     at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:399)
     at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
     at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:890)
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1743)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:833)
```

## Answer
Je ne vois rien de directement lié à ce stacktrace qui ait été modifié récemment.

D'après la ligne du stacktrace ça semble être lié à un logout UI (`/logout`) , vous confirmez ? 

Si oui le `session.invalidate()` incriminé est peut être surabondant car, en fct de la manière dont est configuré votre ident/authent la session a peut être déjà été invalidée avant d'arriver à cet appel final pendant le logout.

Comme c'est la toute dernière instruction et que ça dit juste que la session est déjà invalide c'est à priori sans gravité.

On va juste ajouter un try catch pour `IllegalStateException` afin de ne cracher qu'un warning propre dans ce cas.
