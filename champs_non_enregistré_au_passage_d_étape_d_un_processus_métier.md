# Champs non enregistré au passage d'étape d'un processus métier

**URL:** https://community.simplicite.io/t/8700

## Question
### Request description
Bonjour, j'ai un comportement non-voulu sur un processus métier.

### Steps to reproduce

 Lorsque je suis sur la 1ere activité, je peux renseigner 4 attributs.

![Capture d'écran 2024-09-03 115148|690x382, 75%](upload://bPXqiwAax2W2VHqD2be2bsj5F7.png)

Pareil pour la 2nd activité avec une mutitude de champs à renseigner.

![Capture d'écran 2024-09-03 115232|690x323, 75%](upload://FCj0wTaaEo8IkBNNm3zKz34pgx.png)

Cependant lorsque j'arrive dans la 3e activité qui est celle de la synthèse( activité 1 + 2) ,2 attributs de la 1ere activité ne sont pas enregistré ( "Produit ou service " et "type"). Et les autres attributs lié à d'autres activité le sont bien.

![Capture d'écran 2024-09-03 115404|690x348, 75%](upload://zP9gjcu57n7YIPdcNEH8R2zRAzN.png)

Le seul moyen d'avoir ses 2 champs bien enregistrer est de les reconfigurer en synthèse (activité 3) ou bien :
     
     -de l'activité 1 
     -aller vers la activité 2, 
     -faire précédent vers l'activité 1
     -sélectionner les champs lié à ses 2 attributs
     -refaire suivant pour aller dans la 2  
     -suivant encore dans la 3 
   à ce moment là, cela marche les 2 attributs de la 1er activité sont bien dans la 3e

Auriez-vous une idée d'ou pourrait venir ce problème et pouvoir le régler pour que tous soit pris en compte dès le 1er passage ?


### Technical information

[details="Instance /health"]
```text
Platform]
Status=OK
Version=6.1.2
BuiltOn=2024-08-05 20:47
Git=6.1/467048f75ed27520b8cf7eca0ba57eeb2e0e1a0f
Encoding=UTF-8
EndpointIP=100.88.202.116
EndpointURL=http://lbc-77449-app-f4787f7fc-tcr56:8080
TimeZone=Europe/Paris
SystemDate=2024-09-03 14:44:13
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
Tout est possible.
Vous pouvez effectivement vous passer de l'activité 1.
Dans ce cas, il faut pré-créer l'objet nécessaire dans le preLock (avant ouverture) de l'activité 2 qui devra être de type Mise à jour (et pas création) à la place d'aller chercher le rowId de l'activité 1.

Exemple :

```java
@Override
public Message preLock(ActivityFile context) {
	String step = context.getActivity().getStep();
	if ("MyStep2".equals(step)) {
		// pre-create the object before update at step 2
		ObjectDB o = getGrant().getTmpObject("MyObject1");
		try {
			o.resetValues(true, ObjectField.DEFAULT_ROW_ID);
			o.setFieldValue("myField1", "...");
			// ...
			o.getTool().validateAndSave();
		}
		catch (Exception e) {
			AppLog.error("error", e, null);
			return Message...
		}
		// Force the row_id to be opened at step 2
		context.setDataFile("Field", "row_id", o.getRowId());	
	}
	return null;
}
```
