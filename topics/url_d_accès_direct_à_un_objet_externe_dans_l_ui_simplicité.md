# URL d'accès direct à un objet externe dans l'UI Simplicité

**URL:** https://community.simplicite.io/t/8858

## Question
Bonjour,

Est-il possible d'avoir une url permettant d'accèder directement au rendu d'un objet externe dans l'UI Simplicité (en passant avant par l'authent login/mot de passe Simplicité ou SSO si besoin) ? et de pouvoir récupérer les éventuels paramètres passé dans l'url dans les paramètres de la méthode display() de l'objet externe ?

Le besoin serait d'avoir le même comportement que pour les urls suivantes :

- Accès direct à la liste des fournisseurs dans le module de démo : http://localhost:8060?l=DemoSupplier
- Accès direct au formulaire d'un fournisseur dans le module de démo : http://localhost:8060?f=DemoSupplier;1

Avec ces urls si l'utilisateur est déjà authentifié il arrive directement sur la bonne page et s'il n'est pas authentifié il passe par la page de connexion avant d'arriver directement sur la bonne page.

J'ai essayé avec cette url http://localhost:8060/ui/ext/DemoCatalog mais j'ai un json qui s'affiche :

![image|690x82](upload://6y7MUsMcc9bV8WBWn8mHWoOVBlM.png)

Au lieu d'avoir cette page :

![image|690x284](upload://weKcFmTt9nQAjjkHZARPffSt8jI.png)

## Answer
Bonjour

Nous prévoyons une livraison de nouvelles révisions v5 (5.3.61) et v6 (6.1.20) d'ici la fin de la semaine, peut être dès aujourd'hui en fonction des tests finaux avant release.
