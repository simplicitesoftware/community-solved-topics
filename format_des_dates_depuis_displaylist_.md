# Format des dates depuis DisplayList()

**URL:** https://community.simplicite.io/t/7550

## Question
### Peut-on revoir DisplayList() pour que les dates soient affichées au bon format ? 

J'affiche sur une page d'accueil différents objets externes, dont deux  qui affichent, ou non, sous conditions, des listes d'objet via la méthode ui.displayList().
Je m'aperçois que si on affiche dans une vue une liste via le template depuis Interface>Vue>(la vue)>Editer le template, et que l'on est un utilisateur français (avec les paramètres bien associés), alors les colonnes dates sont affichées après formatage en version francisée. Par contre, si on passe par un affichage d'objet externe, selon les mêmes conditions, alors le formatage ne se fait pas (cf. captures écrans de deux exemples : un depuis l'application sur laquelle on est actuellement et une reproduction du probème sur notre bac à sable avec le module Demo).

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1. Créer une vue
2. Afficher une recherche sur un objet (ex.CrbRhsDemandeListeAgent)
3. Afficher cette même liste via un objet externe. On a pour ce faire créer un objet externe avec notamment ce script Js : 

```
var CrbRhsAccueilAction = (function() {
	var app, responsive = typeof $ui !== "undefined", debug = false;

	function render(params) {
		app = app || (params.pub ? new Simplicite.Ajax(params.root, "api", "", "BIZCD1Oz") // External
				: new Simplicite.Ajax(params.root, "ui")); //Simplicite.Application); // Internal
		// données de l'agent loggué
		var login=$ui.getApp().getGrant().getLogin();
		// aides versées à l'agent pour N-1 et N
		let demande = app.getBusinessObject("CrbRhsDemandeListeAgent");
		let count = 0;
		let number;
		
		demande.search(function(list) {
			for(var i =0; i< list.length; i++){
				ddeTr = list[i];
				if(ddeTr.rhsDemandeAgent_fk__rhsAgentMatricule === login) {
					if(ddeTr.rhsDemandeStatut.equals("10ENCOURSCREA") || ddeTr.rhsDemandeStatut.equals("30ACOMPLETER")) {
						count++;
					}
				}
			number = count;
			}
			
		if(number > 0) {
			$("#CrbRhsAccueilAction .col-sm-3").css({ backgroundColor : "#E5121C"});
			if(number === 1) {
				$("#CrbRhsAccueilAction .title").append( number+" <br> demande");
			} else {
				$("#CrbRhsAccueilAction .title").append( number+" <br> demandes");
			}
			$("#CrbRhsAccueilAction .col-sm-9").append("<h3>En attente d'une action de votre part</h3><img class=\"warning\" src=\"resource?code=warning\" />");
			// Pour afficher les ddes qui necessitent action + si list des ddes ac actions > 0 => .css background rouge
			$ui.displayList("#CrbRhsAccueilAction .list", demande, {
				fixedFilters: {"rhsDemandeStatut": "10ENCOURSCREA ;30ACOMPLETER" , "rhsDemandeAgent_fk.rhsAgentMatricule" : login},
					 showNav: false, // nouvelle navigation
				});
			} else {
				$("#CrbRhsAccueilAction .col-sm-3").css({ backgroundColor : "#c7c7c7"});
				// vert commenté car proposition : gris //$("#CrbRhsAccueilAction .col-sm-3").css({ backgroundColor : "#57af57"});
				$("#CrbRhsAccueilAction .title").append("0 <br> demande");
				$("#CrbRhsAccueilAction .col-sm-9").append("<h3>Pas de demande en cours ou à compléter actuellement</h3>");
			}
		});
	}
	return { render: render };
})();
```
Tout n'est peut-être pas optimum par ailleurs dans ce code :sweat_smile: mais en tout état de cause, on a bien notre résultat (moins le bon formatage des dates) : 
![image|690x357](upload://yNbX3fVA1cmpD7rVJOSH6hCNRkZ.png)

Autre exemple avec le module Demo pour plus de clarté : 
![Exemple avec démo|690x373](upload://wY3muyQyvPGPf4rsLKq86ESPIX3.png)

Ma question est donc la suivante (après recherche dans la doc + le forum + google) : peut-on depuis la méthode displayList() (ou ailleurs) solutionner ce formatage de dates qui ne se fait pas ?

Vous remerciant par avance pour votre aide,
Cordialement, 
Caroline

### Technical information
Simplicité version5.3.26
Built on2024-01-17 18:40
Git info5.3/e677e6d52927d1cb8aca6330c82c5616dc62ca90
Database level5;P03;4aca705f0c03390774341693f64d5c3d
EncodingUTF-8 (system encoding UTF-8)
Time zoneEurope/Paris
OSLinux amd64 3.10.0-1062.9.1.el7.x86_64
ServerApache Tomcat/9.0.85 WEB
DatabaseMySQL 5.5.5-10.2.9-MariaDB-10.2.9+maria~stretch using BLOBs
JVM11.0.6 Oracle Corporation OpenJDK 64-Bit Server VM 11.0.6+10-LTS
Script enginerhino Rhino 1.7.13 2020 09 02
Additional libsApache POI, Docx4j, Apache Tika, JGit, Apache JClouds, Google APIs, Google APIs Firebase

## Answer
Non reproduit en 5.3, en ajoutant la liste des commandes dans un objet externe de vue, les dates sont correctement formatées :

![image|690x344](upload://lTms2V9cRzNv4ix8k5eoYuksjxM.png)

J'ai juste ajouté la liste des commandes dans l'objet externe `DemoCounters` dans une zone `mydiv1`

![image|689x404](upload://kVk7z75g0AzZvAStIg2thzvvUWg.png)

![image|690x349](upload://5tqVlfQSvR3Yn26vXCp5HttFGoy.png)



Quelques remarques sur votre code :

[quote="Caroline, post:1, topic:7550"]
`responsive = typeof $ui !== "undefined"`
[/quote]

La V5 est responsive, plus besoin de tester si on est encore sur la vielle UI.


[quote="Caroline, post:1, topic:7550"]
```
app = app || (params.pub ? new Simplicite.Ajax(params.root, "api", "", "BIZCD1Oz") // External
: new Simplicite.Ajax(params.root, "ui"));
...
let demande = app.getBusinessObject("CrbRhsDemandeListeAgent");
```
[/quote]

D'où vient votre objet et via quel droit/user ? 
car le format des dates dépend du User / "api" est en quelle langue ?
Votre "new app" ne doit pas avoir de grant chargé dans certains de vos usages.
il faut surement appeler le service qui charge le grant distant quand ce n'est pas local.

`app.getGrant({ web:true }).then(/* la suite du code qui utilise cette app et ses droits */)`


[quote="Caroline, post:1, topic:7550"]
```
$ui.displayList("#CrbRhsAccueilAction .list", demande, {
  fixedFilters: {
    "rhsDemandeStatut": "10ENCOURSCREA ;30ACOMPLETER" , 
    "rhsDemandeAgent_fk.rhsAgentMatricule" : login
  },
  showNav: false, // nouvelle navigation
});
```
[/quote]

Attention 
- à l'espace dans le filtre, pour un ENUM il faut mettre les codes séparés par des ";" sans espace
- il faut indiquer `nav:"new"` pour créer une nouvelle navigation ou `nav:"add"` pour l'empiler, si c'est juste une liste dans une vue il n'y a pas de nav à afficher
- en front, le nom logique d'un champ (full-input qui contient le chemin des FKs) utilise un double underscores `__` à la place des `.` (car en javascript le point est un accesseur). Le back se débrouille si on lui poste des `.` ou des `__`, mais pour plus de clarté front/back, il convient d'utiliser des `__` en front.

```javascript
$ui.displayList("#CrbRhsAccueilAction .list", demande, {
  fixedFilters: {
    rhsDemandeStatut: "10ENCOURSCREA;30ACOMPLETER" , 
    rhsDemandeAgent_fk__rhsAgentMatricule: login
  },
  showNav: false // pas de nav de la liste est dans une vue
});
```

Et enfin sur les icones :

[quote="Caroline, post:1, topic:7550"]
`$("#CrbRhsAccueilAction .col-sm-9").append("<h3>En attente d'une action de votre part</h3><img class=\"warning\" src=\"resource?code=warning\" />");`
[/quote]

Vous pouvez plutôt utiliser la méthode `$ui.view.icon(name, class)` qui permet d'utiliser les images ou les fonts awesome + bootstrap directement sur le front (`resource?code...` est une requete http).

Exemple : 

```javascript
$("#CrbRhsAccueilAction .col-sm-9")
  .append($("<h3>En attente d'une action de votre part</h3>")
    .append($ui.view.icon("fas/exclamation-triangle","icon").css("color","red"));
```

On peut récupérer le nom logique d'une icone via l'icon-picker (loupe sur le champ icone d'objet) :

![image|690x310](upload://p3XNnRCraENx0WGj1swkMgrPBkh.jpeg)
