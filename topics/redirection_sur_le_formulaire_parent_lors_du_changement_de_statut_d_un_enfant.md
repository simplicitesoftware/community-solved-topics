# Redirection sur le formulaire parent lors du changement de statut d'un enfant

**URL:** https://community.simplicite.io/t/11492

## Question
*Bonjour,*

J’ai un objet parent qui a plusieurs objets enfants.

Lorsque je suis sur le formulaire enfant et que je valide le formulaire, j’aimerais que mon action (qui change le statut de l’enfant) me redirige vers le formulaire parent.

Merci pour votre aide.

###

## Answer
Bonjour Benoît, bienvenu sur notre forum !

Pour implémenter un tel comportement il y a un exemple dans notre documentation :
https://docs.simplicite.io/docs/core/objects/businessobject-code-hooks/#pre-and-post-save-hooks

> Cette dernière regorge d'exemples de code pour ce type de comportement et bien d'autres. N'hésitez pas à la consulter pour vos prochains développements, et nous restons évidemment disponibles ici pour toute question !

---

Vous pouvez donc implémenter un retour au formulaire du parent avec le code suivant:
```java
// Goto this form instead of reloading the current object
String url = HTMLTool.getFormURL("User", null, "1", "nav=add");
return HTMLTool.redirectStatement(url);
```

La signature de `HTMLTool.getFormURL` dans ce cas étant `(String objName, String objInstanceName, String rowId, String params)`, ce qui dans votre cas d'usage s'adaptera surement comme :

```java
public String yourCustomAction(..) {
    // ... your current action code ...
    String url = HTMLTool.getFormURL("ParentObjectName", null, getFieldValue("fieldParentId"), "nav=add");
    return  HTMLTool.redirectStatement(url);
}
```

J'espère que cela répond à votre besoin !
