# Chat non disponible pour les utilisateurs mais pas pour les administrateurs

**URL:** https://community.simplicite.io/t/4916

## Question
### Request description

Bonjour,

Quand je suis connecté sur un compte administrateur Simplicité, j'ai le Chat qui est présent :
![image|690x78](upload://aRnFpOEK7dGuwI5N8y8tXYOQ2FS.png)

Mais quand je suis connecté en tant qu'utilisateur normal, je n'ai plus accès à ce Chat.
![image|628x121](upload://wjOrlUbbcdGGHaWOzK9i45j6VFK.png)

Je suppose qu'il doit y avoir quelque part dans Simplicité le moyen de mettre des droits d'accès sur le Chat, mais je n'ai pas trouvé de documentation à ce sujet. Pourriez-vous m'aider ?

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.5
BuiltOn=2022-05-25 15:54
Git=5.2/ecae3b828f4cb7eda5e0e6f6e018fca9b12483d7
Encoding=UTF-8
EndpointIP=10.201.58.89
EndpointURL=http://siparex-simplicite-dev-5475d8459-r9nqn:8080
TimeZone=Europe/Paris
SystemDate=2022-05-30 11:10:06
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Bonjour, 

Le social post (chat) est disponible lorsque le compte est habilité au groupe `SOCIAL_USER` ou `SOCIAL_ADMIN`.

Si vous souhaitez que tous vos comptes soient habilités à un de ces groupes, je vous encourage à utiliser la mécanique de "Profil", comme pour le groupe `DEMO_USER` de la démo.

![image|690x434](upload://eaI5YuX60rdIsFDYrhiSkN5PSRu.png)
