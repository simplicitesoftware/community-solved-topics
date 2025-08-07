# Chiffrement des données

**URL:** https://community.simplicite.io/t/5115

## Question
Bonjour,

Dans le cadre de l'un de nos projets nous devons chiffrer un certain nombre de champs en base de données.
D'après le post suivant https://community.simplicite.io/t/cryptage-des-donnees/727 le chiffrement doit être ajouté à "la main" dans les hooks preSave et postSearch.
Dans notre cas nous avons beaucoup de champs à chiffrer. Est-ce que depuis 2017 des évolutions ont été réalisées sur ce sujet ?
Est-ce qu'il existe un autre moyen pour mettre en place le chiffrement plus rapidement, avec du paramétrage et non du code par exemple afin de dire quel champ doit être chiffré ou non ?

Merci d'avance

## Answer
Bonjour!

[quote="FlorentGN, post:1, topic:5115"]
Est-ce que depuis 2017 des évolutions ont été réalisées sur ce sujet ?
[/quote]

Non, rien de nouveau sur le chiffrement des données, le contenu du post que vous citez est toujours d'actualité. 

[quote="FlorentGN, post:1, topic:5115"]
un autre moyen pour mettre en place le chiffrement plus rapidement
[/quote]

Vous pouvez utilisez le pattern "CustomObjectDB" pour enrichir les fonctionnalités d'ObjectDB : vous pouvez faire hériter tous vos objets d'une classe intermédiaire.

ObjectDB <--- **{EncryptedObjectDB <----**} DemoSupplier

# Exemple:

## Implémentation

```java
package com.simplicite.commons.Cryptomator;

import java.util.*;

import com.simplicite.util.*;
import com.simplicite.util.exceptions.*;
import com.simplicite.util.tools.*;


public class EncryptedObjectDB extends ObjectDB {
	private static final long serialVersionUID = 1L;

	// based on https://docs.simplicite.io/documentation/01-core/advanced-code-examples.md#encryption
	@Override
	public String preSave(){
		for(ObjectField f : getFields())
			try{
				if(isEncrypted(f))
					f.setValue(EncryptionTool.encrypt(f.getValue(), getEncryptionKey()));
			}
			catch(EncryptionException e){
				AppLog.error(e, getGrant());	
			}
		
		return super.preSave();
	}
	
	@Override
	public void postSelect(String rowId, boolean copy){
		for(ObjectField f : getFields())
			try{
				if(isEncrypted(f))
					f.setValue(EncryptionTool.decrypt(f.getValue(), getEncryptionKey()));
			}
			catch(EncryptionException e){
				AppLog.error(e, getGrant());	
			}
		
		super.postSelect(rowId, copy);
	}
	
	private static boolean isEncrypted(ObjectField f){
		return !f.isEmpty() && "CONFIDENTIAL".equals(f.getClassification());
	}
	
	private static String getEncryptionKey(){
		// DO NOT STORE THE KEY IN THE DATABASE
		return System.getProperty("encryption.key"); // Simplicite012345
	}
}
```

Dans le cas d'une instance déployée avec Docker, il faudrait passer la clef de chiffrement par, au choix:

* un fichier sur un volume, par 
* une propriété java :  `-e JAVA_OPTS="-Dencryption.key=Simplicite012345"`
* une variable d'environnement

Voir aussi [les exemples dans la doc](https://docs.simplicite.io/documentation/01-core/advanced-code-examples.md#encryption) sur le sujet.

## Utilisation

Pour crypter par exemple le champ "email" du supplier de la démo, il faut

1. faire hériter `DemoSupplier` de EncryptedObjectDB

```java
package com.simplicite.objects.Demo;
public class DemoSupplier extends com.simplicite.commons.Cryptomator.EncryptedObjectDB {
	private static final long serialVersionUID = 1L;
}
```

  2. changer le paramètrage du champ (on a utilisé le caractère de donnée confidentielle ou non, pour l'exemple, c'est un détournement du méta-modèle, et il faut augmenter la taille de la colonne, les données prennent plus de place en base une fois chiffrées)

![Cursor_and_Simplicité®|414x499](upload://xAI8TRcFnHyqoZnKWK5I5SUrdiW.jpeg)

PS: Attention à la reprise de données!

## Avertissement (17/10/22)

Ceci est un exemple, à implémenter avec délicatesse. Voir le post ci-dessous pour quelques conseils supplémentaires.

https://community.simplicite.io/t/probleme-sur-le-dechiffrage-de-certains-champs-herites/5364/5
