# Modifier les droits de création/suppression/modification depuis un tableau dans un formulaire

**URL:** https://community.simplicite.io/t/4575

## Question
Bonjour,

J'ai une relation 1-N entre mon objet métier `DdvGeneralMeeting` (Assemblée générale) et `DdvOrderOfDay` (Ordre du jour).

Dans mon formulaire, j'ai un tableau d'ordre du jour disponible depuis le formulaire de l'assemblée générale. J'aimerais que lorsque le statut de l'assemblée générale est en "Creation", je peux créer/modifier/supprimer un ordre du jour. Mais si le statut n'est pas celui ci, je doit juste pouvoir éditer en liste le tableau d'ordre du jour.

![image|690x357](upload://9RfbG76L59nOGt1PvbBVJDaQidd.png)

Pour réaliser cette contrainte, j'ai penser à 2 choses :
* Utiliser les méthodes telles que `isCreateEnable()` --> Le problème, c'est que ça marche pas de mon coté (peut être une erreur de ma part).
* Utiliser les contraintes de Simplicité. Dans ce cas là (le plus simple) si c'est possible, il faudrait que je puisse sélectionner le statut de l'AG depuis l'objet ordre du jour et je ne sais pas comment faire. PS : j'ai suivi la doc mais j'ai pas trouvé : https://docs.simplicite.io/documentation/01-core/expressions.md

![image|690x265](upload://AfZbVCnhEpXCJMpWPdlOw3RSEXE.png)


**Quelle est la meilleur solution selon vous et comment la mettre en place ?**

## Answer
Cf mon post précédent.
Il faut ramener l'attribut `ddvMetState` de `DdvGeneralMeeting` dans l'objet `DdvOrderOfDay`
https://docs2.simplicite.io/lesson/tutorial/configuration/relations
Il ne faut pas utiliser de simpleQuery pour récupérer la valeur de l'attribut ! 

```
@Override
public boolean isUpdateEnable(String[] row){
	ObjectDB gm = getParentObject();
	if( gm!= null && gm.getName().equals("DdvGeneralMeeting"))
		 return "GM_CREATION".equals(gm.getStatus());	
	return "GM_CREATION".equals(getFieldValue("ddvMetState"));
}
```
De plus mettre ce code dans une méthode et l'appeler dans les hooks appropriés.
