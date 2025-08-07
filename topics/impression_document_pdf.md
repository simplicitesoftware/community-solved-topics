# Impression document PDF

**URL:** https://community.simplicite.io/t/4947

## Question
Bonjour,

Pour publier un document PDF contenant des données d'un objet métier, il faut bien faire comme dans la démo (DemoOrder.printReceipt() pour la méthode derrière la publication + DemoCommon.orderReceipt() qui génère le document PDF) ?

En vous remerciant.

Bruno

## Answer
Ce n'est pas la seule manière de faire mais c'est une des possibilités. Pour plus d'info sur les publications voici la doc de formation à ce sujet: https://docs2.simplicite.io/lesson/tutorial/development/publication et une doc avec des exemples: https://docs.simplicite.io/documentation/01-core/publication-examples.md

Un autre exemple de publication PDF, applicable à des cas simples : https://github.com/simplicitesoftware/module-htmltopdf (utilisation d'un template HTML + conversiion par la lib OpenHTMLToPDF en PDF)
