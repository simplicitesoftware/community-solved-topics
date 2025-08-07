# Sélection multiple d'une référence

**URL:** https://community.simplicite.io/t/8382

## Question
Bonjour,

Je cherche à savoir comment permettre la sélection multiple sur Simplicité. 
J'ai un champ nommé "administrateur" qui pointe vers une table des administrateurs. Actuellement, je ne peux sélectionner qu'un seul administrateur, mais j'aimerais pouvoir en choisir plusieurs.

Dans la capture, par exemple, je veux avoir la possibilité  de sélectionner  X et Y.

Avez-vous des suggestions sur la manière de mettre cela en place sur Simplicité ?

Merci.


![1|690x279](upload://rplBUHBkYEjFr29AtA6c7wf5g0k.png)
![image|690x144](upload://oaFAd6SxIlY94udfUFGVEbyTI64.png)

## Answer
Bonjour,

Il ne faut pas confondre la présentation UI du modèle logique de données qui supporte votre métier.

En effet, il ne peut y avoir de champ "adminitrateurs" au pluriel car 1 champ est par construction mono-valué = correspond à 1 colonne en base. (seul un champ ENUM Multiple peut stocker N valeurs séparées par des ";" mais bien stocké dans une seule colonne, ce n'est pas le cas d'un foreign-key qui référence qu'un seul objet = jointure)

Vous devez donc créer et habiliter un objet "Administrateur" de relation N,N dont la clé fonctionnelle est composée des 2 foreign-keys persistantes (vers Network et Member). Vous pouvez également ajouter des propriétés non clés à cet administrateur.

Ensuite côté présentation UI, toute relation est par défaut un objet lié donc une liste (appelée panel de l'objet parent, ici un Network aura une liste d'Adminitrateurs), mais on peut présenter cette liste en pillbox (qui s'apparente à un affichage de champ simple avec des petites vignettes, donc sans recherche, sans action de liste...) : en insérant la vue du lien dans le formulaire (du Network) avec l'option pillbox sur le Link.

Veuillez regarder la documentation ou les nombreux exemples sur vos projets Renault d'affichage en pillbox.
