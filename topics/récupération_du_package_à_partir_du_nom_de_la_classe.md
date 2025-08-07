# Récupération du package à partir du nom de la classe

**URL:** https://community.simplicite.io/t/6090

## Question
Bonjour,

En travaillant sur l'amélioration de nos tests unitaires, j'aurais voulu savoir s'il existe une méthode pour récupérer le package d'une classe à partir de son nom. (je n'ai pas trouvé mon bonheur dans la Javadoc)

Le but serait de l'utiliser dans ce cadre :

> @Override
> public String unitTests() {
>     return new JUnitTool(getGrant()).run("com.simplicite.tests.MyModule.MyServerTest");
> }

En résumé pouvoir récupérer "com.simplicite.tests.MyModule.MyServerTest" à partir de "MyServerTest".

Merci d'avance,

Benoît

## Answer
Bonjour,

Je ne crois pas que cela existe, dans la mesure où vous connaissez déjà le nom du module et de l'objet, le plus simple c'est :

```java
String cls = Globals.DEFAULT_TESTS_PACKAGE + ".MyModule.MyServerTest";
```

Sinon, s'il faut récupérer le module de l'objet via son nom :

```java
String moduleId = ObjectDB.getModuleIdByName("MyServerTest");
String moduleName = ModuleDB.getModuleName(moduleId);
String cls = Globals.DEFAULT_TESTS_PACKAGE + "." + moduleName + ".MyServerTest";
```
