# Affichage dynamique des bannettes de page d'accueil

**URL:** https://community.simplicite.io/t/11144

## Question
### Request description

Bonjour,
Existe-t-il un hook permettant d'afficher / masquer dynamiquement les bannettes de la page d'accueil ?
J'ai des utilisateurs de même profil mais dont le rôle est défini par des données fonctionnelles, j'aimerais qu'ils ne voient que les bannettes qui les concernent.
J'ai trouvé [ce vieux ticket](https://community.simplicite.io/t/ne-pas-afficher-les-bannettes-vides/993) qui correspondrait à mon besoin, mais je ne sais pas si cela a évolué depuis ?

Merci d'avance pour votre aide
Emmanuelle

## Answer
Bonjour,

En général on passe par un groupe de droits...

Donc si c'est dynamique et en fonction du user, on utilise le hook `PlatformHooks.postLoadGrant` 

- pour ajouter un groupe dédié à ce droit à la session en fonction d'une règle métier (sql where user login...). Ensuite la bannette (héritier filtré de l'objet métier) est à mettre dans ce groupe de droits.

- On peut aussi changer le template de la Vue dynamiquement par code s'il faut juste retirer l'area d'une recherche prédéfinie, sans interdire l'objet lui-même.
`grant.getHome().get/setUITemplate(...)`
