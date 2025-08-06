# La création d'un objet ne doit être possible que depuis le parent

**URL:** https://community.simplicite.io/t/10029

## Question
Bonjour,

J'ai une table "titre" et une table "mouvement". Un titre peut avoir plusieurs mouvements, mais j'aimerai que la création de ces mouvements ne soient réalisables que depuis le formulaire titre et pas possible depuis le formulaire mouvement.

Question subsidiaire, est-ce qu'il est possible de lier la création d'un mouvement à la valeur d'un champ? par exemple si le champ "xy" du titre égale 1 la création d'un mouvement pour ce titre est alors impossible.

Merci d'avance

Fabrice

## Answer
Bonjour Fabrice,

Ton besoin me semble couvert par le hook `isCreateEnable` dans l'objet "mouvement" pour retourner false dans les cas qui t'intéressent.

- tester que le parent object est "titre"
- et qu'un de ses champs "xy=1"


https://docs.simplicite.io/docs/core/objects/businessobject-code-hooks/#access-rights-enablingdisabling-hooks
