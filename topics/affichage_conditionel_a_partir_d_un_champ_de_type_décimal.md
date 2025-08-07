# Affichage conditionel a partir d'un champ de type Décimal

**URL:** https://community.simplicite.io/t/3022

## Question
Bonjour,

J'ai une contrainte qui permet d'afficher ou non les deux champs de droite si le montant est superieur à 0 et les cacher sinon.
![Screenshot_89|690x63](upload://ktxMg0ipvaYfHzjbzICFOmJdlGY.png) 

Lorsque je saisi 50, le champ est transformé en 50,00; les deux champs de droite restent cachée alors qu'il devraient s'afficher. Si je saisie 50 de nouveau, cette fois il s'affichent bien.
De même que lorsque je saisi 0, il restent affiché, mais si je saisi de nouveau 0, il sont bien cachés. 

Est-ce qu'il y a un problème avec le reformatage en décimal ou bien est-ce la méthode de mes impacts qui est mal codée ?

Voila les log en fonction des saisies:
Saisie 1 : 50, log: null
Saisie 2 : 50, log: 50
Saisie 3 : 0, log: 50
Saisie 3 : 0, log: 0


```
(function(){  
	var montant = [VALUE:namExaMontant];
	console.log("montant "+ montant);
	if(montant > 0){
	return true;
	}else{
	return false;
	}
})()
```

## Answer
[quote="JeanMichelC, post:8, topic:3022"]
le script est déclenché 2 fois pour chaque changement
[/quote]

[quote="nathalie, post:7, topic:3022"]
`field.ui.on("input change", function() {...`
[/quote]

- input = trigger à chaque caractère saisi
- change = quand on sort du champ (enter, tab, blur...)

Donc forcement quand on tape 5 + enter ou tab, ça déclenche 1 "input" et 1 "change".
C'est le fonctionnement nominal d'un champ input.
Mettez l'un l'autre suivant votre besoin mais pas les 2 évènements.

Une contrainte se déclenche qu'au "change". Donc si le besoin est de déclencher un trigger à chaque frappe clavier, il faut donc coder comme l'indique @nathalie et utiliser "input" ou "keyup".
