# Ajouter un filtre par défaut dans Select

**URL:** https://community.simplicite.io/t/6930

## Question
Version : 5.2.42

 Dans le contexte de notre projet,Nous avons besoin de mettre en place un filtre par défaut pour une liste d'éléments, mais nous faisons face à des difficultés pour le configurer correctement.

Notre situation implique deux objets, à savoir l'objet A (Enfant) et l'objet B (Parent), avec une relation de type 1..n entre eux. Notre objectif est d'afficher dans l'IHM A uniquement les éléments de l'objet B qui possèdent un statut spécifique.

![image|690x226](upload://nQ68Vzm2oiVB5MAE5YyClLylcZY.png)


Dans le but d'atteindre cet objectif, nous avons entrepris plusieurs tentatives en utilisant les fonctions initList, preSearch et specSearch. Malheureusement, aucune de ces approches n'a donné les résultats souhaités, et le filtre par défaut ne fonctionne pas correctement.

## Answer
Vous pouvez utiliser le hook initRefSelect. 
https://docs.simplicite.io/docs/core/businessobject-code-hooks
Il est appelé lorsque vous cliquez sur la loupe pour sélectionner une donnée objet B. 
Il vous permettra de positionner un filtre sur un attribut de l'objet B.

ou utiliser dans le code la notion de ref instance (isRefInstance) 

 
```
@Override
 	public void preSearch() {
 		if(isRefInstance() && ...){
 			setFieldFilter("Status", "X");	
 		}	
 	}
```
