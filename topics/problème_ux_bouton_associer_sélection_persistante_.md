# Problème UX – Bouton "Associer" (sélection persistante)

**URL:** https://community.simplicite.io/t/11465

## Question
### Request description
Bonjour,

Je rencontre un comportement que je n’arrive pas à résoudre proprement et je souhaiterais avoir votre avis sur la bonne pratique standard à adopter.

####  Contexte

* Objet principal : `legalDataprocess`
* Objet associé : `legalDataprocessSubPurpose`
* Association réalisée via le bouton standard **« Associer Sous-finalités »**
* Relation de type vue / association classique
![image|690x345](upload://asPrbuikqfhVQJZMuWQjeMTlo5i.png)

####  Comportement attendu

Lorsque l’utilisateur clique sur **Associer Sous-finalités** :

* la liste des sous-finalités s’ouvre
* l’utilisateur sélectionne **uniquement la / les nouvelles sous-finalités à ajouter**


####  Steps to reproduce

* Lors de la **première association**, tout fonctionne correctement
![image|690x414](upload://4220mzWpHF0PwxhmDSscuFj3jD5.png)
* Lors d’un **deuxième clic** sur *Associer Sous-finalités* :
 la liste s’ouvre **avec les sous-finalités déjà associées pré-cochées**
  
![image|690x319](upload://bzMAHGOB5k36QG0ok7yFROrXM0s.png)

   l’utilisateur est obligé de **décocher manuellement** les sous-finalités déjà associées, puis de cocher uniquement celle qu’il souhaite ajouter.

Cela crée une contrainte UX et un risque d’erreur pour l’utilisateur.

####  Question

Quel serait, selon vous, le **meilleur moyen standard** (et maintenable) pour :

* soit **ouvrir la liste sans pré-sélection**
* soit **n’afficher que les sous-finalités non encore associées**
* soit toute autre approche recommandée 

Je cherche une solution compatible avec les mécanismes standards Simplicité.


Merci d’avance pour vos retours et recommandations.

Cordialement,
Elyass Boussif



### Technical information

[Platform]
Status=OK
Version=6.2.15
BuiltOn=2025-08-15 11:39
Git=6.2/309efbdf46b217e3145711d1c47c3e5ad5459aa5
Encoding=UTF-8
EndpointIP=100.88.252.73
EndpointURL=http://bca-71077-app-595cf98557-8cdsk:8080
TimeZone=Europe/Paris
SystemDate=2026-01-27 13:15:41

[Healthcheck]
Date=2026-01-27 13:15:41
ElapsedTime=7

## Answer
Bonjour Elyass,

En effet la sélection en liste est persistante par défaut, il est possible dans votre cas d’utiliser le hook `postAssociate` pour implémenter le premier comportement que vous mentionnez; *ouvrir la liste sans pré-sélection*

L'association étant souvent utilisée pour les `<N,N>` elle est donc portée par un tierce objet, qui doit lui porté le code implémentant le comportement souhaité avec `child.listUnselectAll();` :

```java
@Override
public String postAssociate(ObjectDB parent, String parentFk, ObjectDB child, String childFk)
{
    child.listUnselectAll();
    return null;
}
```

Ainsi après l'action d'association, l'objet porteur de la `<N,N>` demandera la dé-sélection de tous les objets enfants (ici **legalDataprocessSubPurpose**). Une telle méthode est facilement maintenable car très légère d'un point de vue du code, et n'entraîne pas de manipulation compliquée ou de modifications de vos objets.

Cela correspondrait donc au premier moyen standard que vous mentionnez, et en ce qui concerne le deuxième c'est faisable mais avec des approches (à ma connaissance) plus difficilement maintenable...
