# Contenu d'une Alerte : URL redirigeant vers l'enregistrement sur la plateforme

**URL:** https://community.simplicite.io/t/3604

## Question
Bonjour,
est-il possible d'intégrer dans le contenu d'une alerte, un lien URL qui permet à l'utilisateur d'être directement redirigé vers l'enregistrement où on attend de lui une action ? 

merci, 
Ophélie

## Answer
Si votre message vient du back, vous pouvez retourner du contenu HTML dans le message, exemple :

```java
@Override
public List<String> postValidate() {
	List<String> msgs = new ArrayList<>();
		
	String url = HTMLTool.getFormURL("User", "the_ajax_User", "1", "nav=add");

	msgs.add(Message.formatError("ERROR_CODE",
		"Message 1 <a href='"+url+"'>follow this link</a>",
		null));

	msgs.add(Message.formatSimpleError(
		"Message 2 <a href='"+url+"'>follow this link</a>"));

	return msgs;
}
```

Résultat :

![image|545x84](upload://rfvglPSeFqWOHn4fDsfz5B3VY3A.png)

- Utilisez HTMLTool.getFormURL ou getListURL pour aller sur un objet ou une liste 
- en remplaçant "User" par votre objet métier
- et "1" par votre row_id
- l'instance "the_ajax_XXX" = instance principale de l'objet en recherche/édition sur la UI
