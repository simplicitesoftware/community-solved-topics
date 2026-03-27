# Enum multiple en edit cell en présentation pillbox/select2

**URL:** https://community.simplicite.io/t/11822

## Question
### Request description

Bonjour,

J'ai besoin de votre avis sur un contournement mis en place pour un souci d'UX sur les champs select2 :
J'ai un énuméré multiple en présentation Pillbox avec Edit cell activé.
Si on souhaite choisir plusieurs valeurs d'un coup avec la touche Ctrl, ce n'est pas possible en liste car le saveCell se déclenche et recharge toute la liste.

J'ai donc déplacé le listener de **change** vers **close** pour ce type de champ.
Voici mon code (pour un champ précis en attendant votre retour)

```
            let chgFct = $._data($("#field_cdpFinpdtdescCarBrand_id61")[0], "events").change[2].handler;
            $._data($("#field_cdpFinpdtdescCarBrand_id61")[0], "events").change.pop();
            $("#field_cdpFinpdtdescCarBrand_id61").on('select2:close', chgFct);
```

Est-ce que cela vous semble viable ? J'ai l'impression que c'est bancal car si l'ordre des event change évolue, je risque de supprimer n'importe quoi.
Auriez-vous une solution plus propre en tête ?

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.6
Variant=full
BuiltOn=2026-03-12 16:20

## Answer
Merci de nous aider à qualifier ces composants dans des usages poussés, étant donné le nombre de points de fonction à paramétrer/tester quasi illimité.

Ce sera poussé en 6.3.7.

<kbd>Click</kbd> : select/unselect d'un item + change => auto-save edit-cell

<kbd>Ctrl+click</kbd> : 
- select/unselect N items : trigger des `change` partiels/avec un context particulier `select-multi` pour ne pas faire d'auto-save en edit-cell
- <kbd>keyup</kbd> pour déclencher le `change` final sans context = auto-save de l'edit-cell

On n'a pas pu tout améliorer surtout au niveau RGAA où le focus/sélection via <kbd>ArrowKey + Enter</kbd> reste unitaire. Par contre le bouton `x` d'une pillbox pour retirer un enum sera désormais accessible au clavier, il ne l'était pas.

Il te faudra mettre une aide sur ce champ pour expliquer l'usage du <kbd>Ctrl</kbd>.
