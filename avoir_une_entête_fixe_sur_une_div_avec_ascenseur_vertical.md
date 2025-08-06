# Avoir une entête fixe sur une div avec ascenseur vertical

**URL:** https://community.simplicite.io/t/6005

## Question
### Request description

Bonjour,

J'ai une vue en liste avec beaucoup de colonnes, pour laquelle j'ai fait en sorte que l'ascenseur horizontal soit toujours visible.

```
.objlist.object-RciDrpView .table-responsive{
	overflow-y:auto;
	height:35rem;
}
```
J'ai donc deux ascenseurs sur ma div de liste, un horizontal, un vertical.
L'ascenseur de mon navigateur n'apparaît plus car le nombre de lignes visibles ne dépasse plus la taille de l'écran.

Mon problème est que quand je scrolle à l'aide de l'ascenseur vertical de div, l'entête n'est plus visible.
J'ai l'impression que l'événement ne se déclenche que sur le scroll du navigateur.
J'ai tenté par tous les moyens d'ajouter la classe sticky-header à la balise thead sur le scroll de ma div, sans succès.

Pouvez-vous m'aider ?

Merci d'avance !
Emmanuelle

## Answer
Au 21e siecle il doit être possible de scoller sans utiliser la barre de scroll
- 2 doigts+ slide sur le touch pad
- molette de souris moderne (avec maj ou ctrl enfoncé, ou molette qui est sensible à l'orientation, il faut aller dans ses options)

Si tu veux revenir à un Excel-like-non-paginé, il faut retirer l'option de pagination de la liste (ce qui signifie charger toute la table, donc forcer à saisir quelques filtres), et mettre des scroll sur la table de hauteur fixe via STYLES/CSS.

Pour fixer le header en haut, rien de standard en CSS, ce serait trop simple que de mettre un style "fixed" sur le thead. Tu pourras le faire plus facilement si les colonnes sont également de largeurs fixes.

Bref tout sauf responsive, il faut éduquer les utilisateurs à utiliser une interface web qui a été optimisée pour ça. Sinon il y aura d'autres contraintes d'ergonomie.
