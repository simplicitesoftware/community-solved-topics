# [PROBLEME] Champ Module utilisateur : champs obligatoire

**URL:** https://community.simplicite.io/t/4802

## Question
### Request description

Bonjour,

J'ai un objet métier `HrSalarie` qui extends `User`. Lorsque j'enregistre `HrSalrie`, j'ai ce message qui s'affiche :
![image|250x60](upload://uL29O7A091JIiiP8lLS2pIVCg6U.png)

Le module est pourtant bien renseigné dans l'objet parent `User` :
![image|690x210](upload://8mct6kVmnsbHfuBcNEaiXPjtxsz.png)
Voici l'objet HrSalarie (Qui extends `User` juste au dessus) :
![image|690x415](upload://x3hLrzhuMmJj32jn1uORapdgl4e.png)

Je précise que cette erreur Module ne s'affiche que à l'enregistrement de l'Objet `HrSalarie` et pas pour l'enregistrement de l'objet parent `User`.

**Avez-vous une idée ?**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.2
BuiltOn=2022-04-29 15:38
Git=5.2/a2c69b2ee78658770a248e617730e607252990ca
Encoding=UTF-8
EndpointIP=10.201.58.85
EndpointURL=http://siparex-simplicite-dev-777bcd4cfc-dqxdr:8080
TimeZone=Europe/Paris
SystemDate=2022-05-03 14:28:15
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Bonjour, 

Avez-vous implémenté le code détaillé dans ce post : https://community.simplicite.io/t/custom-user-object/3400 ? Notamment le hook `preValidate`.
