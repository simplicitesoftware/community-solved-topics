# Recherche en liste sur vue pré filtrée

**URL:** https://community.simplicite.io/t/5642

## Question
### Request description

Bonjour, j'ai une vue de type Search sur laquelle j'ai mis un filtre sur un champ de type Liste de valeurs.

![image|244x122](upload://kcK8eddfHjgHAFW6qcuEcVsfeGR.png)


J'aimerais pouvoir quand même rechercher sur ce champ parmi les valeurs acceptées dans mon filtre, mais la zone de recherche n'apparaît pas.

![image|453x140](upload://svhUDBO2TvDF0UnaV7nBqNi53bn.png)

Y a-t-il un moyen ?

Merci !

## Answer
Bonjour,

Ce n'est pas possible puisque la liste est déjà pré-filtrée sur ce champ.
Si l'utilisateur pouvait modifier ce filtre, comment pourrait-il revenir à ces filtres plus tard ?
Cette fonctionnalité sert à afficher des bannettes avec des filtres statiques.

A mon avis, votre de besoin est peut être de positionner des filtres par défaut sur cette instance, mais modifiable pour le user ensuite : 

```java
public void postLoad() {
  if (isHomeInstance())
    setFieldFilter("rciAppstate", "INSTALLED;PROJECT"); // or "in ('INSTALLED','PROJECT')"
}
```
Mais rien de forcé dans la predefined search pour laisser le statut à la main de l'utilisateur.

Sinon utilisez la fonctionnalité qui permet d'afficher les recherches prédéfinies de l'objet dans un dropdown en liste :

Activez le sur l'objet 

![image|350x80](upload://v0MfgsScy8yitPT8FMskBCsvGmn.png)

- Edition = pour permettre à l'utilisateur d'en créer, 
- sinon Usage seul = il faut livrer N recherches prédéfinies sur l'objets
- Accès en liste = oui

ou une seule instance par code :

```java
if (isHomeInstance()) {
  setPredefSearch(true);
  setPredefSearchOnList(true);
}
```

L'utilisateur peut choisir ou effacer la recherche en cours :

![image|690x184](upload://fCU8mBSaRnOsbbT8awc8vt0Eafi.png)
