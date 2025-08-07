# L'objet externe Web page est-il toujours valide?

**URL:** https://community.simplicite.io/t/10390

## Question
### Request description

Bonjour,

Les objets externes de type Web Page sont-ils toujours fonctionnels ?
J'ai tenté l'implémentation de base et quand j'essaie d'accéder à mon objet, j'ai la chaîne retournée par le DisyplayBody à l'écran

![image|531x132](upload://ntun3CRvUNRIZv2SF9CM2gfGXSv.png)

J'ai suivi cette [documentation](https://docs.simplicite.io/make/userinterface/externalobjects/webpage/#usage).

Merci d'avance pour votre aide,
Emmanuelle

[Health check](https://ear-trn.k8s-stage.grouperci.com/ui)

[Platform] Status=OK Version=6.2.10 BuiltOn=2025-05-23 10:17

## Answer
Il y a des exemples d'objets externe de type pages publiques et/ou publiques+privées sur l'appstore autour de la démo (certains décrits lors de ce webinaire : https://community.simplicite.io/t/presentation-devenez-maitre-dans-l-art-de-la-customisation-ui-standard-et-uis-alternatives/10154)

Un exemple basique qui correspond au cas d'une simple page publique est celui-ci

```java
public class MyExtObject extends com.simplicite.webapp.web.JQueryWebPageExternalObject {
	private static final long serialVersionUID = 1L;

	@Override
	public String displayBody(Parameters params) {
		try {
			JQueryWebPage wp = getPage();
			wp.appendJSInclude(HTMLTool.simpliciteClientJS()); // If using the npm JS client lib
			wp.appendJSInclude(HTMLTool.getResourceJSURL(this, "CLASS"));
			wp.appendCSSInclude(HTMLTool.getResourceCSSURL(this, "STYLES"));
			wp.setReady(getName() + ".render(" + params.toJSONObject().toString() + ")");
			return HTMLTool.getResourceHTMLContent(this, "HTML");
		} catch (Exception e) {
			AppLog.error(null, e, getGrant());
			return e.getMessage();
		}
	}
}
```

Avec le triptique usuel de resources HTML/JS/CSS, ex: le JS:

```javascript
class MyExtObject{
	static render(params) {
		const app = simplicite.session({ endpoint: 'uipublic' }); // instnanciate the npm client lib for the public user
		app.info(`Lib version: ${simplicite.constants.MODULE_VERSION}`);
...
	}
}```
