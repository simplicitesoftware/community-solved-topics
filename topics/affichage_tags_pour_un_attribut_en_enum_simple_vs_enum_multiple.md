# Affichage tags pour un attribut en enum simple vs enum multiple

**URL:** https://community.simplicite.io/t/8933

## Question
### Request description

Bonjour,

Je rencontre un comportement différent dans l'affichage des tags lorsque l'attribut est configuré en `enum` simple ou `enum` multiple.

* Lorsque l'attribut est configuré en `enum` simple, les tags s'affichent correctement sous forme de badges colorés.
![Capture d'écran 2024-10-21 120310|623x483, 50%](upload://yGrf8ultxX72CdVGLORoW2hybPQ.png)

* lorsque l'attribut est en `enum` multiple, l'affichage n'est plus le même et les tags apparaissent sous forme de texte simple sans la mise en forme des badges.
![Capture d'écran 2024-10-21 120434|415x462, 50%](upload://5PqT5j6HW8USilKPb4J7qiFgrXU.png)

( J'ai entre les 2 screen ajouté un role à un record pour montrer que c'est multi et non simple).


Est-ce un comportement normal, et serait-il possible d'avoir le même affichage de tags (avec les badges) pour un attribut `enum` multiple comme pour la simple?



Notre UseCase se veut multiple dans le choix des roles et visuellement au niveau de l'UI avoir le 1er screen en résultat de liste.

Merci d'avance pour votre aide :slight_smile: 

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.1.6
BuiltOn=2024-09-13 16:21
Git=6.1/dfa6a2c301a0b79b7667cb2f921b3c5a38f0d51c
Encoding=UTF-8
EndpointIP=100.88.203.215
EndpointURL=http://lbc-77449-app-7ffbb96546-q82rc:8080
TimeZone=Europe/Paris
SystemDate=2024-10-21 12:13:16

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=303
EnabledUsers=22
LastLoginDate=2024-10-21 12:00:07```
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
Voilà dans la prochaine revision (6.1.12) les items d'une liste de valeur multiple s'afficheront en liste de la même manière que dans le cas d'une limite de valeur unique:

![image|690x173](upload://cxXLSA2xR3lGk75ttXpVSD8vE0a.png)

PS: ce sera backporté en v5
