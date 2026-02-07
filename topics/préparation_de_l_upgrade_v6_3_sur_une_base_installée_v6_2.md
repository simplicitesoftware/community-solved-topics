# Préparation de l'upgrade v6.3 sur une base installée v6.2

**URL:** https://community.simplicite.io/t/11533

## Question
Bonsoir,

Nous sommes en préparation active des upgrade vers la v6.3 de nos référentiels.

Dans ce contexte, nous avons commencé à aligner nos codes Java sur le niveau d’exigences requis par le nouveau compilateur [ECJ](https://docs.simplicite.io/versions/release-notes/v6-3#ecj-java-compiler). Néanmoins, compte tenu de l’effort potentiellement nécessaire pour mettre nos codes à niveau, nous envisageons de prédéfinir une valeur surchargée de la variable JAVA_COMPILER_OPTIONS dans nos bases installées en v6.2 avec une configuration moins stricte.

Cela peut-il poser un problème avec le processus d’upgrade interne de Simplicité ?

## Answer
Le patch 6.3 créé le param système en `upsert` et sans la `sys_value2` donc s'il est déjà précréé avec une valeur surchargée c'est bien cette valeur surchargée qui sera prise en compte en 6.3 (en 6.2 ce param n'existant pas).

Ce param en tant que tel n'a pas d'impact sur le processus d'upgrade niveau plateforme, c'est juste qu'il sera pris en compte à la recompilations du code applicatif lors des clear caches.

Pour limiter les risques d'erreur de compilation (les warnings ne sont pas bloquants) il convient d'anticiper le refactoring de son code dès la 6.2, en particulier corriger **toutes** les utilisations de deprecated qui trainent => certaines des choses dejà deprecated en 6.2 passent, en effet, en deprecated "for removal" en 6.3. Par contre les choses qui deviennent deprecated en 6.3 ne le sont jamais directement "for removal" donc pas bloquant (mais idéalement il faudra refaire une chasse aux deprecated une fois migré en 6.3 histoire d'anticiper le prochaines versions, avec ECJ ce sera plus simple car ça sortira en warnings à la compilation)

Ensuite il faut vérifier si on est concerné par les potentiels breaking changes indiqués dans la [release note de la 6.3](https://docs.simplicite.io/versions/release-notes/v6-3/#compatibility-breaking-changes), hormis la suppression de la lib `commons-discovery` (qui a peu de chances d'être utilisée) et la suppression du support de l'API v1 OpenDataSoft (qui de toute façon n'existe plus coté OpenDataSoft), il ne devrait pas y avoir de pb (à priori vous n'utilisez pas le connecteur OIC FranceConnect legacy non plus)

Par contre pour avoir toutes les features de développement il est impératif de se mettre explicitement en "development mode" (ex: vai la ver d'en `DEV_MODE="true"`) car en 6.3 certaines features sont désormais inhibées par défaut (et ce sera encore plus vrai en 7.0).

C'est aussi l'occasion de se reposer, plus généralement, les bonnes questions vs les [Guidelines de sécurité](https://docs.simplicite.io/docs/security) entre vos instances de dev/test/preprod/prod
