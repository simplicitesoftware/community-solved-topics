# setFilter sur un lien virtuel

**URL:** https://community.simplicite.io/t/8871

## Question
### Request description

Bonjour,

Question 101 désolée mais je fais un setFilter sur une clé virtuelle et la searchSpec de mon lien ne s'applique pas.

Est-ce que c'est censé fonctionner ? Ou je commets une erreur quelque part ?

```
String objName = item.getLinkedObjectName();
		String refFieldName = item.getRefFieldName();
		
		ObjectDB linkedObj = getGrant().getObject("CRIT_ITEM_", objName);
		linkedObj.resetFilters();
		
		String filterFielValue = item.getFilterFieldVal();
		if (!filterFielValue.isEmpty())
			linkedObj.setSearchSpec(linkedObj.getSearchSpec() + " AND " + filterFielValue);
		
//Filtre sur la clé virtuelle	
		linkedObj.setFieldFilter(refFieldName, getRowId());
		
		if (linkedObj.getField("rciFieldIsArchived", false) != null)
			linkedObj.setFieldFilter("rciFieldIsArchived", false);
		
		int nb = linkedObj.search().size();
		linkedObj.setSearchSpec(linkedObj.getDefaultSearchSpec());
```
--> le search me ramène même les lignes qui ne sont pas liées à mon getRowId()

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=5.3.47
BuiltOn=2024-09-09 17:56

## Answer
Bonjour Emmanuelle,

Pour moi mettre un filtre sur une clé virtuelle n'a pas trop de sens car c'est normalement une champ ID sans colonne physique (donc pas de `where t.col='filter'` possible). Il y a juste sa search spec sur le Link qui est ajouté au `where` en remplaçant le token `[ROWID]` par le parent Id de la liste.

J'ai pas tout compris à ton code, mais pour forcer le filtre d'un lien virtuel sur un autre parent, il faut changer de parent context :

```java
// set the parent values
parentObject.select("1234");
// Set the parent context to replace the virtual link [ROWID]
linkedObj.storeParentContext(parentObject, refFieldName, parentObject.getValues());
linkedObj.search()...
```

Et il faut jamais faire de :
`int nb = linkedObj.search().size();`
mais juste
`int nb = linkedObj.getCount(); // ou count()`
sinon tu charges la table/requete en mémoire pour n'en compter que les lignes.
