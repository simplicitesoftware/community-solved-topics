# Objet inaccessible via script front, la méthode "search" ne ramène rien

**URL:** https://community.simplicite.io/t/3881

## Question
Bonjour,

J'ai un problème avec le script front ci-dessous, je n'arrive pas à accéder à un objet métier.
J'ai simplifié au maximum pour identifier le problème mais je ne trouve pas.


```
	function pushFirstNodes()
	{
		var appSearch = app.getBusinessObject("RciAppSub"), listAppSearch = [];
		
		console.log(appSearch);
		appSearch.search(function(listAppSearch) {
           //Je n'atteins pas cette partie du code
		},{

		});
	}
```
Par contre si je remplace RciAppSub par d'autres objets, le search les atteint bien.
Je ne vois pas de différence entre les paramétrages de mes objets métier.

Sauriez vous me donner des pistes pour identifier mon problème ?

Merci d'avance pour votre aide
Emmanuelle

/health
Version=4.0.P25
BuiltOn=2021-08-31 22:38 (revision 97272cb9362c8966378105679b80fa488568a5e1)

## Answer
Tout va bien, ce sont les paramètres d'appel qui ne sont pas bon dans ma réponse, le 2eme argument ce sont les filtres/tris, les autres paramètres sont ensuite :

```
appSearch.search(function(listAppSearch) {
			// success
		},{
			myField: "filter",
			order__otherField: -1
		},{
			error: function(err) {
				debugger;
				// err = {"type":"error","response":{"messages":
				// 	["Required search filter: ..."],"level":2}}
				console.error("error", err);
 			}
		});
```

Autres choses à savoir sur les filtres obligatoires : 
- le contrôle de filtre obligatoire n'est bloquant que pour les objets UI (comme l'instance the_ajax_xxx) sauf pour un panel (panel_ajax_xxx déjà filtré sur l'objet parent)
- donc pour requêter sans contrainte en front = il faut utiliser une instance tmp, comme par exemple :

```javascript
var appSearch = app.getBusinessObject("RciAppSub", "tmp_ajax_RciAppSub");
```
