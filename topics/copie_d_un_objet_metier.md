# Copie d'un objet metier

**URL:** https://community.simplicite.io/t/5515

## Question
Version=5.2.20

Bonjour, j'essaie de récuperer certaines données de cet objet
![image|235x500](upload://1REBGmrKiHmcwlM98mTyaInFHp2.png)
dans cet objet là
![image|214x500](upload://lcz0j78CSIbPA9moDBApTcz7iB4.png)

Voici mon code (celui-ci est appelé dans un postCreate de l'objet parent "reportingParticipation"):
```
public void generateFinancialHistory(String partId, String rptPartId)
	{
		ObjectDB financialHistory = getGrant().getTmpObject("EvlFinancialHistory");
		financialHistory.resetFilters();
		financialHistory.setFieldFilter("evlFinValId.evlValCpnId.evlCpnDate", getFieldValue("evlRptDate"));
		for (String[] fin : financialHistory.search()) {
			financialHistory.setValues(fin);
			ObjectDB reportingFinancialHistory = getGrant().getTmpObject("EvlRptFinancialHistory");
			reportingFinancialHistory.setFieldValue("evlRfinRpaId", rptPartId);
			reportingFinancialHistory.setFieldValue("evlRfinAnnee", financialHistory.getFieldValue("evlFinClosingDate"));
			reportingFinancialHistory.setFieldValue("evlRfinFinancialType", financialHistory.getFieldValue("evlFinType"));
			reportingFinancialHistory.setFieldValue("evlRfinEBITDA", financialHistory.getFieldValue("evlFinEbitda"));
			reportingFinancialHistory.populate(true);
			reportingFinancialHistory.create();
			}
	}
```
et l'erreur dans les logs:
```
2022-11-21 15:56:39,240|SIMPLICITE|ERROR||http://siparex-simplicite-dev-546fddd684-c7jqk:8080||ECOREDB001|system|com.simplicite.util.engine.ObjectManager|create||Error SQL query: Create failed for object EvlRptFinancialHistory and row ID = 0
    org.postgresql.util.PSQLException: ERROR: value too long for type character(1)
     at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2676)
     at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2366)
     at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:356)
     at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:496)
     at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:413)
     at org.postgresql.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:190)
     at org.postgresql.jdbc.PgPreparedStatement.executeUpdate(PgPreparedStatement.java:152)
     at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeUpdate(DelegatingPreparedStatement.java:135)
     at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeUpdate(DelegatingPreparedStatement.java:135)
     at com.simplicite.util.engine.DBAccess.update(DBAccess.java:1542)
     at com.simplicite.util.engine.ObjectManager.create(ObjectManager.java:2037)
     at com.simplicite.util.engine.ObjectDirect.create(ObjectDirect.java:390)
     at com.simplicite.util.ObjectDB.create(ObjectDB.java:1236)
     at com.simplicite.objects.Evaluator.EvlReporting.generateFinancialHistory(EvlReporting.java:136)
     at com.simplicite.objects.Evaluator.EvlReporting.createReporting(EvlReporting.java:90)
     at com.simplicite.objects.Evaluator.EvlReporting.postCreate(EvlReporting.java:39)
     at com.simplicite.util.ObjectHooks.postCreate(ObjectHooks.java:610)
     at com.simplicite.util.engine.ObjectManager.create(ObjectManager.java:2111)
     at com.simplicite.util.engine.ObjectDirect.create(ObjectDirect.java:390)
     at com.simplicite.util.ObjectDB.create(ObjectDB.java:1236)
     at com.simplicite.util.engine.ObjectManager.save(ObjectManager.java:3380)
     at com.simplicite.util.engine.ObjectDirect.save(ObjectDirect.java:478)
     at com.simplicite.util.ObjectDB.save(ObjectDB.java:1318)
     at com.simplicite.util.ObjectDB.save(ObjectDB.java:1305)
     at com.simplicite.webapp.tools.JSONServletTool.create(JSONServletTool.java:1127)
     at com.simplicite.webapp.ObjectJson.create(ObjectJson.java:529)
     at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:642)
     at com.simplicite.webapp.servlets.AbstractJSONServlet.service(AbstractJSONServlet.java:102)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:779)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.AuthMethodFilter.doFilter(AuthMethodFilter.java:220)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter(HTTPHeadersFilter.java:39)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:62)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:183)
     at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97)
     at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:541)
     at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:135)
     at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
     at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
     at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78)
     at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:360)
     at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:399)
     at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
     at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:893)
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1789)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:833)
```

j'ai bien vérifié que les champs à copier était du bon type et de la bonne taille, mais le problème persiste, j'ai également vérifié qu'aucun de mes champs à copier n'était vide.

Cordialement,
Paul-alexandre

## Answer
Bonjour,
Vu avec Alistair, nous n'avons pas réussi à exploiter la requête SQL pour savoir d'ou venait le problème.
L'utilisation d'un businessObjectTool et d'un validateAndSave à permis de résoudre le problème.
