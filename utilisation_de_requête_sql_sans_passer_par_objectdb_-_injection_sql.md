# Utilisation de requête SQL sans passer par ObjectDB - > Injection SQL

**URL:** https://community.simplicite.io/t/3925

## Question
Bonjour,

Pouvez-vous me confirmer que le fait d'utiliser des requêtes SQL classiques avec le getGrant.update(SQL) (ou tout autre requête SQL) avec des paramètres concaténés avec des + permet d'injecter du SQL. (cf. ci-dessous).


Je ne vois pas dans le code de Simplicité un mécanisme permettant d'éviter les injections lorsqu'on fait ce genre de requête ci-dessous. (sauf bien entendu utiliser les save, validateAndSave avec des objectDB).

Merci d'avance

Cf. doc OWASP : 

**Scenario #1**: An application uses untrusted data in the construction of the following vulnerable SQL call:
<b>`String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";`</b>
**Scenario #2**: Similarly, an application’s blind trust in frameworks may result in queries that are still vulnerable, (e.g. Hibernate Query Language (HQL)):
<b>`Query HQLQuery = session.createQuery("FROM accounts WHERE custID='" + request.getParameter("id") + "'");`</b>
In both cases, the attacker modifies the ‘id’ parameter value in their browser to send: ‘ or ‘1’=’1. For example:
<b>`http://example.com/app/accountView?id=' or '1'='1`</b>

This changes the meaning of both queries to return all the records from the accounts table. More dangerous attacks could modify or delete data, or even invoke stored procedures.

## Answer
Oui surtout si la donnée vient directement d'un input front.

Un hacker peut également injecter du code dans les champs HTML pour exécuter un script. Il en va de même pour les contenus HTML des input/textarea, Simplicité encode systématiquement les données.

Donc s'il y a du code spécifique pour alimenter des champs, idem il faut escaper correctement les contenus : 

Code en back
```java
Tool.toHTML("<p>Hello world!</p> <script>..xhr request to hacker...</script>");
```

Code en front
```javascript
$(div).text("<p>Hello world!</p> <script>...xhr request...</script>");
```

ou pour volontairement insérer du contenu riche mais bien retirer les scripts :

```javascript
$(div).htmlSafe("<p>Hello world!</p> <script>...xhr request...</script>");
$(div).appendSafe("<p>Hello world!</p> <script>...xhr request...</script>");
```

Ces extensions jQuery de Simplicité afficheront "Hello world!" dans un paragraphe, mais n'exécuteront aucun script, ou `<img onload="script...">`....
