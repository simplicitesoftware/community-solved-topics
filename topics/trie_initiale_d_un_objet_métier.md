# Trie initiale d'un Objet Métier

**URL:** https://community.simplicite.io/t/4463

## Question
Bonjour,

Je souhaite "simplement" changer l'ordre d'affichage des données pour un Objet Métier en particulier.
Dans le contexte, je souhaiterais avoir le plus récent en haut (et c'est l'inverse qui est initialement fait sur Simplicité).

Je suppose que cela doit se faire dans le Hook preload (à l'aide d'un setOrder) ?... mais je ne trouve pas d'exemple/article semblable à ce sujet pouvant m'aider.

Auriez vous des conseils/tips ?

## Answer
Bonjour, 

L'ordre de tri se paramètre au niveau de l'attribut d'objet, cf l'aide sur le champ "Ordre de tri"

![Capture d’écran 2022-02-25 à 17.44.55|611x400](upload://sZYehCDNSqIB1aOnIP7Z4VrWibu.png)


Si vous souhaitez que la liste soit par défaut triée par date de création décroissante, je vous recommande de créer un attribut "date de création" qui prend pour valeur le champ système "created_dt".

Si vous souhaitez rendre dynamique le tri de vos listes, il faudra effectivement utiliser `setOrder` mais plutôt dans le hook `initList`
