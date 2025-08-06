# Fail to complete the tutorial

**URL:** https://community.simplicite.io/t/9829

## Question
### Request description

*Hi,
I followed the Simplicity tutorial, the 4 firsts steps from "getting started" menu.
Seems i missed something cause when i log with the usertest account nothing appears on the windows.
I tried to redo several times the tutorial, cleared cache each time, no evolution.
Thanks for your help.*

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.following the 4 firsts steps of the tutorial (https://docs.simplicite.io/category/1-getting-started)

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
Bonjour,

Nous avons trouvé une cause possible à votre problème. C'est lié à une récente évolution du menu qui masque l'item de Domaine s'il n'y en a qu'un seul, pour ne voir que ses items directement, et éviter d'avoir un menu dropdown. 

Cette feature entre en conflit avec une autre règle qui, si un domaine ne contient qu'une seul item, est remplacé par l'item lui-même.

En attendant un correctif, pour voir votre domaine, il suffit d'y ajouter un autre objet ou d'activer sa page d'accueil (sur le paramétrage du domaine mettre "Masquer la page d'accueil = non"). Ainsi le domaine contiendra au moins 2 items, et ne sera pas masqué par CSS.
