# Sélectionner un utilisateur depuis un champ dans un formulaire

**URL:** https://community.simplicite.io/t/4625

## Question
### Request description

Bonjour,

J'ai un champ qui me permet de sélectionner un utilisateur. Le problème, c'est que ce champ j'arrive à le modifier uniquement en **Designer**. Tous les autres utilisateurs n'arrivent pas à modifier ce champ (il est en lecture seul).

C'est le seul champ du formulaire qui pose problème.
De plus, tous les champs qui permettent de sélectionner un utilisateur sur mon module ont le même comportement (Du coup, je sais que ça ne viens pas du formulaire en particulier).

**PS :** Je n'ai aucune contrainte sur ces champs.

**Avez-vous une idée du problème ?**

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
SystemDate=2022-04-01 10:41:18
```
[/details]

## Answer
[quote="Elcoco, post:4, topic:4625"]
Est-ce que mettre des droits de lecture sur cet objet User pour mes 4 groupes suffiraient ?
[/quote]

:white_check_mark:

Simplicité ne laissera pas sélectionner un objet sur lequel on n'a pas les droits, j'espère que ça fait sens :slight_smile:
