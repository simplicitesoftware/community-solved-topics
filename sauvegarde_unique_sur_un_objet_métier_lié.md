# Sauvegarde unique sur un objet métier lié

**URL:** https://community.simplicite.io/t/4972

## Question
Bonjour,

Je n'arrive pas à sauvegarder les données de l'objet souhait orientation qu'une seule fois.
Une fois les données saisies et enregistrer une fois lorsque je modifie une donnée elle est réinitialisé avec la première valeur saisie.
Je vous joins une copie extraite des données en jeu.
![image|690x367](upload://gKF6lRjNr4vvBCXS5Su4KcSOf7X.png)
Le lien entre le dossier pmfp et l'objet souhait/orientation est un lien de ce type
![image|690x356](upload://3EFxtHqG21EDqIsf0AXcSo4ZEVj.png)

Nous affichons les données d'un dossier PMFP dans un onglet.
Ensuite sur une action le dossier change d'état et passe à un état (favorable) qui affiche l'onglet souhait/orientation.
Je peux saisir l'onglet et enregistrer.
Ensuite si je veux modifié une donnée l'enregistrement ne fait rien comme s'il y avait un rechargement de l'ancienne donnée.
L'utilisateur qui utilise ces objets (dossier PMFP et souhait orientation) à des droits CRU.
Tous les utilisateurs ont des droits CRUD sur l'objet parent le dossier.

Est ce que vous pourriez m'aider sur une piste ?

Cordialement
Thierry

## Answer
Je viens de trouver pourquoi ça ne fonctionnait pas. Il faut que les attributs de ton objet `LadSouhaitOrientation` soient modifiables "Partout" (sauf pour l'id et autres champs calculés).
