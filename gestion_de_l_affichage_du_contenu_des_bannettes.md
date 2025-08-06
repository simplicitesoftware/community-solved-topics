# Gestion de l'affichage du contenu des bannettes

**URL:** https://community.simplicite.io/t/10394

## Question
Bonjour,

J'ai une gestion d'état avec l'affichage des bannettes. 

Les bannettes ont un texte qui s'affiche par défaut. Comment est-ce que je peux agir sur ce texte et le modifier pour afficher d'autres données?

Merci.

Fabrice

## Answer
Le libellé correspond *par défaut* à la concaténation des champs clé fonctionnelle de l'objet. 
Cette valeur est surchargeable :
* Avec l'attribut "Titre complémentaire" de l'objet métier ex : `[VALUE:demoSupCode] [VALUE:demoSupName]`
![image|690x287](upload://dki0D7gYrCNN70SBmOowO352TLF.png)

* Via le hook `getUserKeyLabel`, comme expliqué dans la [documentation](https://docs.simplicite.io/docs/core/objects/businessobject-code-hooks/#short-label-hook) et avec un exemple dans le module **Demo** pour l'objet `DemoOrder` :

```java
/** Hook override: custom short label */
@Override
public String getUserKeyLabel(String[] row) {
	// Custom short label
	return getGrant().T("DEMO_ORDER_NUMBER") + getFieldValue("demoOrdNumber", row);
}
```
![image|690x213](upload://3zRzjRLDiR4HHR8lNCC7jGNJj5I.png)
