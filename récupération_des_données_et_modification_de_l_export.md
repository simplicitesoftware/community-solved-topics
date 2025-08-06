# Récupération des données et modification de l'export

**URL:** https://community.simplicite.io/t/9587

## Question
Bonjour,

je souhaite créer un bouton "Exporter" et du code java qui récupère les données sélectionnées dans un tableau et les exports en excel.

Pour ce faire, je construis le tableau a partir d'une requête SQL grace à getSelectedIds(), puis  j'utilise la fonction generateToByteArray de ExcelTool.

Le problème est que j'ai des éléments qui provienne de jointures imbriquées ce qui rend la requête beaucoup trop complexe à générer.

J'aimerais savoir s'il y avait un moyen de récupérer les données sélectionnées dans le tableau ainsi que le champ correspondant sans faire une requête SQL.

## Answer
Bonjour, 

A priori, le cas d'usage que vous souhaitez implémenter est documenté ici : [Publications / Mulitple records publications](https://docs.simplicite.io/docs/integration/publications/publications#multiple-records-publications)

Vous avez également un exemple de publication Excel basée sur une selection de lignes dans le code de l'objet DemoContact du module Demo téléchargeable depuis l'AppStore de votre instance
