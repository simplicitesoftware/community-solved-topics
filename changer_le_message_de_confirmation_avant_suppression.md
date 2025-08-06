# Changer le message de confirmation avant suppression

**URL:** https://community.simplicite.io/t/7774

## Question
### Request description

Bonjour,

Est-il possible en 5.3 de modifier le message de confirmation des actions socle ?
J'ai vu que c'était une feature ici mais je ne sais pas si elle a été implémentée ?
https://community.simplicite.io/t/confirmation-avant-creation/5896

Merci d'avance,
Emmanuelle

## Answer
Bonjour,

Le message de confirmation de suppression est un texte statique `CONFIRM_DEL`, il est tout à fait possible d'en changer.

- globalement en modifiant le TEXT en back
- ou localement en front en changeant le libellé chargé en mémoire `$app.texts.CONFIRM_DEL`
Par exemple en 5.3, sur un formulaire dans le `form.onload`, et en remettant l'ancien texte dans le `form.unload`.
