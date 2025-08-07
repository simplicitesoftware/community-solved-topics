# Le contenu d'un champ “Multi-Documents” disparaît suite à une contrainte

**URL:** https://community.simplicite.io/t/4904

## Question
Bonjour,
Je constate que le contenu d'un champ de type “Multi-Documents” se vide dès que j'applique dessous une contrainte de visibilité.

Je m'explique, nous avons la possibilité d'ajouter des photos pour un bien dans le champ **propertyPhotoPlus** qui de type “Multi-Documents” 

Afin de ne pas charger tout le temps le formulaire d'un bien, nous proposons l'affichage ou non de ces photos via le flag **propertyPhotoPlusFlag**.

![image|487x500](upload://ggb14VfVndsyyjK79V1e1FZpy5m.jpeg)

Or, à chaque fois qu'on mets le flag à 'Non' et qu'on enregistre. Si on le remets à "Oui", les photos ne sont plus là.

Voici la définition de l'attribut et la contrainte concernée :
![image|690x269](upload://u4eKe8rKqDNfAPXm6Wtqj2yyGoR.png)


![image|690x319](upload://2wdOKbcv5ro4tkqWhqNUGXbP1h8.png)

Et voici dans l'objet Document les photos présentes qui ensuite ne sont plus là une fois que la contrainte de visibilité est exécutée :

![image|690x341](upload://285i4YA1bLeFzrhHZJGTc1Q2MlQ.png)

![image|690x180](upload://8CiNNWDIT2w6Zl2vItotZDiiZkq.png)

![image|430x225](upload://iNrIE0QEaL0dJswtRYBxv4SU9TB.png)


Est-ce un comportement normal ? aurais-je oublié de paramétrer qq choses ?

Merci d'avance pour votre aide.
Abed.

## Answer
Bonjour Ophélie,

Je confirme que suite au correctif livré par @Francois (version 5.2.5), le pb est bien résolu et les documents sont bien présents, avec ou sans la contrainte.

A+
Abed.
