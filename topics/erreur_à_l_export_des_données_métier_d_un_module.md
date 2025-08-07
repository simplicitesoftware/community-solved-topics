# Erreur à l'export des données métier d'un module

**URL:** https://community.simplicite.io/t/5465

## Question
### Request description

Bonjour,

Quand j'exporte les DATA sur notre environnement de prod, j'ai l'erreur suivante

![image|690x183](upload://h2kivGXGMr19j9OzZM43CqqSRZb.png)

Je vois de quel objet il s'agit (un objet Historic) mais je n'arrive pas à comprendre l'erreur.

Pouvez vous m'aider ?
Merci !
Emmanuelle


### Technical information

[details="Instance /health"]
```text
Version=4.0.P25
BuiltOn=2022-08-24 11:46 (revision fcb3c9f4bdea7a2dc035ce2f98bbb41bd0fe2bb2)
```
[/details]

[details="Simplicité logs"]
```text
2022-11-08 08:36:17,127 ERROR [com.simplicite.objects.System.Module] SIMPLICITE|http://simplicite-6cc47dc8bc-w9nxs:8080||ERROR|designer|com.simplicite.objects.System.Module|exportData||Event: Error during module RCIB data export
    java.lang.NullPointerException: Cannot invoke "com.simplicite.util.Message.isOk()" because "m" is null
     at com.simplicite.objects.System.Module.exportData(Module.java:779)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
     at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
     at java.base/java.lang.reflect.Method.invoke(Method.java:568)
     at com.simplicite.util.engine.ObjectManager.invokeActionSync(ObjectManager.java:3768)
     at com.simplicite.util.ObjectDirect.invokeAction(ObjectDirect.java:669)
     at com.simplicite.util.ObjectDB.invokeAction(ObjectDB.java:1989)
     at com.simplicite.util.ScriptedObjectDB.invokeAction(ScriptedObjectDB.java:1058)
     at com.simplicite.webapp.tools.JSONServletTool.action(JSONServletTool.java:1678)
     at com.simplicite.webapp.ObjectJson.action(ObjectJson.java:660)
     at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:616)
     at com.simplicite.webapp.servlets.AbstractJSONServlet.service(AbstractJSONServlet.java:67)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:764)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:77)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.AuthMethodFilter.doFilter(AuthMethodFilter.java:138)
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
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1789)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:833)
2022-11-08 08:36:17,126 ERROR [com.simplicite.util.IntegrationDirect] SIMPLICITE|http://simplicite-6cc47dc8bc-w9nxs:8080||ECORED0001|system|com.simplicite.util.IntegrationDirect|exportModuleData||Error Unable to export module data
    java.lang.NullPointerException: Cannot invoke "com.simplicite.util.integration.FlowXML.getObjects()" because "objxml" is null
     at com.simplicite.util.engine.Interface.exportModuleData(Interface.java:2486)
     at com.simplicite.util.IntegrationDirect.exportModuleData(IntegrationDirect.java:379)
     at com.simplicite.util.Integration.exportModuleData(Integration.java:679)
     at com.simplicite.objects.System.Module.exportData(Module.java:778)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
     at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
     at java.base/java.lang.reflect.Method.invoke(Method.java:568)
     at com.simplicite.util.engine.ObjectManager.invokeActionSync(ObjectManager.java:3768)
     at com.simplicite.util.ObjectDirect.invokeAction(ObjectDirect.java:669)
     at com.simplicite.util.ObjectDB.invokeAction(ObjectDB.java:1989)
     at com.simplicite.util.ScriptedObjectDB.invokeAction(ScriptedObjectDB.java:1058)
     at com.simplicite.webapp.tools.JSONServletTool.action(JSONServletTool.java:1678)
     at com.simplicite.webapp.ObjectJson.action(ObjectJson.java:660)
     at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:616)
     at com.simplicite.webapp.servlets.AbstractJSONServlet.service(AbstractJSONServlet.java:67)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:764)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:77)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.AuthMethodFilter.doFilter(AuthMethodFilter.java:138)
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
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1789)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:833)
```
[/details]

## Answer
Bonjour,

L'export DATA d'un module parcours les objets flagués comme "exportable" avec un ordre d'export.
Ils sont mis en mémoire XML puis sérialisés dans un ZIP, donc plutôt dédié à exporter des données de références.

Si le retour du back est "null", c'est qu'il y a une exception bas niveau.

- on peut ajouter un catch pour savoir pourquoi
- à mon avis c'est un problème de taille mémoire insuffisante

Essayez de faire un export "XML Simplicité" ou "ZIP Simplicité" de chaque objet métier non filtré unitairement, pour voir si l'un d'entre eux pose un problème d'export (caractère non utf-8, 
heap/stack overflow...)

En V5, on va voir pour flusher sur disk au fur et à mesure de l'export pour éviter de tout garder en mémoire jusqu'au ZIP.
