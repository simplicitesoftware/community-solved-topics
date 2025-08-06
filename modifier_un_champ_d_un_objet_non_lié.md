# Modifier un champ d'un objet non lié

**URL:** https://community.simplicite.io/t/5675

## Question
Bonjour,

Pour donner du contexte, un objet B est lié à un objet C, et un objet A est lié à ce même objet C, sans que A et B soient liés
A partir de champs modifiés d'un objet [A], je veux modifier un champ booléen d'un objet [B] non lié. Pour ce faire

* je vérifie que le champ que je cherche à modifier est déjà créé 
* je récupère mon objet temp
* je met un filtre pour ne récupérer que la ligne qui m'intéresse 
* je modifie le champ

Néanmoins je ne parviens pas à mettre en place le filtre pour ne sélectionner que la ligne qui m'intéresse. Le setFieldFilter ne me permet pas de récupérer la valeur d'un champ.


mon bout de code :
```
           if(res != null) { // si la requête vers la bdd trouve la ligne dans laquelle on veut modifier une info on continue
                ObjectDB tiers = g.getTmpObject("LadTiers"); // récupération de l'objet temp B non lié
                BusinessObjectTool TiersTool = tiers.getTool();
                AppLog.info(LadDossierPmfp.class, "postUpdate", "Dans la boucle du res != null", g);
                
                synchronized(tiers){

                    tiers.resetFilters();
                	tiers.setFieldFilter(FIELD_TIERS_DEMANDEUR_ID, getFieldValue("ladDospmfpDemId")); // je filtre sur un champ qui partage la même valeur entre l'objet B (FIELD_TIERS_DEMANDEUR_ID = "champTiersdemandeur...") et l'objet A (celui dans lequel on est, ladDospmfpDemId)
                	AppLog.info(LadDossierPmfp.class,"postUpdate"," récupération du champdem_id : "+ tiers.getFieldValue(FIELD_TIERS_DEMANDEUR_ID),g); // ne renvoie rien
                	AppLog.info(LadDossierPmfp.class,"postUpdate"," récupération du champ avant modif: "+ tiers.getFieldValue(FIELD_TIERS_SYNCHRONISER),g); // ne renvoie rien
                	tiers.setFieldValue(FIELD_TIERS_SYNCHRONISER, true); // modification du champ booléen à true
					AppLog.info(LadDossierPmfp.class,"postUpdate"," récupération du champ après setValue : "+ tiers.getFieldValue(FIELD_TIERS_SYNCHRONISER),g);
					
                }
				try{
                       TiersTool.validateAndSave(); // sauvegarde de la valeur modifiée dans l'objet cible B
                       tiers.resetFilters(); // reset du filtre
                       AppLog.info(LadDossierPmfp.class,"postUpdate"," récupération du champ après validate and save: "+ tiers.getFieldValue(FIELD_TIERS_SYNCHRONISER),g);
                }catch(Exception e){
                       AppLog.error(getClass(), "creationTiers", "Error creating object", e, getGrant());
                }
```

[details="Instance /health"]
```text

Les 2 premiers logs getFieldValue ne me renvoient rien, car les champs ne sont pas trouvés.
Et le validateandSave() m'indique qu'il est impossible de créer l'objet Tiers car il doit vouloir créer une nouvelle entrée à partir de mon setFieldValue étant donné qu'il n'a pas trouvé le champ FIELD_TIERS_SYNCHRONISER.

Comment devrais-je m'y prendre avec le filtre ?

Cdlt,

Clément

[Platform]
Status=OK
Version=5.2.25
BuiltOn=2022-12-08 16:28
Git=5.2/b6ade203bbb1542df426ee173be5abaa0746c664
Encoding=UTF-8
EndpointIP=172.19.0.2
EndpointURL=http://e1433ddea090:8080
TimeZone=UTC
SystemDate=2022-12-28 15:23:00

[Application]
ApplicationVersion=2.1.5
ContextPath=
ContextURL=http://localhost:8080
ActiveSessions=1
TotalUsers=11
EnabledUsers=8
LastLoginDate=2022-12-28 15:15:04

[Server]
ServerInfo=Apache Tomcat/9.0.70
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=5.10.16.3-microsoft-standard-WSL2
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.5
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.5+8
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=176796
HeapSize=655360
HeapMaxSize=6533120
TotalFreeSize=6054556

[Cache]
ObjectCache=266
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=23
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.6 (Debian 13.6-1.pgdg110+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.5.1
DBDate=2022-12-28 15:23:00
DBDateOffset=0
DBPatchLevel=5;P02;02060c9fd8a4f4cb39e2a5f8e2d14215
UsingBLOBs=true

[Healthcheck]
Date=2022-12-28 15:23:00
ElapsedTime=197


```
[/details]

