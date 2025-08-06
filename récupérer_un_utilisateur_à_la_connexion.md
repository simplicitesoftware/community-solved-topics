# Récupérer un utilisateur à la connexion

**URL:** https://community.simplicite.io/t/4721

## Question
### Request description

Bonjour,

Sujet pas très important, mais j'ai une petite question :
* Lorsqu'un utilisateur se connecte à Simplicité, existe il un Hook qui permet de récupérer l'utilisateur qui en en train d'essayer de se connecter ? même chose lorsqu'il se déconnecte ?

L'objectif est de récupérer cet utilisateur (ID ou autre chose) avant même que Simplicité vérifie si le compte est actif ou non.

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
SystemDate=2022-04-15 11:12:18
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
[quote="Elcoco, post:4, topic:4721"]
`postDisconect()`. Cette méthode existe-elle (ou une méthode similaire) ?
[/quote]

C'est plutôt un équivalent  preDisconnect: [PlatformHooks.logout(g)](https://docs.simplicite.io/5/javadoc/com/simplicite/util/ScriptedPlatformHooks.html#logout(com.simplicite.util.Grant)) (après le logout, on n'a plus d'information sur le user...)

[quote="Elcoco, post:4, topic:4721"]
créer en tant que **code partagé**
[/quote]

C'est bien ça :) 


[details="Screenshot"]

![POF__preprod_|690x198](upload://e8Yl6CXs1J83IZ7ZLBOOR4NnjOc.jpeg)

[/details]

[quote="Elcoco, post:4, topic:4721"]
je n’ai pas trouvé de tutoriel à ce sujet.
[/quote]

Ça ne fait pas partie des tutos mais c'est dans l'intro de la doc [PlatformHooks](https://docs.simplicite.io/documentation/01-core/grant-code-hooks.md), si vous avez du mal à trouver l'info, je recommande [ce tips & tricks](https://community.simplicite.io/t/how-to-find-information) ;)
