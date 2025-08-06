# Valeur par défaut formulaire de création dans un business process

**URL:** https://community.simplicite.io/t/10468

## Question
### Request description

*Bonjour,*

Dans le cadre d’un business process, j’aimerais pour simplifier l’utilisation par l’utilisateur mettre des champs par défaut dans un formulaire de création.

Le post similaire suivant : https://community.simplicite.io/t/affichage-dune-valeur-par-defaut-dans-un-champ-dun-formulaire/8996

ne répond pas à mon besoin puisqu’il ne s’agit pas ici pour cela de surcharger la valeur par défaut pour tout l’objet mais uniquement dans le cadre du business process.

Plus précisément mon besoin est :

* L’utilisateur sélectionne un site

  ![Select site BP|690x343](upload://a3H5B7iAODEirjoP7ROMTwlhw2Z.png)
* Dans l’étape suivante, il souhaite créer un nouveau TPL :

  ![Create tpl BP|690x263](upload://8udpfEpmL334IK97C68vQZ6heC9.png)
* Lorsque le formulaire s’affiche, je veux que le site précédemment sélectionné soit pré renseigné (ST47068241 dans Real estate asset Identifier pour cet exemple)

  ![Form creation tpl|690x377](upload://uOOdz47SSsHlqzcwrhqc6r1c7vX.png)

  
  Pour l’instant, dans le hook preLock je parviens à récupérer le row_id du site sélectionné et j’ai tenté de le set dans l’objet et d’utiliser la méthode setDefault mais ça ne fonctionne pas. J’imagine que c’est parce qu’il faudrait passer par le hook initCreate mais je ne peux pas l’utiliser puisqu’il n’est pas présent dans la classe Processus.

  ![code tpl|543x203](upload://5kin4xtDUFtqhmtBJBk80ek4JDj.png)

Auriez-vous des conseils pour m’aider à répondre à ce besoin svp ?

Thomas

### Steps to reproduce

*This request concerns a 5.3.67 Simplicité instance*

### Technical information

[details="Instance /health" open]
```text

[Platform]
Status=OK
Version=5.3.67
BuiltOn=2025-04-11 11:34
Git=5.3/e334b5e28643fc368f39b881aeeb2f57f2627fcc
Encoding=UTF-8
EndpointIP=100.88.75.136
EndpointURL=http://rfs-70537-app-545b985d95-znn78:8080
TimeZone=Europe/Paris
SystemDate=2025-08-05 09:33:15

[Application]
ApplicationVersion=0.16 dev
ContextPath=
ContextURL=https://rfs-70537-app.ext.gke2.int.gcp.renault.com
ActiveSessions=2
TotalUsers=379
EnabledUsers=351
LastLoginDate=2025-08-05 09:27:28

[Server]
ServerInfo=Apache Tomcat/9.0.104
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[OS]
Name=Linux
Architecture=amd64
Version=6.6.87+
DockerImageName=almalinux9
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.14
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.14+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=211275
HeapSize=335872
HeapMaxSize=2928640
TotalFreeSize=2804043

[Cache]
ObjectCache=286
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=1
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
VendorName=postgresql
ProductName=PostgreSQL
ProductVersion=15.12
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.7.5
DBDate=2025-08-05 09:33:15
DBDateOffset=0
DBPatchLevel=5;P03;f0ca291621149bc79765db12ce1e0102;67
UsingBLOBs=true

[Healthcheck]
Date=2025-08-05 09:33:15
ElapsedTime=12

```

[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
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
Bonjour, 

A date, la plateforme ne différencie pas la création via la liste principale de l'objet et la création via un process, i.e. il s'agit de la même instance, on ne peut donc pas conditionner l'implémentation de l'`initCreate` au nom d'instance. 

Il faut donc implémenter un pattern qui permet de passer une valeur saisie/sélectionnée au sein du process au hook `initCreate` de l'objet. 

On peut utiliser les paramètres stockés au niveau Grant : `getGrant().setParameter("MY_PARAM", "param_value"`([setParameter](https://platform.simplicite.io/5/javadoc/com/simplicite/util/GrantCore.html#setParameter(java.lang.String,java.lang.String))).

En prenant le cas du process implémenté dans le module Demo (téléchargeable depuis l'App store de votre instance)

Dans `DemoOrderCreate.java` :
```
@Override
public void postValidate(ActivityFile context) {
	String step = context.getActivity().getStep();
	// étape de sélection du fournisseur
	if ("ORDC-200".equals(step)) {
		String rowId = context.getDataValue("Field", "row_id");
		// valorisation d'un paramètre custom
		getGrant().setParameter("wkf_sup_id", rowId);
	}
}
```

Dans `DemoProduct.java` : 
```
@Override
public void initCreate() {
	// récupération du param setté dans le process
	String wkfSupId = getGrant().getParameter("wkf_sup_id"); 
	if (!"".equals(wkfSupId)) {
		setFieldValue("demoPrdSupId", wkfSupId);			
	}
}
```

Dans votre cas, vous pouvez appliquer la même logique à l'objet TPL avec une valorisation du paramètre dans l'étape de sélection du Site.

Il faut penser à également implémenter dans votre process les hooks abandon / cancel / terminate : https://docs.simplicite.io/docs/core/businessworkflow-code-hooks pour supprimer / setter à vide le paramètre custom. 

PS : votre instance n'est pas à jour avec la dernière release de la 5.3, il faut impérativement vous maintenir à jour pour qu'on puisse vous aider au mieux.
