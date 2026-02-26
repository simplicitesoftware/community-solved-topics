# Création d'un module pour gestion OAuth

**URL:** https://community.simplicite.io/t/11681

## Question
Bonjour,

J’ai suivi les consignes de ce poste, [Implémentation du parseAuth](https://community.simplicite.io/t/implementation-du-parseauth/11635). Cela fonctionne bien cependant il a fallu modifié des paramètre système stocker dans le module System et des ressources du module UI. Je souhaiterai empacter ses modifications dans un module adhoc (connectionOAuth) pour déployer plus facilement. Cela ne pose pas de problème avec les ressources que je peux changer de modules sans difficulté par contre je ne peux rien faire pour le paramètre système `AUTH_PROVIDERS` qui est inclus dans le modules système et que je souhaiterai surcharger ou changer de module.

Je suis bloqué à cette étapes.

Cordialement,

## Answer
Non il n'y aura bien qu'un seul paramètre système (le module ne fait pas partie de la clé fonctionnelle des objets système).

Le fait qu'un param soit dans un module X ou Y ne change rien au fonctionnement (le module c'est une pure notion de packaging)
