# Gestion des niveaux de logs

**URL:** https://community.simplicite.io/t/4831

## Question
Simplciité 5.1.43

Bonjour, 

J'ai ce genre de logs de debug dans la console :

```
2022-05-09 14:42:49,695||DEBUG|http-outgoing-480: Close connection
2022-05-09 14:42:49,695||DEBUG|Closing connections idle longer than 60000 MILLISECONDS
2022-05-09 14:42:33,072||DEBUG|Connection manager shut down
```

Je pense que c'est des logs qui proviennent d'un package style **org.apache.http**, mais impossible de le savoir vu que l'origine n'est pas renseignée. 

J'ai procédé à la modification du logback.xml dans notre image docker en ajoutant les deux dernière lignes lors du builds de l'image pour tester mais sans changement :

```
<!-- JGit logging to info level -->
<Logger name="com.simplicite" level="info"/>
<Logger name="org.apache.http" level="info"/>
```

## Answer
Les logs applicatives Simplicité (= celles qui passent par `AppLog` et sont pilotées par les log events et/ou les params systèmes `LOG_*`) sont traitées par Log4J et donc configurées dans `<webapp root>/WEB-INF/classes/log4j2.xml`.

Par défaut Les appenders Log4J sont en niveau debug pour pouvoir activer à la demande les traces applicatives de niveau debug. 

Si d'autres libs tierces utilisent Log4J et que vous ne voulez pas leurs traces de niveau debug, il faut les mettre en exception => c'est par exemple ce qu'on fait pour la lib JGit.

Ou alors vous pouvez remonter le niveau de log global de Log4J.

En // à ce logging Log4J il y a d'autres libs qui utilisent d'autres loggers, en particulier le logging Java de base (`java.logging`), qui est configurée dans `<webapp root>/WEB-INF/classes/logging.properties`. Par defaut au niveau `FINE`, là aussi vous pouvez le remonter si besoin

Tomcat utilise, je pense, aussi ce logging Java de base, mais sa configuration est à priori plutôt dans le `<tomcat root>/conf/logging.properties` mais celui de la webapp prend peut être le dessus => rien de spécifique à Simplicité, à voir plutôt dans la doc ou les forums Tomcat.

Il ne me semble pas avoir déjà vu le type de traces de debug que vous indiquez, il y a peut être des choses que vous avez configuré qui induisent l'apparition de ces traces.

NB: Nous ne livrons aucune configuration par défaut pour d'autres cas de logging (LogBack etc.)
