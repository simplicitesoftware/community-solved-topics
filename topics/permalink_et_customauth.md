# Permalink et CustomAuth

**URL:** https://community.simplicite.io/t/10878

## Question
### Request description

Bonjour,

J’ai un souci d’utilisation des permalinks avec une authentification custom.

J’essaie d’accéder à mon objet externe via la syntaxe `/ui/l/<permalink URI>`

Si j’utilise la connexion SSO, mon URL est transformée en `/ui/?permalink=<permalink URI>`
Mais quand je passe par mon customAuth, je suis redirigée sur la page d'accueil.

Y a-t-il un moyen de récupérer les permalink en customAuth ?

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.2.16
BuiltOn=2025-09-11 13:31

## Answer
Le deeplink doit être récupéré et conservé en session (comme le scope et le deeplink), genre:

```
// Set scope
String scope = getScope(request);
if (!Tool.isEmpty(scope))
	session.setAttribute(Globals.SESSION_SCOPE, scope);

// Set permalink/deeplink
String permalink = MainPublicServlet.getPermaLink(request);
String deeplink = getDeeplink(request);
if (!Tool.isEmpty(permalink))
	session.setAttribute(Globals.SESSION_PERMALINK, permalink);
else if (!Tool.isEmpty(deeplink))
	session.setAttribute(Globals.SESSION_DEEPLINK, deeplink);
```
Et si la session est recrée à un stade,  il faut aussi y recréer les attributs de session, genre:

```java
String scope = (String)session.getAttribute(Globals.SESSION_SCOPE);
String permalink = (String)session.getAttribute(Globals.SESSION_PERMALINK);
String deeplink = (String)session.getAttribute(Globals.SESSION_DEEPLINK);

session.invalidate();
session = request.getSession(true);

session.setAttribute(Globals.SESSION_SCOPE, scope);
session.setAttribute(Globals.SESSION_PERMALINK, deeplink);
session.setAttribute(Globals.SESSION_DEEPLINK, deeplink);
```
