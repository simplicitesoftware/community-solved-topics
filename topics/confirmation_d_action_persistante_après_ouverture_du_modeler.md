# Confirmation d'action persistante après ouverture du modeler

**URL:** https://community.simplicite.io/t/8468

## Question
### Request description

Bonjour,
J'ai une action avec confirmation + attributs d'action. Elle exécute un code front qui utilise le modeler.

![image|690x288](upload://73SggK1bO3eJkMK6oDFm8m47qCJ.png)
![image|569x369](upload://q89tEt82N1BrHmrcUA2BisL861P.png)

Mon souci est qu'après ouverture du modèle créé, la popup de confirmation ne disparaît pas.

![image|690x240](upload://aM3JdgiPKGQncNvfs00FFv0lhpY.png)

Je ne passe jamais dans ce close

![image|690x303](upload://7a6MCOyJ9ySg1yvybqgumAP9Qql.png)

Savez-vous comment je peux régler le problème ?
Merci d'avance,
Emmanuelle

## Answer
Bonjour,

- Une action back/java retourne explicitement une erreur ou non (ce callback est appelé car le comportement est donc déterminé par ce que répond le back : OK=fermer, KO=erreur sur le dialogue).
- Une action front en `javascript` ne peut pas savoir si c'est OK ou non, c'est donc à ce code front de le faire.

Le code front d'une action avec attributs de dialogue doit donc explicitement indiquer quand il faut fermer le dialogue ou bien afficher une erreur et y rester.

`$ui.view.tools.dialogClose()` : ferme le dialog le plus haut
`$ui.view.tools.dialogClose("dialogname")` : ferme un dialogue donné

De la même manière c'est le code front qui doit afficher ou retirer un éventuel spinner si le traitement est long/asynchrone pour bloquer les interactions utilisateurs :

`$ui.view.showLoading()`
`$ui.view.hideLoading()`
`$ui.alert(...)`
