# Bouton comparaison entre deux modules (fichier)

**URL:** https://community.simplicite.io/t/5962

## Question
Bonjour,

Je remarque une différence visuelle entre la version 5.1 et 5.2, concernant la comparaison de module par fichier.

En effet sur la 5.1, je trouve bien les boutons d'action en bas de page :
![image|690x162](upload://yfNM9ahN88VyP6rcPD05fqyayHH.png)

Cependant, sur la 5.2 je ne trouve plus les boutons :
![image|690x58](upload://en1rEgRTtxFGKnBbDBEUzQ3m2w1.png)

Ceux-ci ont ils changés de place ? Comment est il possible de générer le patch XML en 5.2 ?

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.28
BuiltOn=2023-01-20 16:41
Git=5.2/863cfad4c8c21998884a167b5f88de0c00e7d44d
Encoding=UTF-8
EndpointIP=xxx
EndpointURL=xxx
TimeZone=Europe/Paris
SystemDate=2023-03-01 08:55:27

```
[/details]

## Answer
Avec l'arrivée du format JSON dans les exports de module en arbre, le workflow ModuleDiff hérité de la V3 et qui compare le XML n'était plus utilisable dans ce contexte (il a été supprimé en 5.2).

Seul son écran de comparaison legacy XML a été gardé : fabriqué en back avec des API V3, qui ne sait pas faire de push/pull, ni fabriquer un patch partiel, etc. Mais du coup cet écran n'étant plus dans un screenflow, il n'y a plus de bouton d'action. On pourrait voir pour reconduire la partie de génération de patch mais ce n'est plus trop le sens de l'histoire.

Le comparateur JSON est plus évolué pour sélectionner tout ou partie des différences, et créer un patch XML dans un sens comme dans l'autre (push ou pull) entre 2 repository (URL/GIT/remote/fichier). 
L'export de module en fichier JSON éclatés est en train d'être revu car il pose des problèmes bloquants sur Windows (qui limite la taille des path à 256). L'arbre JSON va donc être simplifié à une seule racine.

Bref pour utiliser la fonctionnalité de génération de patch, il faudra passer vos modules en format JSON.
