# Window.opener null dans une publication

**URL:** https://community.simplicite.io/t/3150

## Question
Bonjour,

Sur un de mes objets j'ai une publication qui ouvre une page HTML dans un nouvel onglet.
Certains des éléments de cette page sont cliquables et ouvrent un formulaire d'objet dans la fenêtre mère.
Cela fonctionnait mais je constate aujourd'hui que j'ai une erreur due au opener qui est devenu null.

![image|367x217](upload://uM74VZnt8UfTRnEnMi248VW6c8G.png) 

Le code qui plante


```
var ui = window.$ui || window.parent.$ui || window.opener.$ui;
ui.displayForm(null, RciApplication, this.getAttribute('id'), { showNav: true, nav: new });
```
> Version=4.0.P25
> BuiltOn=2021-03-24 00:20 (revision 0ab578dff484419fee9205b41be7f805473ce9a4)


Est-ce quelque chose a pu changer à ce niveau ?

Merci d'avance !
Emmanuelle

## Answer
C'était bien ça, depuis la version Chrome 88 de Janvier dernier, le `window.opener` est null par défaut quand on ouvre un TAB via un `<a target=_blank>`.

On a forcé le `rel="opener"` et tout est rentré dans l'ordre, en espérant que Chrome ne change pas encore la règle de sécurité, auquel cas on sera contraint de faire un `window.open` (qui ouvre un navigateur et pas un simple TAB). Idem pour Edge qui utilise chromium.

Firefox ne supportant pas le target=_blank n'avait pas ce problème.
