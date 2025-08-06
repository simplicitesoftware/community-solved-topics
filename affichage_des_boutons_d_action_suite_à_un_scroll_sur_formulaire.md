# Affichage des boutons d'action suite à un scroll sur formulaire

**URL:** https://community.simplicite.io/t/5097

## Question
Bonjour,

Peut-on forcer l'affichage des boutons d'actions dans la barre des actions lors d'un scroll vers le bas
Il n y a que les boutons de transition d'état qui sont affichés.

![image|690x107](upload://g4XIslF2dZd1VIhiGNyQ8NelRcT.png)

Simplicité version 5.2.11

## Answer
Bonjour, 

Tu peux ajouter du css à l'objet métier pour afficher ces boutons dans la floating bar:

```css
.floating-bar{
	[data-action="MyAction"]{
		display: inline !important;
	}
}
```
