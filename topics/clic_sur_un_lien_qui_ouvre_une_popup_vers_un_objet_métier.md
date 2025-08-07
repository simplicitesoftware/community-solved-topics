# Clic sur un lien qui ouvre une popup vers un objet métier

**URL:** https://community.simplicite.io/t/5112

## Question
Bonjour,

J'aimerai pouvoir ouvrir une popup qui affiche la vue d'un objet métier quand je clique sur la valeur d'un attribut (ici LADOM dans l'exemple ci-dessous). Est-ce possible ? Si oui, Comment s'y prendre ?
![financeurs|690x281](upload://8fxTlOyrsdcIwfeuw2WJTCVpS7V.png)

En vous remerciant.

Bruno

## Answer
Vu en atelier, il faut modéliser une relation N-N entre l'objet référentiel et Financeurs avec un rendu pillbox.
Lors de la création d'un dossier PMFP, par financeur créer un Échéancier qui va porter les informations Délégation / Filière / Poste / Financeur. Cet objet Échéancier va avoir N lignes (objet métier Échéances)
