# Décoder le State renvoyé par OKTA

**URL:** https://community.simplicite.io/t/10643

## Question
### Request description

*Bonjour,*

Notre Use case est le suivant : 

* un utilisateur accède à un formulaire via une URL deeplink qui lui est transmise par mail
* il se connecte dans un premier temps avec OpenIdConnect
* si la connexion est OK, il accède à son formulaire → cela fonctionne
* si la connexion est KO, il est connecté avec un user générique lui donnant accès à ce formulaire uniquement, + un popup de demande de compte qui crée chez nous un JIRA → cela ne fonctionne pas car au retour KO d’OKTA, nous avons perdu le deeplink

Il me semble que nous pouvons retrouver ces informations dans le paramètre State de la réponse OKTA, mais je ne sais pas comment le décoder. Auriez vous des pistes pour moi ?

Merci d’avance !

Emmanuelle

```
[Platform]
Status=OK
Version=6.2.15
BuiltOn=2025-08-15 11:39
```

## Answer
Je lis entre les lignes qu'on parle d'un "SSO" OpenIDConnect.

Le state que nous générons et qui est visiblement bien fourni en retour par l'IdP, y compris en cas d'erreur, ne contient pas de données significatives.

Un éventuel deeplink dans l'appel d'origine est bien géré en cas de retour OK mais pas en cas de retour en erreur, ce qui est logique car on est pas sensé arriver alors ailleurs que sur une page d'erreur.

Dans votre cas il faudrait donc que vous surchargiez la gestion d'erreur via le platform hook [`customErrorResponse`](https://platform.simplicite.io/6.2/javadoc/com/simplicite/util/PlatformHooks.html#customErrorResponse(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse,int,java.lang.Object,java.util.Map)) en y récupérant le deeplink dans la session Tomcat si celle ci est bien toujours accessible (à tester mais je pense que c'est le cas) via `request.getSession().getAttribute(Globals.SESSION_DEEPLINK)`
