# Une expression de valeur par défaut génère une erreur

**URL:** https://community.simplicite.io/t/3753

## Question
Bonjour,

Je  souhaite avoir un champ avec une valeur par défaut du type "LIEU_xxxx", les x étant le rowID.

Dans la doc j'ai trouvé l'expression qui convient : `[EXPR:Tool.format("LIEU-%04d", Long.valueOf([ROWID]))]` mais dans les logs système ça me donne une erreur (je ne l'ai plus si j'enlève l'expression) :

> 2021-08-31 07:57:44,754 ERROR [com.simplicite.util.ObjectField] SIMPLICITE|http://lsllcot01.lausanne.ch:20358||ERROR|designer|com.simplicite.util.ObjectField|evalDefault||Evénement: Default value expression evaluation error for object InscriptionBoLieu and field InscriptionBoLieuId
    com.simplicite.util.exceptions.ScriptException: org.mozilla.javascript.WrappedException: Wrapped java.lang.NumberFormatException: For input string: "" (<Unknown source>#1) in <Unknown source> at line number 1
     at com.simplicite.util.ScriptInterpreter.eval(ScriptInterpreter.java:176)
     at com.simplicite.util.ObjectCore.evalExpression(ObjectCore.java:4794)
     at com.simplicite.util.ObjectCore.evalExpression(ObjectCore.java:4712)
     at com.simplicite.util.ObjectField.evalDefault(ObjectField.java:1471)
     at com.simplicite.util.tools.JSONTool.objectFieldMetaDataToJson(JSONTool.java:950)
     at com.simplicite.util.tools.JSONTool.objectMetaDataToJson(JSONTool.java:1740)
     at com.simplicite.util.tools.JSONTool.metadata(JSONTool.java:3038)
     at com.simplicite.util.tools.JSONTool.list(JSONTool.java:3269)
     at com.simplicite.webapp.tools.JSONServletTool.search(JSONServletTool.java:763)
     at com.simplicite.webapp.ObjectJson.search(ObjectJson.java:215)
     at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:566)
     at com.simplicite.webapp.servlets.AbstractJSONServlet.service(AbstractJSONServlet.java:69)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:764)
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
     at com.simplicite.webapp.filters.AuthMethodFilter.doFilter(AuthMethodFilter.java:139)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:37)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:183)
     at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97)
     at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:542)
     at com.simplicite.tomcat.valves.APISessionValve.invoke(APISessionValve.java:192)
     at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:135)
     at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
     at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
     at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78)
     at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:357)
     at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:382)
     at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
     at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:893)
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1726)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:834)

Pour info :

> Simplicité version 5.0.63
Built on 2021-08-24 21:21

## Answer
Test fait (en 5.2 alpha) : 
![image|690x249](upload://bnOONp9tpFCMOW19sYilX2Nd6Zu.png)

Expression de valeur par défaut: `[EXPR:Tool.format("TEST-%05d", Long.valueOf(Tool.parseLong([ROWID])))]`

Ca me semble bien marcher. Sur quelle version/revision êtes vous ?
