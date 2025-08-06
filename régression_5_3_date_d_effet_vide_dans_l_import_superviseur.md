# Régression 5.3: date d'effet vide dans l'import superviseur

**URL:** https://community.simplicite.io/t/6868

## Question
### Request description

Bonjour,

Suite à notre mise à niveau en PROD ce dimanche, passage 5.2 à 5.3, nous avons eu une remonté côté métier, nous indiquant que la date d'effet de l'import superviseur, ne se remplit plus, CF image ci après :

![image|690x480](upload://kv1CJa05LJKQduF1JGkxrxLqTuh.jpeg)

Merci d'avance,

Benoît

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.11
BuiltOn=2023-08-07 15:27
Git=5.3/015368bc51913a479e8d682d65ea405c12b45951
Encoding=UTF-8
EndpointIP=xxx
EndpointURL=xxx
TimeZone=Europe/Paris
SystemDate=2023-09-13 09:51:19
```
[/details]

## Answer
Ok vu et corrigé,

Cela fait suite à une optimisation pour ne pas importer un fichier XML vide (si l'adapter ne retourne rien car traite directement les données sans retourner de flux XML).

Seul l'import XML final mettait l'import dans un état "en cours" en précisant la date effective de lancement. Vu qu'il n'est plus appelé, l'état "en cours" et la date d'effet seront positionnés dès le lancement de l'adapter.

Si l'adapter termine correctement, le statut "Import OK" sera toujours positionné.
