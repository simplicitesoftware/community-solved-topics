# Désélections sur des associations

**URL:** https://community.simplicite.io/t/7645

## Question
Bonjour, 

Je souhaite pouvoir désélectionner toutes les lignes de la liste lors du clic sur le bouton "associer". 
Car à la deuxième association, la liste garde les lignes sélectionnées lors de l'association précédente. 

J'arrive bien à désélectionner les lignes mais je ne trouve pas le bon hook.
> if (isRefInstance()) resetSelectedIds();.

J'ai essayé sur les hooks initRefSelect() et initList() mais ces deux hooks ne sont appelés que à la première initialisation de la liste et ne sont pas appelés à la deuxième association.

J'ai essayé avec le hook initAssociate() mais le hook est appelé à chaque changement de page de la liste du coup ça désélectionne ce que j'ai sélectionnée sur la première page quand je change de page. 

Mon besoin : désélectionner uniquement au clic sur le bouton associer.

version : 5.1.66

Avez-vous 

Cordialement,
Florian

## Answer
Florian, 

En l'état la 5.3.27 appelle le hook initAssociate à chaque chargement de page. 
On mettra à disposition un hook `postAssociate` dans les versions à venir permettant de facilement répondre au besoin. 

En attendant, tu peux sans doute contourner le comportement standard en vidant les selectedIds dans un hook de l'objet parent, par exemple : 

```java
@Override
public void initList(ObjectDB parent) {
	getGrant().getRefObject("MyObject").resetSelectedIds();
}
```
