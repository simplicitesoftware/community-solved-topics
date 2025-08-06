# Retrouver le parent dans une action de liste fille

**URL:** https://community.simplicite.io/t/9882

## Question
### Request description

Bonjour,

Je vois d'après [ce ticket](https://community.simplicite.io/t/personnaliser-la-valeur-par-defaut-dun-attribut-daction/5378/6) que dans initAction, getParentObject renvoie l'objet appelant et non son objet parent.
Y a-t-il un autre moyen de récupérer le parent dans l'initAction d'une liste fille ?

Merci d'avance pour votre aide
Emmanuelle

[Platform]
Status=OK
Version=6.2.8
BuiltOn=2025-04-25 10:05

## Answer
Bonjour,

Faudrait essayer un `getParentObject().getParentObject()` ?
je ne sais plus quelle instance d'objet travaille pour des questions d'isolation de données en mémoire. Il faut que `getParentObject()` de l'action soit le panel, si c'est un instance dédiée à l'action (il me semble), ça ne marchera pas.

Sinon l'objet principal d'un formulaire est toujours l'instance main (`the_ajax_x`).
donc un simple `getGrant().getMainObject("x")` devrait fonctionner.
