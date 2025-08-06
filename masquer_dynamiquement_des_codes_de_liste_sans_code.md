# Masquer dynamiquement des codes de liste sans code

**URL:** https://community.simplicite.io/t/4621

## Question
Bonjour,

Est-il possible de masquer dynamiquement par paramétrage des codes de liste d'un champ enum en fonction de la valeur d'un autre champ.

J'ai vu qu'il existait dans les impacts une propriété d'attribut > liste de valeur, mais je ne vois pas comment l'utiliser.

Sinon puis-je utiliser les listes liées avec contrainte d'affichage en fonction de la valeur d'un autre champ. ?

Version : Simplicité version 4.0 patch level P25 Built on 2022-03-25 17:24

## Answer
Dans ce cas vous pouvez effectivement utiliser une contrainte avec un impact de agissant sur la propriété "Liste de valeurs" de votre énuméré cible et définir une Expression du style : `[VALUE:myField] == "toto" ? "LIST_IF_TRUE" : "LIST_IF_FALSE"`

Ce qui ne revient pas tout à fait à masquer des valeurs dans une liste mais plutôt remplacer la liste de valeurs par une autre selon une condition particulière.
