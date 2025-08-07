# Ouvrir / Créer un modèle avec paramètre

**URL:** https://community.simplicite.io/t/3162

## Question
Bonjour,

Je cherche un moyen de passer un paramètre à l'ouverture et la création par code de mes modèles.
C'est à dire au $ui.diagram.open et $ui.diagram.create
En fonction de ce paramètre je vais afficher ou pas certains items dans le OndrawItem. Il faut que ça soit dynamique , c'est à dire que le même modèle s'ouvrira avec ou sans les items selon ce paramètre.

Est-ce possible ?

Merci !
Emmanuelle

> Version=4.0.P25
> BuiltOn=2021-03-24 00:20 (revision 0ab578dff484419fee9205b41be7f805473ce9a4)

## Answer
Bonjour Emmanuelle,

L'idéal est de : 
1. positionner un paramètre utilisateur avant l'ouverture / création, en front avec `$ui.grant.setParameter` ([doc](https://docs.simplicite.io/5/jsdoc/Simplicite.Ajax.Grant.html#setParameter)) ou en back avec `getGrant().setParameter()` 
2. pour pallier à une fermeture inopinée du modèle reseter à une valeur par défaut lors du chargement du modèle dans le hook `Simplicite.Diagram.ModelHooks.MyModel.onLoadModel` (signature `function(_data, cbk) { cbk(); }`), et stocker votre paramètre dans une variable locale au navigateur
3. utiliser cette variable locale dans votre hook `Simplicite.Diagram.ModelHooks.MyModel.onDrawItem`

**Si vous êtes sûr que votre modèle sera uniquement ouvert via votre *ouverture et création par code*, alors la variable locale est inutile**  et vous pouvez bien entendu utiliser votre paramètre utilisateur directement dans `onDrawItem`
