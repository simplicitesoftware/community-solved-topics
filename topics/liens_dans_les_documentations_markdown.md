# Liens dans les documentations markdown

**URL:** https://community.simplicite.io/t/3662

## Question
Bonjour,

Est-il possible, dans la documentation des objets métiers, attributs, ou autre (leurs champs `Description`) de rajouter des liens vers d'autres documentations d'objets métiers, attributs, ... ?
A l'image des champs `<see cref="UnObjet">` en C# ou encore `@see #maMethode()` en Java.
Si oui, comment cela est-il fait avec Simplicité ?

## Answer
On peut inliner la doc d'un objet métier dans un doc markdown via de tags du type:

```text
[OBJECTDOC:MyObject]Name
```

Ou plus globalement d'un module via un tag du type:

```text
[MODULEDOC:MyModuleName]
```

De même il est possible d'inliner les images des modèles via `![]([MODEL:MyModelName])`
