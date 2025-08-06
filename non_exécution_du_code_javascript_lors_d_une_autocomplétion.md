# Non exécution du code javascript lors d'une autocomplétion

**URL:** https://community.simplicite.io/t/5242

## Question
Bonjour,

Je suis entrain de développer un code javascript pour faire de l'autocomplétion de champs à partir d'une liste de suggestion. Le code a été testé et fonctionne dans un cas simple, cependant le javascript est appelé par un objet métier qui est lui même imbriqué dans un autre objet métier. 
La partie concernée se compose d'un objet métier PMFP, et incorpore dans son template l'objet métier Formation. 

Pour mieux visualiser je poste le template et un shéma d'expliquation : 

![Shéma obj métier|690x385](upload://55efpvbp0nMlMFLEBhTnANvYAl0.png)

Le code JS est identique ( mis à part les variables adaptées au template/objetmétier). Les champs contenant une liste de suggestion s'affichent correctement. Cependant la récupération et l'affectation de ces valeurs dans les champs visés par l’autocomplétion ne fonctionnent pas. 
 Le Javascript associé à mon objet métier ne s’exécute pas comme il devrait et ne rentre pas dans la boucle concernant le changement de valeur d'un champ.

![template PMFP-formation|690x299](upload://zYsh8gnTUpLtQTIfr1JdHHBDwxX.png)

**Code js :**
```
(function(ui) {
	if (!ui) return;
	var app = ui.getAjax();
	// Hook called by each object instance
	Simplicite.UI.hooks.LadFormations = function(o, cbk) {
		try {
			console.log("LadFormations hooks loading...");
			var p = o.locals.ui;
			if (p && o.isMainInstance()) {
				p.form.onload = function(ctn, obj) {
					//Le champ ville contient le code postal et la ville
					var ville = ui.getUIField(ctn, obj, "ladFormationsVilleOrganisme");
	                var cp = ui.getUIField(ctn, obj, "ladFormationsCodePostalOrganisme");
					$('#field_ladFormationsCodePostalOrganisme').prop('disabled', true);
					console.log("Avancée 1");
	                ville.ui.on("change mousemove keyup input select click", function() { // ne rentre pas dans la fonction
	                console.log("blocage dans l'auto complétion");
	                	var valVille = ville.ui.val();
	                	if(valVille.indexOf(' ')>0){
	                		ville.ui.val(valVille.substring(6));
	                		cp.ui.val(valVille.substring(0.5));
	                		$('#field_ladFormationsCodePostalOrganisme').val(valVille.substring(0,5));
	                		// on récupère les 5 premières valeurs de ville, qui équivaut au cp
	                    	ui.getUIField(ctn, obj, "ladFormationsCodePostalOrganisme").setValue(valVille.substring(0,5)); 
	            		}
	                }); 
	                	//...
				};
			}
		}
		catch(e) {
			app.error("Error in Simplicite.UI.hooks.LadFormations: " + e.message);
			console.log("Erreur : ", e.message);
		}
		finally {
			console.log("LadFormations hooks loaded.");
			cbk && cbk(); // final callback
		}
	};
})(window.$ui);

```
**Console**
![console|399x139](upload://hWv3vKpjvirPNbXpvf9kEc5JcEL.png)

Est ce que le problème vient de l’imbrication d'un obj métier dans un autre ?
Merci

## Answer
[quote="ClementRudelle, post:1, topic:5242"]
`var ville = ui.getUIField(ctn, obj, "ladFormationsVilleOrganisme");`
[/quote]

En fait le verbe getUIField permet déjà de sélectionner un champ incorporé, la signature complete est la suivante :

`$ui.getUIField(ctn, obj, field, index, silent)`

- dans le cas d'un attribut simple de l'objet sur son formulaire, il n'y pas besoin de l'index.
- dans le cas d'un liste en édition (il y N fois l'input), index = le row_id de chaque ligne
- dans le cas d'un champ action, index = le nom de l'action
- dans le cas d'un object inliné par relation 1,1, index = c'est le nom de la foreign-key

votre code doit donc tester si le formulaire est inliné, pour spécifier de quel attribut inliné on parle. Le onload reçoit également tous les paramètres contextuel de la liste :

```javascript
p.form.onload = function(ctn, obj, params) {
  let ville = ui.getUIField(ctn, obj, "ladFormationsVilleOrganisme", params.inline ? "fkParcours" : null);
  if (!ville.ui.input.length)
     console.log("input not found");
  // ...
}
```

"fkParcours" étant à remplacer par le nom du champ qui joint la formation au parcours père.

On va tout de même revoir Simplicité pour faire une recherche "large" sans avoir à spécifier l'index, mais c'est important à connaitre en cas d'ambiguïté / 2 fois le même champs dans votre formulaire.
