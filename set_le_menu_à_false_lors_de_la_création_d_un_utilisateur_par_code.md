# Set le menu à false lors de la création d'un utilisateur par code

**URL:** https://community.simplicite.io/t/4917

## Question
### Request description

Bonjour,

Lors de la création d'un utilisateur via le code, je souhaite set le menu à false :
J'ai essayé : 
```
usr.setFieldValue("usr_menu", "0");
```
**ou**
```
usr.setFieldValue("usr_menu", 0);
```
**ou**
```
usr.setFieldValue("usr_menu", false);
```

Mais peut importe comme je l'écris, rien ne marche :
![image|512x392](upload://d3mrJI7yhJlw7pA7SXHkptxJIFR.png)

Une idée du problème ?

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
SystemDate=2022-05-30 15:22:18
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Vous pouvez garder l'héritage de SimpleUser (on vous le reccomande d'ailleurs), ajoutez simplement le champ `usr_menu` à votre objet métier.
