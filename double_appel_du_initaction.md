# Double appel du initAction

**URL:** https://community.simplicite.io/t/8092

## Question
### Request description

Bonjour,

J'ai un traitement dans le initAction qui fait appel à une API et prend quelques secondes. Ce n'est pas un problème quand on clique sur l'action, mais il semble que initAction se déclenche aussi à l'ouverture du Form sans qu'on ait cliqué sur l'action, ce qui impacte les performances.

Y a-t-il un moyen de savoir si le initAction est déclenché par le clic action ou par l'ouverture du formulaire ? Je souhaiterais bypasser mon traitement dans le 2ème cas.

Merci d'avance
Emmanuelle

[Platform]
Status=OK
Version=5.3.35
BuiltOn=2024-04-19 12:41

## Answer
Bonjour,

L'`initAction` est effectivement appelé lorsque la UI demande les `metadata` d'un objet possédant une action de confirmation avec des attributs d'action.

On va optimiser cela pour n'envoyer les metadata de confirmation (fields et template) qu'au moment d'appeler l'action, ce qui ne déclenchera qu'un appel à l'`initAction`.

Ce sera livré en 5.3.37.
