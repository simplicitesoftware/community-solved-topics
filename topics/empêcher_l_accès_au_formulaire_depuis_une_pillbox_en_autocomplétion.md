# Empêcher l'accès au formulaire depuis une pillbox en autocomplétion

**URL:** https://community.simplicite.io/t/10252

## Question
### Request description

Dans un formulaire, j'utilise un champ de type **pillbox** pour associer des contributeurs (utilisateurs) via une table d'association. 

Je souhaite que l'utilisateur puisse **ajouter des utilisateurs via l'autocomplétion uniquement**, **sans avoir la possibilité d'ouvrir la fiche utilisateur** en cliquant sur une pill déjà sélectionnée.
![image|517x439, 50%](upload://8nRTG0pZhMX2fZOyC8fVf2a1Zuj.png)



Dans la table d'association, la case "lien navigable" est bien décochée et les utilisateurs ne sont pas cliquables depuis cette liste mais en pillbox on a cependant accès à ce formulaire


Test :

* J’ai tenté un hack front via JavaScript pour désactiver le clic (`onclick`) et modifier le curseur, mais cela **ne s’applique qu’à l’ouverture du formulaire**, car le hook de customisation front ne s’exécute **qu’une seule fois au chargement**.( onLoadForm)

* J’ai également envisagé un `MutationObserver` en front pour surveiller dynamiquement les ajouts de pills, mais cela reste fragile. **Une solution standard, propre côté plateforme, serait fortement préférable.**

* J'ai tenté aussi d'utiliser le hook useForm() dans la table User pour que le formulaire ne soit pas accessible psans les droits associés mais ils ont quand meme accès au niveau de la pillbox.


### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

* Créer un lien entre un objet et `User` via une association N:N avec affichage en `pillbox`.

* Depuis le formulaire, ajouter un utilisateur via l’autocomplétion dans le champ pillbox.
* Constater que la pill nouvellement ajoutée est cliquable et permet d’ouvrir le formulaire utilisateur.

* Objectif : rendre **la pill non cliquable dès son ajout**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.7
BuiltOn=2025-04-11 11:49
Git=6.2/5f5b1cec41cb5a57bc7fc607a1090ae50e325df4
Encoding=UTF-8
EndpointIP=100.88.196.32
EndpointURL=http://lbc-77449-app-7c6b798757-86z46:8080
TimeZone=Europe/Paris
SystemDate=2025-06-25 16:10:56

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://ldm-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=304
EnabledUsers=16
LastLoginDate=2025-06-25 16:03:44

[Server]
ServerInfo=Apache Tomcat/9.0.104
ServerType=WEB
ServerDevMode=false
ServerCompiler=true
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Pb reproduit, effectivement l'ajout en pillbox sur un formulaire en mise à jour ignore le nouveau `followlink` calculé côté serveur, on va corriger.

Par contre en cas de création de pillbox en mémoire (depuis un formulaire en création), il n'y aura pas de followlink par défaut sur les ajouts, car on ne sait pas encore appeler les hooks éventuels puisque rien n'existe encore en base.

Ce sera livré 6.2.13.
