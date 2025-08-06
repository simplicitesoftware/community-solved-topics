# Récupération d'un champs d'objet simplicité importé pour set un identifiant dans un champs

**URL:** https://community.simplicite.io/t/6234

## Question
### Récupération d'un champs d'objet simplicité importé pour set un identifiant dans un champs

Bonjour,
je vous écris concernant une régression que j'ai pu constater ces derniers jours. Cela concerne la récupération de champs sous forme de métadonnées d'un objet simplicité.

### Le besoin

1. Intégration d'un objet simplicité Site d'une application nommée RFS dans un nouvel objet Site Assignment dans une application nommée RFF
2. Récupération du champs Identifier
3. Prendre cette valeur et setFieldValue dans le champs supReaIdentifier de l'objet Site Assignment d'RFF

Voici l'ensemble du code qui était auparavant fonctionnel:

```java
JSONObject linkedPwoRelay = new JSONObject(JSONTool.jsonMetaObject(getGrant(), getFieldValue("supSiaSite"), null));
		
		AppLog.info(getClass(), "SSAA", linkedPwoRelay.toString(), getGrant());

		String site = (String)linkedPwoRelay.get("userkeylabel").toString();
		String[] fullSite = site.split(" ");
		
		String identifiant1 = fullSite[0];
		String identifiant2 = fullSite[1];
		
		Boolean test1 = identifiant1.contains("SIT");
		Boolean test2 = identifiant2.contains("SIT");
		
		if(test1 == true && test2 == true) {
			this.setFieldValue("supReaIdentifier", identifiant2);
			AppLog.info(getClass(), "SSAA", "Y'A 2 SITES", getGrant());
		}
		else {
			this.setFieldValue("supReaIdentifier", identifiant1);
			AppLog.info(getClass(), "SSAA", "Y'A QU'UN SITE", getGrant());
		}
        
        AppLog.info(getClass(), "SSAA", site, getGrant());*/
        
        this.setFieldValue("supReaIdentifier", "test re7");
		this.save();
		AppLog.info(getClass(), "SITE :", this.getFieldValue("supReaIdentifier"), getGrant());
```

L'ensemble de ce code était positionné dans la méthode preValidate().

Aujourd'hui je n'arrive plus a récupérer les informations de mon jsonMetaObject() dans la méthode preValidate() alors que dans la méthode postSave() cela fonctionne normalement. Du coup, si je déplace mon code dans la méthode postSave(), je ne peux pas réaliser mon setFieldValue puisque je ne le verrai pas ensuite dans mon IHM.

Connaissez-vous une solution de contournement pour continuer à utiliser ma portion de code?
D'avance merci.

AISSANI Said

## Answer
Il y avait bien un pb avec les attributs "object" sur des objets remote (ainsi que sur d'autres types d'objets "service") lié un contrôle trop limitatif des foreign keys. Je n'ai pas remonté l'historique pour voir de quand date ce contrôle mais ce n'est pas récent.

En tout cas c'est corrigé dans la 5.2.38 qui a été livrée ce soir. 

Je pense que ça devrait résoudre votre pb => upgradez en 5.2.38

PS: Le module suivant, basé sur la démo, a été enrichi pour démontrer ce type de pattern avec lien "object" sur des objets remote : https://github.com/simplicitesoftware/module-remotedemo, en particulier cf. ce code de l'objet local "commande" qui utilise 2 attributs "object" vers des objets remote "produit" et "client": https://github.com/simplicitesoftware/module-remotedemo/blob/master/src/com/simplicite/objects/RemoteDemo/RemoteDemoLocalOrder.java:

![image|690x233](upload://9gccqkD2d6YhGLPGfPkeWz3Ly63.png)
