# Vue en arbre générale

**URL:** https://community.simplicite.io/t/11127

## Question
### Request description

Bonjour,

Nous avons un objet récursif sur plusieurs niveaux.
Nous cherchons un moyen de l'afficher de façon "dépliable" : une liste des niveaux 1 qu'on peut déplier chacun de façon récursive.
Mais sans devoir cliquer sur les n1 un par un.

Je sais que [c'est faisable en panel mais pas en liste](https://community.simplicite.io/t/affichage-en-arbre-sur-vue-liste-hors-panel/6448).

Auriez-vous d'autres pistes à nous proposer ? Treeview, objet externe ?

Merci d'avance pour vos conseils !
Emmanuelle

## Answer
Je ne crois pas, il faut paramétrer l'affichage du noeud racine :

"Ajouter au menu principal" au lieu de "Accoster à gauche" :

![image|690x293](upload://uCkhLW5YCQExmWf1TOZlgl6MG47.png)

C'est l'utilisateur qui décide d'ouvrir l'arbre depuis le formulaire.
Il est surement possible de forcer ça par code à l'ouverture du menu.
