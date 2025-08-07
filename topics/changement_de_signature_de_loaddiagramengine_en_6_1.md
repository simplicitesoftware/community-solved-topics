# Changement de signature de loadDiagramEngine en 6.1

**URL:** https://community.simplicite.io/t/9625

## Question
### Request description

Bonjour,

Nous migrons de la 5.3 vers la 6.1 et constatons que la méthode loadDiagramEngine a changé de signature. Elle ne prend plus de paramètres et n'appelle plus de callBack.

Nous avons donc changé notre code de la façon suivante

```
5.3
$ui.loadDiagramEngine(false, function() { // Do something});

6.1
$ui.loadDiagramEngine();
//Do something
```

Est-ce correct ?

Merci !
Emmanuelle

## Answer
Effectivement cette méthode retourne une promesse.

`$ui.loadDiagramEngine().then(function...);`

ou la fonction est async
`await $ui.loadDiagramEngine();`

Il faudrait directement migrer en 6.2.
