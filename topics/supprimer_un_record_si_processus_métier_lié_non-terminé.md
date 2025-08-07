# Supprimer un record si processus métier lié non-terminé

**URL:** https://community.simplicite.io/t/8866

## Question
### Request description

Bonjour à tous,

Je travaille actuellement sur un processus métier lié à la création d'un seul objet. Je souhaiterais que l'objet ne soit sauvegardé de façon définitive que lorsque l'utilisateur arrive à la fin du processus, c'est-à-dire après avoir complété toutes les étapes.

Si l'utilisateur s'arrête au milieu du processus sans le terminer, j'aimerais que l'objet soit automatiquement supprimé afin qu'il ne reste pas dans la base de données. Actuellement, l'objet est créé dès le début du processus, mais cela pose problème si le processus n'est pas finalisé.

Avez-vous une idée de comment implémenter cette logique dans Simplicité ? Existe-t-il une méthode ou un hook spécifique que je pourrais utiliser pour contrôler la suppression de l'objet en cas d'abandon en cours de route ?

Merci d'avance pour vos conseils !

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.1.6
BuiltOn=2024-09-13 16:21
Git=6.1/dfa6a2c301a0b79b7667cb2f921b3c5a38f0d51c
Encoding=UTF-8
EndpointIP=100.88.201.139
EndpointURL=http://lbc-77449-app-846c7ffb59-xl2xr:8080
TimeZone=Europe/Paris
SystemDate=2024-10-08 18:17:08

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=302
EnabledUsers=21
LastLoginDate=2024-10-08 16:56:59---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonjour Hamza,

Dans le paramétrage de votre processus, passer le paramètre de `Persistance en fin d'exécution` de vrai à faux devrait résoudre cette erreur:

![image|690x205](upload://tQWQGU30syAhM7k1WGf8d7P54xM.png)

Ce paramètre est destiné au processus de type tache humaine.

Dans le cadre d'une suite d'écrans, il n'y a pas de notion de persistance des données d'activités et de processus.

Ce paramètre devrait être ignoré dans ce cas, ce sera corriger, en attendant vous pouvez le passer manuellement à faux.
