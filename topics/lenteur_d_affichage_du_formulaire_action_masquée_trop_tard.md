# Lenteur d'affichage du formulaire / action masquée trop tard

**URL:** https://community.simplicite.io/t/9754

## Question
### Request description

Bonjour,

Depuis notre passage en V6.2, nous avons un problème de perfs à l'affichage des formulaires. On dirait que le isActionEnable et le onLoad se déclenchent après le chargement des onglets, ce qui laisse les actions Enabled quelques secondes (particulièrement à la première ouverture avec le chargement des contraintes)

Dans l'exemple ci-dessous, nous avons une transition d'état To be validated qui est désactivée dans le isActionEnable, et une action custom Global validation request qui est disabled en javascript dans le onLoad.

A l'ouverture
![image|690x58](upload://8OiWnoXR5aC411Ejldob5wafEVR.png)

Quelques secondes après
![image|690x60](upload://1lakCHL2psl6hcOQueMcBr044Mr.png)

Sommes nous les seuls à avoir ce souci ? Est-ce que ça peut être dû à un problème de chargement des onglets, trop de contraintes ou de pillbox par exemple ?

Merci d'avance pour votre aide,
Emmanuelle

[Platform]
Status=OK
Version=6.2.6
BuiltOn=2025-04-01 17:56
Git=6.2/d92e309e2d5ba05ea4cc37b16858dd3b35dd4720

## Answer
Bonjour,

Exact tu as raison, en fait au moment de `preload`, les métadata ont déjà été digérées dans les paramètres d'affichage du formulaire (variable du scope p).

[quote="Emmanuelle, post:5, topic:9754"]
le style de ma liste de valeurs s’affiche par dessus celui du `disabled` .
[/quote]

Il faut surement forcer ta couleur par un `!important` qui va écraser le style de l'ENUM, exemple :

```css
.btn:disabled, .btn.disabled {
  background-color: #777 !important;
  color: #fff !important;
}
```

Mais c'est plutôt une anomalie, le style de l'ENUM ne devrait pas être placé si l'action est inactive. Comme par défaut la UI masque un bouton `disabled` (besoin de baisser la charge cognitive en terme d'UX), on a jamais eu ce pb de surcharge CSS. Mais bon on peut aussi vouloir griser la couleur de l'ENUM (via opacity ou grayscale).

[quote="Emmanuelle, post:5, topic:9754"]
`$(tbvButton).title = 'Please complete application to 100% before requesting validation';`
[/quote]

Il manque surement un `$(tbvButton).attr("title", ...)`
