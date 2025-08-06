# Erreur à l'ouverture d'un modèle par le Modeler

**URL:** https://community.simplicite.io/t/4039

## Question
Bonjour,

Sur un de mes environnements, à l'ouverture d'un modèle j'ai l'erreur suivante


```
ui-bundle.js?_=97272cb9362c8966378105679b80fa488568a5e1:1220 Uncaught DOMException: Blocked a frame with origin "https://ear-int.k8s-stage.grouperci.com" from accessing a cross-origin frame.
    at Simplicite.UI.Engine.getTop (https://ear-int.k8s-stage.grouperci.com/scripts/ui/ui-bundle.js?_=97272cb9362c8966378105679b80fa488568a5e1:1220:40)
    at new Simplicite.Diagram.Modeler (https://ear-int.k8s-stage.grouperci.com/scripts/ui/diagram-bundle.js?_=97b6be4244f497861783f43672389cac601d115d_20211027121959:34:294)
    at Simplicite.UI.Engine.init (https://ear-int.k8s-stage.grouperci.com/scripts/ui/diagram-bundle.js?_=97b6be4244f497861783f43672389cac601d115d_20211027121959:4:104)
    at Object.<anonymous> (https://ear-int.k8s-stage.grouperci.com/scripts/ui/ui-bundle.js?_=97272cb9362c8966378105679b80fa488568a5e1:524:395)
    at c (https://ear-int.k8s-stage.grouperci.com/scripts/jquery/jquery.js:2:27742)
    at Object.fireWith [as resolveWith] (https://ear-int.k8s-stage.grouperci.com/scripts/jquery/jquery.js:2:28487)
    at l (https://ear-int.k8s-stage.grouperci.com/scripts/jquery/jquery.js:2:78789)
    at HTMLScriptElement.i (https://ear-int.k8s-stage.grouperci.com/scripts/jquery/jquery.js:2:82198)
    at HTMLScriptElement.dispatch (https://ear-int.k8s-stage.grouperci.com/scripts/jquery/jquery.js:2:42571)
    at HTMLScriptElement.v.handle (https://ear-int.k8s-stage.grouperci.com/scripts/jquery/jquery.js:2:40572)
```

Pouvez-vous m'aider à voir d'où vient le problème ?

Mon code


```
			modSearch.search(function(listSearch) {
				
				//If diagram exists opening it
				if (listSearch && listSearch.length) {
				    var modelId = listSearch[0].row_id;
				    var mod = app.getBusinessObject("Model", "tmp_ajax_Model");
				    
				    mod.get(
				    	function() {
						// instanciate in silent mode
							$ui.diagram.open(modelId, { svg:true, hidden:true }, updateDiagram);
						}, 
						modelId, 
						{inlineDocs: true}
						);
				    
				}
  				//Else create it
				else 
				{
					$ui.diagram.create("RCIBAppScope", name, {
						hidden: true, // hide the modeler
						nodes: firstNodes,  // nodes to insert
						fetch: false,   // then fetch related
						module: "RCIB"
					},
					function(diagram) {
						placeNodes(diagram);

					
					});
				}
			},{
			  mod_name: name
			});
```

/health

> Version=4.0.P25
> BuiltOn=2021-10-27 23:17 (revision 97b6be4244f497861783f43672389cac601d115d)

Merci d'avance pour votre aide !
Emmanuelle

## Answer
Si vous n'avez rien changé à la façon d'ouvrir l'application Simplicité (au travers d'un window.open depuis un portail ou autre encapsulation type iframe depuis un autre domaine), cette exception doit être liée a un renforcement de sécurité de votre navigateur ou des changements sur vos domaines.

Pour parer à toute éventualité ou contraintes techniques, on a renforcé le code de la méthode `getTop` pour ne regarder que les fenêtres parentes accessibles. Ce sera livré au prochain build de la maintenance 4.0.P25.
