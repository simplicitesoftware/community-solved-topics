# Alterner la visibilité de 2 champs dans l'affichage en liste

**URL:** https://community.simplicite.io/t/4715

## Question
### Request description

Bonjour,

J'ai 2 champs, ces 2 champs sont en `visible: partout`.
![image|388x93](upload://irZKOElMdnKOqyfBjwxcXzorVjV.png)

J'ai un champ Boolean (`Utilisateur existant`) qui me permet d'alterner ces 2 champs dans mon formulaire.

Le problème, c'est que j'aimerais que ça alterne aussi l'affichage de ces 2 champs dans l'affichage en liste. Ce qui n'est pas le cas pour le moment car les 2 champs sont toujours affichés.

Je gère l'affichage en fonction du champ Boolean dans une contrainte.

Voici l'affichage en liste :
![image|690x227](upload://1WwndgJE2YjoVBz57mSFPoDgGL1.png)

Voici l'affichage dans le formulaire :
![image|690x265](upload://khMRf5Li2Md6t2C1p8UDD1PSLDA.png)

On voit bien que dans le formulaire le champ "`Nom et prénom du responsable`" n'apparait pas. Alors qu'il apparait dans l'affichage en liste.

**Une idée de comment corriger le problème ?**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.37
BuiltOn=2022-04-05 11:19
Git=release/0d9c19594e35d74bd1dead5960d3b31b37337814
Encoding=UTF-8
EndpointIP=10.201.117.1
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-14 11:15:41
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Bonjour,

D'un point de vue purement pratique, imaginons que vous ayez plusieurs éléments dans cette liste et que la valeur du boolean est différente d'une ligne à l'autre comment voulez vous afficher une colonne pour une ligne et pas pour l'autre ?
