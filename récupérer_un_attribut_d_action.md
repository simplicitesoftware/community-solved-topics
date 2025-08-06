# Récupérer un attribut d'action

**URL:** https://community.simplicite.io/t/3250

## Question
Bonjour je souhaiterais savoir comment récupérer un attribut d'action.

Dans la V5 j'ai vu que la fonction prenait en paramètre une action, mais ce n'est pas le cas en V4.

De ce fait quelle est la bonne pratique pour récupérer la valeur du paramètre ?

Merci d'avance,

Benoît

## Answer
Bonjour,

En version 4 vous pouvez passer des paramètres dans le invokeAction via un HashMap
Par exemple 
```
Map<String, String> params = new HashMap<>();
params.put("ACTION_PARAM", value);
String msg = invokeAction("myActionName", params);
```
ou bien comme dans le module Demo pour passer la quantité commandée, utiliser un paramètre d'objet. Il est également possible d'utiliser un paramètre de session (getGrant().setParameter("PARAM",value))
Exemple du postUpdate de DemoOrder
```
ObjectDB prd = getGrant().getTmpObject("DemoProduct");
...
prd.setParameter("QUANTITY", q);
prd.invokeAction("DEMO_DECSTOCK");
prd.removeParameter("QUANTITY");
```
Méthode decreaseStock de l'objet DemoProduct
```
int q = getIntParameter("QUANTITY", 0);
...
```


Cordialement
