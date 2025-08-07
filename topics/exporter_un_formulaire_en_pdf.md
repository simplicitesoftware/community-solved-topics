# Exporter un formulaire en PDF

**URL:** https://community.simplicite.io/t/9052

## Question
### Request description

Bonjour,
J'essaye de créer un bouton qui permet d'exporter un formulaire en PDF et il faudrait que je puisse mettre en forme les données selon un template pré défini.

Quelle serait la meilleure solution?

Je vous remercie par avance.

### Technical information

[details="Instance /health"]
Version=5.3.42
[/details]

## Answer
Vérification faite en v5 il ça ne se faisait pas encore automatiquement via le MIME type forcé. Il faut implémenter ce type de publication de la manière suivante

Un template de publication de type méthode avec un template HTML:

![image|690x297](upload://ja51qWYJ9UNyMXLh9x80T0YPf8m.png)

Et la méthode implémentée comme suit:

```java
public Object myPrintMethod(PrintTemplate pt) {
	try {
		pt.setMIMEType(HTTPTool.MIME_TYPE_PDF);
		return HTMLToPDFTool.toPDF(pt.fillTemplate(this, pt.getTemplate(true), getValues()));
		// ou  pour une publication de liste:
		// return HTMLToPDFTool.toPDF(pt.fillTemplate(this, t.getTemplate(true), getCurrentList())); // Pour une pib
	} catch (Exception e) {
		AppLog.error(e.getMessage(), e, getGrant());
		pt.setMIMEType(HTTPTool.MIME_TYPE_TXT);
		return e.getMessage();
	}
}
```

Cela étant dit, pourquoi restez vous en v5 ?

Celle-ci est désormais en maintenance long terme, cela veut dire une maintenance uniquement corrective destinée aux applications en production **qui n'evoluent plus**.

Si vous travaillez encore activement sur votre application vous avez donc tout intérêt à passer en v6 pour bénéficier des nouvelles fonctionnalités de la plateforme (par exemple cette fonctionnalité de conversion auto HTML => PDF).
