# Accès à CoreCache

**URL:** https://community.simplicite.io/t/12129

## Question
### Request description

Bonjour,

Pour implémenter [ces nouvelles méthodes](https://community.simplicite.io/t/methode-getconstraints/11953/4) (merci beaucoup au passage) j'essaie d'utiliser CoreCache.getInstance() mais j'ai une erreur de compilation.
A-t-on perdu l'accès aux APIs bas niveau, ou est-ce que je dois importer quelque chose en particulier ?

Merci pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.8
Variant=full
BuiltOn=2026-04-24 11:37

## Answer
Effectivement depuis un IDE/projet maven, la librairie Simplicité est limitée pour éviter d'utiliser des couches trop bas niveau / privées.

Par contre depuis l'interface / Ace editor, ça compile :

```java
import com.simplicite.util.engine.CoreCache;
...
CoreCache cc = CoreCache.getInstance();
```

On va ajouter un accesseur aux contraintes d'un objet via l'objet lui-même :


```java
import com.simplicite.util.Constraint;
...
Constraint c = this.getConstraint();
```
