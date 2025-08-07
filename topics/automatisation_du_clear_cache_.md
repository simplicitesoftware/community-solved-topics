# Automatisation du "Clear Cache"

**URL:** https://community.simplicite.io/t/4127

## Question
Bonjour,

Nous souhaitons mettre en place une action qui déclenche un clear cache global à la fin de la journée.

Il y un cron Job qui semble peut être correspondre à ceci :

![image|690x226](upload://oshJYFLTOk5dwUTKio5l3VhEPrk.png)

Mais en vérifiant, cette action ne semble pas se déclencher comme prévu.

Avez-vous des propositions pour ceci?

En vous remerciant

## Answer
Bonjour,

**Cron CheckClearCache** 

- c'est une tache interne qui doit tourner toutes les 5 minutes si vous avez un environnement en cluster / plusieurs noeuds tomcat sur une même base. 
- cette tache permet de vérifier qu'un noeud a vidé le cache et demande aux autres serveurs de faire de même (changement du timestamp du cache mis en base)
- donc ne sert que si les noeuds n'ont pas pu communiquer entre eux via HTTP.
- par défaut elle n'est pas active quand il n'y a qu'un seul tomcat

Il n'y a pas de raison à vouloir scheduler un clear cache global (en dehors d'une mise en production de modules), sauf vouloir contourner un problème non résolu (pb mémoire, contexte non libéré...). Si vous voulez faire un "reset full", il faut plutot arreter tomcat, supprimer le cache serialisé, et redémarrer tomcat, il y a des commandes SIM pour ça, et avec docker il suffit de redémarrer l'image.


**SystemTool.resetCache**

Sinon vous pouvez créer votre propre action qui appelle la méthode `SystemTool.resetCache` :


```java
/**
 * Clears the system cache and update the LAST_CLEAR_CACHE to notify other servers.
 * No UI access is permitted during this operation.
 * @param g User rights
 * @param memory true to clear the cache memory
 * @param core   true clear the core definitions
 * @param invalidateSessions true to disconnect everybody
 * @param notify notify other servers ?
 * @param preCompile pre-compile objects and processes ? (0=no, 1=sync, 2=async)
 */
public static boolean resetCache(Grant g, boolean memory, boolean core, boolean invalidateSessions, boolean notify, int preCompile)
```

avec g = Grant.getSystemAdmin()
