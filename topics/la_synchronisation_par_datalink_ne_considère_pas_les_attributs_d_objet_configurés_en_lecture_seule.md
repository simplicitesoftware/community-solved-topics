# La synchronisation par DataLink ne considère pas les attributs d'objet configurés en lecture seule

**URL:** https://community.simplicite.io/t/8413

## Question
### Request description

*La synchronisation par DataLink ne considère pas les attributs d'objet configurés en lecture seule. Dans ma configuration, j'ai un master en 5.3.41 et un slave en 6.0.14. Je ne pense pas que ça puisse participer au problème mais je le précise au cas où ça aurait de l'importance.*

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1. Master en v5.3 avec objet métier avec des attributs obligatoires (dont ceux de la clé fonctionnelle) et en lecture seule (valeur calculée).
2. Slave en v6.0.14 avec le même objet.
3. DataLink du slave vers le master configuré sur le slave.
4. Activer manuellement la synchronisation (date de référence 2001-01-01).
-> Dans les logs du slave qui fait tourner la tâche pullData on retrouve des erreurs de create précisant que les composantes de la clé fonctionnelle ne sont pas valorisés alors que sur le master les valeurs sont correctes.

5. Sur le slave, reconfigurer les attributs concernés en "Modifiable partout".
6. Réactiver la synchronisation.
-> Les records sont bien créés sur le slave sans erreur.
 
### Technical information

[details="Instance /health"]
slave
```
[Platform]
Status=OK
Version=6.0.14
BuiltOn=2024-06-24 16:23
Git=6.0/29f59bbf1de2a4950b4a895775bf235e3f36d888
Encoding=UTF-8
EndpointIP=100.88.194.221
EndpointURL=http://bca-71077-cron-7bc57876b5-kmlf6:8080
TimeZone=Europe/Paris
SystemDate=2024-06-27 08:57:06
```
master
```
[Platform]
Status=OK
Version=5.3.41
BuiltOn=2024-06-24 16:50
Git=5.3/f7dbbac3ae45828276ade2d0451b56cbafd3dbb9
Encoding=UTF-8
EndpointIP=100.88.201.253
EndpointURL=http://bca-68521-cron-75945fddff-xqsgf:8080
TimeZone=Europe/Paris
SystemDate=2024-06-27 08:58:10
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
Il faut considérer la synchro comme une interface ou un usage particulier.
- L'usage UI ou via API est métier : ton pattern fermé par défaut est parfait
- La synchro est d'un ordre technique : il faut un autre pattern "tout ouvert"

L'utilisateur (d'un groupe particulier) à utiliser pour la synchro doit donc avoir les objets entièrement modifiables (CRUD + attributs R/W).

La V6 apporte des permissions qui peuvent surcharger les attributs d'objets (obligatoire, modifiable...) par groupe, c'est propre mais ca va être fastidieux si tu en as bcp.

Sinon pour factoriser le code, si tes objets héritent tous d'un objet Java, mettre dans le postLoad global un code générique, du style :

```java
// technical synchro = all rights
if (getGrant().hasResponsibility("MY_GROUP_SYNCHRO"))
  for (ObjectField f : getFields())
    f.setUpdatable(ObjectField.UPD_ALWAYS);
```

ou ajouter directement la règle dans tes codes métier qui changent les accès ouvert/fermé...
