# Est-il possible de récuperer un attribut html/ longstring avec java

**URL:** https://community.simplicite.io/t/5289

## Question
Bonjour,

je souhaiterais récupérer le contenu d'un texte rentré dans simplicité, dans mon code java. Sauf que lorsque je recherche dans le diagramme associé le nom qu'il faut rentrer, je ne trouve ni le "full name" ni le "API name" utilisé dans le code pour récupérer des données. (sachant que ceux-ci sont présent pour les attributs de type  plus classiques : int, date, etc...)



![image|249x33](upload://vMHlZoWdLAF31VpewATs3YepsI3.png)
 
![image|297x113](upload://bzqvGVN3UGwuFtxPDbbiuzstE4A.png)


Cordialement,
Paul-Alexandre

## Answer
Bonjour Paul-Alexandre, 

Le "full name" et "API name" ne sont présents que pour les champs ramenés. Ils n'ont pas de sens pour les attributs de l'objet "non ramenés" puisque le nom logique suffit. 

Le full name et API name sont la concaténation du nom logique de la foreign key et du nom logique de l'attribut.

Pour récupérer le contenu d'un attribut d'objet, il suffit donc d'utiliser le nom logique de l'attribut, dans ton cas : `getFieldValue("evlValFinancialComment")`
