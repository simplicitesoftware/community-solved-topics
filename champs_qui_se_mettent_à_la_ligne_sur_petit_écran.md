# Champs qui se mettent à la ligne sur petit écran

**URL:** https://community.simplicite.io/t/5408

## Question
### Request description

Bonjour,
Sur un formulaire j'ai un template d'affichage sur deux colonnes, mais quand j'affiche sur mon écran de portable (très petit), tout s'affiche en une colonne.

Sur grand écran

![image|634x500](upload://spJM3JxsJPLsaJjZUzxzDkf2gfR.png)

Sur petit écran

![image|432x500](upload://56FHPyyJNh9RGr4ifpTMK6ps8Z9.png)

Pourtant il y aurait la place d'afficher les champs côte à côté, ici les utilisateurs doivent beaucoup scroller pour arriver aux onglets en bas.
Y a-t-il un endroit où je peux changer ce fonctionnement ?

Merci !
Emmanuelle

## Answer
Exact, j'avais oublié cette classe.

Simplicité ajoute la classe CSS **.large** si la largeur du div (et pas du screen) est inférieur à XS = 576px.

Cela corrige un problème non solutionnable par media-query : si on est sur un écran même très large, mais qu'une div (de row) dans un template devient trop petite (< xs, si on affiche le modeleur, treeview à gauche...), la classe "large" y est ajoutée pour forcer la largeur à 100% (du row).

On ne changera pas ce fonctionnement. Si vous avez des champs tout petits, il faudra le forcer par un style en dur comme :

```css
<div class="row">
   <div class="col-xs-7" style="width:60% !important; flex:0 0 60%; max-width:60%;">...</div>
   <div class="col-xs-5" style="width:40% !important; flex:0 0 40%; max-width:40%;">...</div>
</div>
```

De plus en V5, il y a un mode compact au choix de l'utilisateur (ou en ajoutant la classe **.compact** à l'area) = le label est à gauche de l'input. Il devient très important d'avoir assez de place en largeur.
Et ça vous évitera d'avoir des formulaires sur 15m.
