# Création d'un utilisateur avec 2 tirets

**URL:** https://community.simplicite.io/t/7920

## Question
### Version
5.3.30

### Description

impossible de créer un login d'utilisateur avec deux tirets qui se suivent.
on a un utilisateur qui a tout ses papiers et comptes d'authentification qui contiennent ses 2 tirets. (ex claire bernard--dupont)

de plus le message d'erreur n'a pas le bon intitulé (Expression non valide: Login (LOGIN_AVEC_APOSTROPHE)

## Answer
La regex qui s'applique sur l'attribut login est `LOGIN` de l'objet système `User`, vous avez la main (en tant que designer) pour changer cette regex pour se caler sur vos besoins spécifiques:

![image|690x355](upload://cc7wQfUDi1Me854QjbZvUPCS05M.png)

en l'occurence utiliser le quantifier `*` (0 ou N) au lieu du `?` (0 ou 1) pour ce qui concerne le tiret `-`
