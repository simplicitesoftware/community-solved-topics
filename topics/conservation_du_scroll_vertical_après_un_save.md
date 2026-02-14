# Conservation du scroll vertical après un Save

**URL:** https://community.simplicite.io/t/11481

## Question
### Request description

Bonjour,
Depuis [cette évol](https://community.simplicite.io/t/should-the-scroll-position-on-form-be-kept-by-default/4514), la position dans l'écran est conservée quand on quitte et revient sur un formulaire.

J'ai l'impression que ça ne s'applique pas quand on fait un Save ou tout autre bouton d'action, car le focus est déplacé sur le bouton. Est-ce bien le cas ? Car j'ai peut-être des choses spécifiques qui contrarient la fonctionnalité.
Si oui, serait-ce possible de garder la position aussi en cas de clic sur bouton ?

Merci d'avance !

[Platform]
Status=OK
Version=6.2.21
BuiltOn=2026-01-15 22:16

PS : nous sommes en train de tester la 6.3

## Answer
On a revu le traitement du save des liens inlinés pour :
- les faire dans l'ordre des liens définis : des `await` successifs à la place du gros `allSettled` de promesses
- et forcer ensuite un `getForUpdate` des données de l'objet parent avant que le formulaire ne s'affiche.

J'ai essayé avec des hooks `postCreate` et `postUpdate` sur le fils en relation 1,1 qui mettent à jour l'objet parent et ça fonctionne.

Ce sera livré en 6.2.23
