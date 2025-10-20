# Paramètre de sécurité server.compiler : possible de définir une stratégie "true au startup puis false après"?

**URL:** https://community.simplicite.io/t/10710

## Question
### Version

*6.2.15*

### Description

Dans le cadre du renforcement de la sécurité de nos services, je souhaite pouvoir désactiver le compilateur java interne. J’ai trouvé que je pouvais le désactiver en basculant la propriété système `server.compiler` à false mais ce faisant, mon application ne démarre pas bien car les sources java ne sont plus compilés au démarrage (logique) et que je ne souhaite pas avoir à les ajouter dans une image statique. Je souhaite juste que le service une fois démarré ne permette pas de modifier et recompiler le code mais que la dernière version disponible du code lue en BD soit bien prise en compte à chaque démarrage.

J’essaye aussi de bénéficier de la propriété `platform.securelevel=9`. Cependant, ce niveau de sécurité inhibe totalement le healthCheck de telle sorte que les services ne sont jamais considérés comme démarrés dans Kubernetes. Ce niveau de sécurité devrait réponde a minima un statut http`200`(fusse avec un contenu renvoyé vide) ou au moins renvoyer la réponse prévue dans le platformHook customHealthCheck.

## Answer
En fait un "secure level" à géométrie variable fait double emploi avec les différents mécanismes existants qui permettent déjà de choisir finement ce qu'on ouvre/ferme => son seul intérêt serait de centraliser l'endroit où on le dit...

NB: certain mécanismes de durcissement ne sont pas de niveau applicatif (ex: les white lists qui sont des filters Tomcat), le "secure level" configurable ne concerne mécaniquement que le niveau applicatif

C'est pour cela qu'on met plutôt en avant le docker compose durci comme point de centralisation et d'illustration de tout ce qui peut être fait en termes de durcissement tout en laissant la possibilité de faire son choix au cas par cas
