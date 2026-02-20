# Questions sur l'apparence du Menu

**URL:** https://community.simplicite.io/t/11623

## Question
### Request description

Bonjour,
Après avoir crash-testé les objets inlinés, je m'attaque au paramétrage du Menu utilisateur à gauche, et j'ai quelques questions (pas urgentes) :
- comment fonctionne le paramètre MENU_STYLE ? J'ai essayé toutes les valeurs et je ne vois pas de différence
- comment fonctionne le paramètre user Default domain ? J'ai essayé de mettre quelques domaines mais ça ne les ouvre pas par défaut

Mon besoin est de déplier tous les sous menus de mon domaine à la connexion de l'utilisateur.

Merci d'avance pour vos réponses !
Emmanuelle

[Platform] Status=OK Version=6.3.4 BuiltOn=2026-02-16 12:31

## Answer
Bonjour Emmanuelle,

Le paramètre `MENU_STYLE` n'est plus supporté depuis l'utilisation d'une UI responsive (v4), le fonctionnement & l'apparence du menu sont maintenant uniformes :
- tout les éléments sont plié, et le style est en accordéon
- si il contient moins de 3 domaines, alors ils aparaissent deplié (pas leurs sous-menus)
- 1 seul élement par niveau est déplié en parallèle 
     - si j'ai X domaines je ne peux en ouvrir qu'un à la fois au clic (idem pour les sous-menus)

Pour tout ouvrir à la connexion, est possible d'ajouter du code dans le SCRIPT de la disposition  pour assigner les bonnes classes sur les éléments du menu dans le `ui.ready` :

```javascript
$(document).on("ui.ready", function() {
		console.log(">>> UI READY <<<");
		// customize UI here	
		$("ul.main-menu > li")
			.addClass("active");

		$("ul.main-menu > li > ul.sub-menu")
			.css("display","block");
		
		$("ul.main-menu > li > a.js-sub-menu-toggle")
			.attr("aria-expanded", "true"); // accessibility purposes
	});
```

> cela laissera les menus ouverts jusqu'au clic de l'utilisateur sur l'un d'eux (pas de soucis lors du clic dans un sous-menu), mais ne dégrade pas les fonctionnalités du menu (filtres, sous-menus dépliant, etc)

Pour garder tout ouvert de façon persistante il faut plutôt ajouter des styles annulant la logique active/display-block, cette fois dans le STYLE de la disposition :

```css
ul.main-menu > li,
ul.main-menu > li.active {
	& > ul.sub-menu {
		display: block !important;
	}
}
```

> cette option ne donne pas la classe "active" aux `<li>` du menu, ni l'attribut `aria-expanded=true` sur les `<a>`, mais ne dégrade pas les fonctionnalités du menu (filtres, sous-menus dépliant, etc)
> -> Pour palier à ces soucis, il est possible de combiner les deux approches !

J'espère que cela répond à ton besoin :grin:
