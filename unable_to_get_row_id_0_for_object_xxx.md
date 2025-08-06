# Unable to get row ID 0 for object XXX

**URL:** https://community.simplicite.io/t/4375

## Question
Bonjour,
 
Je souhaite créer une nouvelle formation pour un employé. Voici le code de ma méthode :
```
private void createTrainingOnUser(ObjectDB usr){
		try{
			ObjectDB train = Grant.getSystemAdmin().getTmpObject("HrFormations");
			BusinessObjectTool trainOt = train.getTool();
			trainOt.getForCreate();
			
			train.resetValues(true);
	        train.setRowId(ObjectField.DEFAULT_ROW_ID);
	        train.setFieldValue("hrFrmSalId", usr.getRowId());
	        train.setFieldValue("hrFrmType", "OFFICE");
	        train.setFieldValue("hrFrmStatus", "DEMAND");
	        train.setFieldValue("hrFrmDate", getFieldValue("hrEmpArrivalDate"));
	        trainOt.validateAndSave();
		} catch(Exception e) {
			AppLog.error("[IN parseAuth] Error creating new training for users", e, Grant.getSystemAdmin());
		}
	}
``` 

Le problème, c'est que j'obtiens l'erreur suivant : 
![image|690x69](upload://9mWDoyaM8g7omQiWTqCLYoDwQnj.png)
voici ma table:
![image|316x236](upload://mFS5zEXQilXlaYLcjet32WZW7Wr.png)


**Petite précision :** J'ai utilisé le même logique de code pour ajouter un nouvel utilisateur et ça fonctionne.

Auriez-vous une idée d'où peut provenir l'erreur ?

## Answer
Votre code est redonnant: si vous faites `resetValues(true)` et `setRowId(ObjectField.DEFAULT_ROW_ID)`, faire un `getForCreate` avant ne sert à rien.

Ensuite y-a-t il une raison d'utiliser le grant système plutôt que le grant courant ? 
Dans un cas comme dans l'autre le grant doit avoir les droits de création sur l'objet en question.
