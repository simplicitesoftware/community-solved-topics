# Script SQL fichier resource

**URL:** https://community.simplicite.io/t/5657

## Question
Simplicité 5.1.54

Bonjour,

Nous avons une fonctionnalité d'export qui repose sur dès requêtes SQL assez conséquentes.Est-il possible de les stocker en tant que ressource plutôt que dans le code Java et les charger dans le code pour pouvoir ajouter des paramètres et les exécuter ?

Il me semblait qu'on pouvait faire ça via le menu ressource mais je ne trouve pas de documentation à ce sujet.

Merci d'avance.

## Answer
Bonjour Jean-Michel, 

Tu peux sans doute l'ajouter en tant que code partagé (Administration > Code partagé) de type "Script SQL"

Dans le code, tu peux récupérer le contenu comme ceci :
```java
SharedScript script = getGrant().getSharedScript("my_script");
String source = script.getSource(getGrant());
```
