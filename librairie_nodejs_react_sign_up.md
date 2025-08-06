# Librairie NodeJS / React / Sign Up

**URL:** https://community.simplicite.io/t/4838

## Question
Bonjour,

J'aimerais savoir s'il y'a une possibilité de créer un nouvel utilisateur (actif) en front (reactJS) à partir de la librairie npm.
Je ne vois aucune fonction permettant cela dans la documentation ci-dessous.

https://simplicitesoftware.github.io/nodejs-api/index.html

Si ce n'est pas possible aujourd'hui, avez vous prévu de l'intégrer dans le futur ?

Merci d'avance pour votre réponse.

@Paul_S et @Abed

## Answer
Il n'y a pas besoin d'API dédiée, c'est possible en manipulant l'objet `User` ou, mieux, un objet custom qui hérite de `SimpleUser` ou un objet métier ad hoc qui "pilote" coté backend son user associé et ses droits.

En général, on ne donne que les droits de create au user "public" du frontend sur cet objet et avec une search spec restrictive (ex: 1=2) pour que ça ne soit pas une porte ouverte pour se faire pirater ses données client.
