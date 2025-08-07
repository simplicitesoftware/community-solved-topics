# Surcharger l'ordre des colonnes d'un objet hérité

**URL:** https://community.simplicite.io/t/6044

## Question
### Request description

Bonjour,

On a configuré un objet B hérité d'un objet A.
Sur l'objet B, nous avons modifié l'ordre des Objects Fields (paramétrage du champ Order)
Mais l'ordre visible reste celui de l'objet A.

Si nous vidons le champ "Extend of Code", on remarque que les champs suivent bien l'ordre modifié dans l'objet B.

Mais nous souhaitons conserver l'héritage de l'objet A.

Pouvez-vous nous indiquer la bonne marche à suivre pour modifier l'ordre des champs tout en conservant l'héritage ?

Merci d'avance.

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.32
BuiltOn=2023-02-20 14:50
```
[/details]

## Answer
Il me semble qu'on peut réordonner par surcharge de l'objet field.
Peut être que vos champs sont dans des areas, donc ne peuvent pas en sortir (l'ordre sert au sein d'une zone si elles sont affichées).

Une autre approche, si vous redéfinissez tous les champs (l'ordre, ou le template ou les zones/areas), vous pouvez aussi ne pas déclarer l'héritage au niveau de la définition (champ extend vide pour ne pas charger le père avant l'objet), mais juste garder l'héritage de classe au niveau du code Java pour hériter des hooks du parent.
