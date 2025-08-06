# Impossibilité de créer un objet select

**URL:** https://community.simplicite.io/t/6031

## Question
### Problem description

Il est impossible de créer un objet select sur la version 5.2.34 avec n'importe quel type de BDD.

### Steps to reproduce

![image|690x314](upload://xBf9MASa7sTOINFISxDfSrKuwCf.png)
 

### Technical information

Simplicité version 5.2.34
Built on 2023-03-12 23:41

## Answer
Il faut désormais créer avec la requête:
![image|639x474](upload://1M2Nqp3C67JPsXm1SRqo9z4ttbj.png)

Nous avons ajoutés des contrôle sur les objets select et service pour vérifier que ce qui est paramétré est bien correct (en l'occurence pour un objet select il faut un statement qui commence par `select` dans la search spec)
