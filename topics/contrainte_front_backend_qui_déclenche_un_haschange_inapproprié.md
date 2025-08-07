# Contrainte Front/Backend qui déclenche un hasChange inapproprié

**URL:** https://community.simplicite.io/t/8897

## Question
### Request description

Bonjour,

Sur une contrainte Front/ Backend, j'ai un impact de type modification de liste de valeur qui déclenche un hasChange inapproprié alors qu'il n'y a aucune modification de valeur sur le formulaire ce qui délcenche la popup de confirmation de sauvegarde alors que l'on clique uniquement sur le bouton "Fermer"
Cette popup ne devrait pas être affichée.

### Steps to reproduce

Paramétrage :

![image|690x271](upload://fKUhq7LdOYBmv9KYs57w3A1MmLo.png)


### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
**Version=5.3.48**
**BuiltOn=2024-09-13 14:47**
Git=5.3/eabe8a342a09dc94a30086ecc233891e8b706ef7
Encoding=UTF-8
EndpointIP=XXXXXXXXXX
EndpointURL=http://XXXXXXX:8080/simplicite
TimeZone=Europe/Paris
SystemDate=2024-10-16 09:12:58

[Server]
ServerInfo=Apache Tomcat/9.0.87.redhat-00003
ServerType=WEB

[JavaVM]
Version=17.0.11
Vendor=Red Hat, Inc.
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.11+9-LTS

[Database]
Vendor=4
VendorName=oracle
ProductName=Oracle
ProductVersion=Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.24.0.0.0
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

## Answer
Ce sera livré sur toutes les versions.

On en a profité pour créer une méthode helper qui fait tout ça en front, elle sera appelée par la contrainte, mais pourra être utilisée simplement par les hooks front pour recharger une liste dynamiquement :

```js
myfield.ui.setList("MY_LOV_NAME")`
```

A savoir :
- Appeler le back-end pour recharger le tableau des items `myfield.listOfValues`
- Redessiner la UI `myfield.ui.redraw()` = select2 / radio buttons...
- Appliquer le `myfield.ui.change()` que si la valeur n'existe plus = le champ est retourné à vide
