# Script sur modification de liste

**URL:** https://community.simplicite.io/t/3366

## Question
Bonjour,

J'utilise un script et de l'autocomplétion d'un champ pour remplir les autres champs depuis ce dernier (par simple traitement de chaîne de caractères).
J'ai donc un fieldCompletion dans mon objet métier et un script front pour remplir les champs à partir du premier saisi dans le formulaire.
Cependant, le script ne semble pas être appliqué dans le cas ou on modifie la liste et ajoute une ligne.

La complétion des autres champs se fait par un 
`etabNom.ui.on("change", function() {/* set des valeurs */});`

`etabNom` étant récupéré comme ceci: 
`var etabNom = ui.getUIField(ctn, obj, "eqlCat2DroitEtabNom");`

Est-ce qu'il faut récupérer ce champ d'une autre façon dans le cas d'un ajout de ligne par modification de la liste ?

## Answer
En V4 il n'y a pas de hook dédié par ligne, il n'y a  que `list.onload`
donc vous devez faire une boucle pour le faire à la fin du chargement de la liste

```javascript
$('tbody>tr',ctn).each(function() {
  //chaque tr contient le row_id de la ligne
  var id = $(this).attr("data-rowid");
   ... votre code ...
});
```
