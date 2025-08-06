# Empêcher une exécution simultanée

**URL:** https://community.simplicite.io/t/9935

## Question
Bonjour,

J'ai un bouton qui exécute une méthode pour parcourir toutes les lignes de la table et les synchroniser avec les données du contrôle des habitants. 

Comme ce processus est long, j'aimerai empêcher les autres utilisateurs (qui ne voient pas que le processus est en cours d'exécution) de cliquer sur le bouton pour relancer le processus.

Y a-t-il une manière de faire que vous préconisez?

Merci pour vos réponses

Fabrice

## Answer
Un pattern de ce type là devrait répondre au besoin:

```java
Grant sys = Grant.getSystemAdmin();

String param = "MON_PROCESSUS";
String val = sys.getSystemParam(param);

if (Tool.isEmpty(val)) {
	sys.setSystemParam(param, Tool.getCurrentDateTime());
	try {
		// ici le processus long...

		return Message.formatSimpleInfo("Le processus est terminé");
	} finally {
		sys.removeSystemParam(param, false);
	}
} else {
	return Message.formatSimpleInfo("Un processus est déjà en cours depuis: " + val);
}
```

Quitte à checker aussi ce param dans le `isActionEnable` pour faire disparaitre le bouton mais c'est moins clair pour les users
