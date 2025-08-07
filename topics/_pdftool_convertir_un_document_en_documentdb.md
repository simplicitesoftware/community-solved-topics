# [PDFTool] Convertir un Document en DocumentDB

**URL:** https://community.simplicite.io/t/4531

## Question
Bonjour,

Je génère un PDF grâce à la classe `PDFTool`. J'aimerais insérer ce document dans un champ de type `DocumentDB` dans ma BDD.

`PDFTool` créer un objet de type Document (`com.lowagie.text.Documen`t). Cependant, pour insérer le PDF dans ma table en BDD, j'ai besoin d'utiliser `setFieldValue()` avec une valeur non pas de type Document, mais de type DocumentDB.

**Comment convertir les 2 types ?**

## Answer
L'erreur vient peut être du nom du Document créé. Est-ce qu'en mettant "Pouvoir.pdf" le résultat est le même ?
