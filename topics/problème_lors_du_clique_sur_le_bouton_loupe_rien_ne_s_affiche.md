# Problème lors du clique sur le bouton loupe, rien ne s'affiche

**URL:** https://community.simplicite.io/t/6286

## Question
Bonjour, 

Sur notre projet nous rencontrons un problème. En effet lorsque nous souhaitons cliquer sur l'icone loupe dans le menu ci-dessous, nous n'avons aucun retour écran. Alors que normalement nous devrions avoir une pop-in qui s'affiche avec la liste des différents centres.

![image|690x174](upload://62fT81uPQTdJnf14oDiKZaGhdW9.png)

En regardant les logs nous avons une erreur qui est remonté coté front la voici: 
```text
Uncaught TypeError: Cannot read properties of undefined (reading 'createLink')
    at Simplicite.UI.Engine.display (ui-bundle.js?_=59:1188:759)
    at next (ui-bundle.js?_=59:967:15)
    at Simplicite.UI.Engine.onload (ui-bundle.js?_=59:961:197)
    at Simplicite.UI.Engine.loadCSS (ui-bundle.js?_=59:686:126)
    at next (ui-bundle.js?_=59:961:144)
    at Simplicite.UI.Engine.onload (ui-bundle.js?_=59:965:185)
    at Object.<anonymous> (ui-bundle.js?_=59:680:393)
    at c (jquery.js:2:28294)
    at Object.fireWith [as resolveWith] (jquery.js:2:29039)
    at l (jquery.js:2:79800 
```

Je ne sais pas si cela aide mais nous avons d'autres icones loupes sur cet écran et elles fonctionnent toutes correctement. 

Le code customisé que nous avons mis en place pour la classe namCentre, nous avons essayer de la commenter pour savoir ce n'était pas une erreur d'implémentation de notre part mais nous avons le même comportement avec  ou sans le code customisé. 

Auriez-vous une idée de ce qui cause ce problème? et si oui savez vous comment potentiellement le résoudre? 

En vous remerciant 🙂

## Answer
Bonjour,
Votre question relève de la formation de base :

https://docs2.simplicite.io/lesson/tutorial/configuration/relations
