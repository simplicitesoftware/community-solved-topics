# Vue basée sur requête SQL

**URL:** https://community.simplicite.io/t/4965

## Question
Bonjour,

Pour un besoin particulier, je dois mettre en place une vue qui rassemble plusieurs objets. Je vais devoir passer par une requête SQL (notamment avec un UNION) pour obtenir les champs tels qu'ils me sont demandés.
C'est une vue qui ne servira qu'en consultation.
Quelle est la meilleure façon de procéder ? Publication, objet externe ?

Merci d'avance pour votre aide,
Emmanuelle

## Answer
Bonjour,

Il existe la notion d'objet select. Un objet select est un objet métier dont le contenu est basé sur le résultat d'une requête SQL. 
Le nom de la table sera select. Il faudra associer autant d'attributs à l'objet select que de colonnes retournées par la requête select. 
La requête se définit dans le filtre de l'objet ou dans le postLoad de l'objet en utilisant setSearchSpec("select ...");

L'objet est bien sûr en lecture seule pour tous les profils utilisateurs.
