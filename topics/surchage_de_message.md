# Surchage de message

**URL:** https://community.simplicite.io/t/3268

## Question
Bonjour,

je voudrais n'avoir qu'un seul message à la place de la liste des champs obligatoires

![image|690x202](upload://miFqRIYOoivrz7NCiY216F5cQ9g.png) 

Je pensais faire cela dans le postValidate mais lorque les champs sont obligatoires le message que je construit dans le postValidate ou prevalidate n'est pas pris en compte. est ce possible de le faire sans modifier la configuration des champs ?
Merci d'avance

Thierry

## Answer
[quote="david, post:8, topic:3268"]
j’avais le souvenir que les messages d’erreur du `preValidate` étaient bloquants
[/quote]

Le preValidate n'a jamais été bloquant, il sert à préparer les données pour le validate des champs :
- champs (re)calculés ou (re)formatés ou valeur par défaut
- changer le caractère obligatoire pour bypasser le controle et le remettre au postValidate
- Depuis les hooks en Java on peut bien surcharger le validate directement (en faisant attention d'appeler le super.validate à un moment donné). Ca n'a rien de risqué c'est tout l'intérêt de l'héritage Java.

[quote="Thierry1, post:1, topic:3268"]
je voudrais n’avoir qu’un seul message à la place de la liste des champs obligatoires
[/quote]

Ces messages ne sont pas là pour être retirés en terme d'UX. Sinon mettez juste une regle CSS pour rendre invisible les div > 3 dans les STYLES de l'objet (montrer que 3 erreurs à l'utilisateur).

C'est plutôt l'objet/écran ou le processus de saisie UX qui est à revoir si la UI est amenée à avoir 50 erreurs.

- Le erreurs liées à un champ sont cliquables pour mettre le focus directement sur le champ, et ce notamment s'il est dans un onglet caché. Sinon l'utilisateur ne peut pas comprendre qu'il y a des erreurs cachées (tabs ou scroll vertical).
- Si vous remplacez cet entête par un message "Vous avez des erreurs" l'utilisateur devra tout scroller et ouvrir tous les tabs...
- Si vous avez 50 champs obligatoires pour une raison métier, mettez les de préférence ensemble/à proximité pour que l'utilisateur n'arrive jamais à avoir 50 erreurs. La petite étoile * lui permet de vite repérer ce qui est obligatoire
- Un autre design-pattern est de ne saisir que qq champs obligatoire en début de processus ou en création (la clé fonctionnelle, les références...) et de rendre les autres champs obligatoirse qu'au fur et à mesure qu'on avance dans le processus. Ou juste limiter les nb de champs obligatoires à la création avec un test de isNew() dans une contrainte.
