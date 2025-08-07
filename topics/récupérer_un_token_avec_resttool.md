# Récupérer un token avec RESTTool

**URL:** https://community.simplicite.io/t/4497

## Question
Bonjour,

J'ai une API REST que je veux utiliser directement dans le **code java**.
J'ai lu la documentation (javadoc) de la classe RESTTool, et je n'arrive pas à récupérer le token bearer (`erreur 400 bad request` à chaque fois).

Pourtant l'URL est la bonne. Donc la seule solution c'est que le body soit faux.
J'ai seulement ses 3 informations à renseigner :
* client_id --> info1
* client_secret --> info2
* grant_type --> info3

Pourriez-vous m'aidez à trouver la syntaxe exacte du POST à effectuer pour récupérer le token ?

Sachant que lorsqu'on utilise l'API sous AZURE, tout fonctionne. Voici la configuration :
  
![image|649x298](upload://8S3UyVvpDKcupmIBKBB93xQlq4W.png)

## Answer
Merci pour l'aide, en fait, il s'agissait bien de 2 problèmes :
* Le `client_secret` n'était pas le bon
* Il fallait comme vous l'avez dit rajouter explicitement le `application/x-www-form-urlencoded`
