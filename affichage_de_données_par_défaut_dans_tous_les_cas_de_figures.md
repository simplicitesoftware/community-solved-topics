# Affichage de données par défaut dans tous les cas de figures

**URL:** https://community.simplicite.io/t/9136

## Question
Bonjour,

J'ai trois tables :

* Entite
* Titre
* AchatVente

Entite est liée à Titre (0,n)
Titre est liée à AchatVente (0,n)

Pour faciliter le traitement et l'affichage :

* lorsque j'ouvre un formulaire Entite j'aimerai que seuls les Titre de l'année en cours sont affichés
* lorsque j'affiche le formulaire Titre j'aimerai aussi que seuls ceux de l'année sont affichés
* dans les 2 cas l'utilisateur doit pouvoir supprimer ce filtrage par défaut pour faire d'autres recherches

En parcourant le forum j'ai trouvé des informations pour que la table Titre soit filtrée par défaut sur l'année en cours

```
	@Override
	public void preSearch() {
		AppLog.info(getClass(), "preSearch titre a été appelé //  INIT_FILTER_FLAG_TITRE ::::::  " + INIT_FILTER_FLAG_TITRE,null, getGrant());
		if(isMainInstance() && getGrant().getBooleanParameter(INIT_FILTER_FLAG_TITRE, true)){
			getGrant().setParameter(INIT_FILTER_FLAG_TITRE, false);
			
			int anneeEnCours = Tools.nouvelleAnnee(0,"");
			setFieldFilter("ParticipationTitreAnnee", anneeEnCours);
		}

	}
```

ça fonctionne bien sur l'objet principal, mais pas sur la vue Titre qui se trouve dans le formulaire Entite.

Comment dois-je compléter mon code?

Merci
Fabrice

## Answer
[quote="Francois, post:2, topic:9136"]
isPanelInstance
[/quote]

Merci... tout fonctionne comme prévu :-)
