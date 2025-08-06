# Export conditionnel de champs d'objets référencés par un objet

**URL:** https://community.simplicite.io/t/6564

## Question
Description

Je souhaite exporter "conditionnellement" les attributs d'un objet référencé par un autre objet.

En gros, je souhaite exporter certains champs d'un objet_2 (affiché en onglet dans le formulaire de l'objet_1), lorsque j'exporte l'objet_1.

Dans le fichier XLS produit, une feuille nommée "objet_2" est bien générée, mais cette dernière ne contient pas tous les attributs que je souhaite y trouver.

En gros, l'objet_2 contient des contraintes/impacts de visibilité sur certains champs, mais je me demandais si ces contraintes étaient "exécutées" lorsqu'on exporte l'objet_1 (référençant l'objet_2) ?

J'avais pensé ajouter un test dans une des contraintes de visibilité de l'objet_2, du style
"export_objet_1" == [OBJECTINSTANCENAME]
mais ça ne semble pas fonctionner...

Merci pour votre aide.

## Answer
Ok vu, en fait les objets liés dans un export Excel ne sont pas des instances d'export comme l'objet principal (isExportInstance), ce sont bien des instances panel (isPanelInstance avec le parent object d'export renseigné), donc le code ne peut pas être mis dans le postLoad (trop tôt, le parent n'est pas encore renseigné), ni dans le preExport (pas appelé).

Exemple dans la démo d'un export de "client", pour masquer le code client dans l'onglet "commande" :

```java
// DemoOrder
@Override
public List<String[]> postSearch(List<String[]> rows) {
	if (isPanelInstance() && getParentObject()!=null && getParentObject().getName().equals("DemoClient")) {
		AppLog.info("demoCliCode exportable = false", null);
		getField("demoCliCode").setExportable(false);
	}
	return rows;
}
```

On devra garder l'instance panel pour compatibilité ascendante; Par contre, on va améliorer la recherche en base pour invoquer la méthode `searchExport` paginée, et non pas un `search` non paginé, afin de bénéficier des hooks pre/postExport des objet liés.
