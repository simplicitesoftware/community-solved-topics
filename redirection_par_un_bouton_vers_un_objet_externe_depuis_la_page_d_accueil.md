# Redirection par un bouton vers un objet externe depuis la page d'accueil

**URL:** https://community.simplicite.io/t/3781

## Question
@RmnVgx pour effectuer une redirection vers un formulaire, en mise à jour, directement depuis le javascript:

```javascript
var objectName = "xxxObject";
var id = n;
$ui.displayForm(null, objectName, id, { nav: "add"});
```

## Answer
Pour afficher un objet externe, il faut passer en paramètre une URL :

```javascript
var app = $ui.getAjax(); // application services
var extobj = "CmpCompteurAbsences"; // external object name
var embedded = true; // true = no iframe, false = load the URL in a iframe
var param = null; // or string or object { key:value, ... }
var url = app.getExternalObjectURL(extobj, param, embedded);
console.log("debug url = " + url);

var ctn = null; // container null = main work zone, or any div selector
$ui.loadURL(ctn, url, { showNav:true, nav:"new" });
```

Quand on part d'une page d'accueil en général on met `nav:"new"` pour démarrer un nouveau fil d'Ariane à partir de cette URL
