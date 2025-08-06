# java.io.IOException: Empty document / JavaTool.getJavaDocument

**URL:** https://community.simplicite.io/t/7962

## Question
### Request description

*Suite à l'import de module automatique via la fonctionnalité import-spec.yml, nous observons de nombreux cas d'Exception `java.io.IOException: Empty document / JavaTool.getJavaDocument` La solution de contournement appliquée consiste à réediter le code de l'objet concerné (ajout/suppression d'un espace par exemple) puis sauvegarder pour déclencher une recompilation dans le conteneur sur lequel le user (avec un rôle DESIGNER) est connecté. Cela permet de résoudre temporairement le problème dans le conteneur courant jusqu'au prochain démarrage d'un autre conteneur portant la même configuration. Ce problème est d'autant plus saillant que nous ne pouvons pas facilement accéder à un conteneur en particulier pour appliquer la procédure décrite et que la population des conteneurs est très changeante dans le contexte GKE/K8S. Je ne suis pas certain que la fonctionnalité import-spec.yml soit directement en cause mais les seuls objets concernés sont ceux des modules importés par ce moyen. Par contre, l'erreur survient au sein de conteneurs pour lesquels nous avons inhibé cette étape d'import-spec (en gros, nous essayons de faire en sorte que l'import spec soit réalisé par le premier conteneur qui démarre et que les suivants ne fassent rien car la configuration est partagée au sein d'un CloudSQL commun).*

*Nous observons ce comportement sur les version 5.2 (5.2.54 a priori à jour) et 5.3.28.*

```
2024-03-22 11:59:31,582|SIMPLICITE|INFO||http://rcf-70786-app-5c5bd48bf4-8vn4f:8080||INFO|designer|com.simplicite.objects.System.ObjectInternal|partialClearCache||Event: Partial clear cache for object RenaultPerson
2024-03-22 11:59:31,548|SIMPLICITE|INFO||http://rcf-70786-app-5c5bd48bf4-8vn4f:8080||INFO|system|com.simplicite.util.engine.CoreCache|loadDynamicJar||Event: Loaded dynamic JARs
2024-03-22 11:59:31,548|SIMPLICITE|INFO||http://rcf-70786-app-5c5bd48bf4-8vn4f:8080||INFO|system|com.simplicite.util.engine.DynamicClassLoader|DynamicClassLoader||Event: Instanciate DynamicClassLoader@1ab9fc26
2024-03-22 11:59:29,518|SIMPLICITE|INFO||http://rcf-70786-app-5c5bd48bf4-8vn4f:8080||INFO|system|com.simplicite.util.engine.DynamicClassLoader|compile||Event: Compiling all classes from src:/usr/local/tomcat/webapps/ROOT/WEB-INF/src to bin:/usr/local/tomcat/webapps/ROOT/WEB-INF/bin
2024-03-22 11:59:29,121|SIMPLICITE|INFO||http://rcf-70786-app-5c5bd48bf4-8vn4f:8080||INFO|system|com.simplicite.util.tools.JavaTool|getClass||Event: Java class com.simplicite.objects.RenaultPerson.RenaultPerson compiled
2024-03-22 11:59:20,411|SIMPLICITE|ERROR||http://rcf-70786-app-5c5bd48bf4-8vn4f:8080||ECORESC001|system|com.simplicite.util.engine.ScriptAgent|prepareSource||Script error: RenaultPerson
    java.io.IOException: Empty document
     at com.simplicite.util.tools.JavaTool.getJavaDocument(JavaTool.java:795)
     at com.simplicite.util.engine.ScriptAgent.prepareSource(ScriptAgent.java:250)
     at com.simplicite.util.ScriptedObjectDB.prepareSource(ScriptedObjectDB.java:63)
     at com.simplicite.util.ScriptedObjectDB.postLoad(ScriptedObjectDB.java:114)
     at com.simplicite.util.engine.ConfigurationObject.postLoad(ConfigurationObject.java:40)
     at com.simplicite.objects.System.SimpleUser.postLoad(SimpleUser.java:54)
     at com.simplicite.util.ObjectHooks.postLoad(ObjectHooks.java:29)
     at com.simplicite.util.engine.ObjectLoader.load(ObjectLoader.java:105)
     at com.simplicite.util.engine.ObjectDirect.init(ObjectDirect.java:48)
     at com.simplicite.util.ObjectDB.init(ObjectDB.java:244)
     at com.simplicite.util.ObjectDB.load(ObjectDB.java:222)
     at com.simplicite.util.engine.CoreCache.instantiateObject(CoreCache.java:4110)
     at com.simplicite.util.engine.CoreCache.getObject(CoreCache.java:4043)
     at com.simplicite.util.engine.CoreCache.preCompileObject(CoreCache.java:459)
     at com.simplicite.util.engine.CoreCache.getObjectDefinition(CoreCache.java:3962)
     at com.simplicite.objects.System.ObjectInternal.initUpdate(ObjectInternal.java:514)
     at com.simplicite.util.ObjectHooks.initUpdate(ObjectHooks.java:79)
     at com.simplicite.util.ObjectContext.apply(ObjectContext.java:379)
     at com.simplicite.webapp.ObjectContextWeb.apply(ObjectContextWeb.java:291)
     ...
     at java.base/java.lang.Thread.run(Thread.java:833)
```

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
OK si un seul noeud execute l'import par importspec ça devrait aller (on fait ce genre de choses en permanence, s'il y avait un pb de ce type on l'aurait vu passer).

Pour améliorer les choses on va regarder pour ajouter un principe de lock à la manière du lock de la cron pour s'assurer qu'un seul noeud effectue les imports (ça peut devenir rapidement compliqué si on doit prévoir le cas où un noeud serait tué en plein pendant l'import, donc pour faire simple on va laisser cas de coté pour le moment)

Tu ne m'as pas répondu sur ce qui est utilisé comme critère pour considérer qu’une instance est totalement démarrée. je pose la question car c'est un point d'attention à avoir vs la conception du lock.

PS: le flag de mise à jour auto des modules était une ancienne feature d'avant les importspecs. Ca permettait de forcer le réimport de modules via une tâche cron dans une logique de "continuous delivery" basique de l'époque (NB: c'est pas aussi subtil que l'import spec car ça ne checke pas la version pour vérifier que re réimport est nécessaire ou pas). Bref rien à voir avec la mécanique de l'importspec et c'est assez obsolète vs les usages actuels CI/CD, donc plutôt à éviter.
