# Affichage de la loupe sur recherche par parent N+2

**URL:** https://community.simplicite.io/t/3427

## Question
Bonjour,
![image|690x122](upload://1dEC8c5iGvGrDWixa4dVyq45LPm.png)

De ce que je comprends, on a une loupe a coté de Code département car il s'agit de l'objet père direct. Mais est-il possible également d'avoir la possibilité de sélectionner une région de manière indépendante du département sachant que c'est le parent N+2? 

Merci d'avance.

## Answer
Après analyse, c'est fait dans l'autre sens, si on sélectionne un A, ça renseigne A et B et C, mais on ne peut pas chercher C seul (sauf à saisir dans le champ sans la loupe).

Ce besoin de lookup est bien au backlog, mais n'a pas été encore implémenté car il faut revoir le service back "populate" pour qu'il puisse être partiel (chercher et alimenter une FK non racine), ensuite ce ne sera pas un problème pour la UI d'ajouter une loupe. A suivre.

En attendant, il faut utiliser la loupe de A, puis la loupe de B dans le popup qui s'affiche.
