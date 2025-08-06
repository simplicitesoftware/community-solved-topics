# Bouton Associate inopérant en cas de clé double

**URL:** https://community.simplicite.io/t/5809

## Question
### Request description

Bonjour,

Pour un besoin client, j'ai paramétré un objet de lien "N,NN" c'est-à-dire qu'on associer à A, soit une instance de B, soit une instance de C via cet objet.
Dans le panel, j'ai bien deux actions Associate mais il ne se passe rien quand je clique dessus. En inspectant je vois qu'il y a des `<li>` mais pas de `<button>`, est-ce que ça expliquerait mon problème ? Ai-je mal paramétré mon lien ?

![image|475x322](upload://cW9eQoKwCvr437WvqsgvGUieMot.png)


Merci d'avance pour votre aide,
Emmanuelle


### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.28
BuiltOn=2023-01-20 16:43
```
[/details]

## Answer
J'ai créé un objet à 3 pates depuis A vers B ou C et je n'ai aucun soucis pour associer B ou C sur une V5.2 à jour.

L'objet NNN contient uniquement 3 foreign keys :
- 1 obligatoire et clé fonctionnelle, avec le lien vers A avec Associate = Visible
- Les 2 autres vers B et C en clé fonctionnelle mais facultative.


La UI affiche bien 2 actions d'association, puis propose de sélectionner des B ou C, puis les associe à A.

Bref ça fonctionne, votre modèle doit être un peu différent ou manquer des droits suffisants pour faire cette opération (droit de lecture sur B/C et de création sur la NNN).
