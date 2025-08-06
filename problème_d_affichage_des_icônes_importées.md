# Problème d'affichage des icônes importées

**URL:** https://community.simplicite.io/t/9131

## Question
### Request description

Bonjour,je rencontre un problème concernant l'utilisation d'icônes dans l'affichage d'énumération 

 J'ai une configuration où j'utilise des icônes Boostrap (comme `bi-pencil-square`), et elles s'affichent correctement mais lorsque j'utilise des icônes personnalisées importées (Desyre de mon groupe), ces dernières ne s'affichent pas correctement.

![Capture d'écran 2024-11-26 154750|201x381, 75%](upload://6wW0G0BnyHsVQnnyzAKwbs6iPQb.png)


Dans mon exemple ci-dessus, l'enum "Master" utilise une icône importée et présente une anomalie d'affichage, et l'enum Adaptation (qui utilise une icône Bootstrap) fonctionne parfaitement.

Avez-vous une idée de ce qui pourrait causer ce problème ?

Merci d'avance pour votre aide :slight_smile: 



### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.1.14
BuiltOn=2024-11-13 12:35
Git=6.1/34709826975d46845d2c518ac5815bd118d09709
Encoding=UTF-8
EndpointIP=100.88.224.125
EndpointURL=http://lbc-77449-app-8d7c7c954-tq995:8080
TimeZone=Europe/Paris
SystemDate=2024-11-26 15:53:25

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=301
EnabledUsers=22
LastLoginDate=2024-11-26 15:30:02

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
Bonjour,

A mon avis ton icone n'a pas de dimension et le bouton ignore sa largeur.
Comment est importé l'icone ? est-ce une font ou une image ?

Simplicité ajoute la class CSS "icon" qui force une `font-size:1rem`, qui permet à certains display "inline" (les boutons d'action sont en inline-block) de bien calculer la taille du contenu.

![image|690x160](upload://c3ILbpPAzbBf8abBwHbnfKwXyC2.png)

Si ton icone est un PNG, il faudra plutôt spécifier/forcer un style 
`width:1rem` ou `min-width:1rem` 

ou basculer le bouton en `display: flex`... par du CSS

(à voir si on devra l'ajouter à la classe .icon standard ou si c'est spécifique dans votre projet)
