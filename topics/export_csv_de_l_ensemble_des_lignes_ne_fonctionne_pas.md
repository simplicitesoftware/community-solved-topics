# Export CSV de l'ensemble des lignes ne fonctionne pas

**URL:** https://community.simplicite.io/t/3806

## Question
Bonjour,

Sur un affichage en liste, sans rien cocher, je fais un export CSV. Le bouton d'export indique bien 357 éléments mais dans mon fichier CSV je n'ai que la première ligne.

![image|690x243](upload://AlKZdg8GOHP7nO5JFpcegYAUod3.png)
![image|480x183](upload://9jL6g1LOkJTArNAPyYFxv1p0YjR.png)

Je recommence l'opération en choisissant Select all, mais j'obtiens le même résultat, seulement la première ligne.

Comment procéder pour exporter toutes les lignes ?

Merci d'avance
Emmanuelle

> Version=4.0.P25
> BuiltOn=2021-08-31 22:38 (revision 97272cb9362c8966378105679b80fa488568a5e1)

## Answer
Les appels asynchrones pour charger les listes liées (en pillbox) forcent un filtre sur une ligne à la fois (par appliquer d'éventuelles règles sur les search-specs du link pour remplacer des champs en fonction du parent). Et il n'y a pas de méthode finale à tous ces appels asynchrones (genre promise) pour retirer le filtre sur le row_id de l'instance.

Un `getRowIdField().resetFilter()` sera ajouté dans les exports de liste pour gérer ce cas particulier, en attendant, il faut le faire dans le hook `preExport`.
