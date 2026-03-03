# Plusieurs groupe de raccourcis

**URL:** https://community.simplicite.io/t/11497

## Question
### Bonjour,

Je suis à la recherche d’une solution, si cela est possible, pour diviser ou regrouper certains raccourcis afin de les répartir en colonnes distinctes lors de la mise en page de la page d’accueil.
L’objectif est de faciliter la lecture en regroupant des items de même nature.

Mes raccourcis fonctionnent correctement, mais je ne trouve pas d’option native permettant leur répartition ou leur regroupement visuel.

Cette fonctionnalité existe-t-elle nativement (et, le cas échéant, où puis-je la trouver) ?
À défaut, est-il possible de la développer ? Si oui, auriez-vous une première piste ou une orientation technique à me proposer ?

Je vous remercie par avance pour votre aide.

Cordialement,

### Technical information

[details="Instance /health"]
```text
6.2.18
```

[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```

[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```

[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*

[/details]

## Answer
Bonjour, 

Il n'est pas possible de choisir unitairement les raccourcis à afficher dans une Vue, vous pouvez éventuellement ouvrir une feature request. 

En attendant, vous serez obligé de passer par un objet externe dédié à chaque groupe de raccourcis. 
Côté back, vous pouvez utiliser `getGrant().toJSONShortcuts()` et / ou `getGrant().getShortcuts()` pour créer votre liste custom de raccourcis à passer au front.
