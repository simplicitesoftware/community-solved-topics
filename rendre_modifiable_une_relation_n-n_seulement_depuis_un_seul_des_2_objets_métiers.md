# Rendre modifiable une relation n-n seulement depuis un seul des 2 objets métiers

**URL:** https://community.simplicite.io/t/4515

## Question
Bonjour,

J'ai une relation **`Many To Many`** entre 2 objets métiers.
Imaginons que les objets métiers A et B ont une relation **`Many to Many`** par l'intermédiaire d'un objet C.
De ce fait, il est possible de créer des relations entre ces 2 objets grâce à une vue de l'objet C qui est automatiquement ajoutée sur les formulaires.

J'aimerais pouvoir créer une relation entre ces 2 objets uniquement à partir de l'objet A et pourvoir continuer à voir la relation sur les 2 objets A et B.

**Avez -vous une solution ?**

Voici mon objet A (Equipe):
![image|690x354](upload://oldqGHSQKfIOkPidqYFLBHvRuJ0.png)
Voici mon objet B (Politique de droit de vote):
![image|690x329](upload://v9tbjc5t7bGPquMHbmxbVpGKZUe.png)

Je veux pouvoir créer/modifier l'objet C (Posséder) **uniquement** dans l'objet A (Equipe), mais je veux continuer à avoir un visuel de l'objet C (posséder) dans l'objet A (Equipe) et B (politique de droit de vote).

## Answer
Bonjour, 

Vous pouvez implémenter le hook `isCreateEnable` au niveau de l'objet Posséder.

Par exemple :
```
@Override
	public boolean isCreateEnable() {
		//creation is only possible when not a panel instance of MyObj
		return !isPanelOf("MyObj");
	}

```
