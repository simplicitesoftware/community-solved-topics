# Question sur export Générique "Appliquer les préférences de colonnes visibles"

**URL:** https://community.simplicite.io/t/3031

## Question
Bonjour,

A quoi sert "Appliquer les préférences de colonnes visibles" dans les exports génériques ?

![image|690x384](upload://caxxGrAxxGyeLzErH1LmUHZkjfM.png) 

Cordialement,

## Answer
Je ne reproduis pas, les Prefs sont bien prises en compte dans l'export CSV, ça passe par le même objet que pour Excel.
Mais attention : le cas d'un user ADMIN est un cas particulier qui exporte tout et pas que ce qui est visible pour des raisons historiques d'export/import de paramétrage technique (ça ne traduit pas les LOV, etc.).

Pour préciser l'arrivée de ce nouvel export : le besoin métier est de créer des recherches prédéfinies (filtres + tris + préférences) pour avoir des vues sur les données et les exporter dans ce formalisme sans avoir à développer des héritiers ou autre mécanisme pour exporter des vues partielles.

Les autres exports utilisent la définition de l'objet et pas ce qui est réellement affiché par préférence (ordre des colonnes visibles).
