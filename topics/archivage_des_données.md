# Archivage des données

**URL:** https://community.simplicite.io/t/6721

## Question
### Request description

Bonjour,

Nous souhaitons mettre en place une mécanique d'archivage des données de notre application.
Quand on utilise l'action Delete, les données supprimées disparaissent sans log ni possibilité de les restaurer.
Nous voudrions la remplacer par une action de type Archive
- qui garde la donnée avec possibilité de la restaurer, par exemple dans un onglet à part
- sur les objets complexes (objets avec beaucoup d'onglets affichant des objets liés en 1,N ou N,N), il faudrait disposer d'un journal des suppressions de toutes les données liées

Mes questions sont les suivantes :
- existe-t-il un paramétrage socle permettant de faire ceci ?
- sinon, je pensais utiliser deux champs communs à tous mes objets : un booleen Archivé (oui/non) et un champ version intégré à toutes les clés primaires permettant de recréer une ligne archivée sans tomber sur une erreur de clé
-> est-ce une bonne idée ?
-> y a-t-il un moyen de ne créer ce champ qu'une fois plutôt que pour chaque objet métier ?

Merci pour votre aide !
Emmanuelle

## Answer
Oui c'est une stratégie possible d'utiliser un attribut texte (pas forcément persistant) pour faire une "photographie" à date des données liées à un record pour l'enregistrement dans le journal.
