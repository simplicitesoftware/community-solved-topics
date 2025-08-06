# Accès IO controlé

**URL:** https://community.simplicite.io/t/5048

## Question
Simplicité 5.1.46

Bonjour,

nous comptons utiliser l'accès IO pour effectuer les import module.

Peut-on-limiter l'accès IO a un seul utilisateur utilisateur? Ce qui est gênant c'est on peut utiliser le mot de passe IO avec n'importe quel user (actif ou pas) qui a un rôle admin/designer (actif ou pas). Je pensais qu'on pouvait désactiver le role pour désactiver l'IO (https://community.simplicite.io/t/bonne-pratiques-comptes-en-production/4871)

## Answer
En l'état, tout user peut potentiellement accéder au Endpoint I/O avec ses droits propres, donc il ne peut rien faire qu'il n'aurait pu faire via UI ou API (sauf si des règles métier n'ont pas été implémentées au bon endroit - ex: coté UI cliente - mais c'est un autre débat...)

Si vous n'avez pas défini de password I/O global (via la variable d'environnement `IO_PASSWORD` ou le property JVM `io.password`) l'authentification se fait via le password interne du user => si vous ne pouvez garantir la confidentialité sur le password global, vous pouvez donc gérer des passwords individuels par user.

Il est possible d'inhiber totalement le endpoint I/O via le param système `USE_IO` => vous pouvez alors prévoir des procédures où vous activez/désactivez le Endpoint "à la demande" le temps de faire vos imports de module.

Il est aussi possible de filtrer les origines IP autorisées à s'y connecter via un mécanisme de "whitelists" gérées niveau Docker pour modifier les filtres d'accès niveau Tomcat.  cf. https://docs.simplicite.io/documentation/90-operation/docker.md#whitelists => si vos imports sur I/O se font depuis des origines IP déterminées ça peut être une bonne approche pour restreindre l'accès.

Si ces mécanismes ne vous conviennent pas il reste toujours envisageable de faire évoluer la plateforme pour avoir la possibilité d'indiquer d'une manière ou d'une autre les droits d'accès individuels aux différents endpoints (ex: en autorisant la surcharge des `USE_IO/GIT/...` au niveau des param utilisateurs) => c'est envisageable dans le cadre de la 5.3 prévue pour la rentrée.
