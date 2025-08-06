# Conditionnement de l'alimentation des champs d'un objet fils remontés dans objet père

**URL:** https://community.simplicite.io/t/4923

## Question
Bonjour,

Je suis sur un écran d’un objet A dans une vue formulaire. Dans un onglet, j’affiche, en formulaire, les champs de l’objet fils B (relation 0,1 dont les attributs ont été incorporés à l’objet fils). Ces champs sont en lecture seule et ne sont alimentés que lorsque le statut de l’objet A est mis à jour pour arriver dans un statut défini.

L'alimentation de ces champs a été implémenté dans le hook preSave de l'objet fils B comme recommandé dans le ticket suivant : https://community.simplicite.io/t/enregistrement-donnees-objet-fils-depuis-objet-pere/4906

Toutefois, on rencontre une problématique. L'alimentation des champs de l'objet B ne doit se faire que lorsque le statut de l'objet A passe de "transmis" à "favorable". Or, dans le hook preSave de l'objet B, on a l'impression que le formulaire de l'objet A a déjà été enregistré. Ainsi, on ne peut plus se baser sur "objetA.getOldStatus()" (valeur de oldStatus = valeur de Status) ou "status.hasChanged()" (toujours à false). Ce qui a pour conséquence de regénérer l'alimentation des champs de l'objet B à chaque fois que l'on enregistre le formulaire de l'objet A au statut "favorable".

Comment faire pour conditionner l'alimentation des champs de l'objet A uniquement au passage du statut "transmis" à "favorable" ?

En vous remerciant.

Bruno

## Answer
Bonjour Alistair,

Merci pour ton retour. L'erreur que j'avais était due à des données "vérolées" dans ma base de données locale. 

Du coup c'est bon.
