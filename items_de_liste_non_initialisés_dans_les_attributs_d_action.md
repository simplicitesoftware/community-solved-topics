# Items de liste non initialisés dans les attributs d'action

**URL:** https://community.simplicite.io/t/8290

## Question
### Request description

Je reprends le point 1/ de [ce ticket](https://community.simplicite.io/t/initaction-pour-les-transitions-avec-action-et-champs-de-confirmation-en-row-form/8199/18) que vous avez fermé.
Nous sommes bien sur une version à jour 5.3.39.

Les items d'un attribut d'action ObjectFieldList sont initialisés dans le initAction.

```
ObjectField f = action.getConfirmField(lang, COUNTRY_FIELDNAME);
ObjectField org = action.getConfirmField(lang, ORG_FIELDNAME);
ObjectField orgdom = action.getConfirmField(ORG_DOMNAME_FIELDNAME);
			
ObjectDB sub = getGrant().getTmpObject("RciSubsidiary");
sub.resetFilters();
sub.getField("rciSubScope").setOrder(1);
			
List<String[]> subList = sub.search();
			
f.getList().getItems().clear();
for (int i = 0 ; i < subList.size() ; i++)
{	
	sub.setValues(subList.get(i));
	f.getList().putItem(sub.getRowId(), sub.getFieldValue("rciSubScope"), true);
}
```

Au premier appel de l'action, mes item de liste sont vides.

![image|690x344](upload://kP2XipaotY4phTaNnLtgMfeQV0N.png)

Au deuxième appel ils sont renseignés.

![image|690x468](upload://w1IxMpih7mGInoaSP0KqbHes8ie.png)

C'est le traitement du premier appel qui est effectif au deuxième car si je vide la liste avant de la remplir en ajoutant ceci

```f.getList().setItems(new ArrayList<EnumItem>());```

elle devient vide à tous les appels.

Dans Network, je regarde la Response et constate qu'il semble mis à jour après le passage dans initAction, même si le popup de confirmation attend la fin du initAction pour s'ouvrir.

Avec un sleep() dans le initAction, je vois que la Response est envoyée à 15:38, heure du passage dans initAction, mais mise à jour en dernier à 15:37 soit avant le passage dans initAction.

![image|690x110](upload://fPNqHtjcR7ADLWwJYJiQd6l108C.png)
![image|690x32](upload://67bBUevLBkM8NVrvJ8mb564dc8B.png)

List de valeurs au premier appel (vide)

![image|600x469](upload://jT06zQlwYj7CLVi4ijOj4For49L.png)

Liste de valeurs au 2ème appel (remplie)

![image|466x482](upload://52QbVDP4nR9RLmS3NtIj35DkIRT.png)



Puisque vous ne reproduisez pas sur la Démo, il doit s'agir d'un problème chez nous mais je ne peux pas aller plus loin car je n'ai pas accès au code qui constitue la Response.
Peut-il s'agir de notre architecture ? Ou d'un paramètre particulier ? D'une lenteur ?

Ce ticket n'est pas urgent car nous avons contourné en production en passant par une liste statique.
Merci.

## Answer
C'est un field simple avec une liste simple...

Je pense avoir compris, c'est un problème de cache lorsque le champ n'a jamais été chargé après un clear cache global. En fait ça se produit une seule fois de mon côté. On va forcer de le charger avant d'appeler l'initAction.

En attendant tu peux surement faire pareil par code :

```java
// init the default list
f.loadList(obj, "RCICOUNTRIES", getGrant());
// reset list
f.getList().getItems().clear();
// putItem...
```
