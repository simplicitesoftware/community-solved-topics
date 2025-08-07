# Nom de l'instance reste figé suite à un merge

**URL:** https://community.simplicite.io/t/7440

## Question
Bonjour,

Tout d’abord je souhaite une bonne année 2024 à toute l’équipe !

Quand je merge une ligne master avec une autre ligne, l’instance de la ligne master conserve le nom final merge_XXX, est-ce normal ?

![image|690x219](upload://oz5eYVnpBGjk7BDfxm9x8mWaJ0f.png)

![image|690x376](upload://w1rWUApU4m19WEqeS2NzK5uycRk.png)


En plus, suite à ce merge, toutes les autres lignes non concernées, auront aussi un nom commençant par merge_XXX.
Exemple ligne non concernée par le merge : 
**Avant :**
![image|690x407](upload://dsUrenMWEj10Yz0Skoaf1daqnaL.png)
**Après:**
![image|690x399](upload://z43wcO45AkS1Q5IYcSgQOlSqCUZ.png)
Quand je sélectionne les lignes de la liste :des produits :
![image|690x205](upload://tkuxNMWurD6MNlyh5Ytr7C828HJ.png)


Il faut faire un clear cache pour que le nom des instances redevienne normal.
La ligne master :
![image|690x341](upload://kjBjhVy3OK9mtHeMpPa5lmOfraA.png)

![image|187x96](upload://9QXF3OZOLSTSffjrEpPP6mvfTJU.png)

Merci d’avance pour votre aide.

Abed.

## Answer
Ce sera poussé en 5.3.26
pour conserver les métadata de la liste d'origine à la fermeture de la fusion/merge.
