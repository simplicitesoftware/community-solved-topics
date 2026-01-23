# Objet parent non renseigné pour un objet inliné

**URL:** https://community.simplicite.io/t/11354

## Question
### Request description

Bonjour,

J'ai un souci dans un hook avec un objet inliné : au premier passage dans form.onload, le parent de mon objet inliné est null. Il est bien renseigné ensuite.
Ce n'est pas urgent car j'ai un contournement.

Merci d'avance pour votre aide !
Emmanuelle

### Steps to reproduce

- Avoir un objet A avec un lien vers un objet B en inliné
- Mettre un point d'arrêt dans le form.onload de l'objet B
- Afficher le form de A
- dans onload, B.parent est null
- faire un reload sur A
- dans onload, B.parent est bien A

J'ai fait le test sur un objet en liste non inliné et on a bien le parent dans le list.onload dès le premier passage.
Dans le front, je vois que B a bien son parent jusqu'au passage dans ```this.displayForm = function(ctn, obj, rowId, options, cbk)``` puis le perd au moment du``` ui.getNavObject```.

![image|690x172](upload://DtehE3ClGbDv7DUNQnYibVqBhM.png)
*Ici obj.parent = A, o.parent = null*

### Technical information

[details="Instance /health"]
[Platform]
Status=OK
Version=6.2.19
BuiltOn=2025-12-05 11:56
[/details]

## Answer
Dans le cas d'un objet inliné, les paramètres du `displayForm` reçoivent un `inline` avec toutes les infos contextuelles :

```js
p.inline = {
	object: (panel/child object),
	metadata: (panel object).metadata,
	parent: (parent object),
	link: (link definition),
	mandatory: link.minOccurs > 0, // 0,1=optional or 1,1=mandatory
	count: 0
};
```

Tu dois pouvoir y accéder dans le hook `form.onload(ctn, obj, p)`.

Nous allons copier le `parent` dans l'objet directement, pour le cas d'un objet inliné uniquement car en soit un objet main n'est pas sensé avoir un parent, c'est réservé aux listes filles/panel. Mais comme indiqué un objet inliné est hybride.
