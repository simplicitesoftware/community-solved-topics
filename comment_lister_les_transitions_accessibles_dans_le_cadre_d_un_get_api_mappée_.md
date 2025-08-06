# Comment lister les transitions accessibles dans le cadre d'un GET API mappée?

**URL:** https://community.simplicite.io/t/5254

## Question
### Request description

*Bonjour, je cherche à déterminer dans le cadre du traitement d'un GET API les actions disponibles sur le record faisant l'objet du GET. Je n'ai pas eu de soucis pour déterminer l'accessibilité des actions socle UPDATE/DELETE. Pour les actions spécifiques, je pense avoir réussi. Pour les actions de transition, je patauge... Et du coup j'ai un doute sur ce que j'ai fait avant sur les actions spécifiques...*

Voici mon code : (la méthode `getAvailableActionsOnItem` est appelée sur chaque record GET donc une fois sur un GET/rowId et sur chaque record retourné par un GET/search -> c'est dans ce contexte que j'appelle obj.select(rowId) avant de passer obj en paramètre de `getAvailableActionsOnItem`)
```
private List<String> getAvailableActionsOnItem(ObjectDB obj) {
	List<String> availableActionList = new ArrayList();
	if (obj.isUpdateEnable(obj.getValues())) {
		availableActionList.add("UPDATE");
	}
	if (obj.isDeleteEnable(obj.getValues())) {
		availableActionList.add("DELETE");
	}
	List<Action> actions = obj.getGrant().getActions(obj.getName());
	for (int i = 0; actions != null && i < actions.size(); ++i) {
		Action action = (Action)actions.get(i);
		if (obj.getGrant().accessAction(obj.getName(), action.getName()) && action.isEnabled() && action.isServerSide()) {
			if (action.isConfirm()) {
				AppLog.warning("getAvailableActionsOnItem getAction("+action.getName()+").setConfirm(false)", null, obj.getGrant());
				action.setConfirm(false);
			}
			availableActionList.add(action.getName());
		}
	}
	ObjectField statusField = obj.getStatusField();
	if (statusField != null) {
		// AppLog.warning("getAvailableActionsOnItem statusField="+statusField.getName(), null, getGrant());
		List<FieldStateTransition> stateModel = statusField.getStateModel();
		for (int i = 0; stateModel != null && i < stateModel.size(); ++i) {
			Action action = stateModel.get(i).getAction();
			if (action != null) {
				// AppLog.warning("getAvailableActionsOnItem action="+action.getName(), null, getGrant());
				if (/*obj.getGrant().accessAction(obj.getName(), action.getName())*//*DEBT*/stateModel.get(i).getFromState().equals(obj.getValues()[statusField.getIndex(obj)]) && action.isEnabled()) {
					if (action.isConfirm()) {
						// AppLog.warning("getAvailableActionsOnItem getAction("+action.getName()+").setConfirm(false)", null, obj.getGrant());
						action.setConfirm(false);
					}
					// AppLog.warning("getAvailableActionsOnItem added action="+action.getName()+" isActionEnabled="+obj.isActionEnable(obj.getValues(), action.getName())+"", null, obj.getGrant());
					availableActionList.add(action.getName());
				} else {
					// AppLog.warning("getAvailableActionsOnItem isActionEnabled="+obj.isActionEnable(obj.getValues(), action.getName())+" getAction("+action.getName()+") accessAction="+obj.getGrant().accessAction(obj.getName(), action.getName())+" isEnabled="+action.isEnabled()+" fromState="+stateModel.get(i).getFromState()+"", null, obj.getGrant());
				}
			} else {
				// AppLog.warning("getAvailableActionsOnItem tran("+i+") is null", null, getGrant());
			}
		}
	}
	return availableActionList;
}
```
Voici les logs générées par un GET/rowId :
```
2022-09-12 10:22:00,610|SIMPLICITE|WARN||http://a04f396b17ad:8080||WARN|a068181|com.simplicite.commons.RenaultAPI.RESTTranslatedObjectExternalObjectCommons|getAvailableActionsOnItem||Evénement: getAvailableActionsOnItem isActionEnabled=true getAction(PMISURVEYSTATUS-TBD-VAL) accessAction=false isEnabled=true fromState=TBD
2022-09-12 10:22:00,609|SIMPLICITE|WARN||http://a04f396b17ad:8080||WARN|a068181|com.simplicite.commons.RenaultAPI.RESTTranslatedObjectExternalObjectCommons|getAvailableActionsOnItem||Evénement: getAvailableActionsOnItem isActionEnabled=true getAction(PMISURVEYSTATUS-VAL-TBV) accessAction=false isEnabled=true fromState=VAL
2022-09-12 10:22:00,609|SIMPLICITE|WARN||http://a04f396b17ad:8080||WARN|a068181|com.simplicite.commons.RenaultAPI.RESTTranslatedObjectExternalObjectCommons|getAvailableActionsOnItem||Evénement: getAvailableActionsOnItem added action=PMISURVEYSTATUS-TBV-VAL isActionEnabled=true
2022-09-12 10:22:00,609|SIMPLICITE|WARN||http://a04f396b17ad:8080||WARN|a068181|com.simplicite.commons.RenaultAPI.RESTTranslatedObjectExternalObjectCommons|getAvailableActionsOnItem||Evénement: getAvailableActionsOnItem getAction(PMISURVEYSTATUS-TBV-VAL).setConfirm(false)
```
Le problème que je rencontre c'est que `isActionEnabled(values, transition)` renvoie toujours true et `accessAction(objet, transition)` renvoie toujours false... J'ai contourné en vérifiant a minima que le fromState de la transition était bien égal à la valeur courante du statusField mais c'est forcément incomplet car ça ne vérifie pas les droits effectifs du grant courant...
### Technical information

