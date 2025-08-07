# [Problème] Filtre SQL sur une relation

**URL:** https://community.simplicite.io/t/4525

## Question
Bonjour,

J'ai le MCD suivant (la table barré n'intervient pas dans le problème):
![image|447x500](upload://Z5oEPlHMqYBwMh2INPXXoEdqFt.png)

Lorsque je créer un objet `DdvPower`, je veux que dans la popup qui me permet de sélectionner un Fonds de la table `DdvFond` je n'ai de listé que les Fonds qui ont la participation 
de la table `DdvGeneralMeeting`. La liste des fond et de leurs participations ce fait dans la table `DdvFndPart` (cette table est une relation n-n entre `DdvFund` et `DdvParticipation`).

J'ai du mal à trouver le filtre SQL à mettre en place sur la relation entre `DdvPower` et `DdvFund`. De plus, peu importe le filtre que j'écris, j'ai cette erreur.
![image|690x328](upload://ujXpfaRhAflV3gvg6WMWMkSBQlX.png)

**Pouvez-vous m'aider à trouver le filtre SQL à écrire ?**

![image|458x159](upload://e2EIk6wUy8CDLy2BNqXk6E4iAyo.png)

## Answer
Le filtre spécifique de relation est utilisé pour les liens virtuels. 
https://docs2.simplicite.io/lesson/tutorial/development/virtuallinks
