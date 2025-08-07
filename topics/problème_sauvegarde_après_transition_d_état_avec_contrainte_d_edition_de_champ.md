# Problème sauvegarde après transition d'état avec contrainte d'edition de champ

**URL:** https://community.simplicite.io/t/5731

## Question
Version 5.2.27

Bonjour,

Nous avons un problème de sauvegarde lors d'une transition d'état alors que l'utilisateur n'a pas sauvegardé ses modifications à l'avance.

Cela arrive car une contrainte rend le champ concerné en lecture seule dans l'état atteint lors de la transition d'état.

Est-il possible (à l'aide d'un hook?) de sauvegarder le champs sans avoir à modifier la contrainte ? Ou peut-etre existe-t-il une autre paramétrage de contrainte pour rendre ce comportement possible ?

Bonne journée,
Paul-alexandre

## Answer
Merci pour votre réponse.

La solution retenu a été de faire [OLDSTATUS].equals("etat initial de la transition").
