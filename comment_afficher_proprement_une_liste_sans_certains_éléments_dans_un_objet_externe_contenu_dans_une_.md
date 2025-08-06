# Comment afficher proprement une liste (sans certains éléments) dans un objet externe contenu dans une Homepage

**URL:** https://community.simplicite.io/t/7208

## Question
### Request description

Bonjour, 
J'ai une vue HOME qui contient plusieurs objets externes, dont un qui doit afficher de manière conditionnelle la liste filtrée d'un objet (donc potentiellement vide, si le filtre ne donne aucun résultat).

A ce stade, le displayList de l'objet (script JS), dont je masque le header et le footer (et encore quelques éléments) pour plus de clarté pour l'utilisateur, produit un effet de bord dans ma homepage. 

Ma list s'affiche bien dans le container que je lui indique (ce qui me permet de jouer sur le css depuis une feuille de style propre à mon objet externe) SAUF la nav qui contient le titre de l'objet qui s'affiche dans le container #work . nav.

J'ai eu l'idée suivante : créer un script JS sur l'objet métier et dire que si on est sur l'instance homepage, alors cette nav doit disparaitre.

Problème à l'issue de tout ceci et là, je sèche : la nav est retirée sans distinction de TOUS les objets et ce quelque soit l'instance d'affichage (main, home, ...). 

Je peux afficher ma liste autrement dans ma homepage mais j'aimerais trouvé une solution car je ne vois pas comment, sur la base d'un affichage d'une liste filtrée créée depuis le template de ma vue, faire un affichage conditionnel.

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1. Créer un objet métier avec une colonne à filtrer (ex. statut)
2. Créer une vue homepage et y faire figurer des objets externes dont l'un est composé d'éléments divers dont la liste filtrée :
*extrait :* 

```
var CrbRhsAccueilAction = (function() {
	var app, responsive = typeof $ui !== "undefined", debug = false;

	function render(params) {
		app = app || (params.pub ? new Simplicite.Ajax(params.root, "api", "userCrbRhs", "BIZCD1Oz") // External
				: new Simplicite.Ajax(params.root, "ui")); //Simplicite.Application); // Internal
		//affichage du titre du bloc
		$("#CrbRhsAccueilAction .title").append("X <br> demandes");
		$("#CrbRhsAccueilAction .col-sm-9").append("<h3>En attente d'une action de votre part</h3><img class=\"warning\" src=\"resource?code=warning\" />");
		// données de l'agent loggué
		var login=$ui.getApp().getGrant().getLogin();

		let population = app.getBusinessObject("CrbRhsPrmPopulation");
		$ui.displayList("#CrbRhsAccueilAction .list", population, {
			filters: {"rhsPrmPopulationActif": "1" },
			fixedFilters: { "rhsPrmPopulationCode": "GPELUS" },
			nav: "new", // nouvelle navigation
		});
```

3. Constater que la balise #work .nav .breadcrumb contient le titre de l'objet dont la liste est pourtant affichée (pour ma part) dans le container "#CrbRhsAccueilAction .list".

4. Tenter de récupérer le coup en créant un script js sur l'objet métier ; extrait : 

```
// CrbRhsPrmPopulation front side hook
(function(ui) {
	if (!ui) return;
	const app = ui.getAjax();
	// Hook called by each object instance
	Simplicite.UI.hooks.CrbRhsPrmPopulation = function(o, cbk) {
		try {
			console.log("CrbRhsPrmPopulation hooks loading...");
			const p = o.locals.ui;
			// si on est sur la page d'accueil => certaines balises de la liste sont cachées pour des questions UX 
			if(p && o.isHomeInstance()) {
				p.list.onload = function(ctn, obj) {
					//masquer le titre de l'objet en mode liste sur la homepage
					console.log($("#work .nav"));
					$("#work .nav").remove();
...
```

Restant à dispo pour plus d'info,
Cordialement,
Caroline

### Technical information
Simplicité version5.3.22
Built on2023-11-11 10:20
OSLinux amd64 3.10.0-1062.9.1.el7.x86_64
ServerApache Tomcat/9.0.82 WEB
DatabaseMySQL 5.5.5-10.2.9-MariaDB-10.2.9+maria~stretch using BLOBs
JVM11.0.6 Oracle Corporation OpenJDK 64-Bit Server VM 11.0.6+10-LTS

## Answer
Bonjour,

Il suffit de retirer nav:"new" ou nav:"add" de vos displayList.
Ou alors essayez l'autre paramètre showNav:false ou nav:"hide"

De plus vous n'instanciez pas des objets home sur votre page d'accueil.

app.getBusinessObject("x", "home_ajax_x")

Sinon isHomeInstance sera faux.
