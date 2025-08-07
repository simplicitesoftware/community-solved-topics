# Valeur précédente retournée par ui.val dans le change

**URL:** https://community.simplicite.io/t/6259

## Question
### Request description

Bonjour, j'ai un souci sur un champ que j'essaie de mettre à jour dynamiquement en fonction d'un autre, en front sur l'interface.

J'ai fait un script JS qui a l'air similaire à cette solution : https://community.simplicite.io/t/pb-de-valarisation-dun-attribut-par-contrainte-dans-le-cas-dun-update/1424/4

```
// CrbPcaDossier front side hook
(function(ui) {
	if (!ui) return;
	var app = ui.getAjax();
	// Hook called by each object instance
	Simplicite.UI.hooks.CrbPcaDossier = function(o, cbk) {
		try {
			console.log("CrbPcaDossier hooks loading...");
			var p = o.locals.ui;
			if (p && o.isMainInstance()) {
				p.form.onload = function(ctn, obj, params) {
					var qpe = ui.getUIField(ctn, obj, "pcaDossierInstPartExt");
					var qpr = ui.getUIField(ctn, obj, "pcaDossierInstPartRegion");
					
					qpe.ui.on("change", function() {
						console.log("Valeur part ext : " +qpe.ui.val());
            			var valQpe=parseFloat(qpe.ui.val());
            			if (!isNaN(valQpe))
            				qpr.ui.val(100-valQpe);
					});
				};
			}
		} catch (e) {
			app.error("Error in Simplicite.UI.hooks.CrbPcaDossier: " + e.message);
		} finally {
			console.log("CrbPcaDossier hooks loaded.");
			cbk && cbk(); // final callback
		}
	};
})(window.$ui);
```
J'ai peut-être raté quelque chose mais ça ne fonctionne pas, j'obtiens la valeur précédente de mon champ qpe au lieu de celle qui vient d'être changée.

J'ai affiché qpe.ui.val() dans la console pour confirmer qu'il y avait bien décalage et pas juste un problème d'affichage, ici après avoir changé 50 en 30 :
![image|690x458](upload://8htpt9ieMqShPxPvGUyFwzioUr3.png)
->
![image|690x404](upload://ljI8A1Lg3217cCjDqbWf6PAWiOv.png)

Remettre immédiatement une nouvelle valeur retourne la valeur 30, et ainsi de suite.

Une idée de ce qui pourrait causer cela?
Merci

## Answer
Merci pour ton retour, j'ai enfin compris...

D'après ton debugger le champ est un big decimal, et la valeur utilisée est **bigdec** = "15.00" qui permet de stocker la valeur sans perte de précision sous forme de String (sinon en javascript on ne peut pas stocker plus que des float = double precision). 

Dans le cas d'un change cette variable n'est pas bien actualisée et du coup ça explique l'effet retard de cette variable en front. On va voir pour améliorer ça pour que la valeur bigdec s'actualise correctement à chaque "keyup" ou "input".

Par contre pourquoi utiliser un bigdecimal pour un champ %, un simple décimal 6,2 devrait convenir à votre besoin. 

Et sinon `pe.ui.input` est déjà un objet jQuery donc un tableau, donc en fait c'est `pe.ui.input[0].value` pour accéder à la valeur native de l'input.
