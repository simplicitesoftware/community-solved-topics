# Recherche sur champs ramenés

**URL:** https://community.simplicite.io/t/5284

## Question
### Request description

Bonjour,

J'ai un objet Service version qui a une relation 1,N vers un objet Service. Cet objet Service a une relation 1,N vers un Type.
A partir de Service version, j'aimerais pouvoir faire une recherche "loupe" sur le Type du Service, mais j'ai l'impression que ce n'est pas possible sur les champs ramenés d'un objet lié. Seule la recherche textuelle est disponible.

![image|690x194](upload://98bLxO0pDA9lw2UjlKLwAd9UYi0.png)


Avez-vous une solution ?

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
Oui c'est standard en V5, la loupe est proposée sur chaque objet lié directement ou en cascade.
Exemple sur l'objet habilitation, on peut chercher le nom d'une action ramenée depuis la fonction :

![image|690x117](upload://3nAuddzqI92Wk5voedAd4YTIymj.png)

Cette feature n'a pas été backportée en V4 LTS, car on y reporte que du correctif.

Avez-vous prévu de passer en V5 ?
