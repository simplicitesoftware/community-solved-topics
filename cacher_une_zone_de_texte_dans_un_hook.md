# Cacher une zone de texte dans un hook

**URL:** https://community.simplicite.io/t/3073

## Question
Bonjour,

est-ce possible de cacher une zone de texte au moment d'un hook tel que initCreate ?
Je n'ai pas vu dans la doc, de méthode permettant de récupérer une zone de texte par son code.

## Answer
Les zones de textes sont directement insérées dans le template, ça ne peut donc pas se contrôler via le paramétrage. Pour le contrôler au niveau du code back, il faudrait modifier le template HTML de la zone, ce qui est peu pratique...

Du coup l'idéal c'est un script JS pour contrôler ça (créer une ressource d'objet de type JS nommée "SCRIPT", éditer et ajouter ça dans le hook JS)

```javascript
p.form.onload = function(ctn, obj) {
	if(obj.isNew())
		$('div.text[data-text="CODEZONE"]').hide();
};
```

Pour information, pour ce genre de situations, on a plutôt tendance à utiliser les aides. En ouvrant la traduction de l'attribut, on trouve des options pour mettre des placeholders, des bulles d'aides en formulaire, en liste etc; et l'objet "Aide contextuelle" (lié à l'objet métier) peut permettre d'afficher des aides d'objet selon le contexte d'affichage.
