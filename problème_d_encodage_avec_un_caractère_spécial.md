# Problème d'encodage avec un caractère spécial

**URL:** https://community.simplicite.io/t/5233

## Question
### Request description

Bonjour,
J'ai un problème d'encodage avec le Ô. Dans le titre il apparaît correctement mais dans le champ nom le circonflexe se transforme en tréma.

J'ai essayé de ressaisir le champ sans succès :-/

![image|690x182](upload://trCBKIGBj8Q5IB9TQYoKRYHTkss.png)

Merci d'avance pour votre aide !
Emmanuelle

### Technical information

[details="Instance /health"]
```text
Status=OK
Version=4.0.P25
BuiltOn=2022-05-24 11:34 (revision 21f6d6308a3d6a0b1abf0cb8d5de537157727df2)
Encoding=UTF-8
```
[/details]

## Answer
Ca semble juste être un pb d'affichage en input box:

A zoom 100% ça semble être un Ö:
![image|349x255](upload://w28l9S3TKt2LMoeh9tZCLXO6lJ7.png)
Mais à 125% on voit bien que c'est un Ô:
![image|383x304](upload://sjHiA3NPTsKKURBqS79eKXcurFk.png)

D'ailleurs en liste on voit que c'est OK:
![image|522x275](upload://fyGOC4Oqepj6VaxK9QrqZytIEwx.png)

En changeant la taille de la police il y a des tailles où c'est OK:
![image|690x388](upload://n2VljJrMYk3vXTsN3p4kvbkmLKA.png)

J'ai testé sur une page de test Boostrap et il y a le pb:
![image|690x245](upload://laSvvtbWG5Nsz89rQuOk0Gr3YF2.png)

Bref, il faut plutôt adresser la demande au support Boostrap...
