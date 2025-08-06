# Choisir le séparateur d'un énuméré multiple

**URL:** https://community.simplicite.io/t/7004

## Question
### Request description

Bonjour,

Dans le cas d'un field énuméré multiple, est il possible de modifié le type de l'espaceur ?

Choisir entre ";", ",", " ", etc ?

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.13
BuiltOn=2023-09-08 13:14
Git=5.3/fca5758c61ade32f90b9f1401ebe18ec1b6d3e71
Encoding=UTF-8
EndpointIP=xxx
EndpointURL=xxx
TimeZone=Europe/Paris
SystemDate=2023-10-10 08:47:13
```
[/details]

## Answer
Bonjour,

Ce serait remonter niveau physique un besoin purement technique de transformation front, ici c'est plutôt à adresser par une **publication** sur mesure.

Sinon pour s'en passer, vous devrez pour le user/profil qui exporte :
- créer un champ calculé invisible mais exportable qui fait le "replace" souhaité
- et passer le champ ENUM d'origine en non exportable
