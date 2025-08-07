# Configurer une instance depuis un script

**URL:** https://community.simplicite.io/t/3332

## Question
Bonjour,

Est-il possible, depuis un script shell (bash, zsh ou autre), de configurer les paramètres systèmes d'une application Simplicité, de créer et déclencher l'import de certains modules, ... En bref, d'automatiser des tâches sur Simplicité depuis le serveur qui héberge l'instance.

Merci d'avance !

## Answer
Importer un module se fait via un appel du même genre (service `moduleimport` au lieu de `xmlimport`)

<ins>ATTENTION</ins> il est **impératif** d'utiliser le service `moduleimport` dans le cas d'un import de module pour avoir le diff final.

Cf. https://docs.simplicite.io/documentation/02-integration/io-commandline.md
