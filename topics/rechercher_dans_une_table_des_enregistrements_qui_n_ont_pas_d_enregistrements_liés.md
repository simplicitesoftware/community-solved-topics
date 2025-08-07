# Rechercher dans une table des enregistrements qui n'ont pas d'enregistrements liés

**URL:** https://community.simplicite.io/t/5299

## Question
Bonjour,

Dans une table j'effectue une recherche pour obtenir une liste de personnes correspondant à plusieurs critères :

```
	public void rechercherSeul(Map<String,String> params) {
		String dateN = params.get("dateNaissanceHabitant"); // YYYY-MM-DD HH:MM:SS
		String dateS = params.get("dateDebutSejour"); // YYYY-MM-DD HH:MM:SS
		this.resetFilters();

		this.getField("DomsecoBoHabitantStatutHabitant").setFilter("Actif");
		this.getField("DomsecoBoHabitantTypeResidence").setFilter("Secondaire");
		this.getField("DomsecoBoHabitantEtatCivil").setFilter("='Celibataire' or ='Divorce' or ='Veuf' or ='SepareDeFait' or ='PartenariatDeces' or ='SepareLegal' or ='PartenariatDissous' or ='PartenariatDissousInconnu' or ='PartenariatSeparationDeFait'");
		this.getField("DomsecoBoHabitantDateDebutSejour").setFilterDateMax(dateS);
		this.getField("DomsecoBoHabitantDateNaissance").setFilterDateMin(dateN);
		this.getField("DomsecoBoHabitantEtatDossier").setFilter("is null");
	}	

```
chaque personne est susceptible d'avoir des enregistrements liés, mais j'aimerai ajouter comme critère qu'il ne doit pas y avoir d'enregistrement lié

c'est possible?

Merci

```
Simplicité version4.0 patch level P25Built on2022-07-23 00:06 (revision b8e0951a1092464ec965f2b1cac8bf7c8b6b8501)
```

## Answer
J'ai pensé à cette possibilité, mais je  n'ai pas réussi à la mettre en oeuvre
