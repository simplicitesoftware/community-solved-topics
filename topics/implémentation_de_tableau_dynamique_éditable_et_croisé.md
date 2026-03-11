# Implémentation de tableau dynamique, éditable et croisé

**URL:** https://community.simplicite.io/t/4952

## Question
Bonjour,
nous aurions besoin d'implémenter une saisie particulière de montant avec 2 filtres.
Sur un dossier il y a un département rattaché ce qui fait qu'il y a un certain nombre de financements possibles. C'est à croisé avec la filière choisi qui a également un certain nombre de poste budgétaires.

Le nombre de colonnes et de lignes sont configurés et connus mais ils sont variables.

L'agent saisie des montants (en vert) dans les 2 exemples sur les données qui sont saisissables car possible sur le financeur et la filière choisi.
Exemples :
![image|690x189](upload://lObNq1C3wqNpeSfegvDVmhQGviD.png)

Je ne vois pas trop comment réaliser ce genre de besoin. Le tableau dynamique ne permet pas la saisie ni le calcul de somme, un objet métier sous forme de liste aurait pu répondre en parti au besoin mais le nombre de colonne est variable. Entre 5 et 30 colonnes de financeur
Merci pour vos retours.
Thierry Le Corre

## Answer
Tu peux facilement répondre à ce besoin avec le pattern expliqué dans ma réponse précédente. L'admin et l'agent auront juste des droits différents vis-à-vis de l'objet lié. CRUD pour l'un et Read/Update pour l'autre.
