# Ne pas journaliser un attribut dans le journal des modifications

**URL:** https://community.simplicite.io/t/8856

## Question
Bonjour,
Est-il de bypasser la journalisation d'un attribut dans le journal des modifications, (champ purement  technique de l'objet non visible dans le formulaire)?
Cordialement,

Status=OK
**Version=5.3.44**
BuiltOn=2024-07-25 12:00
Git=5.3/d6ccd2b5c05c441d375ae66eaa8a3005e5fdf4e5
Encoding=UTF-8
EndpointIP=127.0.0.1
EndpointURL=https://XXXXXXXXXXXXX:11403
TimeZone=Europe/Paris
SystemDate=2024-10-07 12:13:10

## Answer
Bonjour,

Le journal est techniquement la sérialisation des Undo/Redo (des ObjectXML) en JSON et en HTML. Il n'y a pas de notion de visibilité des champs.

Le champ est exporté dans le redo XML, et donc dans le Journal, s'il est **exportable**.
Il faut donc le paramétrer comme non exportable ou alors par code `f.setExportable(false)`
