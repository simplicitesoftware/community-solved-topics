# Pouvoir récupérer le titre d’un record dans la langue souhaitée

**URL:** https://community.simplicite.io/t/11697

## Question
### Request description

Bonjour,

Dans notre cas, nous envoyons un email automatiquement dans un **postCreate**, suite à la création.

Dans ce traitement, nous construisons le sujet et le corps du mail via :

```
String title = this.getTitle();
```

Le problème est que la valeur retournée dépend de la langue du Grant courant (utilisateur déclencheur).

---

## Use case 1 – Titre complémentaire

Dans un premier cas, le titre est défini via le paramétrage **“Titre complémentaire”**, basé sur la concaténation de plusieurs champs enum :

[VALUE:LegalTextTypeTagDocument]-[VALUE:LegalTextProduct]-[VALUE:LegalTextBrand]

`getTitle()` retourne donc les valeurs traduites des enums selon la langue active.
![image|665x500, 50%](upload://vSnUgvMRexlRIVfmiqpXNxsauCu.png)

---

## Use case 2 – Titre calculé via getUserKeyLabel()

Dans un autre cas, le titre n’est pas issu du “Titre complémentaire” mais est calculé dans `getUserKeyLabel()`.

Là aussi, le résultat dépend de la langue du Grant.

---

## Besoin

Dans les deux cas, nous souhaitons pouvoir afficher dans le même email :

* le titre en français
* le titre en anglais

indépendamment de la langue de l’utilisateur déclencheur comme dans le formulaire
![image|690x294, 50%](upload://raqqmuFWQbQ55iNcqXDpLlErUrg.png)
![image|690x252, 50%](upload://bWJqRQa6axH1edKAvsqP8U9vf6s.png)

---

## Question

Existe-t-il une bonne pratique pour :

* obtenir le titre (`getTitle()` ou `getUserKeyLabel()`) dans une langue donnée
* ou récupérer la traduction des champs enum dans une langue spécifique

Serait-il envisageable d’avoir :

* une méthode du type `getDisplayValue(field, lang)`
* ou une surcharge du type `getTitle(lang)`

L’objectif est d’éviter de modifier globalement la langue du Grant dans le traitement postCreate.

Ou bien,  existe-t-il une autre façon dans le standard Simplicité pour répondre à notre Use Case ?

Merci d’avance pour vos retours. :slight_smile:

## Answer
Bonjour,

Ce n'est pas prévu en effet.
Les API sont globalement basées sur les droits et la langue de l'utilisateur, chaque session ne charge pas toutes les langues de tous les champs ENUM, labels...

- soit il faut changer de langue à la volé et le remettre après traitement, mais pas sûr qu'il n'y ait pas des caches en mémoire à rafraichir également
- soit il faut créer un Grant "static" qui sera utilisé pour instancier les objets dans la langue voulue pour charger le record et appeler les API sur ses instances, couteux en mémoire, par exemple :

```java
// clone des droits à faire une fois
myGrantENU = getGrant().clone("myCloneENU", Globals.ENDPOINT_ANY);
myGrantENU.setLang("ENU");

// et usage pour instancier des objets en anglais
ObjectDB o = myGrantENU.getTmpObject("MyObject");
o.select(rowId);
String title = o.getTitle();
```
