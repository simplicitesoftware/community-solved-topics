# Multiple alert caused by method after transition

**URL:** https://community.simplicite.io/t/3757

## Question
Bonjour,
j'ai une transition d'état qui possède une action, une notification par alerte, et une méthode (javascript) après transition. 
Depuis que j'ai mis la méthode après transition, mon alerte par mail se multiplie (près de 400 exécutions). Comment cela est-il possible ? 

Voici la méthode : 
```
	public List<String> investorValidation(){
		AppLog.info("====================", Grant.getSystemAdmin());
		setFieldValue("evlValManagerComment",getGrant().getLogin()+" - "+getGrant().getDBDate());
		save();
		return null;
	}
```

Un extrait des logs associés où on voit la répétabilité : 
```
2021-08-31 15:43:37,245 INFO [com.simplicite.bpm.Alert] SIMPLICITE|http://demo.simplicite.io:20128||INFO|designer|com.simplicite.bpm.Alert|send||Evénement: ALERT:EVL_ReviewedInvestor_Manager. Email send: Campagne :  2022-01-01 - Commentaire à saisir 
2021-08-31 15:43:37,240 INFO [com.simplicite.bpm.Alert] SIMPLICITE|http://demo.simplicite.io:20128||INFO|designer|com.simplicite.bpm.Alert|send||Evénement: ALERT:EVL_ReviewedInvestor_Manager. Email send: Campagne : 2022-01-01 - Commentaire à saisir 
2021-08-31 15:43:37,238 INFO [com.simplicite.bpm.Alert] SIMPLICITE|http://demo.simplicite.io:20128||INFO|designer|com.simplicite.bpm.Alert|send||Evénement: ALERT:EVL_ReviewedInvestor_Manager. Email send: Campagne : 2022-01-01 - Commentaire à saisir 
2021-08-31 15:43:37,236 INFO [com.simplicite.bpm.Alert] SIMPLICITE|http://demo.simplicite.io:20128||INFO|designer|com.simplicite.bpm.Alert|send||Evénement: ALERT:EVL_ReviewedInvestor_Manager. Email send: Campagne 2022-01-01 - Commentaire à saisir 
....etc...
```
Version=5.1.0
Merci pour votre aide,

## Answer
Bonjour,

Techniquement, une transition d'état est un "save" du champ statut modifié et qui appelle la méthode après transition si elle est renseignée. Donc faire un "save" sur l'instance qui est en train de travailler partira effectivement en boucle. C'est comme faire un "save" dans un pre/postSave.

La méthode après transition est là pour faire des actions en cascade (envoyer un email, mettre à jour un autre objet...), surtout pas pour modifier le record lui-même sinon ça se mord la queue.

Donc pour mettre à jour un champ du record :

- il faut juste setter le champ avant le "save" natif = dans le hook `preSave` ou `preUpdate` en testant les valeurs du statut pour savoir sur quelle transition on se trouve :

```java
// transition EVALUATED > REVIEWED_INVESTOR
if (getOldStatus().equals("EVALUATED") && getStatus().equals("REVIEWED_INVESTOR"))
  setFieldValue("evlValManagerComment", getGrant().getLogin()+" - "+Tool.getCurrentDatetime());
```		

- ou alors en utilisant une autre instance de cet objet : getTmpObject + tmp.select + tmp.setFieldValue + tmp.save
- ou alors en faisant du SQL direct : getGrant().update(...) à réserver au cas rare où on ne veut pas passer par les hooks

PS : pour avoir la date courante il faut utiliser `Tool.getCurrentDatetime()`
car `getGrant().getDBDate()` vous donnera la syntaxe SQL de la date en base.
