# Afficher le libellé au lieu du code dans une recherche

**URL:** https://community.simplicite.io/t/4117

## Question
Bonjour,

Dans le cadre de mes tests de migration de V4 vers la V5, je rencontre un pb au niveau d'une recherche utilisée dans une vue.

La recherche est :

![filtre V4|690x421](upload://4lOSjG9qC0a8KtqsXvIMjmzM1kX.png)

Elle marche bien en V4. Par contre, la liste est vide en V5 :

![liste 0|690x168](upload://mPIBfSA6j6lkey2A1FjRAp2NoE9.png)

En plus, le filtre qui apparaît maintenant, s'affiche avec les codes et non pas des libellés.
Quand je modifie la recherche comme suit :

![filtre sql|690x400](upload://xxkn9RzCdk3nLNFz9IK5WpGXMyX.png)
 
Elle marche bien en V5, mais ce sont toujours les codes qui s'affichent :

![liste 5|690x344](upload://30CWj0eliN6suAAFj6ezTl6qZFx.png)


Pourriez-vous me dire si je dois changer toutes mes recherches de cette façon afin qu'elles soient compatibles en V5 et aussi comment faire pour afficher les libellés au lieu des codes ?

![Simplicite|690x110](upload://zD2wDiwzrSpuViEkKcXv8H7NRoU.png)

Merci d'avance pour votre aide.
Abed.

## Answer
Ok vu, le problème était dans une recherche dans une zone de vue.
Ce sera livré en 5.1.13 et beta.
