# Repo git simplicité

**URL:** https://community.simplicite.io/t/4615

## Question
Bonjour,

J'ai une question par rapport au git/Simplicité.

Je vois bien qu'il y a un bouton **Repository Git** au niveau de l'IHM d'un module.
En cliquant sur ce bouton, il m'emmène vers un autre écran qui m'affiche bien une **URI** et la branche actuelle,  ainsi que 3 boutons : Commit, Supprimer et Actualiser.

Ma question est la suivante , où se trouve ce Repo ? comment peut on y accéder ?
J'ai déjà regardé avec nos Devops mais on ne trouve pas ce projet.

Merci d'avance pour toute information sur ce sujet.

Samih.
Renault ABC

## Answer
Le repo Git d'un module est destiné à être **cloné** en utilisant l'URI indiquée et le user designer ad hoc.

Le contenu de ce repo Git correspond à un **export** structuré (en projet Maven) du module => c'est équivalent à ce que vous obtenez via un export ZIP lorsque le paramètre système `EXPORT_MODULE_ARTIFACTS` est à `yes` => un commit est donc l'équivalent d'un export.

Physiquement il est dans l'arborescence de l'image Docker (je suppose que vous êtes dans ce contexte là) et peut donc potentiellement être mappé sur un volume pour la persistance mais dans tous les cas il faut éviter d'y accéder et surtout d'y modifier des choses (notamment le `pom.xml`) car ce sera de toute façon écrasé au prochain commit.

Il est possible de paramétrer des choses au niveau de votre module pour "piloter" certaines choses au niveau du repo Git du module : indiquer un remote "origin", d'autres remotes, des branches, des settings Sonar etc.
![image|690x246](upload://uw7XNAk3YEORGwP2b9MtDLCvIB9.png)

Il est aussi possible d'exporter un `pom.xml` "projet" pour chapeauter N modules dépendants.

Etc.

Tout cela relève de la formation (typiquement de notre [offre de formation CI/CD](https://community.simplicite.io/t/devops-services-offer/4508)), pas du support sur ce forum qui ne peut pas se substituer à une formation en bonne et due forme.
