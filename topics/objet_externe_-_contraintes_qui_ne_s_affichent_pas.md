# Objet externe - contraintes qui ne s'affichent pas

**URL:** https://community.simplicite.io/t/4444

## Question
Bonjour,

J'ai une contrainte qui rend obligatoires certains champs. Cette contrainte fonctionne bien sous ma **Vue** principale, mais pas pour ma **Vue** qui utilise un **Object Externe** en tant que zone de vue.
![image|690x368](upload://q8GVHy7fnULHsJJoNQMsAC8HQNp.png)

Pourtant, les champs sont exactement les mêmes entre les 2 **Vues** (c'est le même formulaire). Voici ce que ma contrainte m'affiche dans ma **Vue** principal mais pas dans ma **Vue** avec un **Objet Externe**.
![image|690x345](upload://gxCumBqCwLiMadB0k3vmg9iyBYY.png)

Une idée de pourquoi la contrainte ne m'affiche pas les messages "Champs obligatoire" pour la **Vue** avec l'**Objet Externe** ?
![image|690x247](upload://2Q3IZBPcZlsSJDSBafTIM3fgY55.png)


**PS :** Dès que je remplace la Vue avec Objet Externe par la Vue principale, les messages "Champs obligatoire" réapparaissent. Donc il ne s'agit pas d'un problème de droit.

## Answer
Bon, la subtilité c'est qu'il faut explicitement passer l'option `nav` (ici `{ nav: 'new' }` car c'est une page d'accueil) au `displayForm` car sinon le réaffichage suite au save repasse par la vue ce qui fait perdre le contexte du formulaire et notamment les messages.
![image|690x273](upload://ya0ap810H6Rz88j6XTHrpaPNgjX.png)


@Francois c'est vrai que c'est logique (en tout cas quand on debugge le code de la UI) mais peut être faudrait il forcer un `{ nav: 'new' }` quand il s'agit d'une vue de page d'accueil ? En l'état, dans ce genre de cas, le comportement visible est assez contre-intuitif...
