# Masquer le bouton de création en liste dynamiquement

**URL:** https://community.simplicite.io/t/4881

## Question
Bonjour, 

J'ai un BO Examen lié à un autre BO Inscription. 

Les 2 apparaissent dans le menu. 
Dans le formulaire des Examen on peut voir la liste des Inscriptions liées. 
Il y a dans ce formulaire un bouton "associer Jeune" qui permet de créer des Inscription en sélectionnant des Jeunes et le bouton de création est masqué. 

Dans l'affichage en liste des Inscriptions depuis le menu, par contre, on affiche le bouton de création.  

Et c'est là que je suis bloqué : 

Pour ne pas afficher le bouton de création dans la liste fille des inscriptions j'ai implémenté ce hook dans le code des Inscriptions. 
```
    @Override
    public boolean isCreateEnable() {
    	
        ObjectDB parentObject = getParentObject();
        return parentObject == null;
    }
```

Le problème c'est que a cause de ce hook, le bouton "associer jeune" dans le formulaire des examen ne fonctionne plus ( il est présent mais au click, il ne se passe rien ). 

Comment faire pour ne pas afficher le bouton de création tout en ayant un bouton "associer jeune " qui fonctionne ? 

Merci par avance.

## Answer
[quote="Francois, post:3, topic:4881"]
`setListAccessNewForm(false);`
[/quote]

Avez vous essayé de mettre ce code dans le hook `initList` en testant que vous êtes sur l'instance désirée ?
- `isPanelInstance()` = une liste fille 
- ou `isMainInstance()` = la liste principale du menu

Du genre

```java
setListAccessNewForm(isMainInstance());
```
