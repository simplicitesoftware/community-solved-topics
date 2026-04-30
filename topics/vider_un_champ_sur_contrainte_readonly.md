# Vider un champ sur contrainte Readonly

**URL:** https://community.simplicite.io/t/12081

## Question
### Request description

Bonjour,

J'ai une contrainte qui passe en champ (Integer) en updatable = false.
Ma contrainte est back + front car j'en ai besoin pour un calcul de complétude en back également.

Je cherche un moyen de vider la valeur de mon champ à l'activation de la contrainte Readonly.

*Champ en écriture*
![image|690x76, 75%](upload://b43GUBkQigPMwPwKeZQgbUxb22A.png)
*Champ en readonly*
![image|690x55, 75%](upload://l8R2z1GOH6v9GxGRSWBx4X8r8lp.png)

J'ai tenté de mettre en place un deuxième impact de type Field Value, mais je rencontre plusieurs soucis :
- si je mets l'expression de l'impact = "", j'entre dans une boucle infinie car le change() se déclenche à chaque fois (on compare null et "")
- si je mets l'expression de l'impact = null, j'ai une erreur comme quoi ce n'est pas une valeur numérique
![image|663x120, 50%](upload://wmEYdDeTCXgxjE1jrv0UMWzcQDT.png)

- le champ étant passé en Readonly, j'ai l'impression que dans tous les cas, le Save n'envoie pas la nouvelle valeur vide au back

Auriez vous une solution à me conseiller, ou est-ce mieux d'implémenter mon besoin en javascript ?

Merci pour votre aide,
Emmanuelle

Mon paramétrage
![image|690x52](upload://mXcPIWr3DAvHu5yYOi5w5FByW4U.png)
![image|690x67](upload://t9sTAmmxAVN7oSTr0dLCeWiWjW5.png)


[Platform]
Status=OK
Version=6.3.7

## Answer
Je reproduis bien avec ton paramétrage, et ton analyse est la bonne. 

Le code qui génère la liste des champs "condition" fait une recherche par sous-chaine, `demoSupInteger` étant un préfixe de `demoSupIntegerNa`, il était ajouté à cette liste. 

Nous avons rendu le code plus robuste. Ça sera corrigé en 6.3.8
