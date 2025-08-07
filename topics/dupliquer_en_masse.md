# Dupliquer en masse

**URL:** https://community.simplicite.io/t/8939

## Question
Bonjour,

J'ai un script sur initCopy pour :

* Copier des valeurs de l'enregistrement original dans d'autres champs et les mettre en lecture seule
* Copier normalement des champs
* Vider des champs
et tous les champs de l'enregistrement original sont verrouillés.


Le métier désire pouvoir faire ce traitement en masse (sélectionner x enregistrements et lancer leur duplication).

Est-ce que vous avez une suggestion sur la meilleure manière de faire?

Merci d'avance

Fabrice

## Answer
Déjà ça, ça ne va pas:

[quote="fabrice, post:3, topic:8939"]
```
test.getTool().getForCopy(vv);
initCopy();
```
[/quote]

J'ai indiqué d'utiliser `getForCopy(id, **true**)` => le `true` fait que ça appelle le `initCopy` donc pas besoin de l'appeler explicitement.

Mais de toute façon il aurait fallu écrire `**test**.initCopy()` pour travailler sur le bon objet
