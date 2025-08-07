# [PROBLEME] Clef technique null

**URL:** https://community.simplicite.io/t/4809

## Question
### Request description

Bonjour,

Depuis la mise à jour 5.2, lorsque j'enregistre mon objet `DdvVoting`, j'ai cette erreur : 
![image|690x374](upload://qgEMWL6CN2DgAjBD2FZMnoSUuDW.png)

Je ne comprends pas pourquoi puisque ça fonctionnait avant et que le **nom de la décision**, le **nom de l'équipe**, la **politique de vote**, la **condition** sont bien ramenés dans le formulaire quand je clique sur la loupe et que je choisis et tous ces champs se base sur la clef technique **PossessId**.

Dans le `preValidate`, j'affiche cet ID et il est `null` alors qu'il ne devrait pas l'être.
![image|690x8](upload://ij956EeGru30E8wxgnV8JePcMWi.png)
```
AppLog.info("============= Posse ID : " + getFieldValue("ddvVotPossessId"), getGrant());
```

Voici mon MCD :
![image|482x500](upload://ahkoQXjEJTOecfXf1IlwaG8sB6b.png)

Voici la configuration de la clef technique :
![image|690x324](upload://xhZZdvvFIyhM60qq5zR3eMAUQUD.png)

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.2
BuiltOn=2022-04-29 15:38
Git=5.2/a2c69b2ee78658770a248e617730e607252990ca
Encoding=UTF-8
EndpointIP=10.201.58.66
EndpointURL=http://siparex-simplicite-dev-777bcd4cfc-dqxdr:8080
TimeZone=Europe/Paris
SystemDate=2022-05-04 11:32:55
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
C'est réglé pour Posséder du moins.
J'ai simplement supprimé la relation entre Posséder et Equipe. 
Puis je l'ai recrée via le template editor de l'objet : 

![Capture d’écran 2022-05-05 à 13.54.37|690x388](upload://3YZbRnUw4HTjS6pBqL1kDr3569p.jpeg)
![Capture d’écran 2022-05-05 à 13.54.44|690x388](upload://kmXY9pkIPBBfVNOq4NBxx0eOoF5.png)
![Capture d’écran 2022-05-05 à 13.54.56|690x388](upload://gLQEFR4v7efArw4ABFwo56JYqGB.png)
