# Comment configurer un champ d'objet pour pouvoir utiliser la feature du bouton "Corriger" proposée en preValidate?

**URL:** https://community.simplicite.io/t/5218

## Question
La question est dans le titre : 
![image|690x440](upload://6qiNXsogGmTpmdXlew9CzYaO72Q.png)

Mon use case consiste à proposer à l'utilisateur un bouton permettant de recopier une valeur dans un champ en fonction d'une règle métier spécifique. La valeur elle-même serait déterminée dynamiquement (pas une valeur fixe).

## Answer
Bonjour Bruno,

Il faut retourner au validate un message finissant par **#suggest:xxx**.
Avec le helper `Message.formatSuggestion` :

```java

	/**
	 * <p>Formats a suggestion message of specified level</p>
	 * @param code  code (from list of values TEXT)
	 * @param msg   Optional Additional message
	 * @param level Optional level INFO WARNING ERROR FATAL
	 * @param field Optional associated field
	 * @param suggestion Suggestion
	 * @return formatted event : code[:message][#level][#field][#suggest:value]
	 */
	public static String formatSuggestion(String code, String msg, String level, String field, String suggestion)
```

exemple 
`Message.formatSuggestion("SYNTAX_ERROR_XYZ", null, Message.WARN, "myField", "XYZ12345")`
