# Enregistrer des données dans des champs en lecture seul d'un objectDB

**URL:** https://community.simplicite.io/t/7343

## Question
Bonjour,

Nous récupérons des données via un ObJectService et quand on les ajoute dans les champs de notre ObjectDB ils sont bien visibles mais à l'enregistrement, les champs devienne vide (voir CE).

Avez vous une solution à cette problématique ?

ObjectService
![image|690x160](upload://zMcKyg31sSzfPnHdHpNWoAakZh3.png)

Après sélection dans l'object service
![image|690x42](upload://co3zBR4OQe5aKRhVWslC2Lei7cl.png)

Après l'enregistrement des données
![image|690x44](upload://pbkLHHcYTH3RNxK7PiLQ4VIh2dc.png)

## Answer
Si les champs sont en lecture seule ils ne seront pas valorisés effectivement. 

Il faut les paramétrer modifiable et  ajouter un script front qui les met en readonly dans le onload de la page.
