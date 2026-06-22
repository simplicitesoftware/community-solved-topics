# SetSearchSpec bloque les notifications

**URL:** https://community.simplicite.io/t/12404

## Question
Bonjour, 

Je suis mettre en place les notifications au moment de la création d'un objet. Cette objet est une demande d'accès qui associe un login à un groupe. J'ai deux objets un DemandeDacces et un MesDemandes qui hérite du premier. Il y a un setsearchspec dans un post load pour ces 2 objets, pour le premier qui filtre les demandes pour que les administrateur ne voit que les demandes de leur périmètre et pour le deuxième pour voir uniquement les demandes propres à un utilisateur.

L'utilisateur qui créer un demande le fait au travers de l'objet mesdemandes. Je ne sais pas comment activer les notifications. J'ai l'impression que les setsearchspec bloque la création des notification.

```java
@Override MesDemandes
public void postLoad() {
	setDefaultSearchSpec(getSearchSpec() +" and t.id_de_lutilisateur='"+getGrant().getUserId()+"'");
	super.postLoad();
}

@Override DemandeDacces
	public void postLoad() {
		if (!getGrant().hasResponsibility("group admin")){
	    setSearchSpec(getSearchSpec() +
	        "   AND EXISTS(SELECT 1 FROM m_resp r LEFT JOIN m_group g ON r.rsp_group_id = g.row_id "+
	        "   WHERE r.rsp_login_id = " + getGrant().getUserId() +
	        "   AND g.grp_name='group admin')"+
	        	
	        "	OR EXISTS (" +
	        "   SELECT 1 " +
	        "   FROM uiux_profil_utilisateur p " +
	        "   LEFT JOIN m_resp r ON r.rsp_group_id = p.admin_du_profil_utilisateur " +
	        "   WHERE p.row_id = t.uiux_dda_pfu_id " +  // t.uiux_dda_pfu_id est l'ID du profil dans la demande d'accès
	        "   AND r.rsp_login_id = " + getGrant().getUserId() +
	        ")");}
		super.postLoad();
	}
```

1. ### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.3.5
BuiltOn=2026-02-25 23:18
Git=6.3
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=Europe/Paris
SystemDate=2026-03-24 16:14:48

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=0
TotalUsers=4
EnabledUsers=2
LastLoginDate=2026-03-23 14:43:07

[Server]
ServerInfo=Apache Tomcat/9.0.108
ServerType=WEB
ServerDevMode=true
ServerCompiler=true
ServerActiveSessions=0
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=5.14.0-570.60.1.el9_6.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=6484
DiskUsable=6484
DiskTotal=12224

[JavaVM]
Version=21.0.9
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=21.0.9+10-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=808594
HeapSize=1482752
HeapMaxSize=1482752
TotalFreeSize=808594

[Cache]
ObjectCache=55
ObjectCacheMax=10000
ObjectCacheRatio=0
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=16.9
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.10
DBDate=2026-03-24 16:14:48
DBDateOffset=0
DBPatchLevel=6;P03;51af22b13838925e31430a969bd336ba;5
UsingBLOBs=true

[Healthcheck]
Date=2026-03-24 16:14:59
ElapsedTime=11283
```

[/details]

[details="Simplicité logs"]
```
2026-06-03 11:44:17,302|SIMPLICITE|ERROR||http://EGIFR2DEV232V:20028/devjjb|/devjjb|ERROR|l.petit|com.simplicite.util.tools.NotificationTool|createEvent||Evénement: [1]
    com.simplicite.util.exceptions.ValidateException: ACCESS_DENIED
     at com.simplicite.util.BusinessObject.validateAndSave(BusinessObject.java:1586)
     at com.simplicite.util.BusinessObject.validateAndSave(BusinessObject.java:1550)
     at com.simplicite.util.tools.NotificationTool.createEvent(NotificationTool.java:185)
     at com.simplicite.util.tools.NotificationTool.pushInternalNotification(NotificationTool.java:130)
```

[/details]

[details]

[/details]

## Answer
_No answer provided._
