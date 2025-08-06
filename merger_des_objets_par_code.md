# Merger des objets par code

**URL:** https://community.simplicite.io/t/6219

## Question
### Request description

Bonjour,

Pour mettre en place une mécanique de Rollback, j'essaie de merger deux instances par code Java, mais je tombe sur l'erreur ACCESS_DENIED.
Auriez-vous des exemples d'utilisation de cette méthode ?

Merci !
Emmanuelle


```
	public void restore()
	{
		AppLog.info(getClass(), "EFE ", "Restore", getGrant());
		
		this.setFieldValue("rciAppIsBackup", false);
		this.setFieldValue("rciAppOriginAppId", null);
		this.save();
		
		List<String> appToRollback = new ArrayList<String>();
		appToRollback.add(this.getFieldValue("rciAppOriginAppId"));
		
		List<String> msg = this.merge(appToRollback, null);
		if (msg != null)
			AppLog.info(getClass(), "EFE2 Restore ", msg.get(0), getGrant());
		

	}
```

## Answer
- Oui le 1er appel avec `map = null` est pour vérifier que les Ids sélectionnés sont mergeables par code / appel de `isMergeEnable` avec les Ids sélectionnés. Ca permet de ne pas autoriser de fusionner certaines lignes entre elles.
- Enusite lorsque map est non null, c'est que l'utilisateur a coché les éléments à garder (attributs et relations)


**linkIds** est une évolution 5.3 qui permet de dire explicitement quelles liens/reférences on garde ou pas (par exemple que certaines adresses d'une personne). En 5.2, la map ne permet que de dire qu'on garde ou pas l'ensemble des relations d'un objet référencé donné d'un Id (toutes les adresses ou aucune pour chaque homonyme de la personne).
