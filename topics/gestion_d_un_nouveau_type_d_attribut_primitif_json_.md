# Gestion d'un nouveau type d'attribut primitif "JSON"

**URL:** https://community.simplicite.io/t/11425

## Question
### Version

*6.2*

### Description

Nous sommes amenés dans certains cas à gérer un sous-ensemble d’information structurée au format JSON à la maille object field. Le type primitif utilisé dans ce contexte est “Texte long” et les opérations réalisées sont supportées par des instances de JSONObject sérialisées/désérialisées lors des interactions avec le modèle logique.

Lorsque l’attribut d’objet est exposé via une API, le contenu de l’object field est servi en tant que String

```json
{
  ...,
  "thereWeHaveJson": "{\"key\": \"value\"}",
  ...
}
```

Serait-il envisageable que l’object field soit de type primitif JSON pour 

1. pouvoir directement utiliser l’instance de classe JSONObject lors des get|setValue
2. pouvoir directement disposer de la structure JSON dans le body servi par l’API

```
{
  ...,
  "thereWeHaveJson": {
    "key": "value"
  },
  ...

}
```

Par extension de cette logique, est-il envisageable que les autres types primitifs soient servis tels que dans le body json ? (entiers et booléen en particulier)

## Answer
C'est corrigé:

![image|690x276](upload://A3UZumqmDi3knJdf2ATl1OMzp90.png)

Ce sera livré en v7, en v6 (6.2.22 & 6.3.1) et en v5 (5.3.83)

**Attention** vérifier que cette correction ne provoquera pas de régressions du coté des clients de ces APIs qui auraient contourné le pb en faisant un parsing JSON de la valeur JSON renvoyée sous forme de chaine de caractères (la correction en question ne concerne bien que les fields de type texte long **avec rendering JSON**)
