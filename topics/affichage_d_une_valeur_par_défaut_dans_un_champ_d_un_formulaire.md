# Affichage d'une valeur par défaut dans un champ d'un formulaire

**URL:** https://community.simplicite.io/t/8996

## Question
J'ai une question assez basique a priori.
J'ai un formulaire de saisie d'un objet métier dans lequel figure un champ "année". J'aimerais que dans ce champ, l'année courante soit affichée par défaut (à l'ouverture du formulaire donc).
Dans le code de l'objet métier, j'imagine que j'ai juste à faire : setFieldValue("annee", Tool.getCurrentYear());
(où "annee" est le nom de l'attribut concerné dans l'objet métier).

Mais la question est : quel hook dois-je utiliser pour pouvoir faire ça ? J'ai essayé avec initUpdate() mais ça n'a pas l'air de fonctionner.

Au passage : n'y a-t-il pas dans la documentation Simplicité un diagramme d'états-transitions décrivant le cycle de vie d'un objet métier et décrivant (en détail) tous les points de hook possibles ?

## Answer
En V6, en plus de la docs des hooks et les tutos, le "cycle de vie" est donné au runtime en activant les traces des hooks appelés. 

Dans le `postLoad`, vous pouvez ajouter par exemple

```java
traceHooks(TRACE_HOOKS_FULL);
```

Les valeurs possibles :

```java
/** No hook trace in logs (default mode) */
public final static short TRACE_HOOKS_NONE = 0;
/** Trace all hook calls without argument (training mode) */
public final static short TRACE_HOOKS_FULL = 1;
/** Trace only implemented hook calls (simple debug mode) */
public final static short TRACE_HOOKS_IMPLEMENTED = 2;
/** Trace only implemented hook calls with some useful arguments (verbose debug mode) */
public final static short TRACE_HOOKS_IMPLEMENTED_ARGS = 3;
```

Très utile quand on débute ou en debug, et à mettre en commentaire quand on livre ;-)
