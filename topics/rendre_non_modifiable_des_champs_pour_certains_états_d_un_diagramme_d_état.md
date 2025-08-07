# Rendre non modifiable des champs pour certains états d'un diagramme d'état

**URL:** https://community.simplicite.io/t/4391

## Question
Bonjour,

J'ai créé un digramme d'état qui possède 8 états différents.
J'aimerais que lorsqu'on passe par exemple à l'état 4, certains champs de mon formulaire ne soit plus modifiable jusqu'à l'état 8.

J'ai essayé de le faire via le code avec
```
getField("XXX").setUpdatable(false);
```
Le problème c'est que bien évidement ce n'est que temporaire car si je surprime le cache, les champs redeviennent modifiable (normal).
Le deuxième problème, c'est que avec la méthode setUpdatable, les champs deviennent non-modifiable pour tous les états alors que je veux uniquement de l'état 4 à 8.

il doit surement exister un moyen, mais je ne vois pas lequel. Auriez-vous une idée ?

## Answer
Vous pouvez implémenter ce genre de règles via des contraintes (il y a ce genre de chose dans la démo : en fct de l'état de la commande certains attributs sont modifiables ou non)

Sinon c'est à faire par code dans les hooks `initUpdate` / `initCreate` **et** `preValidate`

**Attention**: Il faut se rappeler que les changements dynamiques de paramétrage (ex: changer le caractère obligatoire/facultatif d'un attribut) sont persistants dans le cache Simplicité (un objet ne revient pas tout seul à sa définition d' "origine").

Donc il ne faut pas écrire des `if (condition) f.setUpdatable(true);` mais plutôt des `f.setUpdatable(condition);`
