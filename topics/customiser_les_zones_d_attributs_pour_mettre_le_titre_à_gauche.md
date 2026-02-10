# Customiser les zones d'attributs pour mettre le titre à gauche

**URL:** https://community.simplicite.io/t/11532

## Question
### Request description

Bonjour,
J'ai une demande assez spécifique de présentation d'un objet, qui inclut notamment l'affichage des Zones d'attributs avec le titre à gauche et non au dessus.

![image|690x345](upload://oewm5mbatNnzNj1gpxVG68kkF3X.png)

Il me semble que cette disposition est codée dans le front et que je ne peux pas la changer.

J'ai besoin de votre avis sur la meilleure façon de procéder :

- pour changer de template selon le point d'entrée utiliser pour accéder au formulaire (dynamiquement avec getTemplate, ou plutôt faire un objet hérité ?)
- pour modifier l'apparence des zones d'attribut du formulaire (en jouant sur le CSS, code front, ou texte statique ?) sachant que les utilisateurs vont y faire de la saisie et utiliser les boutons d'action comme sur les formulaires standard

Merci d'avance pour votre aide !
Emmanuelle

[Health check]
[Platform] Status=OK Version=6.3.2 BuiltOn=2026-01-30 20:34

## Answer
Bonjour,

Les panels sont des `card` Bootstrap5 en `display: flex`, il n'est pas prévu de positionner le header dans le template. Mais il suffit d'un peu de CSS pour en changer la présentation.

Par exemple pour la zone 1 du Supplier de la démo :

```css
.objform.object-DemoSupplier [data-areaname="DemoSupplier-1"] .card {
   flex-direction: row;
}
```

Attention, le footer se retrouvera à droite s'il y en a un.
