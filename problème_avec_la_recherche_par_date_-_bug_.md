# Problème avec la recherche par date - bug?

**URL:** https://community.simplicite.io/t/9748

## Question
Bonjour,

Simplicité version6.2.4
Built on2025-03-19 12:10

J'essaie de faire une recherche sur un champ date mais le système semble "tourner en rond" et je n'ai rien dans les logs

![image|690x177](upload://aZOLSSWnISvk95frOBr0UmsIlQ9.png)

mais quand je fais une recherche pour avoir les dates en 2024 par exemple, la table Achat - vente des titres semble tourner en boucle
![image|690x165](upload://azMd0ddB06gLR8yu9PDO7HRDb7k.png)
et plus rien ne se passe.

Et je n'ai aucun logs...

Toutes les autres recherches fonctionnent.. j'ai l'impression que le bug n'est que sur les recherches par période


J'ai le même problème si mets les filtres datemin et datemax par script:
```
			getField("ParticipationAchatVenteDate").setFilterDateMin(anneeEnCours + "-01-01");
			getField("ParticipationAchatVenteDate").setFilterDateMax(anneeEnCours + "-12-31");

```

Merci d'avance.

Fabrice

## Answer
Il y a effectivement une régression en 6.2 (testé sur une 6.2.5 à jour) qui nous a échappée

C'est une anomalie coté UI donc l'erreur est visible dans la console du navigateur
![image|690x388](upload://3QHUmIjrGwgAzx4pokS9LV6qZt.png)

C'est corrigé et ce sera livré dans une nouvelle révision 6.2 (6.5.6) qu'on va releaser en urgence aujourd'hui
