# Configurer une "Child list with creation"

**URL:** https://community.simplicite.io/t/5718

## Question
### Request description

Bonjour,

Pour certains de nos objets qui ont des relations N,N présentés en onglet, nous souhaiterions pouvoir créer en liste directement l'objet lié et non la relation.
Par exemple nous avons des Domaines reliés à des Flux par un objet DomFlux qui ne contient que les clés étrangères. Sur le Domaine, nous voudrions afficher en onglet les Flux et non les DomFLux, et pouvoir créer des Flux en liste (le DomFLux correspondant se créerait donc automatiquement)

Y a-t-il un paramétrage permettant de le faire ? Sinon une méthode adaptée avec une clé virtuelle ?

Merci d'avance pour votre aide !
Emmanuelle

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

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
Oui c'est une autre solution.
Tu créés un lien virtuel entre Flux et Domaine qui sont les flux du domaine via la relation DomFlux.
Et tu codes dans le postCreate du Flux la création de l'objet DomFlux en fonction du getParentObject().getRowId() du Domaine et getRowId() du Flux.
