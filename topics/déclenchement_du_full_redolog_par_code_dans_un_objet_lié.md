# Déclenchement du Full redolog par code dans un objet lié

**URL:** https://community.simplicite.io/t/7160

## Question
### Request description

Bonjour, j'ai un objet A relié par un objet NN à un objet B.
L'objet B a l'option full redolog activée.
Dans le code de l'objet A, j'effectue des modifications sur l'objet B, mais cela n'ajoute pas d'entrée dans le redolog. J'ai l'impression qu'il faudrait que j'active l'option sur l'objet A mais je n'ai pas besoin de logs sur ce dernier.

Vous est-il possible de me dire si c'est le comportement attendu, ou si j'ai mal paramétré ? Si attendu; comment déclencher de façon custom la création d'une entrée redolog ?

Merci d'avance,
Emmanuelle



### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.22
BuiltOn=2023-11-11 10:20
Git=5.3/a649b2ffa0132f5c9a787499559d29cedafc6047
```
[/details]

## Answer
Rien de spécial, le champ HTML est généré avec les données modifiées uniquement.

`rlg_html = objectXML.toHTML(username, label, date)`

Il faut donc que le DataXML de l'objet soit valorisé avec les données avant (TagXML.setOldValue) et après mise à jour (TagXML.setValue) pour que le message HTML ait quelque chose à raconter.
