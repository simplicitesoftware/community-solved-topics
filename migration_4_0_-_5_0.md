# Migration 4.0 -> 5.0

**URL:** https://community.simplicite.io/t/5285

## Question
### Request description

Bonjour,

J'aimerais commencer à tester la montée de version vers 5.0.
Auriez vous une documentation sur la marche à suivre ?

Merci !
Emmanuelle

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
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
Il n'y a pas de procédure particulière, il suffit de remplacer le container 4.0 par un container 5.2 à jour (5.2.15 actuellement), les patches système se feront automatiquement au 1er démarrage.

AU niveau de vos paramétrages et code, pour préparer l'upgrade il faut lire les release notes 5.0, 5.1 et 5.2 pour prendre en compte les points de non compatibilité indiqués. 

En tout état de cause, le prérequis reste d'être sur une 4.0 parfaitement à jour.

**Attention**: avant d'upgrader il convient de faire une sauvegarde (base et dbdoc si pas en BLOB) afin de pouvoir revenir en arrière en cas de gros pb. Il n'y **a pas** de possibilité de faire un downgrade, tout upgrade est donc irréversible (sauf à restaurer une sauvegarde faite avant upgrade)
