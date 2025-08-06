# Masquer / afficher un onglet en mode création

**URL:** https://community.simplicite.io/t/6028

## Question
### Description

*J'aimerai masquer un onglet de formulaire en mode création*

### Etapes pour reproduire

*J'ai reproduit ce qui est décrit ci-dessus sur une instance Simplicité **à jour** et les étapes pour reproduire sont les suivantes:*

```
$('[href="#tabs_work_0_1"]', ctn).hide();
```
J'ai essayé plusieurs choses, mais rien ne fonctionne.

### Information techniques

[details="/health de l'instance"]
```text
---Simplicité version5.2.34
Built on2023-03-12 23:41
Git info5.2/697013c6a37b540d228bc254e05fa056ea67ecc9
Database level5;P02;14f8034ce5a285931ca480a5451ce96e
EncodingUTF-8 (system encoding UTF-8)
Time zoneEurope/Zurich
OSLinux amd64 3.10.0-1160.83.1.el7.x86_64
ServerApache Tomcat/9.0.73 WEB
DatabasePostgreSQL 9.2.24 using BLOBs
JVM11.0.18 Red Hat, Inc. OpenJDK 64-Bit Server VM 11.0.18+10-LTS
Script enginerhino Rhino 1.7.13 2020 09 02
Additional libsApache POI, Docx4j, Apache Tika, JGit, Apache JClouds, Google APIs, Google APIs Firebase
Application name
Context URLhttp://lsllcot01.lausanne.ch:20378
End-pointhttp://lsllcot01.lausanne.ch:20378
Userherve5---
```
[/details]

[details="Logs Simplicité"]
```text
---copier ici les logs serveur **pertinentes**---
```
[/details]

[details="Logs du navigateur"]
```text
---copier ici les logs navigateur **pertinentes**---
```
[/details]

[details="Autres informations pertinentes"]
*----Ex: indiquer le type de dépliement, le type et la version du navigateur, etc.----*
[/details]

## Answer
Bonjour, 

Est-ce qu'il s'agit d'un onglet d'objet lié ou d'une zone d'attribut ?

Dans les deux cas, ça peut être facilement implémenté via une Contrainte dont l'impact porte sur la visibilité de la Zone d'attributs ou la relation d'objet :
![Capture d’écran 2023-03-13 à 11.43.11|689x392](upload://ArLN066r0yKxQMxJX5V3ux2XkB9.png)
