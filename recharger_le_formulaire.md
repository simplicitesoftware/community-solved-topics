# Recharger le formulaire

**URL:** https://community.simplicite.io/t/4661

## Question
Bonjour,

Je change des valeurs dans des champs par code ( avec un validateAndSave).

Les valeurs sont bien changées mais il est nécessaire de recharger le formulaire pour les voir.
![image|118x28](upload://nHOKbRDCVnF3o6Jp2Q0wFhj4PGU.png)


Que puis-je ajouter dans mon code pour recharger le formulaire?
```
		if (this.getField("HertaProcessStatut").getValue().equals("2"))
		{
			this.setFieldValue("HertaProcessStatut", "3");
			this.setFieldValue("HertaProcessDateFichierCSV", dateTimeNow() );
			try{
				new BusinessObjectTool(this).validateAndSave();
			}
			catch(Exception e){
				AppLog.error(getClass(), e.getStackTrace()[0].getMethodName(), "Bouton TransAttr", e, null);
			}

		} else {
			
			return Message.formatSimpleInfo("L'export ne peut se faire qu'à l'étape : \n VALIDE AVANT ATTRIBUTION" );
		}

```


Fabrice

## Answer
Merci! c'est parfait.
