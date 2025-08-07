# Import d'application en v6

**URL:** https://community.simplicite.io/t/7786

## Question
### Request description

Bonjour,

Je tente l'import d'une application d'un environnement à un autre.
L'application comprend 4 modules .

L'instance sur l'environnement cible a été fraichement créée, rien n'y a été fait à part changer le mdp/la langue d'affichage de designer.
Je crée l'application sur la cible, et au moment d'importer, je tombe sur une erreur qui a l'air liée aux traductions.

Voilà ce que le log d'import me dit :

```
2024-02-21 10:40:14
Import application CrbAppSdt...
- Extract GZIP files
done
14ms
- Analyse app-info.json
5 modules format json
Import module CrbAppSdt
- Load JSON tree
done
2ms
- Import data
done
Error in import XML, see logs for details
2sec
2024-02-21 10:40:16 (00:02)
```
Log système lors de l'import ci-dessous.

Est-ce que cela vous dit quelque chose?
Merci,

### Steps to reproduce

1. Créer une application sur l'environnement source, y ajouter les modules 
2. Exporter (paramètres laissés sur JSON/unique file) et télécharger l'archive
3. Créer l'application sur l'environnement cible et importer depuis l'archive

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.0.0
BuiltOn=2024-01-31 12:04
Git=6.0/95f8118d68111c1819535d757aabf0e149238cac
Encoding=UTF-8
EndpointIP=192.168.1.20
EndpointURL=https://Rec-sim:10498/suividspbreizhgo
TimeZone=Europe/Paris
SystemDate=2024-02-21 10:42:30

[Application]
ApplicationVersion=1.0.0
ContextPath=/suividspbreizhgo
ContextURL=https://rec.bretagne.bzh/suividspbreizhgo
ActiveSessions=1
TotalUsers=3
EnabledUsers=1
LastLoginDate=2024-02-21 10:40:16

[Server]
ServerInfo=Apache Tomcat/9.0.85
ServerType=WEB
ServerActiveSessions=0
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1062.1.1.el7.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=4159
DiskUsable=2149
DiskTotal=47224

[JavaVM]
Version=13.0.1
Vendor=N/A
VMName=OpenJDK 64-Bit Server VM
VMVersion=13.0.1+9
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=195288
HeapSize=348160
HeapMaxSize=524288
TotalFreeSize=371416

[Cache]
ObjectCache=402
ObjectCacheMax=10000
ObjectCacheRatio=4
ProcessCache=402
ProcessCacheMax=10000
ProcessCacheRatio=4
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
ProductName=MySQL
ProductVersion=5.5.5-10.2.9-MariaDB-10.2.9+maria~stretch
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-8.3.0 (Revision: 805f872a57875f311cb82487efcfb070411a3fa0)
DBDate=2024-02-21 10:42:30
DBDateOffset=0
DBPatchLevel=6;P00;ca44892f805a01d2085cf54725222024
UsingBLOBs=true

[Healthcheck]
Date=2024-02-21 10:42:31
ElapsedTime=645

