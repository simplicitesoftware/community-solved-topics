# Les modifications réalisées sur un champ de l'objet dans la pop-up de confirmation d'une action ne sont pas postées

**URL:** https://community.simplicite.io/t/6893

## Question
### Request description

Bonjour,

Si on modifie la valeur des attributs dans une pop-up de confirmation d'action les nouvelles valeurs ne sont pas conservées après avoir cliqué sur le bouton "Confirmer".

Nous avions constaté le même comportement il y a un peu plus d'un an lors du passage d'une version mineure de la 5.1 à une autre. Je n'ai pas réussi à retrouver le post dans le forum mais ce comportement n'avait pas été considéré comme un bug mais comme une demande d'évolution de votre côté. Une nouvelle version de la 5.1 était sortie peut de temps après avec l'évolution pour conserver les modifications réalisées dans la pop-up (la Doc Simplicitié est KO je n'ai donc pas pu regarder les releases notes de la 5.1 pour retrouver la version en question :confused:).

### Steps to reproduce

En partant du module de Demo :

1. J'ai créé une nouvelle action pour l'objet DemoOrder avec le paramétrage suivant :

![image|690x336](upload://peJWSWfC1Hm73xnLYNDNQoJ6ID8.png)

![image|690x334](upload://bx1OvnHjr26shSXN9b8kEenY927.png)

![image|690x337](upload://7u69EoPuEru3aqZmSsv8FMkTVfi.png)

2. Dans le code de DemoOrder j'ai ajouté les méthodes suivantes :

```
    @Override
	public void initAction(Action action) {
		
		String actionName = action.getName();
		String lang = getGrant().getLang();
		
		if ("DEMO_ORD_STATUS-P-V".equals(actionName) || "DEMO_ORD_CUSTOM_VALIDATION".equals(actionName)){
			
			ObjectField f = action.getConfirmField(lang, "demoOrdDeliveryDate");
			f.setUpdatable(ObjectField.UPD_ALWAYS);
			f.setRequired(true);
		}
		
	}
	
	public String customValidation(Map<String,String> params) {
		
		for (Map.Entry<String,String> entry : params.entrySet()) {
			AppLog.warning("DEBUG / customValidation / " + entry.getKey() + " : " + entry.getValue(), null, getGrant());
			setFieldValue(entry.getKey(), entry.getValue());
		}
		
		setStatus("V");
		
		try {
				
			var bot = new BusinessObjectTool(this);
			bot.validateAndUpdate();
			
		} catch(ValidateException | UpdateException e) {
			
			AppLog.error("Error", e, getGrant());
			return e.getMessage();
			
		}
		
		return null;
		
	}
```

3. J'ouvre le formulaire d'une commande à l'état "En attente". La date de livraison est "21/09/2023 08:00:00".
4. Je clique sur l'action "ORD CUSTOM VALIDATION" :

![image|690x200](upload://mPCEK764lltRKu9jEBNoKlt3XF8.png)

5. La pop-up de confirmation s'ouvre, je modifie la date de livraison pour mettre "10/09/2023 08:00:00" et je clique sur "Confirmer" :

![image|690x155](upload://yrGj4RCoQyox4C2g5bkeS1KKIDN.png)

6. La commande passe bien à l'état "Validée" comme indiqué dans le code Java, mais la date de livraison indiquée dans la pop-up de confirmation n'a pas été conservée :

![image|690x175](upload://jWCy6lb7VODeJ2mrlDOu2WANN63.png)

Dans les logs on peut voir que la méthode "customValidation" ne reçoit pas dans le paramètre "params" la nouvelle valeur pour la date de livraison :

![image|690x22](upload://1sHqbdw9WsztuUxBRW2kPZGqBkC.png)



Avec Simplicité 5.1.62 et 5.2.47 je n'ai pas ce problème, les modifications réalisées dans la pop-up sont bien conservées après avoir cliqué sur "Confirmer" et avec le même code Java.


### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.3.14
BuiltOn=2023-09-14 16:00
Git=5.3/3426322921bcc8643efdc55d9062fa8fd800eeb8
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2023-09-18 15:43:05

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2023-09-18 15:43:00

[Server]
ServerInfo=Apache Tomcat/9.0.80
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.95.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.8.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.8.1+1
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=296822
HeapSize=512000
HeapMaxSize=2007040
TotalFreeSize=1791862

[Cache]
ObjectCache=238
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=238
ProcessCacheMax=10000
ProcessCacheRatio=2
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=13.12 (Debian 13.12-1.pgdg120+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.6.0
DBDate=2023-09-18 15:43:05
DBDateOffset=0
DBPatchLevel=5;P03;6fe15f9e90e4e748520be6bc2eee7a45
UsingBLOBs=true

[Healthcheck]
Date=2023-09-18 15:43:05
ElapsedTime=113
```
[/details]

## Answer
La mise à jour autorisée par code (via initAction) sur un champ X de l'objet dans une confirmation d'Action sera postée au back en 5.3.17, et accessible dans la méthode de l'action `action.getConfirmField(x).getValue()`.

Attention 
- les éventuelles contraintes ou règles implémentées pour X au niveau du formulaire d'objet ne seront pas appliquées au dialogue de confirmation,
- donc cela ne changera pas la valeur sauvegardée en base, mais uniquement la valeur reçue dans l'action, dont le code spécifique devra appliquer les mises à jour éventuelles pour ce champ (contrôle de saisie, persistance...).

Il convient de préférer un design plus classique :
- où les champs de l'objet sont proposés en lecture seule par défaut pour confirmation de la saisie effectuée sur le formulaire (ex : valider un montant calculé ou un document généré au save)
- où les champs spécifiques ajoutés à l'action permettent de spécialiser son traitement unitaire (ex : indiquer un email pour envoyer une notification, l'email n'est pas conservé sur l'objet mais uniquement utilisé par l'action pour notifier quelqu'un)
