# Les traductions de relations d'objets ne sont pas accessible via l'objet spécialisé TranslateLink

**URL:** https://community.simplicite.io/t/8646

## Question
### Request description

*Les traductions de relations d'objets ne sont pas accessible via l'objet spécialisé TranslateLink. Elles le sont via l'objet hérité Translate filtré sur le (méta)objet "Relation d'objet".*
### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

![image|690x271](upload://r04NwAxWUpvIyHhouqUEvAnKajo.png)

![image|690x228](upload://RGIIInvox8LjbmsFSkRPAOCram.png)

### Technical information

[details="Instance /health"]
```
[Platform]
Status=OK
Version=6.1.2
BuiltOn=2024-08-05 20:47
Git=6.1/467048f75ed27520b8cf7eca0ba57eeb2e0e1a0f
Encoding=UTF-8
EndpointIP=100.88.205.52
EndpointURL=http://p01-74196-app-7f98fb9cf7-5757b:8080
TimeZone=Europe/Paris
SystemDate=2024-08-22 09:02:31
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

oui exact, ce bug a été corrigé avant hier. Problème de filtre mal héritée. Ce sera livré au prochain build.

Il faut passer par la liste de toutes les Traductions et filtrer sur Link en attendant.
