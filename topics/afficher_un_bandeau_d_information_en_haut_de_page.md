# Afficher un bandeau d'information en haut de page

**URL:** https://community.simplicite.io/t/3338

## Question
Bonjour,

Je souhaite ajouter un bandeau d'information personnalisé en haut de mon formulaire.

Certains champs non obligatoires doivent être tout de même rempli à un moment du process pour répondre à un use case précis.
S'ils ne sont pas rempli, j'affiche ce bandeau d'information avec ces champs manquant.

Ce bandeau doit donc s'afficher dès l'ouverture du formulaire et non uniquement à l'update.

Avez-vous une solution à me proposer?

Merci par avance

## Answer
[quote="nathalie, post:3, topic:3338"]
`getContext().addMessage(this, "TEXT", getGrant());`
[/quote]

on peut aussi passer à la place de "TEXT" un Message.formatInfo ou Warning... en paramètre.
Chaque type de message a un affichage différent (rouge, jaune...)
ça évite de changer les styles CSS d'une erreur.
