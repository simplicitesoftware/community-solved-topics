# Problème de valeur d'un attribut qui disparait lors d'une création/update

**URL:** https://community.simplicite.io/t/3199

## Question
Bonjour,

J'ai un souci lorsque je souhaite enregistrer une nouvelle entrée dans mon objet.

J'ai créé une relation NamCentre <--0,N--- NamExamen afin de pouvoir sélectionner un centre lorsque je créé un examen:

![image|690x308](upload://Agn49fR17vcOjdczrfYNMDbywZp.png) 

Mais lorsque j'enregistre ou que j'update un objet examen, l'enregistrement se fait "avec succès" mais a valeur du champ disparait:

![image|690x302](upload://5ijJq4GuN2f1uBOQ9PGWIqAtT28.png) 

J'ai vérifié, il n'y a pas de contraintes correspondant sur l'objet Centre ou Examen.
J'ai l'impression que ça coince au niveau de l'ID du centre, qu'il n'arrive pas à faire la liaison entre le nom et son ID, je ne sais pas..
J'ai aussi vérifié dans la BDD, la valeur n'a pas persisté, ce n'est donc pas un problème côté front.

Si besoin, voici les deux attributs du centre dans l'objet Examen:

![image|690x56](upload://rwfMnSTGbCoQqwV6olgtuwJc1yr.png) 

Avez-vous des pistes de réflexion?

Merci d'avance.

Mahmoud.

## Answer
Bonjour à vous deux,

@David: Ok pour l'upgrade, je met à jour.

@Francois: J'ai testé et ça a fonctionné... Il n'y avait effectivement pas ce champ FK caché dans le template, ce qui empêchait la plateforme de faire le lien, croyant que la simple présence de l'attribut au sein de l'objet serait nécessaire. Du coup j'ai associé mes champs à une zone d'attribut et remonté ma FK en position 10 pour plus de clareté.

Encore merci pour votre support et votre réactivité.

Mahmoud.
