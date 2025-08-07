# Problème au niveau de l'affichage d'un thème

**URL:** https://community.simplicite.io/t/6470

## Question
**Request description**
Bonjour,
Lorsque j'installe le thème "Etat" en version 5.3.2, l'affichage de ma page d'accueil n'est plus bon. Je ne peux accéder aux menu, ils ne sont pas visibles.

**Steps to reproduce**

1. J'ai installé le ThemeEtat
2. Je l'ai affecté à une vue en tant que page d'accueil
3. J'ai affecté cette vue à un groupe au niveau de l'habilitation

## Answer
Bonjour,

[quote="Amadou, post:1, topic:6470"]
J’ai affecté cette vue à un groupe au niveau de l’habilitation
[/quote]

Est ce que ce groupe a des droits d'accès aux domaines et aux objets du menu ?
Retirez le thème et regardez si le profil fonctionne sur un autre thème ou thème par défaut.

Vous devez avoir un problème de scope = 
- la vue doit activer certains groupes de droits (panel active groups)
- le user doit avoir ces responsabilités
