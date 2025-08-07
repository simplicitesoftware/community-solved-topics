# Enregistrement données objet fils depuis objet père

**URL:** https://community.simplicite.io/t/4906

## Question
Bonjour,

Je suis sur un écran d'un objet A dans une vue formulaire. Dans un onglet, j'affiche, en formulaire, les champs de l'objet fils B (relation 0,1 dont les attributs ont été incorporés à l'objet fils). Ces champs sont en lecture seule et ne sont alimentés que lorsque le statut de l'objet A est mis à jour pour arriver dans un statut défini.

Comment faire pour alimenter ces champs côté Back ? 

J'ai essayé 2 choses.
1) Alimenter dans le code de l'objet A, dans le postUpdate (ou preUpdate), via "setFieldValue(%nom_champ%, %valeur_champ%)" mais les champs ne sont pas trouvables.
2) Toujours dans le postUpdate (ou preUpdate) de l'objet A, en récupérant l'objet temp de l'objet B puis en le mettant à jour.
ObjectDB objetB = g.getTmpObject("Objet_B);
BusinessObjectTool bTool = objetB.getTool();
bTool.getForUpdate(row_id);
....
bTool.validateAndUpdate();
==> Erreur : Mise à jour impossible, la donnée a été déjà modifiée par: designer@2022-05-25 12:37:29
Pourtant l'objet est bien défini en "optimistic".

Version de Simplicite : 5.1.31
BDD : PostGre SQL

En vous remerciant.

Bruno

## Answer
Bonjour Bruno, 

Tu peux directement implémenter la logique dans le `preSave()` au niveau de l'objet B :
```java
@Override
public String preSave() {
	
	if(!Tool.isEmpty(getParentObject())){
		setFieldValue("myField", "MY_VALUE");
	}
	
	return null;
}
```
