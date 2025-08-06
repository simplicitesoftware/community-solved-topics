# Rendre obligatoire des attributs non persistés dans un processus

**URL:** https://community.simplicite.io/t/8843

## Question
### Request description

Bonjour,

Je travaille avec un objet qui peut être créé via un processus métier. 
Dans ce processus, j'ai des attributs persistés et non persistés qui sont calculés à l'aide d'expressions calculés.Ses attributs non persisté affiche ce que l'utilisateurs a sélectionner qui a été creer dans une table d'association à cette objet au niveau du back_end

Dans la méthode `preLock` du processus, je rends les attributs obligatoires dans l'activité associés pour empêcher l'utilisateur de passer à l'étape suivante sans les remplir. Cela fonctionne bien pour les attributs persistés, mais pas pour les non persistés.

Par exemple, dans la capture d'écran ci-jointe, l'attribut persisté **Pays de déploiement (Zone Géographique)** est bien marqué comme obligatoire et le système applique correctement cette contrainte. Cependant, l'attribut non persisté **Périmètre** n'a pas le même comportement, et l'utilisateur peut continuer sans le renseigner.

![Capture d'écran 2024-10-04 170443|690x326, 75%](upload://cTb0sUQEgNiYgYOfa5qLOUlONAA.png)

Pour donner un peu + de contexte, nous utilisons plusieurs attributs non persisté dans ce processus pour que l'utilisateur fasse des choix sans passer par une pillbox ( choix vers un autre objet de relation N:N avec création d'un record dans la table d'association) et avoir une meilleur expérience utilisateur pour lui.

Y a-t-il un moyen de rendre les attributs non-persistés obligatoires, soit via le back-end, soit via le front-end ? Des suggestions pour faire respecter cela au niveau de l'interface utilisateur ?

Merci d'avance pour votre aide !

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.1.6
BuiltOn=2024-09-13 16:21
Git=6.1/dfa6a2c301a0b79b7667cb2f921b3c5a38f0d51c
Encoding=UTF-8
EndpointIP=100.88.201.139
EndpointURL=http://lbc-77449-app-846c7ffb59-xl2xr:8080
TimeZone=Europe/Paris
SystemDate=2024-10-04 17:24:37

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=2
TotalUsers=302
EnabledUsers=21
LastLoginDate=2024-10-04 16:00:03

[Server]
ServerInfo=Apache Tomcat/9.0.94
ServerType=WEB
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true---
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

Votre code utilise bien l'instance du processus :
```java
ObjectDB o = getGrant().getProcessObject("LbcLegalText");
o.getField("LegalTextScope").setRequired(true);
```

Je ne reproduis pas le problème avec un champ non persistant obligatoire dans un processus.

- Il est bien requis lors de la validation de l'activité qui appelle le `validate` de l'objet.
Il y a peut-être du code dans l'objet métier `LbcLegalText` lui-même qui joue avec `LegalTextScope` ?

- N'étant pas persistant, si on revient en arrière dans le processus, il n'a plus de valeur car la UI refait un `select` complet de l'objet en base. Si vous avez encore la bonne valeur c'est que du code la remet quelque part (champ calculé ou `postSearch` de l'objet).

Utiliser un champ non persistant/calculé dans l'objet pour "orienter" la suite du processus n'est pas une bonne idée, en tout cas vous oblige à penser/coder à tous les cas d'usage pour contourner la non persistance ou la non appartenance réelle à l'objet : 
- autant le rendre persistant si c'est un information métier comme un autre au choix de l'utilisateur,
- ou créer une étape de routage pour sortir les "faux" attributs de l'objet / activité de condition qui possède des attributs dédiés au processus pour demander à l'utilisateur ce qu'il veut faire ensuite (exemple dans le process de création d'un User, le process demande si l'utilisateur veut ajouter un groupe de droit `AddGroupChoice` en boucle)
