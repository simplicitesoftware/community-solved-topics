# Contrainte updatable back et front

**URL:** https://community.simplicite.io/t/12152

## Question
### Request description

Bonjour,

J'ai un impact de contrainte de type updatable. Ma contrainte est **back et front**.
Mon souci est que si mon objet renvoie ```isUpdateEnable = false```, les champs imapctés par cette contrainte sont quand même en écriture.

J'ai tenté d'ajouter ```obj.metadata.update == true``` à mon impact, mais ça fait planter l'exécution en back.
Y a-t-il une solution hybride, ou dois-je dupliquer mes contraintes comme indiqué dans [ce ticket](https://community.simplicite.io/t/appliquer-une-contrainte-uniquement-si-le-champ-est-modifiable/1195/4) ?

Merci pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.8
Variant=full
BuiltOn=2026-04-24 11:37

## Answer
Bonjour Emmanuelle,

Si l'impact contient du code front, il ne sera par construction applicable qu'en front. 

- A moins qu'on puisse faire en Rhino un `typeof` ou `instanceof` pour savoir si l'objet est une classe Java ou un object javascript. Jamais essayé.
- ou il faut essayer de mettre le code du `isUpdateEnable` dans l'impact en plus de la règle du champ (si la règle est simple)
- ou utiliser le hook front `onload` à la place de la contrainte front, et garder uniquement la contrainte back
- ou dupliquer/spécialiser 2 contraintes front/back comme tu l'envisages

PS : on peut ajouter des accesseurs front pour avoir les mêmes API qu'en back sur ObjectDB et ObjectField pour faciliter la syntaxe des contraintes front+back. Mais ici on parle d'un hook back `isUpdateEnable` non accessible en front.
