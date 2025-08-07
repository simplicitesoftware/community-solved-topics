# Trier les enregistrements sélectionnés

**URL:** https://community.simplicite.io/t/3189

## Question
Bonjour,
J'ai un objet métier dont les attributs sont triés selon un ordre défini.

J'ai une action qui va créer un xml avec les enregistrements sélectionnés ( ou tous les enregistrements si pas de sélection) avec un ordre différent.

> 		ObjectDB entite = this.getGrant().getTmpObject("ParticipationEntite");
		entite.resetFilters();
		entite.resetOrders();
		entite.getField("ParticipationEntiteTypePers").setOrder(1);
		entite.getField("participationDirectionLibelle").setOrder(2);
		//trouve les éléments sélectionnés, si pas de sélection prend tous les éléments
		List<String> ids  = this.getSelectedIds();
		List<String[]> rows  = new ArrayList<String[]>();

Mais au final, c'est l'ordre dans lequel j'ai sélectionné les enregistrements qui est conservé...

## Answer
C'est du java... et comme ça ?

```
String[] list = new String[ids.size()];
list = ids.toArray(list);
```

sinon faites une boucle pour faire le join à la main.
