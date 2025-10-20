# Liste vide si aucun code de liste lié sélectionnée

**URL:** https://community.simplicite.io/t/10594

## Question
### Description

Bonjour,

J’ai un cas d’usage où un attribut **Scope** (enum simple : *Importateur* / *Filiale*) est associé à un autre attribut **Pays de déploiement** (enum multiple).

En fonction de la valeur de **Scope**, une liste liée différente est utilisée :
![image|690x110, 75%](upload://xUOfYllcNroDsYqYvGA6XZa0kxa.png)


* Importateur → `LBC_LIST_COUNTRY_IMPORTER`
* Filiale → `LBC_LIST_COUNTRY_SUBSIDIARY`

Le problème est que si aucun périmètre n’est sélectionné, l’attribut **Pays de déploiement** est vide et affiche *« Aucun résultat trouvé » 
![image|690x272, 50%](upload://9KHJ4eDwbGhlAKM2H5lvLJJW5aK.png)

alors que la liste par defaut de cette attribut est la liste des pays global.
![image|556x500, 50%](upload://44zSjAdSlDApDR1S7ZjhFu0Z0Xd.png)



J’ai voulu essayer d’ajouter une liste liée pour la valeur vide (`empty` ou `null`), mais la configuration oblige à renseigner un code de valeur pour la liste liée, ce qui empêche de gérer le cas par défaut.

### Question

* Existe-t-il une solution native dans Simplicité pour définir une liste par défaut quand l’attribut maître (*scope/périmètre*) est vide ?
* Si non, est-ce prévu ou faut-il forcément passer par un hook (`preSearch`, `setList`, etc.) pour injecter une liste globale par défaut ?

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.2.15
BuiltOn=2025-08-15 11:39
Git=6.2/309efbdf46b217e3145711d1c47c3e5ad5459aa5
Encoding=UTF-8
EndpointIP=100.88.238.174
EndpointURL=http://lbc-77449-app-7ccc77779f-77wcx:8080
TimeZone=Europe/Paris
SystemDate=2025-09-02 15:46:17---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonjour,

Il faut rendre le champ "scope" obligatoire afin de forcer l'utilisateur à choisir une valeur.
Ensuite la liste liée sera correctement valorisée car contrainte par le scope. 

Si le scope est "facultatif" d'un point de vue métier, il faut le gérer par une valeur à part liée à la liste complète des pays que vous aviez définie : exemple *Importateur* / *Filiale* / *Tout pays* et laisser le scope obligatoire.

Ensuite en terme d'ergonomie, pour guider l'utilisateur dans la saisie:
- vous prouvez ajouter une contrainte front qui masque le champ "pays" tant que le "scope" est vide
- ou alors mettre une valeur par défaut au scope comme "Tout pays"

Il n'y a que pour une recherche que la liste liée propose toutes les valeurs possibles (par merge de tous les codes possibles) si l'enum parent est vide. Par contre en base/sur le formulaire avoir un code lié/contraint à un parent vide n'aurait pas sens.

Il faudrait pouvoir modéliser le cas métier : champ parent facultatif et vide => afficher une liste liée par défaut.
