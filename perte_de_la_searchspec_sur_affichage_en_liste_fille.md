# Perte de la searchSpec sur affichage en liste fille

**URL:** https://community.simplicite.io/t/9550

## Question
### Request description

Bonjour,

Nous avons constaté un comportement étrange avec les searchSpec.

Pour reproduire :
- dans le postLoad d'un objet, mettre un setSearchSpec
- afficher l'objet en liste seule, la searchSpec s'applique
- afficher l'objet en liste fille, la searchSpec ne s'applique plus

On dirait que le filtre sur la FK vers l'objet père a écrasé la searchSpec.
Cela ne se produit pas lorsqu'on met le setSearchSpec dans le hook initList (nous avons donc appliqué cette méthode, nous ne sommes pas bloqués).

Nous avons constaté le même comportement en V6 et nous sommes à jour de nos versions.

[Platform]
Status=OK
Version=5.3.62
BuiltOn=2025-02-12 17:25

Merci d'avance pour votre aide !
Emmanuelle

## Answer
La search spec "statique" se positionne programmatiquement via un [set**Default**SearchSpec](http://platform.simplicite.io/5.3/javadoc/com/simplicite/util/ObjectCore.html#setDefaultSearchSpec(java.lang.String))
