# Perte d'information suite à resize de la fenêtre du navigateur et clic sur bouton Quitter

**URL:** https://community.simplicite.io/t/3206

## Question
Bonjour,

Je lance la création d'un enregistrement sur un objet, je renseigne des données. Je resize la fenêtre du navigateur et je clique sur le bouton Quitter. Les valeurs saisies sont perdues.

Est-ce un comportement normal de la plateforme ? 

Si je fais la même opération et que je clique sur le bouton "Annuler" les valeurs sont bien présentes.

Simplicité 4.0
Built on 2021-04-20 18:59 (revision 6c434edfd07c36dbb032b41a6080e5be255c391d)

## Answer
Le popup "save before quit" fonctionne comme ceci :

- Il est déclenché quand un composant cherche à décharger le container dans lequel il y a eu une modification (comme un hasChanged dans l'objet)
- Le bouton "Enregistrer" lance un trigger "save" et ne quitte pas si une erreur est remontée, sinon il charge le nouveau contenu (les éventuels info/warning back sont affichés en popup)
- Le bouton "Quitter" ferme sans sauvegarder avant de recharger le nouveau contenu
- "Annuler" reste sur le formulaire sans rien faire (annule le nouveau contenu qui est demandé)

Quand on "resize" la fenêtre, si on franchit un seuil de dimension entre les tailles desktop | tablet | mobile, l'écran doit se redessiner complètement via un nouveau displayForm.

Dans votre cas, il faut faire Annuler pour ne surtout rien changer. Mais au risque d'avoir un affichage pourri si l'écran devient trop petit.

Il est conseillé de sauvegarder son travail avant de changer de taille d'écran. On ne peut pas tout avoir.
