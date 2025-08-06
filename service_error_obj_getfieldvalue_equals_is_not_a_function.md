# Service error: obj.getFieldValue(...).equals is not a function

**URL:** https://community.simplicite.io/t/9474

## Question
Bonjour,

J'ai défini des contraintes qui servent à définir si mes champs sont updatable ou non, ça fonctionnait parfaitement mais après quelques temps j'ai eu l'erreur suivante :

> Service error: obj.getFieldValue(...).equals is not a function

Cette erreur apparaît sous forme de pop-up répété (3 fois) au lancement de l'app, et lors du changement de la valeur des champs qui ont une contrainte.

Voici le genre d'expression des impacts :

> [VALUE:nomDuChamp] != null && [VALUE:nomDuChamp].equals("Valeur")

Les contraintes sont True et Front-End (j'ai testé Back-end aussi)

Savez vous d'où peut provenir l'erreur ?
Merci.

## Answer
Bonjour, 

Essayez de remaplcer `.equals` par `==`
