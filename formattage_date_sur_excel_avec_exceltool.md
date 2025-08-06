# Formattage date sur excel avec ExcelTool

**URL:** https://community.simplicite.io/t/5709

## Question
Bonjour, je génère un excel à l'aide d'ExcelTool, je souhaiterai pouvoir rentrer avec l'outil des dates formaté au format "date" disponible dans excel 
exemple ci-dessous, la date de gauche est au format "standard", alors que l'autre rentrée manuellement est au format "date".
![image|553x271, 50%](upload://acHO3e2NH5uGK3LMUz7yUkUWoyx.png)
Cela est-il possible ?

J'avais le même problème avec les nombres : celui de gauche etait considéré comme du texte, alors que celui de droite comme un nombre.
![image|507x39, 50%](upload://8uF1k3wxbhF0DzvkN1xVIv2sNxC.png)
Problème que j'ai résolu grâce à la fonction
 `varExcelRow.add(xls.newCell(i++, varInt));
`

j'imagine qu'il faudrait créer un équivalent
 `varExcelRow.add(xls.newCell(i++, varLocalDate));`

## Answer
Est ce que l'export des responsabilités (date de début et de fin) fonctionne ?

Si oui, dans l'argument ObjectField, passez un Field non null pour aider l'API sinon je suppose que la date devient 0 quelque part.

```java
ObjectField fieldDate = new ObjectField(ObjectField.TYPE_DATE);
newCell(i++, "2023-01-03", CellType.NUMERIC, ExcelTool.DATE_CELL_WHITE, fieldDate);
```

Sinon le pb vient de votre Excel.

UPDATE : on va renforcer l'API pour mieux détecter une date si le paramètre field est null, sinon ça parse le CellType.NUMERIC effectivement à 0 par défaut un peu plus tard au niveau du addRow. En attendant, il faut spécifier le type d'attribut pour forcer la date.
