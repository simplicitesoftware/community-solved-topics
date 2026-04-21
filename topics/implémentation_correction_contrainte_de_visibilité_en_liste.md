# Implémentation correction contrainte de visibilité en liste

**URL:** https://community.simplicite.io/t/12075

## Question
### Request description

Bonjour,

Je n'arrive pas à implémenter le [hook postMetadata](https://community.simplicite.io/t/correction-visibilite-sur-contrainte-en-liste/11808/12) pour mon souci de [contrainte de visibilité en liste](https://community.simplicite.io/t/contrainte-de-visibilite-en-liste/11771/10).

Sur le même cas :

```
	public void postMetadata(int context, String[] row) {
    if (context==ObjectDB.CONTEXT_LIST && row==null) {
    	
    	AppLog.info("postMetadata 1 " + getField("demoSupPhone").getVisibility(), getGrant());

        getField("demoSupPhone").setVisibility(ObjectField.VIS_BOTH);
        
        AppLog.info("postMetadata 2 " + getField("demoSupPhone").getVisibility(), getGrant());

    }
```

Dernière ligne = 'SUP', la colonne s'affiche
![image|690x366](upload://xNQ1q4nVmTtQtISDE1aGYk1Hnxb.png)

Dernière ligne != 'SUP', la colonne disparaît
![image|690x365](upload://6FajOmlyR17PEpBLs0rBYjklm8H.png)


Dans les logs je vois que j'entre bien dans la condition
![image|690x57](upload://o0MCu1YXJGOEPHRMVlCZXEJBdWs.png)

Mais ça n'est pas appliqué (ou écrasé ?) sur les métadata
![image|690x345](upload://bblOpZ2JeoIvJqXeSZcu31G0KUl.png)

Pouvez-vous m'aider à la mettre en place ?

Merci à vous !
Emmanuelle

[Platform]
Status=OK
Version=6.3.7
Variant=full
BuiltOn=2026-04-03 09:42

## Answer
Ok désolé je n'avais pas vu ce cas d'usage la dernière fois.

`isCreateEnable` n'est pas vide par défaut, il lance entre autre les contraintes pour tester un impact sur la propriété de "création" de l'objet  :

```java
public boolean isCreateEnable() {
	return !isReadOnly() && checkCreateConstraints() && checkCreateVisibilities();
}
```

`checkCreateConstraints` appelle `ObjectDB.checkObjectPropConstraints` dans un contexte de creation mais il avait des impacts trop larges, il ne doit agir/exécuter que les contraintes impactant les propriétés de l'objet.

On s'en sert très rarement car ce fonctionnement/bug date d'avant la V4...
Ce sera corrigé 6.3.8.
