# Contrainte sur une liste en fonction d'un attribut énuméré simple

**URL:** https://community.simplicite.io/t/8776

## Question
### Request description

Dans le cadre d'un processus métier, nous travaillons avec un objet `LegalText` et nous souhaitons contraindre dynamiquement la liste des pays affichés en fonction de la sélection d'un attribut énuméré dans cet objet.(ici la liste des pays  en fonction du périmètre).

![Capture d'écran 2024-09-20 115457|690x203, 75%](upload://sMNnrjzu2dCrdT7EierMNb2yz5s.png)


### Steps to reproduce

* Le champ `Périmètre` est un attribut énuméré simple avec les options `Importateur` ou `Filiale`.
* Le champ `Pays de déploiement` est un attribut enum multiple qui affiche la liste des pays.

* En fonction de la valeur sélectionnée dans le champ `Périmètre` (soit `Importateur`, soit `Filiale`), nous voulons que la liste des pays dans le champ `Pays de déploiement` se mette à jour dynamiquement, en ne proposant que les pays correspondant à cette sélection.

Comme les 2 attributs sont dans la meme activité, il n'y a pas de save pour recuperer au next step la valeur du périmètre et ajuster la liste donc je pense qu'il faudrait le faire dynamiquement , est-ce possible ?

**Question**

* Comment peut-on gérer cette contrainte directement au niveau du processus métier dans Simplicité ? (script front ou businessProcess) ou bien existe-t-il une manière native de filtrer la liste des pays via des contraintes ou des règles métier, plutôt que d'utiliser un script jQuery ?

* Avez-vous des exemples ou des bonnes pratiques pour ce genre de besoin dans le cadre d'un processus métier ?

En attente d'un retour, à bientôt ! :slight_smile: 
### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
L'évolution a été faite et sera backportée en 6.1.9 

pour pouvoir lier une valeur d'`ENUM` à une liste à choix multiples `ENUM-MULTI`, ce qui devrait répondre à votre cas d'usage sans avoir de code à ajouter.

@Hamza

![image|690x207](upload://j3ec82PsQ2NKd7GodjngGoUEfQ3.png)
