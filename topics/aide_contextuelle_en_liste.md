# Aide contextuelle en liste

**URL:** https://community.simplicite.io/t/11741

## Question
### Request description

Bonjour,

J'ai configuré une aide contextuelle sur un objet avec Context = List et Update form

![image|577x138, 75%](upload://dMEE7egwPPFAQ7WmYRKWDh1wFYn.png)

L'aide s'affiche en form mais pas sur la liste, y a-t-il quelque chose à faire au niveau du template ?
Dans Network je vois que le get renvoie bien mon aide pour le form mais pas le search pour la liste.

![image|690x195](upload://dPNh9OzSyw8zNh1PHgrlogAZ5CW.png)

![image|690x149](upload://wRbxEIdEBVTpPmpzRF5Ka799Lsb.png)

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.4
BuiltOn=2026-02-16 12:31

## Answer
Il faut configurer une aide avec un contexte "Linked list" ou "Liste liée"

Configuration :
![image|690x273](upload://ryoqPJ0umfBUFsiLKEmnbK6ZnFn.png)
Résultat : 
![image|690x381](upload://i6ER9y0jaDp3WTGTiWBXw6xVfEl.png)
