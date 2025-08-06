# Parcourir les objets métiers pour récupérer un attribut

**URL:** https://community.simplicite.io/t/4507

## Question
Bonjour,

J'ai un MCD comme ceci :
![image|690x449](upload://uTluigzv7bKnM5FrgqzbN96EEnA.png)

* Une `assemblée générale` possède **UNE et UNE** seule `participation`
* Un `ordre du jour` possède **UNE et UNE** seule `assemblée générale`

Quand je créer mon ordre du jour je voudrais que dans mon formulaire soient affichées les informations importantes de l'`assemblée générale` lié (Date, Titre, et Participation).
J'ai créer une clef technique (`ddvOodAgId`) pour lier la table `ordre du jour` avec la table `assemblé générale`.

Grâce à cette clef, je peux récupérer la date et le titre de l'assemblée générale. Le problème, c'est que je n'arrive pas à récupérer automatiquement la participation car il faudrait lié 2 clefs techniques.

J'ai essayé une liaison virtuelle, mais cela ne donne pas le résultat voulu.

**Auriez-vous une solution pour récupérer le champ `ddvPartName` de la table participation depuis la table ordre du jour en passant par la table assemblé générale ?**

Voila le formulaire de création d'ordre du jour que je souhaite (les infos AG sont automatique car on créer un ordre du jour depuis une AG):
![image|690x154](upload://6YYqJcpd4c9hmxUN0fZXBdvAmNT.png)

Voici l'AG correspondante :
![image|690x330](upload://xf0hpY98cGDSiGvlkGxaUG9dsmj.png)

## Answer
Bonjour, 

Vous pouvez ramener le champ ddvPartName au niveau de l'objet Ordre du jour. Depuis le template editor de Ordre du jour vous devez avoir la liste des champs de l'objet Assemblée générale, il suffit de sélectionner partName dans cette liste pour l'afficher sur le formulaire de l'objet Ordre du Jour. 

La notion de champs ramenés est abordée dans la leçon Relations : https://docs2.simplicite.io/lesson/tutorial/configuration/relations

Cf également l'exemple de la Démo dans laquelle on affiche le nom du fournisseur du produit sur le formulaire d'une commande.
