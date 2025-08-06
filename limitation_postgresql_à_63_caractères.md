# Limitation Postgresql à 63 caractères

**URL:** https://community.simplicite.io/t/6058

## Question
Bonjour,

Nous venons de nous rendre compte il y a peu que certains nommages de colonnes dans notre base dépassent les 63 caractères ce qui correspond à la limitation de la BDD Postgresql, qui effectue un "truncate" sur les identifiants dépassants les 63 caractères.

Cela génère des erreurs sur certaines requêtes générées automatiquement, car les alias créés sont identiques après un "truncate" (la différence entre les deux n'est visible qu'au-delà des 63 caractères.).

Existe-t-il un paramétrage interne à simplicité pour limiter la taille des noms de colonnes proposés par la plateforme ?

Y a-t-il déjà eu des problèmes remontés de ce type ?

Merci d'avance,

Benoît

## Answer
### En 5.2 et 5.3

Pour éviter d'impacter les autres SGBD ou toute la plateforme, les alias de table seront tronquées à 63 caractères sur PGSQL uniquement (avec un suffixe numérique en cas d'ambiguïté si plusieurs chemins mènent à Rome).

Donc si vous codez des requêtes longues (dans une search-spec), il faudra la spécialiser suivant le SGBD en testant le datasource provider via getGrant().getDBVendor() (ex si on utilise hsql en dev, pg en prod...)

### A partir de la 5.4/V6

Cette limitation à 63 sera généralisée à tous les SGBD pour éviter cette spécialisation du code, mais du coup impactera tout le monde au niveau du code spécifique. Si on n'utilise jamais PGSQL, on pourra changer cette valeur via :

- `DB_NAME_MAX_LENGTH = 63` par défaut du maillon faible PGSQL
- `DB_NAME_MAX_LENGTH = 64` sur MySQL
- `DB_NAME_MAX_LENGTH = 128` sur Oracle 12+
- `DB_NAME_MAX_LENGTH = 2048` ou plus sinon

Ce paramètre servira également à tronquer les noms de toute entité créée : table, colonne, index, séquence...