[details="Simplicité logs"]
```text
2022-12-28 15:33:24,317|SIMPLICITE|ERROR||http://e1433ddea090:8080||ERROR|demo_admin|com.simplicite.objects.ladnext.LadDossierPmfp|creationTiers||Evénement: Error creating object
    com.simplicite.util.exceptions.ValidateException: ERR_REQUIRED: Numéro Tiers
     at com.simplicite.util.tools.BusinessObjectTool.validate(BusinessObjectTool.java:687)
     at com.simplicite.util.tools.BusinessObjectTool.validateAndSave(BusinessObjectTool.java:936)
     at com.simplicite.util.tools.BusinessObjectTool.validateAndSave(BusinessObjectTool.java:905)
     at com.simplicite.objects.ladnext.LadDossierPmfp.postUpdate(LadDossierPmfp.java:507)
     at com.simplicite.util.ObjectHooks.postUpdate(ObjectHooks.java:646)
     at com.simplicite.util.engine.ObjectManager.update(ObjectManager.java:2926)
     at com.simplicite.util.engine.ObjectDirect.update(ObjectDirect.java:435)
     at com.simplicite.util.ObjectDB.update(ObjectDB.java:1275)
     at com.simplicite.util.engine.ObjectManager.save(ObjectManager.java:3396)
     at com.simplicite.util.engine.ObjectDirect.save(ObjectDirect.java:478)
     at com.simplicite.util.ObjectDB.save(ObjectDB.java:1318)
     at com.simplicite.webapp.tools.JSONServletTool.update(JSONServletTool.java:1259)
     at com.simplicite.webapp.ObjectJson.update(ObjectJson.java:611)
     at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:640)
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
     at com.simplicite.webapp.filters.RewriteFilter.doFilter(RewriteFilter.java:62)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at com.simplicite.webapp.filters.HTTPHeadersFilter.doFilter(HTTPHeadersFilter.java:39)
     at com.simplicite.webapp.filters.AbstractFilter.doFilter(AbstractFilter.java:49)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
     at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:163)
     at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:97)
     at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:541)
     at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:135)
     at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:92)
     at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:687)
     at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:78)
     at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:360)
     at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:399)
     at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:65)
     at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:891)
     at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1784)
     at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
     at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
     at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
     at java.base/java.lang.Thread.run(Thread.java:833)
2022-12-28 15:33:24,317|SIMPLICITE|INFO||http://e1433ddea090:8080||INFO|demo_admin|com.simplicite.objects.ladnext.LadDossierPmfp|postUpdate||Evénement: récupération du champ après setValue : 1
2022-12-28 15:33:24,316|SIMPLICITE|INFO||http://e1433ddea090:8080||INFO|demo_admin|com.simplicite.objects.ladnext.LadDossierPmfp|postUpdate||Evénement: récupération du champ avant modif:
2022-12-28 15:33:24,316|SIMPLICITE|INFO||http://e1433ddea090:8080||INFO|demo_admin|com.simplicite.objects.ladnext.LadDossierPmfp|postUpdate||Evénement: récupération du champdem_id :
2022-12-28 15:33:24,316|SIMPLICITE|INFO||http://e1433ddea090:8080||INFO|demo_admin|com.simplicite.objects.ladnext.LadDossierPmfp|postUpdate||Evénement: Dans la boucle du res != null
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
Bonjour Alistair,

navré pour le dérangement, effectivement avec un tiers.select(row_id) ça marche tout de suite mieux :slight_smile: . Je me suis embrouillé avec le setFieldFilter(), qui je pensais produisait le même résultat.
