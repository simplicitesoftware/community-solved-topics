# Surcharge de preSearchIndex dans PlatformHooks

**URL:** https://community.simplicite.io/t/8915

## Question
### Request description

Bonjour,

J'essaie de surcharger preSearchIndex dans PlatformHooks mais j'ai l'erreur suivante

```
Class compilation error (status 1)
/usr/local/tomcat/webapps/ROOT/WEB-INF/src/com/simplicite/commons/RCIB/PlatformHooks.java:190: error: method does not override or implement a method from a supertype
	@Override
	^
1 error
#ERROR
```

Je souhaite utiliser ce hook pour filtrer des résultats dans la recherche globale uniquement.
J'ai tenté d'utiliser le Contexte mais en recherche globale le Contexte ne semble pas mis à jour et prend la valeur de la dernière instance de l'objet affichée.

Y a-t-il un autre moyen d'identifier si on est dans la recherche globale ou non ?

Merci d'avance
Emmanuelle

[Platform]
Status=OK
Version=5.3.51
BuiltOn=2024-10-07 16:56

## Answer
[quote="Emmanuelle, post:6, topic:8915"]
j’ai un setFilter dans le preSearch qui semble s’appliquer au build des indexes,
[/quote]

L'indexation fait une recherche des objets via les couches logiques pour en extraire les contenus indexables, donc ça passe par les hooks des objets.

Il faut inhiber vos règles de gestion dans ce cas, tout comme vous le feriez dans le cas d'un import de données ou un traitement de masse. C'est la même instance qui bosse pour l'indexation :

si `isBatchInstance()` ne rien faire.
