# PDFTOOL.getCell et séparateur de milliers

**URL:** https://community.simplicite.io/t/5061

## Question
bonjour,

j'ai un fonction qui permet de générer un pdf d'état financier. J'affiche les montants avec des séparateurs de milliers en utilisant ce code:

String fraNumber = NumberFormat.getInstance(Locale.FRENCH).format(Double.parseDouble(mt));
PdfPCell cell = PDFTool.getCell(mt);


en version 5.2.8, mon code fonctionne correctement et le résultat est le suivant :
![image|690x180](upload://uoRvSICXLbr3HwBjhvk23kw6uou.png)

depuis le passage à la version 5.2.10, le séparateur de millier n'est plus pris en compte.
![image|690x191](upload://8Z1T3oofIsL7Goq4w0xUojBygmt.png)

le PDFTool.getCell semble avoir changé de comportement entre la V 5.2.8 et la V 5.2.10

## Answer
Testé sur la démo, ce type de code affiche bien la valeur formattée en PDF comme il faut (i.e. au format Français pour un user en Français):

```java
PdfPTable t = PDFTool.getTable(2, false);
(...)
t.addCell(ord.getGrant().toFormattedFloat(ord.getFieldValue("demoOrdTotal"), 10, 2));
(...)
```

Résultat:

![image|120x50](upload://7UyEAbbFR5S8GPfKYY5j6fNmKnq.png)
