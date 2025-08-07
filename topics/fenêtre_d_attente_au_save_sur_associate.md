# Fenêtre d'attente au Save sur Associate

**URL:** https://community.simplicite.io/t/9337

## Question
### Request description

Bonjour et meilleurs vœux à toute l'équipe,

J'ai l'impression que le popup d'attente (waitdlg avec la petite roue qui tourne) s'affiche **derrière** la fenêtre de sélection des champs N,N en cas d'association.
Cela nous crée des effets de bords car on a un traitement un peu long avec des utilisateurs qui cliquent plusieurs fois sur Save & Close.

Pour reproduire
- Associate avec une N,N qui a des champs autres que les clés
- Select
- Save and Close sur l'écran de saisie
-> la petite roue n'apparaît pas (ou alors derrière la fenêtre) et on peut cliquer plusieurs fois sur Save & Close

Merci d'avance pour votre aide,
Emmanuelle

[Platform]
Status=OK
Version=5.3.59
BuiltOn=2024-12-17 18:15

## Answer
Effectivement le showLoading est fait sur le formulaire parent et non le dialogue.
On va améliorer ça, voir retirer le focus du bouton save pour inhiber tout "re-ENTER" .

Ce sera livré en 5.3.61
