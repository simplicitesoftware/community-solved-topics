# Appliquer un filtre dans champ type Enuméré d'une vue liste

**URL:** https://community.simplicite.io/t/5095

## Question
Bonjour,

J'ai un objet métier comportant 2 champs de type Enuméré : Délégation et Filière. Dans la vue liste de l'objet métier, j'applique un filtre sur la Délégation qui affiche les données associées en résultat.

J'aimerais pouvoir appliquer un 2e filtre, cette fois sur le champ Filière. Ce dernier dépend du choix saisi dans Délégation. Or, dans la recherche par liste, j'ai toutes les valeurs de Filière qui me sont proposées. Alors que je ne souhaite afficher que les valeurs possibles de Filière associées à la valeur de Délégation. cf Capture d'écran.

![LADOM-1040_filtre|641x500](upload://tSpsS6N9COJObYboMToesSEWh7x.png)

J'ai essayé avec initRefSelect, setSearchSpec mais aussi en jouant sur l'alimentation des items de la liste dans le postLoad ou preSearch (cf code ci-dessous). Comme Gérard....en vain. 

```
list.getAllItems().clear();
		
			for (String row[] : g.query("select distinct lad_ref_filiere_code, lad_ref_filiere_libelle from lad_ref_filiere order by lad_ref_filiere_libelle asc")) {
    			list.putItem(row[0], row[1], true);
			}
```

Pouvez-vous m'aider svp ?

En vous remerciant.

Bruno

## Answer
Donc si j'ai bien compris, ces énumérés sont saisis par un admin métier.
S'il y a des duplications il faut peut être revoir comment vous créez ces énumérés. Attention également à la suppression d'un élément de la liste de référence et la gestion des records qui utilisent une valeur supprimée. 

Comment gères-tu le filtre sur la liste des Filières selon ce qui est saisi dans Délégation au niveau de tes listes de références ? Est-ce que tu as modélisé un lien 1-N entre les deux listes ? 

D'un point de vue conception, pourquoi ne pas avoir utilisé un lien vers un objet métier plutôt que 2 énumérés ?
