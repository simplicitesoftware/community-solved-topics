# Pas de load des metadata à l'initUpdate pour une pillbox

**URL:** https://community.simplicite.io/t/11176

## Question
### Request description

Bonjour, 

Je viens d'installer la dernière image et j'ai malheureusement encore un souci avec les pillbox :grimacing:

Quand j'affiche mon objet en liste, j'ai bien un get sur les metadata des pillbox pour chaque ligne.
Mais quand je clique sur une ligne, le get n'est pas réeffectué sur cette dernière, ce qui fait que je travaille avec les metadata de la dernière ligne de la liste.

Au chargement de la liste (12 lignes)
![image|690x287](upload://wMcLpnliVZoKupvByjuYB0dIpYw.png)

La dernière ligne est à Draft, ce qui veut dire que j'ai le droit de Create sur les pillbox (codé dans le isCreateEnable)
![image|690x111](upload://8YBFHhPc6rgAgB8VJVWqm4PDAzy.png)

![image|690x68](upload://oFzY3iFWUBVfRd8lAJX0jvtRk0g.png)

Jusqu'ici c'est normal, mais si je clique sur une autre ligne en Validated (pas de droits de Create sur les pillbox), le get n'est pas refait, j'ai donc encore les droits.

![image|690x158](upload://ddeaczrhiXVc8PNznTZAo5ThnKz.png)

*(difficile de montrer l'absence de quelque chose, mais ici je suppose que je devrais avoir une nouvelle ligne)*
![image|690x302](upload://aD3QBKcMdCduNG9ivPKwgthAZqU.png)

![image|690x80](upload://k4bJqo1Pa1i48aMp5Cx0KxSUQqO.png)

En analysant, je vois qu'à cet endroit, ```obj.metadata.context``` est égal à  ```params.context```, ce qui débraye le passage dans getMetaData.

```obj && (!obj.isLoaded() || (params.context && (obj.metadata.context != params.context || params.context == $app.CONTEXT_REFSELECT))) ? obj.getMetaData(params).then(set) : set();```

En mettant ceci avant le chargement de ma ligne, j'arrive à contourner le problème, mais j'avoue que je ne comprends pas trop ce que je fais et quels seraient les impacts.

```$app._businessObjectsCache["RciFormApiDomApp:panel_ajax_RciFormApiDomApp_rciFormApiDomAppFormApiId"].metadata.context = null;```

Je suis donc preneuse de conseils ! Et désolée pour ce nouveau souci "pillbox" ...

Merci !
Emmanuelle

> [Platform]
> Status=OK
> Version=6.2.19
> BuiltOn=2025-12-05 11:56

## Answer
Ca semble aussi corriger le cas 2.
Voici le code utilisé pour tester dans l'objet N,N de la pillbox :

```java
@Override
public boolean isCreateEnable() {
	ObjectDB p = getParentObject();
	if (p!=null) {
		String status = p.getFieldValue("xxx");
		AppLog.info("status="+status + " id=" + p.getRowId() + " new="+p.isNew());
		return "DRAFT".equals(status) || p.isNew();
	}
    return true;
}
```

- En création et en recopie du père : `p.isNew()` est vrai et `p.getRowId()` = "0", et on accède à la création en pillbox
- idem en mise à jour d'un parent en "DRAFT"

On va livrer le correctif.
