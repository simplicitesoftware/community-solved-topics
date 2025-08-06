# Supprimer l'écran de saisie d'attributs à l'association d'un objet

**URL:** https://community.simplicite.io/t/3005

## Question
Bonjour,

Quand j'associe un objet via une relation N,N et que ma relation a des attributs, un écran apparaît pour permettre de les renseigner. Je calcule ces attributs automatiquement donc je cherche un moyen de ne pas avoir cet écran.

> Version=4.0.P25
> BuiltOn=2021-01-25 18:55 (revision 8e9b757c68b3391e16a0570ac07b374ccc25a0e6)

Merci d'avance pour votre aide !
Emmanuelle

## Answer
Bonjour,

Lorsque les attributs sont non visibles la popup n'apparait pas.
Il y a un hook initAssociate dans lequel vous pourriez les placer en non visibles et les rendre visibles dans les autres cas.