```
[/details]

[details="Simplicité logs"]
```text
2024-02-21 10:40:16,949|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ERROR|system|com.simplicite.util.AsyncTracker|error||Event: Error in import XML, see logs for details
2024-02-21 10:40:16,949|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.engine.Interface|importModule||Event: Import module CrbAppSdt duration = 0:00:02
2024-02-21 10:40:16,949|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ERROR|designer|com.simplicite.util.engine.Interface|importModule||Evénement: Module: CrbAppSdt: Error importing module CrbAppSdt: Error in import XML, see logs for details
2024-02-21 10:40:16,949|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ERROR|system|com.simplicite.util.AsyncTracker|error||Event: Error importing module CrbAppSdt: Error in import XML, see logs for details
2024-02-21 10:40:16,876|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.engine.Platform|metadataUpgrade||Event: Upgrade metadata...
2024-02-21 10:40:16,876|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ERROR|designer|com.simplicite.util.integration.SAXImportXML|endProcess||Evénement: Import contains errors: diff is aborted to preserve the previous configuration. Fix the module and re-import.
2024-02-21 10:40:16,876|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|designer|com.simplicite.util.engine.Interface|importXML||Evénement: Import: diff requested...
2024-02-21 10:40:16,833|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.engine.Platform|metadataUpgrade||Event: Upgrade metadata...
2024-02-21 10:40:16,833|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ECOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Erreur I/O: Skipped due to previous error
2024-02-21 10:40:16,833|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ECOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Erreur I/O: Skipped due to previous error
2024-02-21 10:40:16,832 ERROR [/suividspbreizhgo] Validation error: [ERR_REQUIRED:Objet#ERROR#tsl_object]
    
2024-02-21 10:40:16,785 INFO [/suividspbreizhgo] Action: INSERT
2024-02-21 10:40:16,785 INFO [/suividspbreizhgo] New record key row_id
2024-02-21 10:40:16,781 INFO [/suividspbreizhgo] Found field tsl_lang = [FRA]
2024-02-21 10:40:16,781 INFO [/suividspbreizhgo] Found field tsl_value = [Crb sdt prm contrat statut]
2024-02-21 10:40:16,781 INFO [/suividspbreizhgo] Found field tsl_simplehelp = []
2024-02-21 10:40:16,781 WARN [/suividspbreizhgo] Object not found for tsl_object: Action CrbSdtPrmContratStatut
2024-02-21 10:40:16,765 INFO [/suividspbreizhgo] Found field row_module_id.mdl_name = [CrbAppSdt]
2024-02-21 10:40:16,764 INFO [/suividspbreizhgo] Start import object TranslateAction:
2024-02-21 10:40:16,786 ERROR [/suividspbreizhgo] Validation error: [ERR_REQUIRED:Objet#ERROR#tsl_object]
    
2024-02-21 10:40:16,785 INFO [/suividspbreizhgo] Action: INSERT
2024-02-21 10:40:16,785 INFO [/suividspbreizhgo] New record key row_id
2024-02-21 10:40:16,781 INFO [/suividspbreizhgo] Found field tsl_lang = [ENU]
2024-02-21 10:40:16,781 INFO [/suividspbreizhgo] Found field tsl_value = [Crb sdt prm contrat statut]
2024-02-21 10:40:16,781 INFO [/suividspbreizhgo] Found field tsl_simplehelp = []
2024-02-21 10:40:16,781 WARN [/suividspbreizhgo] Object not found for tsl_object: Action CrbSdtPrmContratStatut
2024-02-21 10:40:16,753 INFO [/suividspbreizhgo] Found field row_module_id.mdl_name = [CrbAppSdt]
2024-02-21 10:40:16,752 INFO [/suividspbreizhgo] Start import object TranslateAction:
2024-02-21 10:40:16,832|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ECOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Erreur I/O: Import object TranslateAction, status = KO
2024-02-21 10:40:16,832|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.tools.AuditTool|issue||Event: [runtime] Object TranslateAction: unknown field tsl_type.
    <div class="stack-trace">Thread stack:<div class="s">com.simplicite.util.ObjectCore.getField(ObjectCore.java:4497)</div><div class="s">com.simplicite.util.ObjectCore.getFieldValue(ObjectCore.java:1000)</div><div class="s">com.simplicite.objects.System.Translate.preValidate(Translate.java:120)</div><div class="s">com.simplicite.util.ObjectHooks.lambda$preValidate$22(ObjectHooks.java:607)</div><div class="s">com.simplicite.util.ObjectHooks$Wrapper.call(ObjectHooks.java:100)</div><div class="s">com.simplicite.util.ObjectHooks.preValidate(ObjectHooks.java:605)</div><div class="s">com.simplicite.util.engine.ObjectManager.validate(ObjectManager.java:111)</div><div class="s">com.simplicite.util.engine.ObjectDirect.validate(ObjectDirect.java:168)</div><div class="s">com.simplicite.util.ObjectDB.validate(ObjectDB.java:647)</div></div>
2024-02-21 10:40:16,809|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ECORED0001|system|com.simplicite.objects.System.TranslateAction|getField||Error Object TranslateAction: unknown field tsl_type.
2024-02-21 10:40:16,809|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.tools.AuditTool|issue||Event: [runtime] Object TranslateAction: unknown field tsl_id.
    <div class="stack-trace">Thread stack:<div class="s">com.simplicite.util.ObjectCore.getField(ObjectCore.java:4497)</div><div class="s">com.simplicite.util.ObjectCore.getFieldValue(ObjectCore.java:1000)</div><div class="s">com.simplicite.objects.System.Translate.preValidate(Translate.java:119)</div><div class="s">com.simplicite.util.ObjectHooks.lambda$preValidate$22(ObjectHooks.java:607)</div><div class="s">com.simplicite.util.ObjectHooks$Wrapper.call(ObjectHooks.java:100)</div><div class="s">com.simplicite.util.ObjectHooks.preValidate(ObjectHooks.java:605)</div><div class="s">com.simplicite.util.engine.ObjectManager.validate(ObjectManager.java:111)</div><div class="s">com.simplicite.util.engine.ObjectDirect.validate(ObjectDirect.java:168)</div><div class="s">com.simplicite.util.ObjectDB.validate(ObjectDB.java:647)</div></div>
2024-02-21 10:40:16,786|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ECORED0001|system|com.simplicite.objects.System.TranslateAction|getField||Error Object TranslateAction: unknown field tsl_type.
2024-02-21 10:40:16,786|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ECORED0001|system|com.simplicite.objects.System.TranslateAction|getField||Error Object TranslateAction: unknown field tsl_id.
2024-02-21 10:40:16,785|SIMPLICITE|ERROR||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ECORED0001|system|com.simplicite.objects.System.TranslateAction|getField||Error Object TranslateAction: unknown field tsl_id.
2024-02-21 10:40:16,698|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ICOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Information I/O: Import object ViewItem, status = OK
2024-02-21 10:40:16,605|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ICOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Information I/O: Import object FieldStyle, status = OK
2024-02-21 10:40:15,609|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ICOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Information I/O: Import object View, status = OK
2024-02-21 10:40:15,136|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ICOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Information I/O: Import object Module, status = OK
2024-02-21 10:40:14,450|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ICOREIO001|designer|com.simplicite.util.integration.SAXImportXML|importObject||Information I/O: elements to load = 16
2024-02-21 10:40:14,332|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ICOREIO001|designer|com.simplicite.util.engine.Interface|importData||Information I/O: Scanning xml file: CrbAppSdt.xml from ZIP data
2024-02-21 10:40:14,332|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|ICOREIO001|designer|com.simplicite.util.engine.Interface|importData||Information I/O: Start scanning data, origin: Import module: CrbAppSdt
2024-02-21 10:40:14,318|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.AsyncTracker|add||Event: - Import data
2024-02-21 10:40:14,316|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.AsyncTracker|add||Event: - Load JSON tree
2024-02-21 10:40:14,086|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.AsyncTracker|add||Event: Import module CrbAppSdt
2024-02-21 10:40:14,086|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.AsyncTracker|add||Event: - Analyse app-info.json
2024-02-21 10:40:14,071|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.AsyncTracker|add||Event: - Extract GZIP files
2024-02-21 10:40:14,070|SIMPLICITE|INFO||https://Rec-sim:10498/suividspbreizhgo|/suividspbreizhgo|INFO|system|com.simplicite.util.AsyncTracker|add||Event: Import application CrbAppSdt...
```
[/details]

## Answer
Bonjour,

La log indique que certains objets (ici une Action CrbSdtPrmContratStatut) ne sont pas connus pour leur associer une traduction.

> Object not found for tsl_object: Action CrbSdtPrmContratStatut

Par ailleurs la traduction exportée semble erronée : "Crb sdt prm contrat statut"

Il faut vérifier dans quel ordre vous importez vos modules, et donc à quel moment l'Action `CrbSdtPrmContratStatut` est créée.
- Importez les modules un par un pour vérifier
- puis dans le même ordre au niveau du package (champ ordre)  de l'application

Et enfin que vous n'avez pas de dépendances croisées entre vos modules.
Sinon il faudra repackager vos paramétrages à la source et les réexporter.
