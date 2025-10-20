# Import XML Suppression

**URL:** https://community.simplicite.io/t/10838

## Question
Bonjour,

J’aimerais lors de l’import en xml supprimer toutes les valeurs du PlateformNode pour ensuite ajouter les miennes. J’ai déjà vu avec le if=existes sur l’action tag néanmoins ça me force à mettre en dur toutes les plateformesNodes.

Donc est ce qu’il y a un moyen de toutes les delete lors de l’import?

Merci d’avance

## Answer
Bonjour, 

En standard il n'est pas possible de supprimer en masse des éléments de la base avec une syntaxe :
```
<object>
	<name>MyObject</name>
	<action>delete</action>
	<data>
		<objField>*</objField>
	</data>
</object>
```

Vous serez donc obligés de passer par une implémentation spécifique. Soit via un adapter comme spécifié plus haut, soit via l'appel d'une action associée à un objet dans le fichier XML importé : 

```xml
<object>
	<name>MyObject</name>
	<action>MyCustomAction</action>
    <data></data>
</object>
```

`PlatformNode` étant un objet Système, vous ne pourrez pas y ajouter du code spécifique.
