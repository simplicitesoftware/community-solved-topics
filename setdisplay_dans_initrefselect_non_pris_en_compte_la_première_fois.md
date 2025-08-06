# setDisplay dans initRefSelect non pris en compte la première fois

**URL:** https://community.simplicite.io/t/7757

## Question
Continuing the discussion from [Problème de titre avec setDisplay dans initRefSelect](https://community.simplicite.io/t/probleme-de-titre-avec-setdisplay-dans-initrefselect/7349):

Bonjour,

Je viens de voir que le topic a été fermé mais de mon côté je reproduis toujours l'anomalie en v5.3.27. Est-ce qu'une correction est toujours prévue ?

![Simplicite_v53_setdisplay_initrefselect|video](upload://1FyWE3zblybKUracM2tkIVPxrDA.mp4)

## Answer
Visiblement la modification était insuffisant en 5.3.27.

En 5.3.29 le front sera plus déterministe et forcera un reload des métadata à chaque affichage de la liste des objets référencés du contexte `CONTEXT_REFSELECT` :
- Ca fait sens car si les données du parent changent, on peut vouloir changer des comportements en back via `initRefSelect`
- Et les appliquer sur la liste du picker en front (pas uniquement changer le titre, comme modifier les colonnes visibles, ajouter des filtres statiques, etc.)

J'espère que ça corrigera ton cas.
