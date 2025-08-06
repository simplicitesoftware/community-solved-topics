# Afficher un tableau dans un Template de formulaire (après avoir enregistrer)

**URL:** https://community.simplicite.io/t/4500

## Question
Bonjour,

J'ai un MCD qui ressemble à ça : 
![image|690x315](upload://dYBjpYNDq9zusAGDUfWSyhOow8N.png)

Dans le Template du formulaire de `Campagne`, j'aimerais que quand je créer une campagne, je doive renseigner dans un premier temps le `nom` et le `fond`. Puis une fois enregistrer, à ce moment, un tableau avec toutes les participations de ce fond apparait sous ce formulaire. (Le lien avec toutes les participations peut se faire via la table `Investir` car j'ai l'ID du fond dans la campagne).

Une idée de comment faire ? Puisque pour le moment, mon Template ressemble à ça :
![image|690x271](upload://wt5GrbpqNhuqygPe8zdRXdcy7gA.png)

## Answer
Bonjour,

Vous ne pourrez implémenter ce genre de parcours de modèle grâce à un lien virtuel. 
Voici le lien de la leçon :
https://docs2.simplicite.io/lesson/tutorial/development/virtuallinks
