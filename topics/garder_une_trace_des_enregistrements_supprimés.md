# Garder une trace des enregistrements supprimés

**URL:** https://community.simplicite.io/t/10032

## Question
Bonjour,

J'ai activé le journal des modifications sur la table "mouvement" mais j'aimerai aussi avoir une trace des mouvements qui sont supprimés. Est-ce que c'est possible?

Merci

Fabrice

## Answer
Bonjour,

La suppression physique est par construction non persistante, tout ce qui est lié au record est supprimé en cascade ou la foreign-key remise à null. 

L'objet RedoLog (Menu exploitation Change logs / Journal des modifs) est conservé mais le lien vers le record est remis à vide. Il faut donc ouvrir la table des redolog pour voir qu'il a été supprimé (puisque qu'on ne peut plus ouvrir le formulaire du record supprimé et donc ses changelogs par jointure).

Pour conserver un historique de suppression "logique", il faut plutôt gérer cela par un champ état "supprimé" qui permet de filtrer/masquer la liste pour certains utilisateurs, mais peut rester accessible pour un profil admin.
