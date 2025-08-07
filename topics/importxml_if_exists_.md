# ImportXml if="exists"

**URL:** https://community.simplicite.io/t/9505

## Question
Bonjour,
Je suis en 5.3.56.

J'essaye de remplacer les end-point plateform après un dump et le if="exists" n'est pas pris en compte. Par exemple si je crée un end-point "patate" et que j'importe le fichier ci-dessous j'ai aucun problème le end-point est bien supprimé mais si il est inexistant l'import remonte une erreur `ERROR []   No row found`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<simplicite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.simplicite.fr/base" xsi:schemaLocation="http://www.simplicite.fr/base https://www.simplicite.io/resources/schemas/base.xsd">
<object if="exists">
	<name>PlatformNode</name>
	<action>delete</action>
	<data>
		<ptf_endpoint>patate</ptf_endpoint>
	</data>
</object>
</simplicite>
```

Merci d'avance

## Answer
Le `if="exists"` doit être mis sur le tag `<action>`,

ex:

```xml
<object>
	<name>MyObject</name>
	<action if="exists">delete</action>
	<data>
		<...>
	</data>
</object>
```
