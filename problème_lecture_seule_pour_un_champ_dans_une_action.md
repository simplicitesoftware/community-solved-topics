# Problème lecture seule pour un champ dans une action

**URL:** https://community.simplicite.io/t/4481

## Question
Bonjour,

J'ai une action qui a un formulaire avec un champ. Le champ a l'intérieur de cette action est le même que le champ dans le formulaire général où on peut cliquer sur l'action.

Dans ce formulaire général, je peux modifier le champ, mais dans l'action, le champ est en lecture seule. Je précise que je n'ai aucune contrainte sur ce champ + le champ est en "`modifiable: partout`".
![image|690x328](upload://wTEaVvB4U5pXm1ILk2nDtb0Ivvs.png)

Sur cette capture d'écran, on voit bien que le champ dans le formulaire général est modifiable (il y a le petit calendrier à coté pour le prouver), mais dans l'action, on voit bien que le champ est en lecture seule.

**Une idée du problème ?**

![image|458x155](upload://jxPIUnI5Fe3TEvCIhDNss52AcNL.png)

## Answer
C'est normal : dans un formulaire de confirmation d'action, les attributs de l'objet sont présentés en lecture seule (l'idée est que s'ils sont là c'est juste "pour rappel" de la valeur courante de l'objet lié)

Ex dans l'action d'incrément de quantité dans la démo:
![image|690x368](upload://3EptBQOpfWs9FHRRCHT2QNWkkHb.png)

Bref, si vous voulez des attributs saisissables au niveau de l'action il faut créer des attributs ad hoc.
