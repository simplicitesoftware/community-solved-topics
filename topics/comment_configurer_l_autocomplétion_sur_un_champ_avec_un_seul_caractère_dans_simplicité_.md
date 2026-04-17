# Comment configurer l'autocomplétion sur un champ avec un seul caractère dans Simplicité?

**URL:** https://community.simplicite.io/t/9533

## Question
Bonjour à tous,

Je cherche à configurer un champ avec autocomplétion dans Simplicité, mais je souhaite que la recherche se fasse dès que l'utilisateur tape **une seule lettre** (et non pas après plusieurs caractères).

J'ai configuré l'autocomplétion avec `fieldCompletion`, mais actuellement, la recherche ne s'exécute qu'après que l'utilisateur ait tapé plusieurs caractères. Je souhaite modifier cela pour que la recherche commence dès qu'une seule lettre est entrée, et que les suggestions de l'autocomplétion soient mises à jour instantanément.

## Answer
Bonjour,

Il faut changer le paramètre côté UI, par défaut il vaut 2 car un seul caractère est rarement assez discriminant et effectue une 1ère recherche pour rien.

```js
// in resource 'SCRIPT' of disposition 'responsive5' add :
$(document).on("ui.ready", e => {
  $ui.setCompletionMinSize(1);
  ...
});
```

https://platform.simplicite.io/current/jsdoc/Simplicite.UI.Engine.html#setCompletionMinSize
