# Read only en designer sur table des crons

**URL:** https://community.simplicite.io/t/5044

## Question
### Problem description

Connecté en designer dans la table cron table, le formulaire est en read only.

### Steps to reproduce

![image|690x258](upload://kjwhrwOApIolSfeLjoFSa2kUzJ.png)
 

### Technical information

[Platform]
Status=OK
Version=5.1.44
BuiltOn=2022-05-10 18:36
Git=5.1/a51516647c95b8cab51e136ca72a2a5e5c30e27c
Encoding=UTF-8
EndpointIP=*****
EndpointURL=http://*****
TimeZone=Europe/Paris
SystemDate=2022-07-06 09:10:49

## Answer
Après vérification, des droits avait été ajoutés dans la fonction "CronTable-CMS-V". La suppression a permis de revenir à l'état normal.
