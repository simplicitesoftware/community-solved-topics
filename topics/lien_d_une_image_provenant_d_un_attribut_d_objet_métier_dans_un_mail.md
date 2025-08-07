# Lien d'une image provenant d'un attribut d'objet métier dans un mail

**URL:** https://community.simplicite.io/t/6200

## Question
### Request description

Bonjour, nous rencontrons des difficultés  sur le lien d'une image provenant d'un attribut d'objet métier dans un e-mail, ce qui me laisse à penser que je ne m'y prends probablement pas de la bonne façon. 

Voici ce que j'ai constaté :
Le logo que j'essaie d'obtenir est un attribut image de l'objet métier CrbPcaRefEpci. Je cherche l'instance adéquate et j'essaie d'ajouter l'image au corps de mon mail.
```
	public static String sendMailTest(ObjectDB demande){
		String mailBody="";
		MailTool mailer = new MailTool(demande.getGrant());
		
		mailer.setFrom("passcommerce@bretagne.bzh");
		mailer.setSubject("TEST PCA MAIL");
		
		mailBody="<HTML><BODY style='background-color: #f7f7f7;margin-left:60px;padding-top:0; font-family:Trebuchet MS Regular; font-size:12px; color:black';>";	
		mailBody += "<div style='font-size:12px;max-width:540;background-color: #ffffff;'>";

		MailImage logoEpci = null;
		ObjectDB refEpciTmp = demande.getGrant().getTmpObject("CrbPcaRefEpci");
		refEpciTmp.resetFilters();
		refEpciTmp.resetValues();
		refEpciTmp.setFieldFilter("pcaRefEpciSiren",demande.getFieldValue("pcaDemandeEpciSiren"));
		for(String[] rowEcpi : refEpciTmp.search()) {
			refEpciTmp.setValues(rowEcpi);
			logoEpci=mailer.getMail().documentImage(refEpciTmp,refEpciTmp.getField("pcaRefEpciLogo"));
		
			if (logoEpci!=null) {
				String idLogoEpci=mailer.addImage(logoEpci);
				mailBody+="<img src=\"cid:"+idLogoEpci+"\" />";
			}
		}
		mailBody +="</div></BODY></HTML>";
		
		mailer.setBody(mailBody);		
		mailer.addRcpt(getRcpt(demande,"accuseEnvoiLi_DEMANDEUR"));

		try {
			mailer.send();
			return "OK";
		} catch (Exception e) {
			return Message.formatSimpleError("Erreur d'envoi de mail" + e.getMessage());	
		}
	}
```
Dans cette configuration, documentImage retourne null, et donc l'intégration ne fonctionne pas.

Ensuite pour tester j'ai tenté de retrouver directement l'image avec getDocument sur l'attribut de l'objet CrbPcaRefEpci :
```
	public static String sendMailTest(ObjectDB demande){
		String mailBody="";
		MailTool mailer = new MailTool(demande.getGrant());
		
		mailer.setFrom("passcommerce@bretagne.bzh");
		mailer.setSubject("TEST PCA MAIL");
		
		mailBody="<HTML><BODY style='background-color: #f7f7f7;margin-left:60px;padding-top:0; font-family:Trebuchet MS Regular; font-size:12px; color:black';>";	
		mailBody += "<div style='font-size:12px;max-width:540;background-color: #ffffff;'>";
		
		MailImage logoEpci = null;
		ObjectDB refEpciTmp = demande.getGrant().getTmpObject("CrbPcaRefEpci");
		refEpciTmp.resetFilters();
		refEpciTmp.resetValues();
		refEpciTmp.setFieldFilter("pcaRefEpciSiren",demande.getFieldValue("pcaDemandeEpciSiren"));
		for(String[] rowEcpi : refEpciTmp.search()) {
			refEpciTmp.setValues(rowEcpi);
				
			DocumentDB logoDoc = refEpciTmp.getField("pcaRefEpciLogo").getDocument(demande.getGrant());
			logoEpci=mailer.getMail().documentImage(refEpciTmp,refEpciTmp.getField("pcaRefEpciLogo"));
		
			if (logoEpci!=null) {
				String idLogoEpci=mailer.addImage(logoEpci);
				mailBody+="<img src=\"cid:"+idLogoEpci+"\" />";
			}
		}
		mailBody +="</div></BODY></HTML>";
		
		mailer.setBody(mailBody);		
		mailer.addRcpt(getRcpt(demande,"accuseEnvoiLi_DEMANDEUR"));

		try {
			mailer.send();
			return "OK";
		} catch (Exception e) {
			return Message.formatSimpleError("Erreur d'envoi de mail" + e.getMessage());	
		}
		
	}
```
Et dans cette situation, non seulement l'appel à getDocument retourne bien le document, mais ensuite documentImage parvient également à lier l'image, alors qu'a priori je ne vois aucun lien direct entre les deux.

Je soupçonne un problème d'habilitation, mais si c'est le cas je ne suis pas sûr de comment le régler. Et même si le code de la deuxième version fonctionne, ça ne me parait pas logique et donc potentiellement amené à ne plus fonctionner, ou créer d'autres problèmes.

Voyez-vous ce qui pourrait expliquer cela?

Merci 

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.2.36
BuiltOn=2023-04-05 18:35
Git=5.2/966009edb80e3e6fad18685d6ef8131b63725d28
Encoding=UTF-8
EndpointIP=127.0.0.1
EndpointURL=https://dev-sim:10773/passcommerce
TimeZone=Europe/Paris
SystemDate=2023-04-14 11:07:03

[Application]
ApplicationVersion=1.0.0
ContextPath=/passcommerce
ContextURL=http://passcommerce.dev-sim.cr-bretagne.fr/passcommerce
ActiveSessions=3
TotalUsers=20
EnabledUsers=18
LastLoginDate=2023-04-14 11:02:38

[Server]
ServerInfo=Apache Tomcat/9.0.73
ServerType=WEB
ServerActiveSessions=0
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1062.9.1.el7.x86_64
SystemEncoding=UTF-8

[Disk]
DiskFree=17649
DiskUsable=15229
DiskTotal=57303

[JavaVM]
Version=11.0.6
Vendor=Oracle Corporation
VMName=OpenJDK 64-Bit Server VM
VMVersion=11.0.6+10-LTS
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=122179
HeapSize=417792
HeapMaxSize=524288
TotalFreeSize=228675

[Cache]
ObjectCache=136
ObjectCacheMax=10000
ObjectCacheRatio=1
ProcessCache=11
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
ProductName=MySQL
ProductVersion=5.5.5-10.2.9-MariaDB-10.2.9+maria~stretch
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-j-8.0.32 (Revision: fa4912a849140828e48162a2c396c8df0091bed7)
DBDate=2023-04-14 11:07:03
DBDateOffset=0
DBPatchLevel=5;P02;c49a0b5b4201087167f67be076255c60
UsingBLOBs=true

[Healthcheck]
Date=2023-04-14 11:07:03
ElapsedTime=11
```
[/details]

## Answer
OK c'est vu et corrigé pour le cas des tests unitaires (ou autre usage indirect du même genre = search/select basique sans chargement des docs infos du record).

Ce sera dans la version 5.2.37 livrée d'ici lundi
