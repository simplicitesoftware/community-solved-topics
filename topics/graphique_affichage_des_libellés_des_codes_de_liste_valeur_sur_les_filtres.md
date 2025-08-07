# Graphique : affichage des libellés des codes de liste valeur sur les filtres

**URL:** https://community.simplicite.io/t/3053

## Question
Bonjour,

Dans un graphique, est-il possible d'afficher le libellé et non pas le code de la liste de valeur (attribut qui filtre le graphique)

Exemple :
![image|690x332](upload://zQiQCJRWlhVPfXlLrxhRR4wLHoM.png) 

* ACT = Action
* INI = Initial

Simplicité version : 4.0 patch level P25
Built on 2021-03-24 22:34 (revision c1e2e9af93a82039fab2a2ba7f81bab2f508fa01)

## Answer
Bonjour,

Les graphiques Graph sont de la legacy V3 et deprecated en V4 car leur calcul et affichage est trop limité, on utilise désormais des TC pour fabriquer des graphiques issus des axes. 

En V5 les vieux graphiques sont totalement supprimés, au profit des graphiques d'un TC qui offrent beaucoup plus d'options : 

- Affichage du libellé et non du code, enum trié pas code, ordre de liste ou libellé
- Possibilité d'utiliser un champ calculé non persistant (agrégation en java et pas en base)
- Axe X typé catégorie / date / décimal
- 2 axes Y possibles pour y placer ses axes valeurs
- Echelle logarithmique, gestion des unités...

Via l'éditeur de Vue on peut insérer un TC en n'affichant que son graphique à la place des anciens Graph.
