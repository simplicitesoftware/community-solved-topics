# Problème de recherche globale avec enums multiples sur objets indexés

**URL:** https://community.simplicite.io/t/8765

## Question
### Request description


Bonjour,

Je rencontre un problème avec la fonctionnalité de recherche globale lorsque des enums multiples sont présents sur des objets indexés.( dans le cas de la sélection multiple et non unitaire).

### Steps to reproduce

Dans un premier temps, j'ai effectué une recherche globale sur un objet avec une enums multiples ( lié au pays de déploiement) dans sa clé fonctionnelle, et je n'ai obtenu qu'un seul enregistrement en sortie.
![Capture d'écran 2024-09-17|690x178, 75%](upload://hg1xFPDA6LgUQswnNjP3rkwGRxR.png)

 Les valeurs d'enum étaient séparées par un "/" sans espace dans le texte complet de l'index de l'objet, ce qui a causé l'échec de la recherche pour certains termes spécifiques.( dans notre example france/spain).
![Capture d'écran 2024-09-17|690x125, 75%](upload://gkPi2ZYtzVDpuMI0c4OKkrsoGfi.png)


Pour investiguer, j'ai modifié l'index en changeant la séparation des valeurs d'enum par des virgules au lieu de "/". 
![Capture d'écran 2024-09-17 |690x358, 50%](upload://nz5xqztuUXR7gYIcnBwu1pqg5E9.png)

Après cette modification, la recherche globale a fonctionné correctement, retournant les résultats attendus. ( avec une ou plusieurs valeurs dans cette enum multiple).
![Capture d'écran 2024-09-17|690x174, 75%](upload://pqGPitBdwOEXIAY8C9joab5oqdu.png)


Comment pourrais-je configurer ou normaliser cette séparation dans les indexes pour que la recherche globale soit fiable et dans le standard Simplicité ?

Merci d'avance pour votre aide,

Cordialement,

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=6.1.6
BuiltOn=2024-09-13 16:21
Git=6.1/dfa6a2c301a0b79b7667cb2f921b3c5a38f0d51c
Encoding=UTF-8
EndpointIP=100.88.204.156
EndpointURL=http://lbc-77449-app-846c7ffb59-g486c:8080
TimeZone=Europe/Paris
SystemDate=2024-09-17 12:16:39

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=312
EnabledUsers=24
LastLoginDate=2024-09-17 12:00:03


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
Bonjour,

Effectivement l'indexation concatène les `field.getDisplayValue()` des champs indexables (valeurs traduites et pas les codes en base). Après vérification, cette méthode utilise un `/` par défaut pour séparer les valeurs d'un énuméré multiple.

Sur PGSQL nous venons de changer la requête de recherche fulltext pour être plus user-friendly, on va en profiter pour remplacer le séparateur par un simple espace lors de l'indexation.

Il faudra réindexer vos données à la prochaine livraison 6.1.7.
