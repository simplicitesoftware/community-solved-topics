# La journalisation (redolog) n'est pas prise en compte dans le contexte des appels API

**URL:** https://community.simplicite.io/t/5318

## Question
Continuing the discussion from [Besoin de création de redolog lors d&#x27;appel API](https://community.simplicite.io/t/besoin-de-creation-de-redolog-lors-dappel-api/3191/9):

### Version

*Version=5.2.14 BuiltOn=2022-09-09 19:11*

### Description

*La journalisation (redolog) n'est pas prise en compte dans le contexte des appels API alors que LOG_ACTIVITY et LOG_SESSSION sont bien définis dans le grant du user appelant.*

## Answer
Effectivement, il y manquait l'appel au redolog car cette couche via ExternalObject n'hérite pas du service REST qui l'implémentait bien.

Explications :

Pour que le Journal du "redolog" soit bien archivé (avec toutes les mises à jour en cascade qui pourraient exister dans les hooks de l'objet), il faut que la méthode appelante arme un stack d'undo/redo = 2 FlowXML qui vont enregistrer les modifs du thread à partir de ce point. Un peu comme un begin transaction et commit/rollback :

- DEBUT = UndoRedoPool.prepareUndoRedo(obj)
- faire des modifs avec obj, pouvant contenir des mises à jour en cascade (via des ObjectDB)
- FIN OK = UndoRedoPool.confirmUndoRedo(obj)
- FIN KO = UndoRedoPool.ignoreUndoRedo(obj)

Exemple :

```java
try {
	// Prepare undo/redo to trace all further changes
	UndoRedoPool.prepareUndoRedo(obj);

	// ...
	obj.getTool().validateAndUpdate();
	// ...

	// SUCCESS = Confirm undo in pool
	if (obj.hasChanged(false))
		UndoRedoPool.confirmUndoRedo(obj); // => stored in logs and/or DB
	else // not changed
		UndoRedoPool.ignoreUndoRedo(obj); // => discard from memory
}
catch (ValidateException | UpdateException e) {
	// ERROR : Discard stack
	UndoRedoPool.ignoreUndoRedo(obj);
	return "functional error";
}
catch (Throwable e) { // Catch any other throwable
	// Discard stack
	UndoRedoPool.ignoreUndoRedo(obj);
	return "technical error";
}				
```


Ensuite dans les hooks enfants (postSave... sont exécutés dans un même thread), il n'est pas nécessaire de faire ce sandwich, les mises à jour vont s'empiler dans la stack déjà armée. Ca ne fonctionne pas si on lance des actions asynchrones (qui iront dans un autre thread).

Ce sera livré au prochain build 5.2.17.
