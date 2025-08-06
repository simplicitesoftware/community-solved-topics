# Création d'API Rest

**URL:** https://community.simplicite.io/t/10215

## Question
Bonjour,

J'aimerais créer une API REST, j'ai donc créé un objet externe qui extends RESTServiceExternalObject.

Je ne sais pas comment faire pour renvoyer les chemins url_base/unite, url_base/unite/{id} et url_base/unite/{id}/enfant vers une unique classe ? Faut-il renvoyer chaque chemin vers un objet différent en utilisant URI_MAPPINGS?

Peut-on récupérer l'id facilement? (autrement qu'utiliser split sur l'url).
Est il possible d'utiliser l'orm  afin d'effectuer des recherches directement ?

Merci d'avance

## Answer
```java
List<String> parts = params.getURIParts(getName());
```

Renvoie la liste des parties d'URI au delà du nom de l'objet Ex: si l'URI d'appel de l'objet externe est `/api/ext/MonObjet/a/b/c` la liste renvoyée sera `a, b, c`

Pour ce qui est de l' "ORM", il est bien entendu possible d'utiliser les APIs Java des objet métier comme n'importe où dans Simplicite.

Par contre êtes vous sûr de ne pas être en train de réinventer des choses qui existent déjà ?
= soit les APIs REST standards (qui ne nécessitent aucun développement), soit les API REST dites "mappées" qui nécessitent un peu de code ou de config JSON pour se caler sur des nommages et une structure ad hoc de parcours des objets métier (ex: cette API custom dans la démo: https://github.com/simplicitesoftware/module-demo-apis/blob/master/src/com/simplicite/extobjects/DemoAPIs/DemoAPI1.java)

Implémenter une API REST de base est à réserver à des cas plus spécifiques (i.e. pas juste de l'exposition d'objets métiers)

PS: pour rappel il est possible de mapper les URIs standards sur des URIs alternatives des objets externes grâce au paramètre `URI_MAPPING`, ex: dans le cas des 2 APIs custom de la démo :

```json
[
	{
		"destination": "/api/ext/DemoAPI1$1",
		"source": "^/demo/v1(.+)$"
	},
	{
		"destination": "/api/ext/DemoAPI2$1",
		"source": "^/demo/v2(.+)$"
	}
]
```
