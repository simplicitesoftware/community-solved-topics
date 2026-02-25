# Contexte UPDATE en création

**URL:** https://community.simplicite.io/t/11655

## Question
### Request description

Bonjour,
J'ai une contrainte basée sur la condition CONTEXTE:CREATE et elle ne s'applique pas.
En debuggant je vois que le contexte est toujours égal à UPDATE.

```p.constraints ? ui.applyConstraints(ctn, obj, null, null, $app.CONTEXT_UPDATE, display) : display();```

Est-ce voulu ? Si oui y a-t-il un autre moyen d'appliquer la contrainte en create, ou je dois plutôt passer par le postLoad ?

Merci !
Emmanuelle

[Platform]
Status=OK
Version=6.3.4
BuiltOn=2026-02-16 12:31

## Answer
Bonjour,

Il y avait une raison historique pour simplifier le nombre de contextes du formulaire à créer/tester pour signifier une mise à jour au sens large. Le contexte ne gère pas la combinatoire creation en formulaire ou en liste par exemple. Le contexte aurait dû être pensé séparément de l'affichage mais la UI a évolué pour permettre des creations/mises à jour dans des contextes de liste, popup, pillbox...


En général il suffit juste de tester `obj.isNew()` ou `obj.isCopy()` pour savoir s'il s'agit d'une création. 

Ou d'utiliser les hooks `initCreate/Copy/Update` avant affichage, ou `preValidate/Create/Update` au save.
