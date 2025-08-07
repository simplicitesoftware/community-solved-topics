# Intégration Lemon Learning

**URL:** https://community.simplicite.io/t/8834

## Question
Bonjour,
 
Nous souhaitons intégrer un outil d'assistant digital appelé "Lemon Learning" dans Simplicité v5.3.45. 
Le principe d'intégration est décrit ici: 
https://deployer.lemonlearning.fr/d%C3%A9ploiement/par-int%C3%A9gration-directe
 
Il consiste à 
- intégrer une css dans la balise body de chaque page de l'interface utilisateur
- intégrer une ligne javascript avant la balise </body> de chaque page de l'interface utilisateur
 
Comment pouvons nous intégrer ces lignes de code dans le ou les gabarits de pages Simplicité ?
NB: l'idéal serait de pouvoir gérer les gabarits dans un de nos modules.
 
Cordialement,

## Answer
Bonjour,

J'ai réalisé des tests d'intégration sans trop de soucis avec LemonLearning il y a deux ans, en me basant sur la documentation que vous évoquez ("Intégration directe").

Dans Simplicité, vous n'avez pas directement accès au HTML de la disposition pour intégrer tel que préconisé par Lemon. La stratégie recommandée est d'utiliser les hooks de la disposition par défaut de `/ui` qui s'appelle `responsive5`. 

Pour ce faire, naviguez vers la disposition en question (Interface > Disposition > `responsive5`) et éditez la ressource `SCRIPT` de cette disposition pour y intégrer le code suivant:

```javascript
/* Specific client script */
(function($) {
	$(document).on("ui.loaded", function() {
		$ui.loadCSS("https://static.lemonlearning.com/player/bundle.css");
		$ui.loadScript("https://static.lemonlearning.com/player/bundle.js");
	});
})(jQuery);

function LemonLearningReady (player) {
	player.start();
}
```

Veillez également à modifier la ressource pour qu'elle soit correctement intégrée à votre module.

![Simplicité|690x498](upload://ntLg0018fbKmWbBFM8VTk5bQpEi.jpeg)

Pour information, tout le reste du travail de test de cette solution a été réalisé à l'époque dans l'environnement Lemon.

Cdt,
