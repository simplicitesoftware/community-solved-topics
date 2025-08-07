# Erreur à la création d'une instance avec une pillbox intégrée

**URL:** https://community.simplicite.io/t/5790

## Question
### Request description

Bonjour,

J'ai un formulaire de création avec pillbox + Create intégrée. Depuis la 5.0 je peux directement associer avec la pillbox, mais quand j'essaie j'obtiens une erreur.

![image|690x364](upload://ddOsIVU8aGiZ6rcvjDIstspv2zs.png)

Et quand ensuite je reviens sur une nouvelle création, l'association semble être restée en mémoire

![image|652x500](upload://7oJrLMrIa4Q39rdpTtFwHIfJsF4.png)

Pouvez vous m'aider ?
Merci !
Emmanuelle



### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.26
BuiltOn=2022-12-20 22:00
Git=5.2/032e02559b23adcd0564356a4dc0444dddc989d3
```
[/details]

## Answer
Lors d'une création avec une pillobox, les références associées sont gardées en mémoire.
Au save :
- la UI commence par faire la création de A qui semble fonctionner
- puis elle boucle sur les associations pour les créer (2 appels ajax pour chacun getForCreate + create).

Les références sont stockées en mémoire, et ne sont pas dépilées en cas d'erreur, ce qui explique la rémanence pour ne pas perdre sa saisie.

Je pense que le service getForCreate de la relation avec le parent = row_id 452 en paramètre retourne une erreur. Mais il faudrait regarder plus en détail les appels Ajax et les réponses.

si c'est la cas il faudra voir pourquoi A n'est pas sélectionnable une fois créé (filtre ou search-spec sur l'objet service... ?).
