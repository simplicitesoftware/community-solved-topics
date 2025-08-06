# Champ ramené obligatoire après un setUpdatable

**URL:** https://community.simplicite.io/t/6660

## Question
### Request description

Bonjour,

J'ai un objet A sur lequel je crée un champ ID référence vers un objet B ; et le champ Nom ramené de l'objet B.
Sur l'objet B, le champ Nom est obligatoire.
Mais sur l'objet A, la référence à B n'est pas obligatoire.

Dans le postLoad, je fais un ```Nom.setUpdatable(ObjectField.UPD_ALWAYS)```.
J'ai l'impression que cela rend le champ nom obligatoire sur A, même si la référence à B n'est pas renseignée.

Merci !
Emmanuelle



### Technical information

[details="Instance /health"]
```text
Version=5.3.8
BuiltOn=2023-07-10 20:23
Git=5.3/4502a60a63d445a5ec961e13b5f62415953c5056
```
[/details]

## Answer
Oui cette feature serait pratique pour des cas simples d'usage de champ joint non clé.
Ca reste assez compliqué car les API font des contrôles d'intégrité entre les ids/les clés envoyées, ou complète ce qui manque pour la couche métier, etc. Pouvoir forcer une mise à jour d'un champ lié au milieu de ce traitement n'est pas sans risque de régression.

Sur le fond c'est assez confusant pour l'utilisateur de mélanger 2 notions : le caractère obligatoire ou non d'une relation et celle du champ joint au niveau des champs de saisie sur l'objet père (la UI ne doit pas le faire). Au final on fait souvent autrement / par exemple on démoralise le champ sur A et on le copie au postSave dans B / ou on ajoute un handler "change" qui fait la mise à jour dans B...
