# La méthode front getField().setValue() ne met pas à jour l'item

**URL:** https://community.simplicite.io/t/6803

## Question
### Request description

Bonjour,

J'ai l'impression qu'en front la méthode getField().setValue() met à jour obj.metadata.field mais pas obj.item.
Quand je fais un setValue puis save, ma modification n'est pas prise en compte.
Si j'ajoute obj.item.field = ... cela fonctionne.

Est-ce normal ?

Merci !
Emmanuelle

## Answer
Oui, c'est un accesseur de l'objet javascript `Simplicite.Ajax.ObjectField` utilisé par la UI front : 
- en formulaire `obj.metadata.field[x].v`
- ou en édition de liste `obj.list[i].meta.field[x].v`

l'item courant sert juste à la couche ajax "simple" pour véhiculer les données. Il n'est pas utilisable dans une édition de liste par exemple.

Pour récupérer l'item pour ajax :
- il faut passer par `obj.getValues()`, ou getOldValues, resetValues ...
- et passer cet item à la couche ajax `obj.save(callback, obj.getValues())`
