# Affichage traduction de valeur de liste (énuméré multiple) au niveau des filtres appliqués sur ma liste

**URL:** https://community.simplicite.io/t/6056

## Question
### Request description

Bonjour,

J'ai constaté que lorsque je suis en vue liste et que je souhaite filtrer cette même liste sur un champ de type énuméré multiple, l'étiquette indiquant mon filtre appliqué laisse apparaître le code de la valeur sélectionnée dans le filtre et non la valeur traduite. 

### Steps to reproduce

Je suis actuellement en version 5.2.33 de Simplicité

- Sur un objet métier, mettre en place un champs de type énumérer multiple sur lequel une recherche est possible (recherche de type case à cocher dans mon cas, mais ce choix ou un autre ne change rien à mon soucis).
- Lancer une recherche sur ce champ en cochant certains des valeurs de la liste de valeur
- constater que l'étiquette qui apparait en haut de la liste, avec les différents filtres appliqués, référence le code de la valeur de liste et non la traduction dans la langue de l'utilisateur.

Cordialement, 
Joffrey

## Answer
Bonjour, 

Ce n'est pas reproductible sur une version à jour 5.2.34.
Exemple sur le module Demo, recherche des commandes par statut. 
Ce sont bien les traductions des codes de liste qui s'affichent dans la langue de l'utilisateur connecté.
