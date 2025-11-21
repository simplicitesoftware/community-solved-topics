# Bloquer l'UI du formulaire lors d'action asynchrone

**URL:** https://community.simplicite.io/t/10964

## Question
### Request description

**Bonjour,**

Dans notre cas d’usage, nous avons un traitement qui, dans le pire des cas, peut durer jusqu’à 5 minutes. Ce traitement est actuellement déclenché par une action synchrone, ce qui impacte l’expérience utilisateur.

Nous souhaitons le rendre asynchrone afin de restituer rapidement la main à l’utilisateur, tout en poursuivant le traitement en arrière-plan.

Dans ce contexte, existe-t-il une fonctionnalité standard permettant de :

* désactiver temporairement l’édition des champs du formulaire concerné

* empêcher l’exécution d’autres actions sur ce formulaire

L’objectif est d’éviter toute interaction concurrente ou incohérente pendant que le traitement asynchrone s’exécute.

Merci d’avance pour votre aide !

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.15
BuiltOn=2025-08-15 11:39
Git=6.2/309efbdf46b217e3145711d1c47c3e5ad5459aa5
Encoding=UTF-8
EndpointIP=100.88.192.96
EndpointURL=http://lbc-77449-app-79d865f799-46gds:8080
TimeZone=Europe/Paris
SystemDate=2025-11-04 10:05:35

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://ldm-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=2
LastLoginDate=2025-11-04 10:05:10

[Server]
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true

[JavaVM]
HeapFree=111999
HeapSize=266240
HeapMaxSize=5636096
TotalFreeSize=5481855

[Cache]
ObjectCache=319
ObjectCacheMax=10000
ObjectCacheRatio=3
ProcessCache=2
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Healthcheck]
Date=2025-11-04 10:05:35
ElapsedTime=9
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
[quote="JordanSO, post:13, topic:10964"]
actions synchrones avec job interne asynchrone qui ont une transition d’état
[/quote]

Une Transition n'est effectivement pas comme une Action utilisateur, l'action qui est liée sert juste à afficher un bouton de transition qui lancera un update du statut + appels des callback paramétrés en synchrone. Une transition d'état n'a jamais été conçue pour lancer des taches longues/asynchrones. Donc la mécanique asynchrone via AsyncTracker n'existe pas dans ce contexte (l'invoke method de la transition ne doit pas trouver cette signature).

A mon avis : 
- il faut retirer l'action de votre transition, pour qu'elle soit similaire aux autres
- et lui rajouter l'update de l'état qui ne sera pas fait tout seul
