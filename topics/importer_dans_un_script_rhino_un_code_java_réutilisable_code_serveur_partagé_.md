# Importer dans un script Rhino un code Java réutilisable (Code serveur partagé)

**URL:** https://community.simplicite.io/t/3573

## Question
Bonsoir,
est-il possible d'importer dans le code d'un objet implémenté en Rhino une classe Java implémentée dans un code partagé ?

Plus précisément, j'ai la classe suivante :
```
package com.simplicite.commons.RenaultAPI;

import ...;

public class DBBToolBox implements java.io.Serializable {
	private static final long serialVersionUID = 1L;
	public void publish(ObjectDB onj, String event) { ... } throws xxx ...
}
```
Et le code Rhino d'un objet avec (par exemple) la méthode postCreate dans laquelle je voudrais utiliser DBBToolBox.publish(...)
```
BCSILegalEntity.preDelete = function() {
	importPackage(Packages.com.simplicite.commons.RenaultAPI);
	importClass(Packages.com.simplicite.commons.RenaultAPI.DBBToolBox);
	try {
		DBBToolBox.publish(this, "Deleted");
	} catch(e) {
		console.error(e);
	}
};
```
 -> L'instruction importClass génère une erreur `InternalError: Function importClass must be called with a class; had "[JavaPackage com.simplicite.commons.RenaultAPI.DBBToolBox]" instead` et sans l'instruction importClass, l'usage de DBBToolBox génère l'erreur `ReferenceError: "DBBToolBox" is not defined` (ça ne marche pas non plus avec le path complet com.simplicite.commons.RenaultAPI.DBBToolBox).

## Answer
Super!
merci beaucoup (je ne l'aurais pas inventée celle-là).
:slight_smile: 
![2021-07-20 11_20_21-KISS - RCM|690x155](upload://HAkJid5XMg7hLzG9argywDxCGk.png)
