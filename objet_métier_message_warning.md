# Objet métier message warning

**URL:** https://community.simplicite.io/t/4764

## Question
### Request description

Bonjour,

Sur mon objet métier, j'ai ceci comme message :
![image|648x500](upload://5D6YD9hqNXUALknG2rJuesHFA4U.png)


Voici mon MCD :
![image|690x364](upload://gsYUcCjVt5haCjdRKzU4CvuSC8r.png)


Sachant que ma table `DdvFndPart` est seulement une table de relation n-n entre `DdvFund` et `DdvParticipation`. Je ne veux pas mettre de lien vers `DdvTeam` ou `DdvSgp` dans `ddvFndPart`.

Suis-je obligé ? ou est-ce que je peux juste ignorer le message ?

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.39
BuiltOn=2022-04-13 18:24
Git=release/e929cbae23c2441b4cb0a66b9501de0159ee7c92
Encoding=UTF-8
EndpointIP=10.201.117.43
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-25 10:00:45
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Bonjour, 

Il ne s'agit pas de créer un lien vers ces autres objets, simplement d'ajouter à la table `DdvFndPart` les attributs qui composent la clé fonctionnelle des objets liés.
