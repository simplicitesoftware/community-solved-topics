# Actions présentées en liste non groupées

**URL:** https://community.simplicite.io/t/8687

## Question
### Request description

*Les actions configurées dans un groupe d'actions ne sont pas groupées lorsqu'elles sont présentées en liste.*

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

 
![image|633x500](upload://uRdXz0N1cEDD1WR4goGtX9MDMvz.png)

![image|690x133](upload://wdOz52fE9TFAcMxPaLcSKE0jQtZ.png)

![image|690x224](upload://bLQzVmZ9TRU4PWb6RNW2EdGPAFu.png)

![image|690x310](upload://sUkCHl6Gph8PsG5Qmq10FYx4TnO.png)


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
Bonjour Bruno,

Effectivement c'est un oubli, ça n'a été implémenté que sur les formulaires mais on va l'ajouter simplement aux listes, car les méta-données du groupe d'actions sont déjà envoyées en front.

Ce sera livré en 6.1.5
