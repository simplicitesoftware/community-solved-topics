# Accès SQL Read only

**URL:** https://community.simplicite.io/t/6203

## Question
Simplicité 5.1.59

Bonjour,

est-il possible de limiter la fonctionnalité d'accès BDD à des requêtes READ ONLY ?
![image|598x411](upload://tc5gVEMyoNvkzxHvT4qdkRQFg8q.png)

Merci d'avance

## Answer
Un objet "select" est un objet pour lequel le designer définit une requête SQL spécifique. Il y a des exemples dans la demo:
![image|690x290](upload://28tg45ACBtfzjxwHuA2Rcw3C9pe.png)

Conceptuellement c'est une "vue" = un objet fait pour du read only (puisque c'est un select) mais ça bénéficie des mécanismes standards applicables à tout objet métier = droits, pagination, attributs filtrables, recherches prédéfinies, tableaux croisés, etc.

Le composant DBAccess est fondamentalement un outil de dev à mettre dans les mains de gens qui savent ce qu'ils font et à ne jamais utiliser en PROD (sauf cas exceptionnel)

Ce n'est pas un outil métier donc, non il n'y a pas d'historisation des requêtes (autre qu'en mémoire pendant la session)  ni traçabilité particulière (autre que la traçabilité SQL standard).

Si votre besoin c'est de gérer un "catalogue" de requêtes rejouables ça devient du métier = à modéliser (ex: un objet "Requête" avec un attribut texte SQL et un mécanisme pour récupérer le résultat de la requêtes = un attribut fichier avec le CSV résultant, ou un objet lié pour historsier les CSV résultants, une action, etc.)

Dans tous les cas je maintient qu'il n'est jamais  sain de mettre dans les main d'utilisateurs métier (même si le métier c'est exploitant) des mécanismes pour faire des requêtes SQL **libres** = risques en termes de droits, risques légaux (ex: RGPD), risques techniques (ex: si grosse requête qui finit en out of memory) etc.

Si votre client interdit les accès en base via un outil de base de données ce n'est sans doute pas pour que cette interdiction - à priori légitime - soit contournée par des outils au niveau applicatif.
