# Version de moment.js

**URL:** https://community.simplicite.io/t/6696

## Question
Bonjour,

Je voudrais savoir la version de moment.js dans Simplicité. Je n'ai pas trouvé cette information de façon précise. La seule mention disponible est dans les fichiers ".js.map" qui indique "version: 3".

Est-il possible de la trouver dans le projet ? Est-il possible de monter de version de nous même de la librairie ? Si non, pourriez vous réaliser une mise à jour pour avoir la version la plus récente dans le cas ou la version actuellement utilisée est ancienne en raison de vulnérabilités détectées dans la librairie.

Cette information nous a été remonté par le client lors d'un audit de sécurité sur la version 5.2 de Simplicité.

Lien des vulnérabilitées:
- https://security.snyk.io/vuln/SNYK-JS-MOMENT-2440688
- https://security.snyk.io/vuln/SNYK-JS-MOMENT-2944238

En vous remerciant par avance.

## Answer
Notre stratégie d'upgrade des composants tiers est décrite dans le document suivant: [dependencies](https://docs.simplicite.io/docs/quality#dependencies)

En résumé on n'upgrade **au fil de l'eau** les dépendances tierces (Java ou JS) que sur la version mineure en développement (i.e. la 6.0 actuellement). Sur les versions mineures releasées et en phase de maintenance court terme (i.e. la 5.2 jusqu'en septembre) ou long terme (i.e. la 5.3 pendant les 3 prochaines années et la 4.0 jusqu'en janvier 2024) on n'upgrade les composants tiers qu'en cas de vulnérabilité majeure (ex: Log4Shell).

S'agissant de la lib JS moment.js < 2.29.2, les seules versions mineures concernées seraient les versions mineures 5.1 et 5.0 mais celles -ci ne sont plus en phase de maintenance : la maintenance court terme de la 5.1 est expirée depuis octobre 2022, celle de la 5.0 depuis septembre 2021.
