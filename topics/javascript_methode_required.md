# Javascript Methode required

**URL:** https://community.simplicite.io/t/3404

## Question
Bonjour,

Je travaille avec simplicité 5.0.50.

J'ai implémenté une ressource javascript ou j'agis sur la partie dynamique d'un formulaire notament sur des visibilités de champs. J'ai besoin de jouer aussi avec le caractère obligatoire d'un champ mais cela ne semble pas marcher :

```
var namEpciLibelleDep =  ui.getUIField(ctn, obj, "xx");
namEpciLibelleDep.ui.required(true);
```

## Answer
```
 $(f.ui.input).closest(".form-group").addClass("required");
```

C'est parfait ça. Merci beaucoup. Derrière je refait la validation en  back donc pas de soucis.
