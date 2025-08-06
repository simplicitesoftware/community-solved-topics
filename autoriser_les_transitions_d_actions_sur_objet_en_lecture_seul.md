# Autoriser les transitions d'actions sur objet en lecture seul

**URL:** https://community.simplicite.io/t/6844

## Question
### Version

Bonjour,
Quand mon instance d'objet est en attente de validation, il ne doit plus être possible de le modifier, mais il doit être possible de le passer au statut Validé.
Aujourd'hui (si j'ai bien compris) les transitions d'actions ne sont possibles que si le IsUpdateEnable est à True.
Il serait utile d'avoir aussi un IsTransitionEnable distinct.

Merci !
Emmanuelle

## Answer
Il suffit de marquer l'état comme "Read only fields", ainsi le formulaire sera en read only mais les boutons de transition seront toujours présents et utilisables.
