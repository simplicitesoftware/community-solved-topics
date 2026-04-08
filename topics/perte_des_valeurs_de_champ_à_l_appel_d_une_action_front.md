# Perte des valeurs de champ à l'appel d'une action front

**URL:** https://community.simplicite.io/t/11936

## Question
### Request description

Bonjour,

J'ai une action front qui ouvre un formulaire d'objet. Le nom de l'objet doit être calculé en fonction de la ligne sur laquelle l'action a été exécutée.
Mon souci est qu'à l'arrivée dans l'action, je n'ai plus que le rowId de la ligne dans les valeurs de l'item donc je ne peux pas calculer ce nom.

Cela a l'air d'être voulu car les valeurs sont explicitements vidées dans ```doActionCustom```

```
            if (rowId) {
                obj.item = {};
                obj.setRowId(rowId);
```

Est-ce que je dois faire un ```get``` avant le displayForm ? Je trouve ça dommage dans le sens où j'avais déjà récupéré les valeurs en liste, de plus, le displayForm refait un get derrière.
Auriez-vous une autre solution à me suggérer ?

Mon action
![image|496x220, 75%](upload://jn19aBwtlSb6TMu8P9hxGznU1Qr.png)

```
	viewSummary() 
	{
	    var d = $('<div/>'), dlg;
	     
	    function close() {
	         $ui.view.tools.dialogClose(dlg);
	    }

        var id = "Summary view";
        dlg = $ui.view.tools.dialog({
                name: id,
                content: d.attr("id", id),
                width: "60%"
            });
		
		let obj = $app.getBusinessObject('Nom d'objet calculé', 'Instance de l'objet');
		$ui.displayForm(d, obj, this.item.row_id, {
		        onsave: null,
		        onsavenew: null,
		        onsavecopy: null,
		        onsaveclose: null,
		        onclose: close
		});
	}
```

Merci !
Emmanuelle

[Platform]
Status=OK
Version=6.3.7-preview
Variant=full
BuiltOn=2026-04-01 18:33

## Answer
On ne voit pas la définition complète dans ta copie d'écran.
D'après ton post la définition c'est URL = `javascript:obj.viewSummary()`.
Si `backend = true` c'est qu'il y a aussi un nom de méthode back à appeler avant le redirect vers l'URL ?
