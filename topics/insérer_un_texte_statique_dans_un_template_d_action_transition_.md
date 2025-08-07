# Insérer un texte statique dans un template d'action (transition)

**URL:** https://community.simplicite.io/t/4626

## Question
### Request description

*J'ai inséré un texte statique dans un template d'action (une transition d'état) mais la traduction dans la langue de l’utilisateur n'est pas affichée. Le popup ne restitue que le code.*

*This request concerns an **up-to-date** Simplicité instance
and those are the steps to reproduce it:*

![image|613x237](upload://eTnv5X9j0vwOccbSGAouoNDM0HD.png)

![image|690x286](upload://awlbumSXa9Vz8Bc5pVYpDw4xoiD.png)
 
![image|569x499](upload://8UX49V84KN9szBITsZ6r24jinzH.png)

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.36
BuiltOn=2022-03-25 23:37
Git=release/8329db12a092c6c91775901c9f207681792bbea1
Encoding=UTF-8
EndpointIP=21.0.9.4
EndpointURL=http://769167602c07:8080
TimeZone=Europe/Paris
SystemDate=2022-04-01 12:57:25
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

[details="Browser logs"]
```text
NA
```
[/details]

[details="Other relevant information"]
NA
[/details]

## Answer
[quote="Francois, post:2, topic:4626"]
Essayez avec une syntaxe en snake case “_” comme les autres
[/quote]

Bonjour François,

C'était bien ça... une fois le code reconfiguré en notation snake case ça fonctionne.
Merci beaucoup.
