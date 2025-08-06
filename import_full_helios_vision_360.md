# Import FULL HELIOS Vision 360

**URL:** https://community.simplicite.io/t/7639

## Question
Bonjour,

l'import FULL HELIOS sur V360 s'arrete au bout de 5 minutes.
pourriez vous nous dire quel est le souci de NullPointerException?
**[m[32m2024-01-25 14:05:45,359|SIMPLICITE|INFO||http://59ffc069e505:8080||INFO|designer|com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS|logInfo||Evénement: Import (mise à jour) du site 0241501 (row ID: 930) en 12 ms** derniere site traité avant l'exception.
[m[31m2024-01-25 14:05:45,362|SIMPLICITE|ERROR||http://59ffc069e505:8080||ECORED0001|system|com.simplicite.util.engine.ObjectDirect|search||Error TdfSiteHELIOS
java.lang.NullPointerException: Cannot invoke "com.simplicite.util.engine.ObjectInterface.select(com.simplicite.util.ObjectDB, String, boolean)" because the return value of "com.simplicite.util.ObjectDB.getInterface()" is null
	at com.simplicite.util.ObjectDB.select(ObjectDB.java:1022)
	at com.simplicite.util.ObjectDB.selectWithoutFilters(ObjectDB.java:1065)
	at com.simplicite.util.tools.BusinessObjectTool.get(BusinessObjectTool.java:140)
	at com.simplicite.util.tools.BusinessObjectTool.getForUpdate(BusinessObjectTool.java:256)
	at com.simplicite.util.tools.BusinessObjectTool.getForCreateOrUpdate(BusinessObjectTool.java:418)
	at com.simplicite.util.tools.BusinessObjectTool.getForCreateOrUpdate(BusinessObjectTool.java:369)
	at com.simplicite.util.tools.BusinessObjectTool.getForUpsert(BusinessObjectTool.java:458)
	at com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS.importSite(TdfCommunImportHELIOS.java:275)
	at com.simplicite.adapters.TdfInfraHELIOS.TdfImportHELIOS.lambda$importHELIOS$0(TdfImportHELIOS.java:69)
	at com.simplicite.util.engine.ObjectManager.search(ObjectManager.java:400)
	at com.simplicite.util.engine.ObjectManager.search(ObjectManager.java:320)
	at com.simplicite.util.engine.ObjectDirect.search(ObjectDirect.java:304)
	at com.simplicite.util.ObjectDB.search(ObjectDB.java:927)
	at com.simplicite.util.tools.BusinessObjectTool.search(BusinessObjectTool.java:795)
	at com.simplicite.adapters.TdfInfraHELIOS.TdfImportHELIOS.importHELIOS(TdfImportHELIOS.java:55)
	at com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS.process(TdfCommunImportHELIOS.java:728)
	at com.simplicite.util.Adapter.applyAdapter(Adapter.java:384)
	at com.simplicite.util.engine.Interface.importData(Interface.java:553)
	at com.simplicite.util.engine.Interface.importADP(Interface.java:485)
	at com.simplicite.util.engine.IntegrationDirect.importADP(IntegrationDirect.java:203)
	at com.simplicite.util.Integration.importADP(Integration.java:452)
	at com.simplicite.objects.TdfInfraHELIOS.TdfSiteHELIOS.importHelios(TdfSiteHELIOS.java:32)
	at com.simplicite.objects.TdfInfraHELIOS.TdfSiteHELIOS.importHelios(TdfSiteHELIOS.java:72)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:568)
	at com.simplicite.util.engine.ObjectManager.invokeActionSync(ObjectManager.java:4439)
	at com.simplicite.util.engine.ObjectDirect.invokeAction(ObjectDirect.java:660)
	at com.simplicite.util.ObjectDB.invokeAction(ObjectDB.java:2164)
	at com.simplicite.util.CronJob.launch(CronJob.java:461)
	at com.simplicite.util.engine.JobQueue$Job$1.run(JobQueue.java:160)
	at java.base/java.lang.Thread.run(Thread.java:840)
[m[32m2024-01-25 14:05:45,364|SIMPLICITE|INFO||http://59ffc069e505:8080||INFO|system|com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS|logInfo||Event: Fin de l'import d'un total de 921 records de sites en 44407 ms
[m[31m2024-01-25 14:05:45,364|SIMPLICITE|ERROR||http://59ffc069e505:8080||ERROR|system|com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS|logError||Event: Erreur pendant l'import des sites (Cannot read field "m_lang" because "this.m_data" is null) (Cannot read field "m_lang" because "this.m_data" is null)
java.lang.NullPointerException: Cannot read field "m_lang" because "this.m_data" is null
	at com.simplicite.util.GrantCore.getLang(GrantCore.java:943)
	at com.simplicite.util.engine.CoreCache.getObjectCacheKey(CoreCache.java:4186)
	at com.simplicite.util.engine.CoreCache.getObject(CoreCache.java:4237)
	at com.simplicite.util.engine.GrantManager.getObject(GrantManager.java:84)
	at com.simplicite.util.engine.GrantDirect.getObject(GrantDirect.java:636)
	at com.simplicite.util.Grant.getObject(Grant.java:2410)
	at com.simplicite.util.Grant.getIsolatedObject(Grant.java:2553)
	at com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS.getObject(TdfCommunImportHELIOS.java:86)
	at com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS.getObject(TdfCommunImportHELIOS.java:82)
	at com.simplicite.adapters.TdfInfraHELIOS.TdfImportHELIOS.importHELIOS(TdfImportHELIOS.java:89)
	at com.simplicite.commons.TdfInfraHELIOS.TdfCommunImportHELIOS.process(TdfCommunImportHELIOS.java:728)
	at com.simplicite.util.Adapter.applyAdapter(Adapter.java:384)
	at com.simplicite.util.engine.Interface.importData(Interface.java:553)
	at com.simplicite.util.engine.Interface.importADP(Interface.java:485)
	at com.simplicite.util.engine.IntegrationDirect.importADP(IntegrationDirect.java:203)
	at com.simplicite.util.Integration.importADP(Integration.java:452)
	at com.simplicite.objects.TdfInfraHELIOS.TdfSiteHELIOS.importHelios(TdfSiteHELIOS.java:32)
	at com.simplicite.objects.TdfInfraHELIOS.TdfSiteHELIOS.importHelios(TdfSiteHELIOS.java:72)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:568)
	at com.simplicite.util.engine.ObjectManager.invokeActionSync(ObjectManager.java:4439)
	at com.simplicite.util.engine.ObjectDirect.invokeAction(ObjectDirect.java:660)
	at com.simplicite.util.ObjectDB.invokeAction(ObjectDB.java:2164)
	at com.simplicite.util.CronJob.launch(CronJob.java:461)
	at com.simplicite.util.engine.JobQueue$Job$1.run(JobQueue.java:160)
	at java.base/java.lang.Thread.run(Thread.java:840)

## Answer
Ok donc en interactif via la UI. 
Plusieurs pbs peuvent se produire dans ce contexte:
-  est-ce que votre session a expirée ?
- ou est-ce que vous vous êtes déconnectés de cette session ?
- ou est-ce que quelqu'un a fait un clear cache sur cette instance ?
- ou est-ce que vous avez modifié la définition d'un des objets utilisés par ce traitement ?
- etc.

Quand vous lancez un traitement long, il faut le faire en indépendance de la session en cours.

Pour cet import, normalement l'action s'execute via sa planification dans la crontab:
![image|690x223](upload://i8zS0mDQnWjyRwqFq5RqBeN9Pp7.png)

Si vous tenez à pouvoir le faire interactivement via la UI, je vous suggère de passer l'action en "Session isolée":
![image|690x189](upload://fsOQvb5Eg9obI3j8tRaQbH5B6HG.png)

**ATTENTION** Dans tous les cas, il faut ne faire aucune opération de paramétrage susceptible d'alterer le cache Simplicité pendant que le traitement s'execute
