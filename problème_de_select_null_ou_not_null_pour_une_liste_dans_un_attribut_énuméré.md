# Problème de Select (null) ou (not null) pour une liste dans un attribut énuméré

**URL:** https://community.simplicite.io/t/9272

## Question
J’ai reproduit le pb sur Démo en rendant l’attribut demoOrdStatus non obligatoire :
On peut sélectionner les autres valeurs mais pas les (null) ou (not null)
![image|690x429](upload://pkTP7xSCj8bUi7zYlolvdi6gY8Q.png)


Merci d'avance pour votre aide.

[Platform]
Status=OK
Version=6.1.18
BuiltOn=2024-12-17 12:35

## Answer
Bonjour,

Merci pour ton retour, effectivement le `change` s'annule pour ces 2 checkbox un peu à part.
On va corriger en 6.1, ça ne se reproduit pas en 5.3.
