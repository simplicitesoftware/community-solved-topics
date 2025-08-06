# Ability to rename table/column

**URL:** https://community.simplicite.io/t/6136

## Question
### Request description
Bonjour, 
Au sein de la documentation pour la version 5.2 de Simplicité, il est noté qu'il y a une possibilité de renommer la table/colonne lors de l'installation d'un module. Je voulais savoir si cela implique une modification de la base de données ? 

Merci d'avance

## Answer
Bonjour et bienvenue @OumamaK !

L'évolution que vous citez concerne la capacité de Simplicité à suivre correctement les changements de **noms fonctionnels** d'objet et d'attribut. Ça n'implique pas de modification de la BDD, à moins que vous ne changiez également le **nom physique** de l'objet ou de l'attribut. Comme on change en général le nom fonctionnel et le nom physique, Simplicité fait les changements nécessaires en base. Ça a justement été mis en place pour faciliter les changements de noms fonctionnels sans prévoir d'opérations manuelles de reprises de données.


[details="pour rappel, la section de la release note"]

![Simplicité®_5_releasenote_releasenote-5_2|690x429](upload://eTFiOdVOkYHbLINEz4ApieAkHv2.jpeg)
[/details]
