# Question ouverte sur l'UX du cas d'association / sélection par défaut des records précédemment associés

**URL:** https://community.simplicite.io/t/4544

## Question
### Request description

*----Lors du déroulement de la séquence d'association (contexte de vue d'une liste fille depuis un formulaire parent), le système pré-sélectionne tous les records précédemment associés. De ce fait, certains utilisateurs sont amenés à saisir des informations de détail dans le popup affiché par la suite en pensant que ces informations iront s'inscrire sur les nouvelles lignes ajoutées. Hors, comme toutes les lignes précédemment associées sont sélectionnées, les nouvelles saisies iront écraser les précédentes.----*

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and those are the steps to reproduce it:*

1.Associer un ou plusieurs records + saisir des infos de détail dans le popup proposé
2.Recommencer la séquence en ajoutant un record
3.Les infos de détail saisies en 1 sont écrasées par celles saisies en 2

![image|690x225](upload://eBuCVs372KDR6lAh4vXmVXUVpx8.png)

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=5.2.0-beta
BuiltOn=2022-03-16 17:37
Git=prerelease/96d4f99aff10712b57b11fa063570a6913648701
Encoding=UTF-8
EndpointIP=149.202.171.75
EndpointURL=http://renault.simplicite.io:10028
TimeZone=Europe/Paris
SystemDate=2022-03-17 16:02:26---
```
[/details]

[details="Simplicité logs"]
```text
---NA---
```
[/details]

[details="Browser logs"]
```text
---NA---
```
[/details]

[details="Other relevant information"]
*----NA----*
[/details]

## Answer
L'évolution a été poussée en 5.1+

Une nouvelle classe CSS **`highlight`** permet de surligner les lignes déjà liées, mais sans les cocher par défaut dans l'écran d'association en masse.

L'utilisateur devra donc 
- cocher les nouvelles lignes à associer 
- et/ou re-cocher celles à modifier si la N,N possède des attributs non clés
