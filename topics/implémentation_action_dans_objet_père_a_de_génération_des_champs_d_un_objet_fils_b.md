# Implémentation action, dans objet père A, de génération des champs d'un objet fils B

**URL:** https://community.simplicite.io/t/4924

## Question
Bonjour,

Voici ce que l'on essaie de faire :
Je suis sur un écran d’un objet A dans une vue formulaire. Dans un onglet, j’affiche, en formulaire, les champs de l’objet fils B (relation 0,1 dont les attributs ont été incorporés à l’objet fils). Ces champs sont en lecture seule et ne sont alimentés que lorsque le statut de l’objet A est mis à jour pour arriver dans un statut défini OU quand on clique sur un bouton type action affiché dans l'objet père A.

On souhaite développer la méthode derrière l'action (suite au clic sur le bouton associé) pour regénérer les champs de l'objet B depuis l'objet A. Cette méthode doit être implémentée dans l'objet A si j'ai bien compris. Toutefois, nous nous heurtons à la problématique remontée dans le ticket suivant : https://community.simplicite.io/t/enregistrement-donnees-objet-fils-depuis-objet-pere/4906

Comment implémenter cette génération des champs de l'objet fils B depuis une action attachée à l'objet père A ?

En vous remerciant.

Bruno

## Answer
Bonjour, 

Dans le post lié, il s'agissait d'alimenter les champs au save du parent. Avec des champs incorporés, le save du parent déclenche également le save de l'objet incorporé. 

Si il faut appeler la valorisation des champs au clic d'un bouton d'action, tu peux implémenter quelque chose du style : 

```java
public void populateOrCreateChildObject(){
	Grant g = getGrant();
	ObjectDB child = g.getTmpObject("MyObj");
	BusinessObjectTool childT = obj.getTool();
	
	try{
		//create or update
		String childId = //get linked object row_id
		synchronized(child){
			if(child.select(childId)){
				AppLog.info("exists", g);
				childT.getForUpdate(childId);
				/*
				 set values
				*/
				childT.validateAndSave();
			}
			else{
				childT.getForCreate();
				/*
				 set values
				*/
				childT.validateAndCreate();
			}
		}
	} catch(Exception e){
		//handle various exceptions
	}
}
```
