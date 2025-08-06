# Question sur des logs d'erreur

**URL:** https://community.simplicite.io/t/3763

## Question
Bonjour,

dans les logs il y a l'erreur :

2021-09-01 15:04:35,879|SIMPLICITE|ERROR||http://efs-simpl-f7f6db6d5-9nmwz:8080||ERROR|system|com.simplicite.util.tools.HTMLTool|getCrosstabURL||Evénement: Outdated deprecated method, please use none (legacy UI has been removed), call stack: com.simplicite.util.AppLog.deprecation[1018]
     com.simplicite.util.AppLog.deprecation[1002]
     com.simplicite.util.tools.HTMLTool.getCrosstabURL[4995]
     com.simplicite.util.engine.ScriptInterpreter.eval[177]
     com.simplicite.util.engine.ScriptInterpreter.eval[135]
     com.simplicite.util.GrantCore.evalExpression[374]
     com.simplicite.util.GrantCore.evalExpression[362]
     com.simplicite.util.GrantCore.evalExpressionAsString[395]
     com.simplicite.util.GrantCore.evalURLExpression[383]
     com.simplicite.util.MenuItem.getURL[384]
     com.simplicite.util.MenuItem.toJSON[966]
     com.simplicite.util.MenuItem.toJSON[705]
     com.simplicite.util.Grant.toJSONMenu[3923]
     com.simplicite.util.Grant.toJSON[4055]
     com.simplicite.webapp.tools.JSONServletTool.applicationService[217]
     com.simplicite.webapp.servlets.AbstractJSONServlet.service[91]
     com.simplicite.webapp.filters.RewriteFilter.doFilter[86]
     com.simplicite.webapp.filters.AbstractFilter.doFilter[37]
     com.simplicite.webapp.filters.AuthMethodFilter.doFilter[139]
     com.simplicite.webapp.filters.AbstractFilter.doFilter[37]
     com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter[39]
     com.simplicite.webapp.filters.AbstractFilter.doFilter[37]
     com.simplicite.tomcat.valves.APISessionValve.invoke[192]

A quoi correspond cette erreur ?

[Platform]
Status=OK
Version=5.1.0-releasecandidate
BuiltOn=2021-07-29 19:08
Git=prerelease/57a0faad740d100f5c066752e31275a975b3852e
Encoding=UTF-8
EndpointIP=172.16.0.16
EndpointURL=http://efs-simpl-f7f6db6d5-9nmwz:8080
TimeZone=UTC
SystemDate=2021-09-01 15:06:53

[Application]
ApplicationVersion=0.38
ContextPath=
ContextURL=https://simpl.prp.efs.multimediabs.com
ActiveSessions=2
TotalUsers=34
EnabledUsers=33
LastLoginDate=2021-09-01 15:04:35

[Server]
ServerInfo=Apache Tomcat/9.0.50
ServerType=WEB
User=root

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-862.14.1.0.h197.eulerosv2r7.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=8866
DiskUsable=8338
DiskTotal=10015

[JavaVM]
Version=16.0.1
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=16.0.1+9
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=159429
HeapSize=300620
HeapMaxSize=1540288
TotalFreeSize=1399097

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=188
ObjectCacheMax=10000
ObjectCacheRatio=1
ProcessCache=1
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=12.6
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.2.23
DBDate=2021-09-01 15:06:53
DBDateOffset=0
DBPatchLevel=5;P01c;f8792fa7210632e20c0f8ce28a2d8d97
UsingBLOBs=true

[Healthcheck]
Date=2021-09-01 15:06:53
ElapsedTime=9

## Answer
Voilà le patch à appliquer:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<simplicite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.simplicite.fr/base" xsi:schemaLocation="http://www.simplicite.fr/base https://www.simplicite.io/resources/schemas/base.xsd">
<object>
	<name>ObjectExternal</name>
	<action>update</action>
	<data>
		<obe_name>EfsCollectesPlanifiees_R1</obe_name>
		<obe_type>E</obe_type>
		<obe_url><![CDATA[javascript:$ui.displayCrosstab(null, "EfsCollectePlanifiee", "EfsCollectePlanifiee-R1", { inst: "pilotage_EfsCollectePlanifiee" })]]></obe_url>
	</data>
	<data>
		<obe_name>EfsCollectesPlanifiees_R2</obe_name>
		<obe_type>E</obe_type>
		<obe_url><![CDATA[javascript:$ui.displayCrosstab(null, "EfsCollectePlanifiee", "EfsCollectePlanifiee-R2", { inst: "pilotage_EfsCollectePlanifiee" })]]></obe_url>
	</data>
</object>
</simplicite>
```

NB: J'ai poussé cette modif sur le module sur GitHub et j'ai aussi appliqué ce patch sur l'instance de PROD
