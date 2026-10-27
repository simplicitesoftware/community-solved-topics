# Versions de la librairie Google Cloud Storage embarquée dans Simplicité v6.3

**URL:** https://community.simplicite.io/t/13387

## Question
### Request description

Bonjour,

Nous mettons en mettre en place une feature de mirroring entre la BD et Google Cloud Storage (GCS) : certains documents sont copiés dans un bucket GCS, d'où ils peuvent être restauré à la demande dans l'application. Nous avons donc un besoin fort de pouvoir vérifier l'intégrité des documents stockés dans GCS avant de les restaurer.(Contexte de gestion de documents à valeur juridique).

Nous avons reçu une communication de Google annonçant qu'à partir de la version 2.62 du SDK Java Google Cloud Storage, les checksums (CRC32C) sont calculés et validés automatiquement à l'upload. Cela nous intéresse directement.

Lien vers la communication : [https://docs.cloud.google.com/storage/docs/data-validation?hl=fr]

En regardant notre image Simplicité, nous constatons que la librairie Google Cloud Storage est présente en version 2.54.0 (google-cloud-storage-2.54.0.jar), ainsi qu'une seconde fois en version 2.7.0 (google-cloud-storage-2.7.0.jar, et googlecloud-2.7.0.jar). Nous n'ajoutons aucune librairie de notre côté dans l'image.
![image|690x361, 75%](upload://iEqn9Qhzxi60VrvPbsjvsfzU8oC.jpeg)




**\*\*Nos questions\*\***

1\. Pourriez-vous nous éclairer sur la présence de ces deux versions, et nous indiquer laquelle est effectivement utilisée par la plateforme ?

2\. Une montée de version de cette librairie vers la 2.62 ou plus est-elle envisagée dans une prochaine version de Simplicité ? Si oui, à quel horizon ?

Merci d'avance pour votre retour.

Cordialement, 

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
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
