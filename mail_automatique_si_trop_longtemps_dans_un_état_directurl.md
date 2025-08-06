# Mail automatique si trop longtemps dans un état + DIRECTURL

**URL:** https://community.simplicite.io/t/4769

## Question
### Request description

Bonjour,

J'aimerais pouvoir envoyer un mail quand un objet est resté trop longtemps dans un état sans changer (disons tous les mois).

Voici la configuration de mon état :
![image|690x175](upload://z1iqZhmqtFlrjIBXGOLtGwPJ2Nn.png)
(Relance toutes les 10 secondes pour pouvoir tester rapidement)

Voici la configuration de mon alerte :
![image|690x292](upload://fxbxLbG5axSGETVwlrLfzYXyOOJ.png)

Je ne reçois aucun email.
**Quelle est le problème selon vous ?**

**PS :** Je précise que je possède bien un objet dans cette état là. Donc l'alerte devrait se déclencher 1 fois.
![image|690x140](upload://jpbfJVFBljime4CUU9vGLV1oIE1.png)


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
SystemDate=2022-04-26 09:48:04
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Aucun soucis avec [DIRECTURL]. 

Vous ne devez pas voir correctement configuré le paramètre système `DIRECT_URL`
exemple DIRECT_URL = https://app.mydomain.fr

C'est l'URL publique de votre application (et non pas un localhost:8080 ou un domaine inaccessible depuis un email que Gmail doit tronquer car invalide), le serveur tomcat ne parvient pas toujours à savoir 'qui il est' depuis l'extérieur, il faut l'aider. 

ensuite le token [DIRECTURL] sera bien subdtitué avec DIRECT_URL + tiny URI de votre objet

`<a href="[DIRECTURL]">GOTO ORDER</a>`
`<a href="https://app.mydomain.fr?f=DemoOrder;4">GOTO ORDER</a>`
