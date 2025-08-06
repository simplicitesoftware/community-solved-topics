# Problème d'import de module

**URL:** https://community.simplicite.io/t/4642

## Question
Bonjour,

J'ai exporté en XML un module de notre environnement de PROD et je veux l'importer dans mon instance de dév.

L'import se termine en erreur. Je ne trouve pas d'erreur dans le log (je fais une recherche sur "error").

Ce que je constate :

* les objets métiers et les attributs ne sont pas importés
* les fonctions ne sont pas importées
* le domaine est importé mais évidemment il n'y a pas d'objets dans le menu principal et pas de fonction

C'est la 1re fois que je rencontre ce problème... où est notre erreur?

System log
```
2022-04-04 15:44:22,185|SIMPLICITE|ERROR||http://lsllcot01.lausanne.ch:20458||ERROR|designer|com.simplicite.util.integration.SAXImportXML|process||Evénement: Error during XML processing
    org.xml.sax.SAXParseException; lineNumber: 5210; columnNumber: 88; The element type "obo_script_id" must be terminated by the matching end-tag "</obo_script_id>".
     at org.apache.xerces.util.ErrorHandlerWrapper.createSAXParseException(Unknown Source)
     at org.apache.xerces.util.ErrorHandlerWrapper.fatalError(Unknown Source)
     at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
     at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
     at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
     at org.apache.xerces.impl.XMLScanner.reportFatalError(Unknown Source)
     at org.apache.xerces.impl.XMLNSDocumentScannerImpl.scanEndElement(Unknown Source)
     at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContentDispatcher.dispatch(Unknown Source)
     at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Unknown Source)
     at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
     at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
     at org.apache.xerces.parsers.XMLParser.parse(Unknown Source)
     at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source)
     at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Source)
     at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source)
     at java.xml/javax.xml.parsers.SAXParser.parse(SAXParser.java:197)
     at com.simplicite.util.integration.SAXParserAdapter.process(SAXParserAdapter.java:58)
     at com.simplicite.util.integration.SimpleSAXParserAdapter.process(SimpleSAXParserAdapter.java:122)
     at com.simplicite.util.engine.Interface.importSAX(Interface.java:949)
     at com.simplicite.util.engine.Interface.importSAX(Interface.java:1032)
     at com.simplicite.util.engine.Interface.importData(Interface.java:661)
     at com.simplicite.util.engine.Interface.importXML(Interface.java:394)
     at com.simplicite.util.engine.Interface.importModule(Interface.java:1562)
     at com.simplicite.util.engine.IntegrationDirect.importModule(IntegrationDirect.java:416)
     at com.simplicite.util.Integration.importModule(Integration.java:1596)
     at com.simplicite.util.Integration.importModuleXML(Integration.java:740)
     at com.simplicite.objects.System.Module.importModule(Module.java:917)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
     at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
     at java.base/java.lang.reflect.Method.invoke(Method.java:566)
     at com.simplicite.util.engine.ObjectManager.invokeActionSync(ObjectManager.java:4154)
     at com.simplicite.util.engine.ObjectDirect.invokeAction(ObjectDirect.java:658)
     at com.simplicite.util.ObjectDB.invokeAction(ObjectDB.java:2079)
     at com.simplicite.util.ScriptedObjectDB.invokeAction(ScriptedObjectDB.java:888)
     at com.simplicite.util.ObjectDB.invokeAction(ObjectDB.java:2047)
     at com.simplicite.webapp.tools.JSONServletTool.action(JSONServletTool.java:1893)
     at com.simplicite.webapp.ObjectJson.action(ObjectJson.java:684)
     at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:674)
     at com.simplicite.webapp.servlets.AbstractJSONServlet.service(AbstractJSONServlet.java:89)
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
     at com.simplicite.webapp.filters.AuthMethodFilter.doFilter(AuthMethodFilter.java:174)
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
     at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:889)
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1743)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:829)
```

Fabrice

## Answer
Ok. J'ai corrigé le xml avec la méthode XMLTool et c'est passé.

Merci.
