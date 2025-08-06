# Disparition de tous les grant sur les fonctions & Contraintes non exécutée

**URL:** https://community.simplicite.io/t/4670

## Question
### Request description

Bonjour,

J'avais une fonction avec plusieurs groupes en tant qu'habilitation.
Je voulais les supprimer. J'ai donc cliquer sur le bouton "Tout sélectionner".
![image|690x148](upload://opRioX3zskdpJgu0XHAZweaRgjm.png)

J'ai ensuite fait une suppression de masse.
![image|690x169](upload://zcf4btLqUliMr8qdgTEsMcGwULL.png)

Un bug c'est alors produit. Tous les Grants (habilitations) de toutes mes fonctions de tous mes modules créé ont été supprimé.
Il s'agit pour moi d'un bug de l'application, mais je voulais avoir votre avis avant.

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.37
BuiltOn=2022-04-05 11:19
Git=release/0d9c19594e35d74bd1dead5960d3b31b37337814
Encoding=UTF-8
EndpointIP=10.201.117.1
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-08 09:30:49
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Bonjour,

J'ai importé votre module sur une instance vierge, et ai créé une AG avec un état post "création". J'ai constaté les logs suivants:

![System_log|690x304](upload://ocBSQJu7XWMSUuqJYc3KZAJmw9p.jpeg)

Ladite ligne 14, correspondant à la dernière contrainte ajoutée, révèle l'usage d'une syntaxe `[STATUS:dvdMetState]` non reconnue par Simplicité (c'est soit `[STATUS]` soit `[VALUE:dvdMetState]`).

En corrigeant la contrainte en question, tout semble rentrer dans l'ordre.

----

Au-delà de la question de configuration, vous avez eu du mal à diagnostiquer le problème:

1. parceque vous n'avez pas essayé de reproduire le problème sur une instance vierge => peut-être n'êtes vous pas en capacité de lancer facilement des instances vierges? Dans ce cas, il faut monter en compétences sur les [devops Simplicité](https://community.simplicite.io/t/devops-services-offer/4508)
2. parceque le log event `ECORESC002` précisément en place pour détecter les contraintes mal rédigées, ne semble pas se déclencher sur votre instance. On va investiguer.
