# Metadata in Object

**URL:** https://community.simplicite.io/t/9424

## Question
### Request description

Bonjour, 

J'aimerai savoir comment je peux faire pour forcer un éléments qui vient d'une autre instance de simplicité dans un objet à avoir les metadata que je veux :

![image|504x102](upload://bH3v8cjWlx6cQuBMjD2oTYysusN.png)
 

### Technical information

[details="Instance /health"]
```
[Platform]
Status=OK
Version=5.3.61
BuiltOn=2025-01-16 09:26
Git=5.3/00544332802a4dc0aa22e4306929d5cd30ff9a5c
Encoding=UTF-8
EndpointIP=100.88.64.29
EndpointURL=http://rfs-70537-api-b7f596fbc-vhskq:8080
TimeZone=Europe/Paris
SystemDate=2025-01-23 14:50:38
```
[/details]

## Answer
Les remote objets sont vus comme des objets métiers par la plateforme. 
Vous pouvez surcharger le titre par paramétrage 
![image|658x499](upload://heloL8gdLOEWrWDi6LkF6fbtJic.png)
Par défaut il met la traduction de l'objet : valeur de la clé fonctionnelle. 
Vous pouvez afficher la valeur d'un ou plusieurs autres champs en utilisant

> [VALUE:fieldname]
