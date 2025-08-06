# Le user "service" crée des sessions à chaque call API dans l'instance Simplicité source

**URL:** https://community.simplicite.io/t/3822

## Question
Bonsoir,
J'ai une instance "front" Simplicité (en 4.0.P25) dans laquelle est configuré un objet service A lié à une autre instance "back" Simplicité (en 5.1) qui héberge l'objet A. Je ne suis pas convaincu que les différences de versions soient en cause.

La consultation en liste ou en formulaire de A fonctionne a priori sans soucis particulier sur les instances "front" et "back".

L'instance "front" configure par ailleurs des objets métier dont l'un des champs d'objet est un lien de type "Objet" référençant l'objet service A sur "front". Nous mettons cela en place pour supporter un travail de mapping visant à réconcilier plusieurs listes d'inventaire (des choses A', A'', A''', etc. devant à terme être assimilées par A) pour ne plus utiliser à terme que l'objet A hébergé dans "back" via ses API). Tant que ces travaux de réconciliation ne sont pas terminés, A', A'' ou A''' vont continuer d'exister en parallèle de A.

Le problème que je rencontre est lié à la non réutilisation des sessions API crées dans "back" (via un token demandé par "front"). En effet, à chaque appel API de "front" sur "back" (le token obtenu initialement est bien réutilisé a priori), des sessions s'empilent sur "back". Simplement en parcourant les pages de A' sur "front", je suis arrivé jusqu'à plusieurs centaines de sessions initialisées en parallèle sur "back" (20 nouvelles sessions par page de 20 lignes).

J'ai lu et suivi les préconisations afférentes à la prolongation de la durée de vie du token mais ça reste sans effet.
![image|690x171](upload://qAL02VOCzQMOeJSaTBp4eR7LHmh.png)

## Answer
Nous allons pousser une version améliorée de la valve qui gerera des slashes multiples (ou pas de slash, on ne sait jamais) au début de l'URI => `//api/...` ou `//////api/...` ou `api/...` sera traité comme `/api/...`
