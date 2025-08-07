# Ajouter un filtre par défaut

**URL:** https://community.simplicite.io/t/5744

## Question
Bonjour, 

Je tente d'appliquer un filtre par défaut sur un attribut afin de filtrer un liste.

L'attribut en question est une énumération avec une recherche de type "case à cocher". 

J'ai donc cherché sur le forum et suis tombé sur ce post: [Ajouter un filtre par défaut modifiable](https://community.simplicite.io/t/ajouter-un-filtre-par-defaut-modifiable/1483)

J'ai donc sélectionné l'une des solutions proposées par @Francois qui consiste à ajouter les filtres au niveau du postLoad comme suit :

```
setFieldFilter([nomAttribut], " IN ([liste des codes souhaités pour mon filtre])");
```

Cependant, mon filtre ne semblait pas s'appliquer comme souhaité. 

J'ai donc, dans un premier temps, vérifié que mon filtre était bien appliqué via la fonction `getFieldFilter([nomAttribut]);` => Le filtre est bien appliqué selon mes logs, à la sortie du postload.

J'ai ensuite vérifié l'état de mon filtre dans les autres hooks implémentés et qui s'exécutent lors du chargement de la liste. Les hooks que j'ai surchargés et qui s'exécutent sont les suivants : initList, isCreateEnable, isDeleteEnable. Pour chacun de ces hooks, je vérifie l'état de mon filtre et voilà ce que je constate dans l'enchainement de ceux-ci : 
- postLoad :
  - Entrée : filtre = `"%"`
  - Application du filtre désiré par défaut
  - Sortie : filtre = `" IN ([liste des codes souhaités pour mon filtre])"`
- initList :
  - Entrée : filtre = `" IN ([liste des codes souhaités pour mon filtre])"`
  - Sortie : filtre = `" IN ([liste des codes souhaités pour mon filtre])"`
- isCreateUnable :
  - Entrée : filtre = `" IN ([liste des codes souhaités pour mon filtre])"`
  - Sortie : filtre = `" IN ([liste des codes souhaités pour mon filtre])"`
- initList :
  - Entrée : filtre = "%"
  - Sortie : filtre = "%"
... 
(à partir d'ici, le filtre n'est plus appliqué).

Je suis surpris de voir l'exécution du hook initList une seconde fois. J'ai fait le tour des hooks sans trouver de piste sur un éventuel "resetFilters()" ou un changement de filtre sur ce champs. Je voulais donc savoir si j'étais passé à côté de quelque chose et si vous aviez une idée de piste à creuser pour résoudre ce problème. 

Sinon, quelle autre implémentation me permettrait de m'assurer de placer mon filtre par défaut tout en laissant ce filtre modifiable par l'utilisateur suite au premier chargement de la liste ?

## Answer
Avez-vous essayé cette solution?

https://community.simplicite.io/t/default-filtering-on-object/2955?u=scampano
