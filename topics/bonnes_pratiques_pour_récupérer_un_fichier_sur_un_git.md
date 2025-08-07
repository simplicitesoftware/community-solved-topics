# Bonnes pratiques pour récupérer un fichier sur un GIT

**URL:** https://community.simplicite.io/t/9415

## Question
### Request description

Bonjour,

Nous devons implémenter un moyen de récupérer des fichiers stockés sur un Git avec accès par token.
La fonctionnalité doit être disponible en liste (chaque instance a un fichier disponible sur le GIT qui doit se télécharger à la demande de l'utilisateur).

Je ne sais pas quelle est la meilleure façon de procéder,

- pour la UI : action, publication, champ External file ?
- pour le traitement : puis-je utiliser la classe GitTool, et si oui, y a-t-il des exemples quelque part ? Ou y a-t-il une meilleure façon de faire ?

Merci d'avance pour vos conseils !
Emmanuelle

## Answer
Oui une publication de type méthode qui appelle l'URL retourne un byte array ou un stream du résultat (stream + fichier temporaire sous try/catch si on parle d'un gros fichier) semble une bonne approche, à voir aussi en fct du type du fichier
