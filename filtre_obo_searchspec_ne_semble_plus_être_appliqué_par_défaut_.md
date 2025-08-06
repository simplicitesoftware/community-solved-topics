# Filtre obo_searchspec ne semble plus être appliqué (par défaut)

**URL:** https://community.simplicite.io/t/4000

## Question
Bonjour,
Dans le cadre d'un héritage, j'observe une différence de comportement entre la v4 et la v5 sur la prise en compte du filtre obo_searchspec (forçant le filtre sur le sous-type de l'héritier) qui n'est plus appliqué lors des imports XML.

J'ai essayé de restaurer le comportement initial en ajoutant explicitement un setSearchSpec(getDefaultSearchSpec()+"...") dans le preSearch mais ça n'est pas pris en compte dans le cadre des imports XML.

```
	@Override
	public void preSearch() {
		/*
		 ** DEBT: obo_searchspec lost in translation
		 */
		if (!getSearchSpec().contains(getDefaultSearchSpec())) {
			warn("preSearch", "DEBT/obo_searchspec lost in translation getSearchSpec="+getSearchSpec(), this);
			setSearchSpec(getDefaultSearchSpec()+" AND "+getSearchSpec());
		}
		/**/
	}
```

Version=5.1.10
BuiltOn=2021-10-21 00:59
Git=release/80f882d651de1e53044367f00a1f1b5e1bf46c6e

## Answer
Apres vérification, la searchspec est bien présente même pour un héritier d'un objet system. 

Par contre elle ne sert pas à retrouver une FK basée sur les données fournies dans le XML.

Il faut bien que le XML soit complet, les champs inutiles pouvant être juste masqués sur la UI.
