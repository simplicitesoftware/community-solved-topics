# Demande de solution efficace pour rendre un objet non modifiable via contrainte globale

**URL:** https://community.simplicite.io/t/10135

## Question
**Bonjour,**

Je souhaiterais savoir s’il existe une méthode simple et rapide dans Simplicité pour rendre tous les champs d’un objet non modifiables en fonction d’un profil utilisateur donné, via une contrainte globale, sans devoir paramétrer un impact champ par champ (utile si objet avec beaucoup d'attributs).
Version actuelle du socle Simplicite : **5.1.66**

### Contexte :

* Objet concerné : `NamJeune`
* Nombre important de champs (environ une centaine)
* Objectif : Interdire la modification des champs de l’objet aux utilisateurs ayant le rôle `NAM_DSIN`, tout en leur laissant l’accès en lecture.

### Solution testée (non concluante) :

J’ai créé une contrainte avec effet **frontend**, de type **expression**, portée **sur l'objet** `NamJeune` :
![image|690x336](upload://zr8uo55VTgCeuahf6pwAmfWMUvl.png)

* **Propriété impactée** : `Modifier`
* **Expression** utilisée : `![HASRESP:NAM_DSIN]`
![image|690x292](upload://gk7kqYPYQGdunIAcWdLlRvoAz5e.png)

### Résultat :

Lors de mes tests, les utilisateurs disposant du rôle `NAM_DSIN` peuvent toujours modifier les valeurs des champs et enregistrer les modifications. Cela ne semble donc pas suffisant pour bloquer les actions de mise à jour sur l’objet.

### Attentes :

Je cherche une solution plus simple que de définir un impact pour chacun des attributs manuellement (ce qui serait très lourd à maintenir), par exemple :

* Une contrainte de type expression sur l’objet qui empêche toutes modifications en une seule fois ?
* Un mécanisme natif ou une bonne pratique recommandée pour ce type de besoin ?

Merci d’avance pour votre retour et votre aide.

Bien cordialement,

## Answer
Bonjour,

De manière générale, la bonne pratique est d'associer au groupe uniquement une `fonction` en `lecture seule` et non `CRUD`. 
Cependant, si le profil utilisateur inclut un autre groupe qui a également les droits de modification, l'objet restera modifiable.
Nous recommandons de concevoir les groupes de sorte à ajouter des droits au profil plutôt que d'essayer d'en retirer.
Si vous ne pouvez pas réduire les droits au niveau du groupe, il est également possible de le faire par code dans l'objet :
* Si la modification doit être impossible, quel que soit le contexte (liste, panel, formulaire, etc.) : 
Vous pouvez surcharger le hook [postLoad](https://platform.simplicite.io/5.1/javadoc/com/simplicite/util/ObjectHooks.html#postLoad(com.simplicite.util.ObjectDB)) de l'objet et utiliser la fonction [changeAccess](https://platform.simplicite.io/5.1/javadoc/com/simplicite/util/GrantCore.html#changeAccess(java.lang.String,boolean,boolean,boolean,boolean)) pour modifier les droits :

```java
@Override
public void postLoad() {
	Grant g = getGrant(); 
	if(g.hasResponsibility("NAM_DSIN")){
		g.changeAccess("NamJeune",false,true,false,false);//String obj, boolean create, boolean read, boolean update, boolean delete
	}
}
```
* Si vous souhaitez une gestion plus fine des accès : 
Vous pouvez surcharger le hook [isUpdateEnable](https://platform.simplicite.io/5.1/javadoc/com/simplicite/util/ObjectHooks.html#isUpdateEnable(com.simplicite.util.ObjectDB,java.lang.String[])) de l'objet en fonction du contexte.

L'une de ces solutions correspond-elle à votre besoin ?
Cordialement,
Candice.
