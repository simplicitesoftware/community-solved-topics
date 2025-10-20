# Migration de 5.3.71 vers 6 script rhino

**URL:** https://community.simplicite.io/t/10361

## Question
Bonjour, 

J'ai vu sur un autre topic  [Migration V5 vers V6 bloquée à cause de script Rhino encore présent](https://community.simplicite.io/t/migration-v5-vers-v6-bloquee-a-cause-de-script-rhino-encore-present/8198) qu'il fallait supprimer le code source si il était présent 
![671d1620de188d864c771c161d89ed058d2c01c6|690x330](upload://xCg4KTLeBf7qbQrkllAfGdJBk9Y.png)
Sauf qu'en 5.3.71 ce n'est plus la même façon de faire 
![image|690x224](upload://sqZwBosQcBAA09jHkmLZOWi7mGc.png)

et même principe pour le responsive5 est ce qu'il faut que je supprime toutes les ressources pour que la migration fonctionne car actuellement j'ai le même message d'erreur 
```
UPGRADE FAULT
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
This version 6 does not support Rhino script anymore to implements Hooks.\n==> All legacy Rhino scripts have to be refactored to more efficient Java classes.
==> Rhino scripts are only dedicated to expressions, calculated fields and constraints.
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
```
De plus, j'ai regardé dans la table ' m_script_usage` je n'ai que du code partagé sur des objets métiers mais en java donc est ce que ça peut poser problème étant donné que ce ne sont pas des scripts rhino ?

Merci d'avance et je ne sais pas si j'ai été assez clair

## Answer
Non il ne faut surtout pas supprimer les `Resource` web, qui ne sont pas du rhino back, mais bien du code JS front. (tout comme les hook front du modeleur en JS, cf requête de David `not like...`)

`m_script_usage` servait à utiliser/partager un script rhino dans plusieurs objet métier en back.

il faut juste vider cette table

`delete from m_script_usage`

En java V6, le code partagé rhino, si vous en aviez dans cette table (ou onglet "Script usage" des objets métier), doit être remplacé par de l'héritage ou une classe commune.
