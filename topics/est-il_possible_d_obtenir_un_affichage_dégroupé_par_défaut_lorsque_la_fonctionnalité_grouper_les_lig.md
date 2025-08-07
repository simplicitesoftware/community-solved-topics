# Est-il possible d'obtenir un affichage dégroupé par défaut lorsque la fonctionnalité "Grouper les lignes" est activée?

**URL:** https://community.simplicite.io/t/5027

## Question
Simple question d'UX...

J'ai paramétré la fonction "autoriser le group by" sur un objet ainsi que l'obf_group_by d'un object field.
L'affichage groupé fonctionne très bien mais est-il possible d'obtenir un affichage dégroupé par défaut lorsque l'utilisateur arrive sur le liste ?

## Answer
#### Au niveau paramétrage des champs groupables en back

L'ordre des champs groupés est stocké dans chaque attribut (comme pour l'order by).

Pour grouper sur x,y :

```java
getField("x").setGroupByOrder(1, this);
getField("y").setGroupByOrder(2, this);
```

Les valeurs initiales sont dans set/getGroupByDefault() si on veut les remettre.


#### Au niveau du mode par défaut en front

C'est le front qui gère le flag du toggle groupé/dégroupé, par défaut il passe à vrai si un champ est groupable. Donc à mettre à l'init de l'objet front

```javascript
Simplicite.UI.hooks.MyObject = function(obj, cbk) {
	obj.locals.ui.list.groupBy = false;
	// ...
	cbk();
};
```

Le flag n'est pas géré en back.

cf tous les paramètres front :
https://docs.simplicite.io/documentation/04-ui/responsive.md
