# Module diff en instance distante : Traductions non prises en compte et non livrable

**URL:** https://community.simplicite.io/t/12662

## Question
### Request description


Lors d'un diff module entre pré-prod et prod, les **traductions** (labels d'attributs, d'actions objet, etc.) sont **détectées comme différentes** : leurs lignes apparaissent surlignées (orange) dans le diff.

Mais lorsque je tente de résoudre cette différence via **`Pull from remote` / `Update now`**, la plateforme affiche :

> **« Nothing to update in local DB. »**

À l'inverse, pour tous les autres éléments (objets, actions, paramètres...), le cycle détection → Push/Pull fonctionne parfaitement : la différence est bien appliquée et disparaît du diff après synchronisation.


### Steps to reproduce


1. Sur une instance, modifier une traduction (ex. label d'une action objet) en FRA et/ou ENU.
2. Lancer le Module diff (UI) entre Local et Remote.
3. Constater que la ligne de traduction est surlignée comme différente.
4. Cliquer sur `Pull from remote` (ou `Update now`).
5. Obtenir **« Nothing to update in local DB. »** → la différence persiste.

### Éléments déjà vérifiés de mon côté

* Les traductions font partie du **périmètre / scope du module**.
* **FRA et ENU activées** sur les deux instances.
* La différence de traduction est **réelle**.
* Pour les autres éléments (objets, actions, params), détection **et** Push/Pull fonctionnent normalement. 

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.3.9
Encoding=UTF-8
TimeZone=Europe/Paris
SystemDate=2026-07-06 12:53:46

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://ldm-cron.int3.applis.renault.fr
ActiveSessions=1
LastLoginDate=2026-07-06 12:37:53

[Server]
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[JavaVM]
HeapFree=225599
HeapSize=411648
HeapMaxSize=1497088
TotalFreeSize=1311039

[Cache]
ObjectCache=624
ObjectCacheMax=10000
ObjectCacheRatio=6
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Healthcheck]
Date=2026-07-06 12:53:46
ElapsedTime=7
---
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
_No answer provided._
