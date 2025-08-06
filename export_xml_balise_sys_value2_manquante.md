# Export XML : balise sys_value2 manquante

**URL:** https://community.simplicite.io/t/6805

## Question
### Request description

J'ai remarqué qu'en faisant un export XML d'un paramètre système, la balise "sys_value2" n'est plus présente dans le fichier.

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.11
BuiltOn=2023-08-07 15:27
Git=5.3/015368bc51913a479e8d682d65ea405c12b45951
Encoding=UTF-8
EndpointIP=xxx
EndpointURL=xxx
TimeZone=Europe/Paris
SystemDate=2023-08-24 15:28:15
```
[/details]

## Answer
[quote="Benoit, post:1, topic:6805"]
sys_value2
[/quote]

Effectivement le champ est passé en non-exportable dans les patch V5.3.
Ca reste un paramètre de l'attribut modifiable en étant ADMIN+system.

Il sert à surcharger pour chaque instance (recette/prod...) la définition par défaut livrée dans le module dans `sys_value`. Le rendre exportable par défaut va écraser les surcharges éventuelles sur les autres environnements. Ce qui n'est pas le comportement attendu, la valeur surchargée doit le rester après un import.

Ce changement de comportement est très récent.
C'est un fix de début juin d'après la release note 

<h3 id="version-5.3.4">5.3.4 (2023-06-03)</h3>

- Fixed do not export `sys_value2` in module to keep overridden value on target platform
