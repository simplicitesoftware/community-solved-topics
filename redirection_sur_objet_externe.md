# Redirection sur objet externe

**URL:** https://community.simplicite.io/t/5139

## Question
Bonjour je souhaite créer une barre de recherche sur la page d'accueil, permettant de rediriger les utilisateurs sur un formulaire d'objet, permettant de choisir un type, et de rentrer une référence :

![image|690x118](upload://gUEU8ly0jC6xFFO11RA05Gtc9vh.png)

J'ai essayer de faire une redirection en "dur", pour tester, mais cela ne marche pas. Pourtant je passe bien dans le log "action ok".

Voici mon code java :

	@Override
	public Object display(Parameters params) {
		
		setDecoration(false);
        appendCSSInclude(HTMLTool.getResourceCSSURL(this, "STYLES"));
        
		try {
        
        String action = params.getParameter("action");
        
	        if (action != null) {
	        	AppLog.info(getClass(),"---action--->","action ok",getGrant());
	        	return HTMLTool.javascriptStatement("$ui.displayForm(null, 'MlaAftersaleItem', 21138, null);");
			}
			return javascript(getName() + ".render(" + null + ");");
		} catch (Exception e) {
			AppLog.error(null, e, getGrant());
			return e.getMessage();
		}
	}

Le code javascript :

var MlaSearchExt = (function($) {

    function render(data) {

        console.log("***MlaSearchExt*** : " + data);

		let selectText = document.getElementById("selectText");
		let inputfield = document.getElementById("inputfield");
		
		inputfield.addEventListener("keypress", function(event) {
			if (event.key === "Enter") {
				event.preventDefault();
				selectText.innerHTML
				let type = selectText.innerHTML;
				let ref = inputfield.value;
				console.log(type + "/" + ref);
				if (type !== null && type !== "" && ref !== null && ref !== "" && !hasWhiteSpace(ref)) {
					save(type+";"+ref)
				}
			}
		});
    }
    return {
        render: render
    }
    
	function hasWhiteSpace(s) {
		return /\s/g.test(s);
	}
    
    function save(param) {
		var url = "/ui/ext/MlaSearchExt?action=on";
		$.ajax({
			url: url,
			data: {recherche: param},
			type: "post",
			dataType: "json",
			success: function (code_html, statut) {},
			error: function (resultat, statut, erreur) {},
			complete: function (resultat, statut) {}
		});
	}

})(jQuery);

Je récupère bien le type et la référence côté front, avec console.log(type + "/" + ref), je récupère aussi l'info côté back.

Cependant la commande return HTMLTool.javascriptStatement ne marche pas.

J'ai fait le test avec une valeur qui marche en la lançant dans le terminal, la redirection fonctionne bien : $ui.displayForm(null, 'MlaAftersaleItem', 21138, null);

Si vous avez une piste je suis preneur.

Merci d'avance,

Benoît



[Platform]
Status=OK
Version=5.1.44
BuiltOn=2022-05-10 18:36
Git=5.1/a51516647c95b8cab51e136ca72a2a5e5c30e27c
Encoding=UTF-8
EndpointIP=xxxxx
EndpointURL=xxxxx
TimeZone=Europe/Paris
SystemDate=2022-08-10 12:53:42

[Application]
ApplicationVersion=0.10
ContextPath=
ContextURL=xxxxx
ActiveSessions=2
TotalUsers=33
EnabledUsers=12
LastLoginDate=2022-08-10 12:48:36

[Server]
ServerInfo=Apache Tomcat/9.0.62
ServerType=WEB
ServerActiveSessions=3

[OS]
Name=Linux
Architecture=amd64
Version=5.10.107+
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.3+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=1519178
HeapSize=2129920
HeapMaxSize=7131136
TotalFreeSize=6520394

[Cache]
GrantCache=0
GrantCacheMax=0
GrantCacheRatio=0
ObjectCache=101
ObjectCacheMax=10000
ObjectCacheRatio=1
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.15
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.3.5
DBDate=2022-08-10 12:53:42
DBDateOffset=0
DBPatchLevel=5;P01;94dfa153d22f9e8ecd37b949c00b442c
UsingBLOBs=true

[Healthcheck]
Date=2022-08-10 12:53:42
ElapsedTime=7

## Answer
[quote="Benoit, post:6, topic:5139"]
* Quel est l’impact de renseigner ou non le premier paramètre ? le fait de mettre ‘#work’ ou null
[/quote]

Le premier argument de la méthode est pour spécifier le container, en l'occurence, `null` va faire la même chose que `'#work'`

[quote="Benoit, post:6, topic:5139"]
* Dans mon exemple, l’ID 21138 est récupéré à partir du Back. Est il possible, et “propre” de le récupérer à partir du Front ? et si oui aurais tu un exemple de récupération d’un id d’objet à partir de la valeur d’un de ses “Field”
[/quote]

Tout à fait possible il y a des exemple dans le module de démo (Objet externe DemoPlaceNewOrder), il faut passer par la méthode [.search(..)](https://docs.simplicite.io/5/jsdoc/Simplicite.Ajax.BusinessObject.html#search) de la lib Ajax
https://community.simplicite.io/t/mise-a-jour-dune-progressbar-dimport/2210?u=alistair

[quote="Benoit, post:6, topic:5139"]
* Comment ce fait il que la commande “HTMLTool.javascriptStatement” ne marche pas dans ce cas précis ? (je l’ai déjà vu dans des exemples comme celui ci après)
[/quote]

Je ne sais pas, il faudrait que je teste avec le même pattern que toi. En l'occurence tu utilises le même objet externe pour afficher la search bar ET pour rediriger. Si tu découplais les deux, peut-être que ça fonctionnerait mieux (un objet externe pour la search bar et un pour la redirection selon une valeur en entrée), mais ça me semble être un pattern un peu tordu alors que tu as tout ce qu'il faut pour faire porter l'intelligence par le front.
