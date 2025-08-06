# Envoi de pièce-jointe (Mail et Alertes)

**URL:** https://community.simplicite.io/t/4004

## Question
Bonjour,

Je n'arrive pas à envoyer de pièces jointes dans mes mails (https://docs.simplicite.io/5/javadoc/com/simplicite/util/Mail.html#sendWithAttach(java.lang.String[],java.lang.String,java.lang.String,java.lang.String[],java.lang.String[],java.lang.String,java.lang.String,java.lang.String,java.lang.String[],com.simplicite.util.Mail.MailAttach[],com.simplicite.util.Mail.MailImage[])) ni dans mes alertes (https://docs.simplicite.io/5/javadoc/com/simplicite/bpm/Alert.html#send(com.simplicite.util.ObjectDB,java.util.List).

J'essaie d'envoyer par exemple un fichier test.txt, que je crée à la volée, puis stocke dans le dossier temporaire (getGrant().getTmpDir()) :

![image|690x139](upload://umMXiwPfLce5YKO5EaQeBnA8upe.png)

Le mail est envoyé, mais sans la pièce-jointe.

Lorsque j'essaie le même bout de code sur une instance en V4, je reçois bien la pièce-jointe test.txt.

J'ai également essayé avec une alerte (Alert) pour voir si j'obtenais de meilleurs résultats, mais rien n'y fait... 

Auriez-vous une idée ? Je ne crois pas qu'il y ait de mail avec pièce jointe sur la démo.

Merci de votre aide !

Alexandre 


![image|690x89](upload://mBLD36hKMLLQfRIwmO7qNCvflzW.png)

## Answer
Bonjour,

L'envoi de pièces jointes ne pose pas de soucis particulier.
Dans votre test, le ficher semble vide, de plus est-il détruit avant envoi du mail proprement dit / asynchrone ? 

Les envois sont asynchrones par défaut pour ne pas bloquer l'utilisateur si le serveur SMTP est long a répondre. cf paramètre `EMAIL_SEND_ASYNC`.

```java
try {
	String file = getGrant().getTmpDir() + "/test.txt";
	java.io.FileWriter r = new java.io.FileWriter(file);
	r.write("xxx");
	r.close();
	new Mail(getGrant()).sendWithAttach(
		new String[]{"xxx@xxx.fr"}, null, null, null, 
		"test email", "content...", Mail.MAIL_MIME_TYPE_HTML,
		new String[]{ file }, null);
}
catch(Exception e) {
	AppLog.error("error", e, getGrant());
}
```
