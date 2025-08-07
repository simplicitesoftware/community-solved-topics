# Fenêtre avec message « Voulez-vous enregistrer vos modifications avant de quitter ? » lors de la consultation d'une donnée

**URL:** https://community.simplicite.io/t/9025

## Question
Des utilisateurs de deux de nos applications basées sur la version v4.0P25 de Simplicité nous remontent un problème similaire : à chaque changement de fenêtre, même sans modification effectuée sur les données du formulaire, une fenêtre avec le message « Voulez-vous enregistrer vos modifications avant de quitter ? » apparait.
Je voudrais savoir si c'est un problème connu de cette version et si le passage à une version ultérieure de Simplicité (le passage à la v5 est prévu puis probablement à la v6 dans la foulée) permettra de résoudre le problème.

[Ticket DOS0048204 - Capture d'écran du problème.pdf|attachment](upload://6CMzvoDrhDnK96T0bT5EAGObqqX.pdf) (66.0 KB)

## Answer
PS:

Je viens de faire un test d'upgrade d'un container démarré sur l'image Docker "out of the box" `registry.simplicite.io/platform:4-latest` (i.e. la revision finale de la v4 indiquée dans ma réponse précédente) vers l'image Docker `registry.simplicite.io/platform:5-latest` (i.e. la révision actuelle de la v5 = 5.3.54) et ça s'est bien passé.

Cela ne presume en rien des travaux à effectuer au niveau de votre application métier pour la rendre compatible v5, cf. les release notes des 5.x pour voir ce qui doit être refactoré notamment au niveau de votre code spécifique:
- [release note 5.0](https://docs.simplicite.io/versions/release-notes/v5-0)
- [release note 5.1](https://docs.simplicite.io/versions/release-notes/v5-1)
- [release note 5.2](https://docs.simplicite.io/versions/release-notes/v5-2)
- [release note 5.3](https://docs.simplicite.io/versions/release-notes/v5-3)
