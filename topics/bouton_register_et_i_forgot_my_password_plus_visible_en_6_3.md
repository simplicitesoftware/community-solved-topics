# Bouton "Register" et "I forgot my password" plus visible en 6.3

**URL:** https://community.simplicite.io/t/11942

## Question
### Request description

Bonjour, 
En version 6.3, je n'arrive plus à afficher les boutons "Register" et "I forgot my password" sur la page de login. Je ne reproduis pas sur une 5.3.
Est-ce qu'il y existe une nouvelle façon d'activer ces boutons en v6 ? 

![image|503x337](upload://8O2ql6SFI1h9I6xepSvgc3D4ZVw.png)

```
[Platform]
Status=OK
Version=6.3.7
Variant=light
BuiltOn=2026-04-03 09:45
Git=6.3/3f01baa9ac25b9b349f607f8d913f3984ec7c924
Encoding=UTF-8
EndpointIP=213.32.74.167
EndpointURL=https://cap.simplicite.io:13643
TimeZone=Europe/Paris
SystemDate=2026-04-07 15:41:27
```

## Answer
Pour password oublié il faut `USE_FORGOT_PWD=yes` **ET** le service de mail configuré.
Idem pour register il faut au moins un groupe registrable **ET** le service mail configuré.

Sans le service de mail ces 2 features ne servent à rien...

**EDIT**

NB: il doit y avoir un warning dans les logs qui dit "No mail service configuration" ou "Malformed mail service configuration: .."
