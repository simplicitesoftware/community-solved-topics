# Automatisation de tâches, modules sur git

**URL:** https://community.simplicite.io/t/2987

## Question
Bonjour,

Est-il possible, avec Simplicité V5, d'avoir un module hébergé sur git, et qu'au moment ou Simplicité essais de récupérer le contenu du module (via un pull), un script s'exécute pour traiter les diverses sources du module.
Par exemple, j'ai un dépôt git qui contient un style fait avec Sass, pour une charte graphique. J'ai un module contenant tout l'aspect graphique de mon application (logos, styles (au format Sass)*, ...). 

\* Les styles sont un submodule git du dépôt du module Simplicité

J'aimerais pouvoir compiler lors du pull le Sass en .css afin que mon module l'utilise pour appliquer mon style à mon application. J'avais donc pensé à exécuter un script une fois le dépôt pull. Script qui traiterait mon fichier en utilisant le compilateur Sass (disponible via npm, NodeJS).

(Si jamais quelque chose n'est pas clair, dites le moi)

Merci d'avance !

## Answer
Hello, petit retour

On a décidé de retravailler le style additionnel. Il nous avait été fourni par une autre équipe, je n'étais pas encore arrivé à la Région à ce moment. Je soupçonne qu'on nous ai fourni le style entier généré par simplicité et non un style additionnel, expliquant alors son volume. J'ai retravaillé le tout en Less, ça tiens maintenant sur moins de 100 lignes comme tu me l'avais dit, en partant du thème Light.

Concernant, Sass, ce n'est donc pas la peine de l'intégrer à SImplicité, en plus que le projet de compilateur n'a pas l'air très fiable. 
(ps: je ne savais pas que Simplicité permettait d'utiliser Less au moment de mon premier choix)

Merci de ton aide dans tous les cas.
