# Ouverture d'un objet externe hors d'une vue

**URL:** https://community.simplicite.io/t/8584

## Question
Bonjour,

Afin de créer un objet métier, je passe d'abord par un objet externe, accessible via un bouton d'action ([EXPR:HTMLTool.getExternalObjectURL("objet externe", "nav=new")], afin de préremplir manuellement certaines informations, puis automatiquement d'autres grâce au code spécifique.
Côté Java, mon objet hérite de ResponsiveExternalObject.

Le problème est que lorsque l'utilisation du bouton d'action se fait sur la vue d'accueil, alors l'objet externe est affiché dans la vue. Je souhaite que l'affichage se fasse hors de cette vue :
![Capture d'écran 2024-08-02 120826|690x188](upload://hVpI77tOdNiv9MR0fJxT2tQ9jJD.png)
![Capture d'écran 2024-08-02 121216|690x194](upload://4WtWu1DXpN4s0GM7iEOX14puwYD.png)

J'ai tenté de manipulé les paramètres URL, notamment avec nav=new, mais je toujours "coincé" dans la vue.

Or, l'affichage cible est celui-ci, obtenu en ajoutant l'objet externe à la liste du menu déroulant :
![Capture d'écran 2024-08-02 121411|690x157](upload://8QvSVE4c8aFsyXHOkXkGfnrwR0v.png)

Est-ce qu'il y a une solution pour ouvrir l'objet externe pour s'affranchir de la vue présente ?

Par avance, merci.

Romain

## Answer
A mon avis il faut forcer l'affichage en dehors d'une iframe de la réponse :

```js
$ui.loadURL(
  null, // default work area
  $app.getExternalObjectURL("MyObjExt", { nav:"new" }), // https:.../ext/...
  { noiframe: true } // inline content
)

```

cf
https://platform.simplicite.io/current/jsdoc/Simplicite.UI.Loader.html#loadURL


- Si l'URL est complète (commence par http), Simplicité affiche le contenu dans une iframe par défaut pour isoler tout contenu qui viendrait d'ailleurs.

- Si l'URL est relative (commence par /), le contenu est directement interprété/inliné.
`getExternalObjectURL` ne  doit pas retourner une URL relative, il faut donc l'aider un peu.

[quote="RomainV, post:3, topic:8584"]
Lorsque je tente d’indiquer une div contenu dans le HTML de mon objet externe (exemple ci-dessus id=“createS4”) alors rien ne s’affiche.
[/quote]

Il ne peut pas s'afficher à l'intérieur de lui-même... Le conteneur est forcement en dehors du contenu !
