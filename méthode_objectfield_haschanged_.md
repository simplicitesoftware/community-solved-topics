# Méthode ObjectField.hasChanged()

**URL:** https://community.simplicite.io/t/4551

## Question
Bonjour,

Je souhaiterais savoir comment fonctionne la méthode getOldValue(). A quel moment exact est setté cette oldValue ?

Je souhaiterais savoir ça car je souhaiterai travailler avec un champ logique non persisté qui serait alimenté dans l'initUpdate et utiliser la methode hasChanged().

Merci d'avance.

## Answer
Dans ce cas je te conseille d'implémenter la valorisation des champs dans le hook `postSelect` pour l'affichage du formulaire et dans le `postSearch` dans le cas où ces attributs sont visibles également en liste.

Ensuite pour vérifier si la valeur de ces champs a été modifiée, au moment d'appeler le `setValue` (toujours dans le `postSelect`) pour valoriser le champ, appeler également un `setOldValue`. 

Avec ça, le `hasChanged` fonctionnera correctement lors de la reconstruction potentielle du JSON dans le hook `preSave`.
