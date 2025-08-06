# Affichage "aucun résultat" d'une liste vide d'un objet

**URL:** https://community.simplicite.io/t/4173

## Question
Bonjour,

Est-ce possible d'afficher un texte "aucun résultat" ou qqch dans le genre lorsque la liste d'un objet est vide comme dans le cas ci-dessous ?

![affichage_liste_aucun_resultat|690x87](upload://9JktlwGwO3lqCiIPRKkUAcBsyDA.png)

En vous remerciant.

Bruno

## Answer
Une liste affiche normallement le nombre de lignes trouvées en dessous du titre, et en dessous de la liste. Votre copie d'écran montre que vous l'avez retiré...

Il n'y a pas de ligne "aucun résultat" prévue, mais vous pouvez ajouter du CSS malin pour le faire dans la ressource STYLES de votre objet :

```css
.objlist.object-MyObject .table > tbody:empty::before {
  display: block;
  content: "Aucun résultat";
  margin: 1rem;
}
```

![image|690x350](upload://6fXwzux8LwLe6uoJlcNwrmVQLjv.png)
