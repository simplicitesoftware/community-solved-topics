# Champ auto-incrément et import CSV

**URL:** https://community.simplicite.io/t/12098

## Question
### Request description

Bonjour,
J'ai un champ *Identifiant* paramétré en auto-incrément (valeur par défaut : *Auto*)

![image|690x108](upload://8LXEL9i0z8AqUCeaUIC8k59sEsX.png)

Si j'importe des données par CSV, l'identifiant reste à Auto.

J'ai tenté de contourner en ajoutant le calcul dans le preImport, mais j'ai l'impression que je dois indiquer moi-même la valeur de l'incrément, ce qui fait perdre l'intérêt de l'auto incrément.

```
	    if (getFieldValue(IDENTIFIER_FIELD).equals("Auto"))
	    {
		    String id = getField(IDENTIFIER_FIELD).increment(this,"1",getField(IDENTIFIER_FIELD).getIncrementPattern());

		    setFieldValue(IDENTIFIER_FIELD, id);
	    }
```

Auriez vous une solution par paramétrage à me conseiller ?

Merci d'avance !
Emmanuelle

[Platform]
Status=OK
Version=6.3.7
Variant=full
BuiltOn=2026-04-03 09:42

## Answer
Je pense que j'ai mal compris, désolé. 

Tu souhaites que l'incrément se calcule automatiquement à l'import ? 

A priori on peut implémenter ça dans le `preCreate` pour forcer le caclul de l'incrément.

```java
@Override
public String preCreate() {
    if (isBatchInstance()) { // import CSV
        ObjectField f = getField("incrementField");
        String idNew = getGrant().getNextIdForColumn(this.getTable(), "row_id");
        f.setValue(f.increment(this, idNew, f.getIncrementPattern()));
    }
    return null;
}
```

Néanmoins, la stratégie varie si le champ auto-incrémenté est clé fonctionnelle de l'objet. Dans ce cas, et c'est pour ça que le code de la plateforme vérifie l'instance, c'est à l'appelant (ici ton fichier CSV) de fournir l'incrément de la ligne.
