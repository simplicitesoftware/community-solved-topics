# Scroll d'une activité dans un processus métier

**URL:** https://community.simplicite.io/t/9036

## Question
### Request description

Bonjour,

Dans un de nos processus métier, nous avons remarqué qu'à chaque passage d’une activité à l'autre, l'affichage de la page suivante conserve la position de défilement de la page précédente. 

Nous aimerions que, lors de la transition entre deux activités, la vue de la page se recentre automatiquement en haut, peu importe la longueur de l’activité précédente.

Cela nous pose un problème dans la page de synthèse ou l'utilisateur et tout en bas de l'activité et ne vois pas qu'elle a changé.

Peut-on faire ce recentrage automatique en haut de page lors du changement d’activité ? Via script à ajouté au processus ou autre ? 

Merci d'avance pour votre aide :slight_smile: 

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.1.6
BuiltOn=2024-09-13 16:21
Git=6.1/dfa6a2c301a0b79b7667cb2f921b3c5a38f0d51c
Encoding=UTF-8
EndpointIP=100.88.215.69
EndpointURL=http://lbc-77449-app-8578c6d894-cfvlq:8080
TimeZone=Europe/Paris
SystemDate=2024-11-08 10:07:25---
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

Ce mécanisme de remettre le scroll et le focus au même endroit est un besoin UX d'accessibilité RGAA, il est surtout utile quand on navigue/enregistre un formulaire ou une liste longue.

Effectivement, il faudrait que le scroll revienne toujours en haut de l'écran dans la cas d'une activité passagère. On va voir pour changer ce comportement UI en 6.1.14.
