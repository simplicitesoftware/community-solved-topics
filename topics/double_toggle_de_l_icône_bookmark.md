# Double toggle de l'icône Bookmark

**URL:** https://community.simplicite.io/t/13328

## Question
### Request description

Bonjour,

J'ai un souci avec un cas très spécifique (sur lequel j'ai réussi à tomber) avec le bouton Bookmark d'un formulaire. Dans mon cas, le clic ajoute / retire bien l'objet aux Bookmarks, mais l'étoile ne change pas d'apparence (ou plutôt, fait un aller retour et revient à l'apparence initiale.)

### Steps to reproduce

1. Avoir un objet A avec un objet B en liste fille
2. B doit avoir au moins une ligne
3. B ne doit avoir aucune action dans sa barre d'actions (même dans le Plus, tout doit être Hidden)
4. Bookmarker A
5. A est bien Bookmarké, mais son étoile reste vide

### Piste d'analyse
Au moment de l'appel à ```bookmarkToggle``` pour B, si aucune action n'est disponible dans sa barre, la variable ```items``` est vide.

Ceci ```b = $view.widget.actionBar(items);``` est donc vide aussi.
```bookmarkToggle``` est appelé avec ```ctn``` vide.

Dans la fonction ```bookmarkToggle```, ```b = $("[data-action=bookmark]", ctn);``` va chercher le bouton Bookmark sur A au lieu de le faire sur B qui n'a pas fourni de conteneur.
Il ajoute un premier event ```ui.bookmark.toggle``` sur l'étoile de A.
On repasse ensuite dans la méthode pour A cette fois, et un 2ème event est ajouté (à raison cette fois-ci.

![image|690x52](upload://j4gj7tyJbwGIVxTllke2RNxH61g.png)


Quand on clique sur l'étoile, l'event est appelé une première fois et colore l'étoile, puis une deuxième et la fait revenir à son état initial.

Merci d'avance !
Emmanuelle

### Technical information

[Platform]
Status=OK
Version=6.3.16
Variant=full
BuiltOn=2026-09-09 19:41

## Answer
_No answer provided._
