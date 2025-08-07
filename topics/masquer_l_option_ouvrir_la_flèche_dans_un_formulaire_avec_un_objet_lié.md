# Masquer l’option « Ouvrir » (la flèche) dans un formulaire avec un objet lié

**URL:** https://community.simplicite.io/t/4873

## Question
Bonjour,

Pourriez-vous me dire svp comment est-ce que je peux masquer le bouton « Ouvrir » (la flèche) d’un objet lié, suivant le profil de la personne connectée ? J’arrive à masquer la loupe avec une contrainte (fk modifiable uniquement si ADMIN), mais la flèche reste présente.

Le but étant que l’utilisateur ne puisse pas ouvrir l’objet lié dans un formulaire.

![image|690x158](upload://tXHzE1E2eSx2WmdUNJdPsGpqgnt.png)


![image|690x155](upload://yQn1UcRwmQuESuhAM1BG5afZRcX.png)



Merci d’avance pour votre retour.

Abed.

Status=OK
Version=5.2.3
BuiltOn=2022-05-10 18:31
Git=5.2/75384808e0fc7f992d50959bdc3fb75a79deac57
Encoding=UTF-8
EndpointIP=149.202.173.228
EndpointURL=http://e3m.simplicite.io:10118
TimeZone=Europe/Paris
SystemDate=2022-05-17 19:14:32

## Answer
Bonjour Abed.

La théorie:
* la loupe est présente si tu as le droit de modifier le champ
* la flèche est présente si tu as le droit de lire l'objet en mode formulaire et que tu as le droit de suivre le lien

Donc:
* Si l'objet n'est jamais accessible pour personne en mode formulaire: on peut utiliser la propriété **"Use form"** de l'objet référencé
* Si c'est juste le lien *depuis l'objet référençant* et *pour un groupe particulier*: comme il n'y a pas de contraintes pour modifier la propriété "use form", pas le choix, on passe en mode hook avec  [canFollowLink](https://docs.simplicite.io/5/javadoc/com/simplicite/util/ObjectCore.html#canFollowLink(com.simplicite.util.ObjectField)) (ça affectera aussi la capacité à cliquer sur les liens en liste)



[details="(Aussi possible en mode JS)"]
Si tu veux juste cacher le bouton sur ce formulaire, tu peux utiliser un petit JS sur l'objet référençant (rendre la flèche "hidden" dans le `form.onload` de ton objet):
```javascript
// I <3 boilerplate
(function(ui) {
	if (!ui) return;
	var app = ui.getAjax();
	// Hook called by each object instance
	Simplicite.UI.hooks.DemoProduct = function(o, cbk) {
		try {
			console.log("DemoProduct hooks loading...");
			var p = o.locals.ui;
			if (p) {
				p.form.onload = function(ctn, obj){
					// =========HIDE ARROW CONDITIONNALY===========
					if(app.getGrant().responsibilities.indexOf("ADMIN")==-1){
						var btn = $(".refopen_field_demoPrdSupId__demoSupCode");
						btn.css("visibility", "hidden");
						btn.css("width", "0");
						btn.css("margin", "0");
						btn.css("padding", "0");
					}
					// ====================
				}
			}
		}
		catch(e) {
			app.error("Error in Simplicite.UI.hooks.DemoProduct: " + e.message);
		}
		finally {
			console.log("DemoProduct hooks loaded.");
			cbk && cbk(); // final callback
		}
	};
})(window.$ui);
```
[/details]
