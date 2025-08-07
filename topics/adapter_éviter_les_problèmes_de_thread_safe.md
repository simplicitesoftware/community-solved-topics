# Adapter éviter les problèmes de thread safe

**URL:** https://community.simplicite.io/t/5113

## Question
Bonjour,

Dans notre application, nous avons un besoin de faire tourner plusieurs adapteurs dans un gap de temps réduit. Ces adapteurs sont susceptibles d'interagir sur des ObjectDB similaires entre eux.

Dans le but d'éviter des problèmes de Thread safe, quel est le meilleur pattern que nous pouvons utiliser ? Le pattern ci après est il adapté au besoin ?

https://community.simplicite.io/t/csv-adapter-example/2110

Concernant l'instanciation des ObjectDB, quelle est la méthode la plus adaptée à notre cas d'utilisation :
- getGrant().getProcessObject(objectName); 
- getGrant().getObject(uniqueId, objectName); 

Merci d'avance pour vos précieux conseils.

Benoît

## Answer
Bonjour,

Pré-requis théoriques:

* la notion d'instance dans Simplicité : [https://docs2.simplicite.io/lesson/tutorial/development/instances](https://docs2.simplicite.io/lesson/tutorial/development/instances)
* la gestion de concurrence avec `synchronized` : https://www.baeldung.com/java-synchronized

## Thread safe

L'exemple typique, tiré du training, est le suivant. Cet exemple est thread-safe et utilise l'instance `tmp_TrnProduct` de la classe `TrnProduct`. À noter que `getTmpObject("TrnProduct")` et `getObject("tmp_TrnProduct", "TrnProduct")` sont strictement équivalents. **Ce n'est pas le type d'instanciantion qui garantit le thread-safe, mais le mécanisme de verrouillage d'instance avec synchronized.**

```java
// chargement d'une instance temporaire
ObjectDB product = getGrant().getTmpObject("TrnProduct");
// bloc synchronized pour empêcher l'utilisation concurrente de cette instance par un autre thread
synchronized(product){
     // opérations sur l'instance
}
```

## Instance

Maintenant qu'on sait faire du thread-safe, se pose la question de quelle instance utiliser, et c'est un choix technique:
- si on utilise la même instance (par exemple `tmp_TrnProduct`) dans tout le code, en thread safe, alors les threads peuvent s'attendre les uns les autres, ce qui peut (selon l'algorithme) créer des embouteillages, ou pire, s'il y a des co-dépendances entre blocs de code, on peut créer des blocages avec des threads qui s'attendent mutuellement...
- si on utilise une instance spécifique à chaque bloc de code (par exemple `mymethod_TrnProduct`) ou pire, à chaque **exécution de code** (par exemple avec `Tool.randomString​(10)+"_TrnProduct"`), on consomme beaucoup de mémoire inutilement (chaque création d'instance alourdit l'utilisation de mémoire par la JVM)

## [bonus] Accès concurrent au record

Si votre code fait des modifications en base sur le même record d'objet, via des threads différents, va se poser la question des accès concurrents sur la base, qui se gère par paramétrage de l'objet métier.

![Simplicité®|664x262, 50%](upload://okIqNbuSBT5yRT8xQ12ykVkXcvk.jpeg)

Cela implique par exemple qu'un `product.getTool().validateAndUpdate()` dans votre bloc synchronized peut parfaitement lancer une `UpdateException` qu'il faut s'assurer de gérer.

## Conclusion

[quote="Benoit, post:1, topic:5113"]
faire tourner plusieurs adapteurs dans un gap de temps réduit. Ces adapteurs sont susceptibles d’interagir sur des ObjectDB similaires entre eux.
[/quote]

- **gap de temps réduit:**  peut impacter selon le mode de lancement des adapteurs, la fréquence de lancement vs le temps d'exécution, etc.
- **ObjectDB similaires:** impacte si plusieurs threads travaillent avec la même instance du même objet.


Dans le cas général, pour les adapteurs, un `synchronized` sur une instance dédiée aux adapteurs obtenue via `getProcessObject`, est la recommandation. Cependant, difficile de répondre absolument sans savoir exactement ce que le besoin exprimé ci-dessus implique exactement, j'espère que les explications données pourront vous aiguiller vers une solution adaptée.

Lecture complémentaire: https://community.simplicite.io/t/simplicite-et-les-blocs-synchronized/4937/3?u=scampano
