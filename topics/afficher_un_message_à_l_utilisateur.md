# Afficher un message à l'utilisateur

**URL:** https://community.simplicite.io/t/4377

## Question
Bonjour,

J'ai un bouton qui déclenche la récupération de données via un ws en fonction d'un n° de contrat.

J'aimerai que si le ws ne retourne rien, il y ait un message pour informer l'utilisateur que le n° de contrat n'a pas été trouvé.


Script d'appel
```
	public void boutonPeopleSoft()
	{...

		try {
			xml = RESTTool.request("", "application/xml", url, "GET", "", null, mapHeader, 10);
			AppLog.info(getClass(), "**********3Data people soft read : " + xml.length(), null ,  getGrant());

		}catch(Exception e){
			AppLog.error(getClass(), e.getStackTrace()[0].getMethodName(), "Bouton PeopleSoft can't read", e, null);
			afficheMessage("Le n° de contrat n'existe pas");
		}
}
```
et la méthode qui devrait afficher le message
```
	public String afficheMessage(String m) {
		return Message.formatSimpleInfo(m);
	}

```
je n'arrive pas au résultat escompté... est-ce que j'ai mal compris l'utilisation de `Message.formatSimpleInfo` ?

Fabrice

## Answer
[quote="fabrice, post:1, topic:4377"]
`public void boutonPeopleSoft()`
[/quote]

Une action doit retourner le message au front donc avoir un return :

```java
public String boutonPeopleSoft()
...
   return afficheMessage("Le n° de contrat n'existe pas");
...
   return null; // pas de message
```

(une action peut aussi retourner du javascript ou un redirect)
