# Appel du beforeSave au moment d'un refSelect

**URL:** https://community.simplicite.io/t/12395

## Question
### Request description

Bonjour,

J'ai un souci avec le hook beforeSave qui se déclenche quand je clique sur la loupe d'une référence.

Mode opératoire :
- avoir un objet A avec une référence vers un objet B
- mettre un alert dans le beforeSave de A
- sur le form de A, cliquer sur la loupe vers B
-> l'alert apparaît

On dirait que c'est l'appel à readValues qui déclenche le beforeSave.

![image|690x202](upload://qkAwmJmM5GmSqEbdhixfJbvZVvw.png)

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.9
Variant=full
BuiltOn=2026-05-08 12:11
Git=6.3/58e3ee3f94cecfc8aaa762e57a41f8e5bdf91454

## Answer
Oui mais cela impactera aussi la signature de la méthode.
Il semble préférable de séparer les hooks pour éviter les confusions.

Après analyse il suffit d'ajouter 
- un hook au niveau de la méthode `$ui.readForm` qui sert à lire tous les fields depuis le formulaire/row :

`obj.locals.ui.form.onread` = `UIBusinessObject.onReadForm(ctn, obj, params, cbk)`

Il permettra de modifier/completer les valeurs lues avant tout usage front. Ce sera avec callback explicite une fois réalisé pour permettre de lire des choses de façon asynchrone (un appel d'API...) comme le fait `beforSave`.

- le hook `beforeSave` sera utilisé par `saveObject` uniquement.

Il permettra de faire des vérifications (bloquantes) avant appel au back.

On va faire les évolutions nécessaires en 6.3.11.
