# Sélection / modification en masse dans la vue tableur

**URL:** https://community.simplicite.io/t/10813

## Question
### Description

Anomalie sur la sélection / modification en masse dans la vue tableur

### Etape pour reproduire

•	Se rendre en vue tableur d’un objet fonctionnel,
•	Sélectionner 2 enregistrements,
•	Cliquer sur "Modifier en masse", puis modifier le champ "Statut",
•	Cliquer sur "Enregistrer" : Le changement s'applique bien aux 2 enregistrements sélectionnés.
•	Revenir en vue tableur
•	Répéter l'opération avec 1 seul enregistrement sélectionné.
•	Cliquer sur "Modifier en masse", modifier le champ "Statut"
•	Cliquer sur "Enregistrer" : Le changement est appliqué à 3 enregistrements, au lieu du seul enregistrement sélectionné.

![modif_masse|690x257](upload://rvo56x9r6qSXyowCtHsfyJ03n7X.gif)

### Environnements techniques

•	Simplicité version 5.3.79
•	Simplicité version 6.2.12
•	Simplicité version 6.2.17

## Answer
Désolé je ne vous ai pas proposé de réelle solution...

Ce comportement étant standard, si vous voulez l'éviter il faut le déclarer vous même. Vous pouvez donc utiliser le hook `postUpdateAll` de votre objet pour désélectionner automatiquement les objets après que la modification de masse se soit faite :

```
@Override
public void postUpdateAll(Parameters params) {
	this.listUnselectAll();
}
```

Voici le résultat:
![Screen Recording 2025-10-09 at 14.42.51|video](upload://5MKYvFd90rg06mL9plbaqsTxvVi.mov)
