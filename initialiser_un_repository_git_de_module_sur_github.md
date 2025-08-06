# Initialiser un repository git de module sur Github

**URL:** https://community.simplicite.io/t/4651

## Question
### Request description

Bonjour,

Je souhaite mettre ne place un GIT sur un de mes modules.
J'ai suivi la procédure de ce topic : https://community.simplicite.io/t/sauvegarde-module-sur-git-externe/962/9

Le problème, c'est que mon paramétrage n'est pas pris en compte.

**Voici mon paramétrage :**
![image|690x267](upload://4QtdLEuHCYsYo6sK5tRTWeEo3Jl.png)

**Voici ce que j'obtiens :**
![image|690x138](upload://tcCQwUDTn4iBPOgEC1XfDKwgHrA.png)

On voit bien que les 2 URL ne correspondent pas.

**Quelle est le problème selon vous ?**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.36
BuiltOn=2022-03-25 23:37
Git=release/8329db12a092c6c91775901c9f207681792bbea1
Encoding=UTF-8
EndpointIP=10.201.117.42
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-06 09:26:01
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
[quote="Elcoco, post:1, topic:4651"]
On voit bien que les 2 URL ne correspondent pas.
[/quote]

Bonjour,

Ce que vous constatez est normal:
- la première est celle que vous configurez, c'est cette de votre **[remote](https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefremotearemoterepository)**. 
- a seconde est celle du repository **local**, exposé via `<url_de_linstance>/git/<nom_du_module>`

**Si on part du principe que vous n'avez jamais rien commité** (ie: sous votre second screenshot, il n'y a aucun commit d'indiqué, et sur github, le repo est vide), et que votre paramétrage se trouve sur votre instance:

1. vérifier que le repo github est vide (cet encadré "QuickSetup" n'est pas disponible sinon)

![module-test|690x403](upload://zidd2sqIP1c3liOfnlVNLUFUNP4.jpeg)

2. vérifier que le repo Simplicité est vide (si ce n'est pas le cas, cliquer sur "supprimer")

![Simplicité®|648x499](upload://hEqNBXWYwWSfm3A9XHTX7XPYX1B.jpeg)

3. faire un premier commit pour créer et initialiser le repo Simplicité:

![8a186644fd9a51a91f78ab37678772b6e84d0dc0_jpeg__JPEG_Image__1395 × 562_pixels_|690x275](upload://6PpeLU0V7lGVM5hhtNrIIKfPXvb.jpeg)

***NB: On remarque qu'il n'y a pas de bouton "pull" ni "push", cela signifie que le repo Simplicité ne connait pas la remote github!***

4. Forcer la prise en compte de la remote configurée sur le module, en sauvegardant l'objet "Module":

![Cursor_and_Simplicité®|690x368](upload://dZxSwhjwADZLusT63W3EAG30N9J.jpeg)

5. retourner sur l'interface git simplicité, et cliquer sur le bouton "push" qui est apparu:

![Simplicité®|690x375](upload://naeecUqZdX780toKZPULaI2fVzG.jpeg)

6. vérifier sur github:

![module-test|578x500](upload://mNmbBhNqjRXpOjW8UQmgkUts91l.jpeg)
