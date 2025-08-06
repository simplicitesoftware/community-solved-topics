# Création de plusieurs records à partir d'un business process

**URL:** https://community.simplicite.io/t/8533

## Question
### Version

v6.0.16

### Description

Bonjour à tous,

Je travaille actuellement sur un processus métier qui permet de créer un enregistrement dans une table reliant plusieurs objets entre eux. Mon objectif est de pouvoir créer plusieurs enregistrements à partir de mon business process.

Pour expliquer plus clairement, j'ai ajouté une activité dans le processus métier qui permet de sélectionner plusieurs instances d'un autre objet. J'aimerais que cette sélection multiple génère autant d'enregistrements en base de données que d'instances sélectionnées. Ces records partageront les mêmes informations pour les activités de sélection unique.

Savez-vous comment je peux implémenter cela ?

(L'idée ici dans mon cas par exemple serait de pouvoir associer plusieurs Ressenti Client à un NITG).

![image|690x322](upload://7IhtnjuMaw4MSqT9X7YfESybaGH.png)


Merci d'avance pour votre aide !

## Answer
Et dans ton cas le mieux est de filtrer sur qualityEvaluationId plutôt que row_id afin que l'utilisateur puisse supprimer manuellement le filtre dans la liste des évaluations.