[details="Instance /health"]
```

[Platform]
Status=OK
Version=5.2.13
BuiltOn=2022-09-01 16:16
Git=5.2/ceeaa2a4f4995109f7c051724c9f36c1eac003f7
Encoding=UTF-8
EndpointIP=21.0.9.4
EndpointURL=http://a04f396b17ad:8080
TimeZone=Europe/Paris
SystemDate=2022-09-12 10:52:52

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://bca.dok-dev.intra.renault.fr
ActiveSessions=2
TotalUsers=8315
EnabledUsers=1870
LastLoginDate=2022-09-12 10:38:27

[Server]
ServerInfo=Apache Tomcat/9.0.65
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=3.10.0-1160.71.1.el7.x86_64
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.4.1
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.4.1+1
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=1216213
HeapSize=2722792
HeapMaxSize=3040896
TotalFreeSize=1534317

[Cache]
ObjectCache=90
ObjectCacheMax=10000
ObjectCacheRatio=0
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=4
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=2
ProductName=MySQL
ProductVersion=5.6.39-log
DriverName=MySQL Connector/J
DriverVersion=mysql-connector-java-8.0.30 (Revision: 1de2fe873fe26189564c030a343885011412976a)
DBDate=2022-09-12 10:52:52
DBDateOffset=0
DBPatchLevel=5;P02;73e57452f56dee646c9f7ac89aff7fa8
UsingBLOBs=true

[Healthcheck]
Date=2022-09-12 10:52:52
ElapsedTime=15
```
[/details]

[details="Simplicité logs"]
```text
Voir ci-dessus
```
[/details]

[details="Browser logs"]
```text
NA
```
[/details]

[details="Other relevant information"]
NA
[/details]

## Answer
Bonjour Bruno,

Je ne suis pas sûr de bien comprendre ta question car les API mappées offrent uniquement des verbes CRUD sur un objet, sans véhiculer de méta-data, ni de droits distants.

- Les actions sont liées aux droits (via fonction habilitées) et non aux objets directement (d'ailleurs on fait un getGrant().getAction)

`List<Action> actions = obj.getGrant().getActions(obj.getName());`
A mon avis, cela ne ramène pas les droits remote, mais uniquement les droits locaux = les actions déclarées et habilitées dans la session pour cet objet.

- Les transitions d'état n'ont pas nécessairement d'Action : au sens UI cela se traduit par afficher un bouton d'action, mais c'est avant tout la liste de valeur ENUM du champ statut qui ne contient que les états/transitions possibles (l'action n'est qu'un raccourci UI pour faire l'update du champ statut + save).

Il faut donc plutôt regarder directement les états possibles dans l'énuméré renvoyé getStatusField().getList() suite au select/get.
- Le premier code de la liste correspond à la valeur/état courant
- Les autres aux transitions habilitées côté remote
