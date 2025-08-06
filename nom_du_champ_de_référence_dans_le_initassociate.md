# Nom du champ de référence dans le initAssociate

**URL:** https://community.simplicite.io/t/3441

## Question
Bonjour,

Y a-t-il un moyen de savoir par quel champ on entre dans un initAssociate ? (le nom de l'internal Id qui permet d'afficher le champ "loupe")
J'ai l'objet parent en paramètre mais c'est tout.

Or sur mon objet j'ai deux associations vers le même objet et je voudrais pouvoir appliquer un filtre selon l'association dont il s'agit.

Merci d'avance pour votre aide !
Emmanuelle

## Answer
Au temps pour moi je viens de trouver le getParentObjectRefField() dans la doc :-)
