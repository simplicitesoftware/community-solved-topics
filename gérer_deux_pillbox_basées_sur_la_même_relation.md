# Gérer deux pillbox basées sur la même relation

**URL:** https://community.simplicite.io/t/8405

## Question
### Request description

Bonjour,

Sur un objet, j'ai affiché deux fois la même pillbox. Je souhaite proposer une saisie en deux temps, l'objet référencé ayant deux niveaux.
Pillbox 1 : niveau 1
Pillbox 2 : les niveaux 2 correspondant aux niveaux 1 sélectionnés

J'ai donc un filtre à ajouter dans le initRefSelect et dans le preSearch.

Mon problème est que je ne sais pas identifier de quelle pillbox j'arrive dans ces deux hook.
Est-il possible de spécifier une instance particulière pour chaque pillbox ? 

Merci d'avance
Emmanuelle

## Answer
La vue en pillbox n'a qu'un seul trigger `change` qui ne dit pas si on ajoute ou on retire quelque chose.

Par contre quand on crée ou supprime quelque chose, il y a des évènements front qu'un composant de la page peut capter et faire des choses :

Simplicité notifie l'ajout ou la suppression d'un élément de pillbox via :

```
$view.notify({
  type: "create", // or delete
  object: obj, // created/deleted object definition
  rowId: "123" // created/deleted row_id
});
```

Il faudrait que la div 2 fasse le ménage quand un objet 1 est créé ou retiré.
Le trigger arrivera à tous les composants qui ont une classe `js-notify` et un handler `ui.notify`

```
div2.addClass("js-notify").on("ui.notify", function(e, notif) ...);
```



https://docs.simplicite.io/docs/ui/responsive

Usage samples:
to update UI elements when one object has been deleted:
```
var table = $(myTable).addClass("js-notify").on("ui.notify", function(e, notif) {
	if (notif.type=="delete" && notif.object.getName()=="MyObject")
		$("tr[data-rowid='" + notif.rowId + "']", table).remove();
});
```

A adapter avec tes règles de merge pour gérer "tmppb" à la main.
