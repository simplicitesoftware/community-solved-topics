# Calcul automatique

**URL:** https://community.simplicite.io/t/4643

## Question
Bonjour,

Dans un formulaire, j'ai plusieurs champs avec des valeurs et des champs qui affichent le résultat de calculs en fonction de ces valeurs.

Actuellement j'ai un bouton "Calculer" qui lance le calcul mais est-il possible d'avoir un calcul automatique dès que je change une valeur sans avoir besoin du bouton?

```
Version=5.1.36
BuiltOn=2022-03-25 23:37
Git=release/8329db12a092c6c91775901c9f207681792bbea1
Encoding=UTF-8
EndpointIP=10.0.32.65
EndpointURL=http://lsllcot01.lausanne.ch:20458
TimeZone=Europe/Zurich
SystemDate=2022-04-05 13:42:10
```

## Answer
Ou bien créer une contrainte Front sur expression = [ISNEW] qui change la valeur du champ.
![image|626x499](upload://vw2dvneUklFrDlBhA7VnBoBdtL5.png)
