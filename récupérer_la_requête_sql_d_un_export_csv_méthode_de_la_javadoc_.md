# Récupérer la requête SQL d'un export CSV (méthode de la javadoc)

**URL:** https://community.simplicite.io/t/6838

## Question
Bonjour,

Je travaille actuellement sur une "extraction" de requête SQL.
Il s'agit là de récupérer la requête SQL de l'export CSV fait avec : ***CSVTool.export(...)*** 
J'aimerais savoir, si possible, comment je pourrais récupérer la requête SQL exacte qui est utilisée pour générer l'export CSV (dans une optique d'adaptation pour nos besoins spécifiques).

Merci d'avance pour votre aide !

Mounir

## Answer
Bonjour,

D'une façon générale on ne peut pas accéder au SQL en mise à jour, on peut tracer les requêtes dans les logs via le paramètre `LOG_SQL_USER = yes`.

L'export fait en plus d'un search normal (pre/postSearch...), un pre/postExport sur l'objet.

Pour modifier le résultat de l'export, il faut donc agir par paramétrage ou par code :
- sur les colonnes ramenées en jouant sur la propriété "exportable" des champs
- sur les lignes, en jouant sur les filtres ou la search-spec de l'instance (preExport) ou sur les lignes ramenées après "select" en base (postExport)

Il est toujours possible de faire un "select" spécifique :
- via un objet "select" dont la search-spec est une requête complête qui ramène des colonnes dans l'ordre des attributs d'objet (y compris les champs cachés comme le row_id et les timestamps si l'objet en possède)
- via une publication et une méthode que fait du SQL
