# Travailler avec git sur un même module sur plusieurs branches

**URL:** https://community.simplicite.io/t/11524

## Question
Bonjour,

J'ai des difficultés à travailler à plusieurs avec git sur un même module sur plusieurs branches
Imaginons que 2 personnes travaillent sur le même module et chaque personne est sur sa branche. Si un objet métier est crée sur la branche A et un autre objet métier est crée sur la branche B quel est le meilleur moyen de merge les branches pour avoir les 2 objets sur la branche A sans conflits ? 

Car le problème que j'ai est que lorsque je merge la branche B dans la branche A, le fichier openapi.yml a plein de conflits difficiles à résoudre car le fichier est complètement désordonné. Il faut donc tout refaire à la main et copier coller les blocs correspondants à chaque objet métier ce qui est très fastidieux. Existe-il un moyen efficace de merge et d'empêcher ou fix les conflits dans les fichiers .yml ?

Merci d’avance pour votre aide.

## Answer
[quote="Gwagju, post:4, topic:11524"]
Ces fichiers peuvent ils être donc mis dans le gitignore ? Si non, pourriez vous détailler exactement la logique à suivre pour réussir à merge (notamment le “mergez attentivement la partie configuration&code”) sans problèmes?
[/quote]

Les fichiers yaml ne font pas partie de la configuration ni du code (dossiers `configuration`, `data`, `docs`, `files`, `resources`, `src`, `test`). Il n'est cependant pas recommendable de les mettre dans le gitignore, car les modifications faites par Simplicité sur ces fichiers seront alors ignorées.

1. comparaison & merge de la configuration et du code & conservation aléatoire de l'une des deux versions yaml
2. import (ou push) dans une instance Simplicité
3. export (ou commit) depuis l'instance Simplicité -> cet export contiendra le yaml à jour

Si le (1) n'est pas clair, c'est probablement qu'il vous faut un peu de formation sur les formats d'export et les techniques de merge.
