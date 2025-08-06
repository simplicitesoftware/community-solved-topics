# Ignorer les ocurrences nulles dans les colonnes d'un crosstab

**URL:** https://community.simplicite.io/t/8731

## Question
### Request description

Bonjour,

J'ai un TC basique avec une date en colonne et un champ Integer en valeur.
J'ai regroupé l'axe date par mois, mais pour certains mois je n'ai pas de données.
Je souhaite que pour les mois sans données, la courbe soit "lissée" jusqu'au mois suivant au lieu de retomber à 0. Est-ce possible ?

![image|690x217](upload://dGIZXju6tpK6utZTfR2tCDUemen.png)

Merci d'avance pour votre aide
Emmanuelle

[Platform]
Status=OK
Version=5.3.46
BuiltOn=2024-08-30 12:32

## Answer
Je ne pense pas qu'on puisse retirer par paramétrage le Total du tableau dès que la donnée est numérique.

- Mais on peut afficher le Max ou la Moyenne et pas la Somme
- Ou masquer le tableau s'il ne sert pas dans la vue
- Ou par CSS à ajouter dans une ressource STYLES de l'objet ou dans la vue, exemple :

```css
.crosstab.crosstab-MyCTname table th:last-child, 
.crosstab.crosstab-MyCTname table td:last-child  {
   display: none;
}
```

on peut bien sûr développer un objet externe qui affiche un simple chart, il doit y avoir des exemples dans les tools & tips.
