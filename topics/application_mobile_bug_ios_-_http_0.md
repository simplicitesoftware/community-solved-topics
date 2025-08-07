# Application mobile : Bug IOS - HTTP 0

**URL:** https://community.simplicite.io/t/4437

## Question
Bonjour,

Je souhaite utiliser l'application mobile. pour tester, 2 personnes ont téléchargé l'application mobile simplicité :
* 1 sous Android (Samsung)
* 1 sous IOS (IPhone)

Sous Android, nous pouvons nous connecter sans problème. Cependant la personne sous IOS ne peut pas se connecter et on obtient l'erreur suivante dans les logs:
![image|690x149](upload://dXPiySqW3XScpyN9rdDqORAk8qi.png)
Sur l'application, la personne sous IOS obtient le code erreur HTTP 0 (sachant que le code 0 n'existe pas pour HTTP).

**PS :** `L'URL + Le login + Le MDP` ont été vérifié plusieurs fois et il n'y a pas d'erreur.
**PS2 :** La version IOS est la 15.3, la version Android (qui fonctionne) est la 10.0.

Une idée d'où peut provenir l'erreur ?

## Answer
Bonjour,

Il doit y avoir un nouveau problème sur iOS avec l'authent via un moteur Cordova. 

La politique d'Apple est de tuer à terme toutes les applications encapsulées (comme une webapp dans Cordova ou phoneGap) au profit de leur langage natif (compilé sur xcode, swift...), ce qui reviendra à développer un front spécifique. Nous ne prévoyons pas de développer actuellement une UI générique pour iOS.

Google/Androïd n'a pas la même politique et Cordova continue de fonctionner..

Bref comme le préconise David, sur iOS le plus simple est de passer par un navigateur.
On perd juste la fonctionnalité de pouvoir lui envoyer des Notifications via Firebase.

On va retester sur iOS pour voir si on peut contourner le problème d'authent du web container encapsulé.
