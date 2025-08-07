# Dysfonctionnement 2 méthodes d'authentification IDP (NetIQ et OKTA) en parallèle

**URL:** https://community.simplicite.io/t/7197

## Question
### Request description

Bonjour, 

Nous avons mis en place récemment une 2ème méthode d'authentification par IDP (OKTA), mais nous constatons des dysfonctionnements lors du switch des rôles, quand les 2 IDPs sont en place en même temps (NetIQ et OKTA). Nous sommes actuellement en version 5.3.11 de Simplicité.

L'authentification des users et la récupération des profils depuis le SSO se font correctement, mais quand un utilisateur, qui dispose de plusieurs rôles, change de profil en étant connecté sur Simplicité, il ne voit pas de différence au niveau de ses privilèges en fonction du rôle choisi. Au contraire, s'il a 2 rôles, par exemple admin et reader, peu importe le profil choisi, l'utilisateur a les droits du rôle avec le plus de privilèges. 

Est-ce que ce dysfonctionnement est déjà connu et corrigé sur une des prochaines versions de Simplicité ? 

### Steps to reproduce

*This request concerns an **5.3.11** Simplicité instance
and these are the steps to reproduce it:*

1. Créer 2 rôles et un utilisateur ayant les 2 rôles
2. Créer 2 tabs (tab1, tab2) au niveau du menu. Le rôle admin doit pouvoir visualiser les 2 tabs du menu alors que le rôle reader doit pouvoir visualiser uniquement le tab1
3. Mettre en place 2 méthodes d'authentification IDP et se connecter via l'une de 2. 

Je vous remercie d'avance pour votre retour.

## Answer
Bonjour, 

Avez vous codé des choses en particulier dans un `PlatformHooks` qui associe l'utilisateur à un Profil particulier ? Si oui, c'est peut être à ce niveau qu'il faut regarder. 

[quote="ktsesme, post:7, topic:7197"]
L’authentification standard n’est utilisé que pour le compte designer.
[/quote]

Rien ne vous empêche de créer un utilisateur avec les 2 profils et de vous connecter avec via l'authentification standard afin de tester le comportement de l'application pour ce genre d'utilisateur. Indépendament de ce que fait l'authent via IDP.
