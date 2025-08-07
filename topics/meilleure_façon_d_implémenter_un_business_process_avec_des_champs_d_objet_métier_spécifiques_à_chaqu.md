# Meilleure façon d'implémenter un Business Process avec des champs d'objet métier spécifiques à chaque étape

**URL:** https://community.simplicite.io/t/6827

## Question
### Request description

Bonjour,

Je travaille actuellement sur la mise en place d'un Business Process dans Simplicité, et j'ai rencontré un défi que je souhaiterais résoudre de la manière la plus efficace possible.

Mon Business Process implique un objet métier complexe avec de nombreux champs. Cependant, à chaque étape du processus, je n'ai besoin que de certains champs spécifiques de cet objet métier pour être visibles et éditables.

J'ai exploré diverses options pour gérer cela mais je ne suis pas sûr de la meilleure approche à suivre pour optimiser la gestion des champs à chaque étape.

Je me demande s'il existe une manière recommandée ou une meilleure pratique pour diviser les champs de l'objet métier en différentes étapes de mon Business Process, en garantissant que seuls les champs pertinents sont visibles et éditables à chaque étape.

Toute orientation ou conseil que vous pourriez fournir serait grandement apprécié. Je suis ouvert à toute suggestion ou méthode que vous pourriez recommander pour résoudre ce problème.

Merci d'avance pour votre aide et vos conseils précieux.

Cordialement,
Elyass

### Technical information

[details="Instance /health"]
[Platform]
Status=OK
Version=5.3.12
BuiltOn=2023-08-25 09:44
Git=5.3/e2cd9f0ea850e3845169840790a1a6ef043fed16
Encoding=UTF-8
EndpointIP=149.202.171.75
EndpointURL=http://renault.simplicite.io:10488
TimeZone=Europe/Paris
SystemDate=2023-09-01 10:40:25
[/details]

## Answer
Merci pour ces précisions,

Effectivement, vos étapes s'apparentent à un screenflow d'aide à la saisie d'un formulaire complexe.
Vous pouvez donc utiliser un Processus :
- dont la première activité est une création / **New**
- les suivantes sont des mises à jour / **Update** du row_id à mapper sur la 1ere activité :
   1) soit sur le même objet et par code, vous pouvez récupérer l'étape et masquer les zones ou les attributs (hook pre/postLock décrit plus haut pour modifier l'instance getProcessInstance et les données de l'activité).
   2) soit sur des objets dédiés à chaque étape (même table physique) qui n'ont que les champs/zones nécessaires
- L'activité finale peut contenir un **Forward** vers l'objet complet

Le 1) à l'avantage de n'avoir qu'un "gros" objet contextualisé par code.

```java
@Override
public void preLock(ActivityFile context) {
	super.preLock(context);
	// any "update" after the "new"
	if (context.getActivity().getStep().equals("MY-STEP-2")) {
		// get the first "new" activity to get the created row_id
		Activity a = getActivity("MY-STEP-1"); 
		String rowId = getContext(a).getDataValue("Field", "row_id");
		// Force current activity to update this record
		context.setDataFile("Field", "row_id", rowId);
		// Simplify object definition
		ObjectDB o = getGrant().getProcessInstance("MyBigObject");
		o.getField("x").setVisibility(ObjectField.VIS_HIDDEN);
		o.getFieldArea("MyBigObject-1").setVisible(false);
		// ...
	}
	// else STEP-3 ...
}
```
Le 2) à l'avantage de n'avoir que des objets allégés paramétrés et sans code (le row_id pouvant se passer par paramétrage dans les activités suivantes : 
Group=`Field`, Name=`row_id`, Value = `[STEP-1.Field.row_id]`.

https://docs.simplicite.io/docs/core/businessworkflow-code-hooks

Voir la démo pour le forward final.
