# Comment supprimer un lien entre 2 objets métier

**URL:** https://community.simplicite.io/t/3946

## Question
Bonjour,

Je découvre Simplicité à travers le tutoriel de formation.
J'ai créé un lien entre 2 objets métier, je n'arrive ni à le modifier ni à le supprimer ?

Avez-vous une idée de comment faire ?
![Simplicité-link|618x500](upload://d9viNsKHhnKzd2m2rxA4Y55cmks.jpeg)

## Answer
Un "lien" est en fait un attribut de type "ID technique" = une foreign key pour utiliser un vocabulaire de base de données.

Donc supprimer un lien = supprimer l'attribut en question (et ses attributs ramenés)
