# Bulk update sur une ligne avec un targetObject

**URL:** https://community.simplicite.io/t/13399

## Question
### Request description

Bonjour,

Quand je fais un bulk update sur un objet avec getTargetObject surchargé, les selected ids sont ceux de l'objet target et non ceux de celui de la liste. Ce sont donc des lignes aléatoires qui sont mises à jour.

### Steps to reproduce


1. Avoir un objet A avec getTargetObject surchargé vers un objet B
2. Afficher A en liste
3. Sélectionner une ligne et faire un bulk update

-> soit ça mouline car le row_id de B ne correspond à rien chez A, soit on met à jour la mauvaise ligne de A

###Piste d'analyse

Dans ```displayListRow```, la data rowId est initialisée avec le rowId de la target

```tr.data("rowId", md.target?.rowId || rowid);```

C'est la variable qu'on utilise pour envoyer le rowId au back lors du selectRow

```id = tr.data("rowId")```

Le selectRow envoie donc le nom d'objet A avec le rowId de B

![image|690x369](upload://ykzDelLx4mT6YJ2bfnVuAeUv2te.png)

![image|690x27](upload://zJwLCNklwF8LmgtFYx0isRdticz.png)


Merci d'avance pour votre aide !

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.3.16
Variant=full
BuiltOn=2026-09-09 19:41
Git=6.3/6ba27b353cea46b8807736e7de1ddb462d83cd64
```

PS : je sais que nous sommes en retard sur les patchs, nous avons un problème réseau en cours d'analyse qui nous empêche de récupérer l'image ...

[/details]

## Answer
_No answer provided._
