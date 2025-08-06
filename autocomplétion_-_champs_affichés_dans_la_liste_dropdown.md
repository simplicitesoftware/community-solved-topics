# Autocomplétion - Champs affichés dans la liste dropdown

**URL:** https://community.simplicite.io/t/5094

## Question
Bonjour,

Peut-on paramétrer les champs afficher dans la liste de l'autocomplétion ?
![image|269x193](upload://lgwlBMjR9VZQ9a4SzfQWY673WRM.png)

L'idée est d'avoir uniquement le libellé du fournisseur. Dans mon exemple :
* Fournisseur ALPHA
* Fournisseur BETA
* Fournisseur GAMMA

Simplicité version 5.2.11

## Answer
Bonjour,

Le popup d'auto-completion utilise une recherche sur la colonne ou l'objet via la table m_index.
- Si c'est un champ texte simple, ça fait un like sur la colonne
- Si c'est un objet lié (ce qui semble ton cas vue la loupe sur le champ), ça fait un like full-text dans m_index et ça affiche par défaut
   1) la clé fonctionnelle en gras = celle générée dans m_index et issue du hook **`getUserKeyLabel`** au moment du save
   2) et des champs affichés en liste non clés (tronqués) = issue du hook **`getUserKeyList`** qui par défaut concatène/tronque les champs visibles en liste et non clés

Autre hook utile **`postSearchIndex`** : résultats trouvés en fonction de la recherche, pour les modifier si besoin après "select" dans m_index. Typiquement pour retirer ou ajouter des résultat suivants des droits particuliers, ça pourrait aussi servir à changer les libellés.

Pour la completion sur un champ simple (pas un objet lié), je pense que c'est abordé dans ce post via le hook **`fieldCompletion`** :
https://community.simplicite.io/t/raffiner-la-liste-de-lauto-completion/4292

Pour répondre à ta question :
- il faut ajouter le hook getUserKeyList à l'objet lié pour la partie 2)
- et pour masquer la clé fonctionnelle tu peux ajouter du CSS pour cacher 1)
- ou plutôt revoir le hook getUserKeyLabel pour ne pas être le code "FOUn" mais le libellé "Fournisseur XXXX" et rebuilder l'index (m_index).
