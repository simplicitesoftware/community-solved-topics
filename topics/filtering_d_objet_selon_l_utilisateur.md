# Filtering d'objet selon l'utilisateur

**URL:** https://community.simplicite.io/t/12233

## Question
Bonjour à tous,

Je travaille sur l'implémentation d'un système de filtrage pour un objet que j'appelle ObjetAProteger. Voici ma structure :

ObjetAProteger : L'objet principal que je souhaite protéger/filtrer.
Filtre : Un objet qui référence ObjetAProteger 
LiaisonUtilisateurFiltre : Une table de jointure pour établir une relation N-N entre les utilisateurs et les filtres.

Mon objectif est d'implémenter un setSearchSpec dans la méthode postLoad pour :

Vérifier si un filtre a été créé pour l'ObjetAProteger.
Si un filtre existe, vérifier que l'utilisateur actuel est bien lié à ce filtre.
Si les deux conditions sont remplies, l'objet s'affiche.

J'ai juste vu le paragraphe Filtering dans la docs mais je ne comprends pas comment l'appliquer à mon cas. Avez-vous une doc plus détaillés à ce sujet ?

merci

## Answer
Le fait de mettre le userid rend le filtre dynamique (fonction de l'utilisateur qui accède à la donnée). 
La case Filtre contient une syntaxe SQL uniquement. Vous avez un exemple dans le tutoriel, un filtre est positionné sur un objet hérité de  TrnProduct. https://docs.simplicite.io/tutorial/enhancing/inheritance
