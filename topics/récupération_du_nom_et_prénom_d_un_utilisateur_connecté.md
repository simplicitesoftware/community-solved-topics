# Récupération du nom et prénom d'un utilisateur connecté

**URL:** https://community.simplicite.io/t/4976

## Question
Bonjour,

Je cherche à récupérer les informations demandées dans le titre depuis un objet métier quelconque. Je suis passé avec le moyen ci-dessous :

```java
String userAttributes = CrowdTool.getUserAttributes(getGrant().getLogin());
```

Cependant, j'ai l'erreur suivante :

```text
2022-06-16 13:55:05,930|SIMPLICITE|ERROR||http://5ffef106419a:8080||ERROR|system|com.simplicite.util.tools.CrowdTool|call||Event: service fault: /user?expand=attributes&username=designer
    java.net.MalformedURLException: no protocol: null/user?expand=attributes&username=designer
     at java.base/java.net.URL.<init>(URL.java:674)
     at java.base/java.net.URL.<init>(URL.java:569)
     at java.base/java.net.URL.<init>(URL.java:516)
     at com.simplicite.util.Tool.readUrlAsByteArray(Tool.java:4500)
     at com.simplicite.util.Tool.readUrl(Tool.java:4318)
     at com.simplicite.util.tools.CrowdTool.call(CrowdTool.java:133)
     at com.simplicite.util.tools.CrowdTool.getUserAttributes(CrowdTool.java:262)
     at com.simplicite.objects.ladnext.LadDossierAct.imprimerBonAct(LadDossierAct.java:463)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
     at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
     at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
     at java.base/java.lang.reflect.Method.invoke(Method.java:568)
     at com.simplicite.util.engine.ObjectManager.invokePrint(ObjectManager.java:4240)
     at com.simplicite.util.engine.ObjectDirect.invokePrint(ObjectDirect.java:678)
     at com.simplicite.util.ObjectDB.invokePrint(ObjectDB.java:2113)
     at com.simplicite.util.PrintTemplate.fillWithCurrentObject(PrintTemplate.java:1616)
     at com.simplicite.webapp.ObjectPrint.printone(ObjectPrint.java:256)
```

Pouvez-vous m'aider svp ?

En vous remerciant.

Bruno

## Answer
Bonjour Bruno, 

Est-ce que le user `designer` existe dans Crowd ?

Pourquoi ne pas utiliser `getGrant().getFistName()` et `getGrant().getLastName()`?
