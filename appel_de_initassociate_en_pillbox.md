# Appel de Initassociate en pillbox

**URL:** https://community.simplicite.io/t/5545

## Question
### Request description

Bonjour,
J'ai l'impression que le hook Initassociate n'est pas appelé quand la présentation est en pillbox, est-ce possible ? Y a-t-il une alternative ?

Merci !
Emmanuelle



### Technical information

[details="Instance /health"]
```text
Version=4.0.P25
BuiltOn=2022-08-24 11:46 (revision fcb3c9f4bdea7a2dc035ce2f98bbb41bd0fe2bb2)
```
[/details]

## Answer
Bonjour Emmanuelle,

L' `initAssociate` est réservé pour la liste d'une association en masse.

Dans le cas d'une N,N en pillbox, c'est l'instance de sélection des références qui est utilisée.
donc il faut utiliser le hook `initRefSelect` sur l'objet lié par la N,N, comme lorsqu'on sélectionne une référence mais dans ce cas on peut en sélectionner plusieurs en front.
