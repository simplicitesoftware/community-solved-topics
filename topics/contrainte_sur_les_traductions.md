# Contrainte sur les traductions

**URL:** https://community.simplicite.io/t/3839

## Question
Bonjour,

Je cherche à savoir s'il est possible d'appliquer des contraintes sur les traductions?

Mon besoin est de pouvoir rendre modifiable certaines listes de valeur par un type d'utilisateur.

Pour ce faire, je m'aide des suggestions du post suivant:  https://community.simplicite.io/t/quel-meilleur-choix-pour-gerer-des-listes-deroulantes/2477

L'idée serait en fait de pouvoir rendre la valeur, et donc la traduction, modifiable ou non par l'utilisateur selon l'état d'une case à cocher que j'aurais ajouté à un objet FieldList étendu à la BO native.

D'où ma question principale, peut-on agir sur les traductions via contrainte?

Merci pour votre aide.

## Answer
Bonjour,

Non, pas de contraintes sur les traductions, mais votre cas d'utilisation est couvert pas le module "Modificator" présent dans l'App Store Simplicité qui permet aux utilisateurs autorisés de modifier les traductions et listes de valeurs de certains modules. 

![Notification_Center|550x500](upload://e9JXZpnNUhAS3CWS22ecZgMaqb4.png)

Ce module est expérimental et nécessite de bien comprendre son fonctionnement. Vous pouvez consulter les sources sur github: https://github.com/simplicitesoftware/module-modificator et nous solliciter pour une réunion sur le sujet.
