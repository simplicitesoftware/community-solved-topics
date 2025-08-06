# Image background page de login

**URL:** https://community.simplicite.io/t/5019

## Question
Bonsoir,

Je souhaiterais pouvoir mettre une image en background, sur la page d'accueil, sur la div auth-main.

J'ai essayé avec du css, du genre :
 ```
background-image: url('https://example.com/bck.png');
```
Cepandant cela ne marche pas.

Quel est la bonne méthodologie pour le faire ?

Enregistrer l'image comme ressource puis la réutiliser dans le CSS ?

Auriez vous un exemple ?

Merci d'avance,

Benoît

## Answer
Précision, pour que ca marche, j'ai du mettre :

background-image: url(/resource?**type**=IMG&**code**=MYIMAGE);
