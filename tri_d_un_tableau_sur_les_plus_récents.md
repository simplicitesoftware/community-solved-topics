# Tri d'un tableau sur les plus récents

**URL:** https://community.simplicite.io/t/3217

## Question
Bonjour,

Peut-on trier un tableau sur la date de dernière modification/création? Je veux afficher mes lignes de la plus récente à la plus ancienne ( peut-être agir sur la colonne UPDATED_DT?)

Je ne trouve pas de paramétrage natif permettant de genre de tri, ou peut-être ai-je mal regardé..

Merci d'avance.

Mahmoud.

## Answer
Merci pour vos réponses.

* J'ai ajouté un champ date et heure
* J'ai donné [DATETIME] en valeur par défaut
* Je mets à jour la date au postValidate pour gérer la mise à jour à l'update
* Paramétré -1 au tri

Ca fonctionne comme je le voulais. Merci à vous.

Mahmoud.
