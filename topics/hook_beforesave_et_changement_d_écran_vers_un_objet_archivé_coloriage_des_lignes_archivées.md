# Hook beforeSave et changement d'écran vers un objet archivé + coloriage des lignes archivées

**URL:** https://community.simplicite.io/t/6815

## Question
### Request description

Bonjour,
Je tente d'utiliser le hook beforeSave. Mon code vise à proposer, en cas de duplicate key avec un élement archivé, de restorer l'archive au lieu de l'objet en cours de création.
Si l'utilisateur répond oui, je le redirige vers l'archive "désarchivée" sans sauvegarder sa création.
Mais il me semble que je n'arrive pas à sortir du hook malgré le cbk(false). Je suis bien redirigée vers l'archive, mais je n'ai pas la main et ça mouline.

Pouvez vous m'aider ?
Merci !
Emmanuelle

Le code qui pose problème
```
											objDup.save(function(){
													$ui.displayForm(null, objDup.getName(), objDup.getRowId(), { nav: "new"}, function(){cbk(false);});
```
Moulinage
![image|690x274](upload://1E29Qop4PzYgaB1fleymSlGQ8NV.png)


Code complet
```
Simplicite.UI.Globals.form.beforesave  = function(ctn, obj, index, cbk) {
					
					if (obj.getName().startsWith("Rci"))
					{
						var keys = obj.getUserKeyFields();
						var objDup = $ui.getAjax().getBusinessObject(obj.getName());
						var filters = {};

						
						for (var i = 0 ; i < keys.length ; i++)
						{
							var key = keys[i];
							if (key.refField == null)
								filters[key.name] = obj.getFieldValue(key.name);
						}
						
						filters["rciFieldIsArchived"] = "1";

						
						objDup.resetFilters();
						objDup.search(function(list) {
	
							if (list.length > 0)
							{
								if (confirm("This object already exists and had been archived. Do you want to restore it ?"))
								{
									objDup.resetFilters();
									
									objDup.selectForUpdate(
										function(item) {
											objDup.getField("rciFieldIsArchived").setValue(false);
											objDup.item.rciFieldIsArchived = false;
											objDup.save(function(){
													$ui.displayForm(null, objDup.getName(), objDup.getRowId(), { nav: "new"}, function(){cbk(false);});
													
													
												}
											);
										}
										, list[0].row_id);
									
									
								}
								else
									cbk();

							}
							else
								cbk();

						}
						,
							filters
						);
					
					}
					else
						cbk();
				};
```

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.10
BuiltOn=2023-07-28 09:49
```
[/details]

## Answer
Pour des raisons évidentes de sécurité, le front n'a aucune vocation à accéder au SQL back (select, update, search spec...), tout comme accéder aux droits du user.

La search-spec d'un lien virtuel reste donc en back :
- dans la définition du link (à corriger avec un jointure/test "archivé")
- ou dynamiquement via accesseur sur la foreign-key du link :

exemple pour surcharger le filtre s'il y en a un dans le postLoad de l'objet lié :

```java
ObjectField fk = obj.getField("refField");
String spec = fk.getRefSearchSpec();
if (!Tool.isEmpty(spec))
  spec = "(" + spec +") and ";
else
  spec = "";
spec += "exists (select 1 from ... not archived ...)";
fk.setRefSearchSpec(spec);
```

Pour la partie front, il faut utiliser le hook `list.onload` ou `list.onloadrow` pour colorier les lignes archivées si elles ne sont pas filtrées / visibles, dans ce cas la colonne/info "archivé" doit être présente en liste pour faire le test et ajouter une classe aux tr/td.

ou sinon (la colonne est cachée ou pas de hook front), il faut retourner la classe de chaque field=td par hook back :

```java
@Override
public String getStyle(ObjectField f, String[] row) {
	Grant g = getGrant();
	if (archived(g, row)) // TODO
		return "row-archived";
	return super.getStyle(f, row);
}
```
et définir la classe .row-archived en front dans une ressource STYLES.

```css
td.row-archived {
	background: red !important;
}
```

**Attention** Le hook `getStyle` doit bien évidement être rapide car appelé pour chaque cellule de la liste.
