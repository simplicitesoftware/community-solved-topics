# Masquage d'une colonne d'une liste via contrainte

**URL:** https://community.simplicite.io/t/2625

## Question
Bonjour

j'ai un objet BCSIRCMModificationRequest contenant 2 champs descriptions EN et FR. Par défault ces champs sont visibles partout.
Je souhaite que l'utilisateur ne puisse voir que la description dans sa langue.
J'ai crée des contraintes sur l'objet. 
![image|690x86](upload://8KiHX85mmSwNEYHRiY6UcusaYex.png) 

Lors de l'édition d'un objet, les champs descriptions sont bien affichés en fonction de la langue de l'utilisateur. Par contre en liste, il y a un comportement "étrange". Les 2 colonnes sont affichées mais seule la colonne dans la langue de l'utilisateur est valuée.
Par exemple : j'ai un requête avec deux descriptions, je suis en langue FR. Ma colonne EN sera vide mais si le champs est renseigné.
![image|270x200](upload://vdHGZB4UsBVz4dwuFhsq2qItswm.png) 

Serait-il possible de mettre en place des contraintes qui masquent totalement une colonne ?
Soit avec une logique de "si aucun item de la liste n'affiche ce champ, on masque la colonne", soit en permettant aux contraintes de s'appliquer sur une liste directement.
Mon objectif serait que toutes les contraintes de visibilité soient écrites au même endroit plutôt que d'en avoir via le paramétrage de "Constraint" et dans un code java pour le initList.

Cordialement
Amandine T.

**[Platform]**
Status=OK
Version=4.0.P24
BuiltOn=2020-09-24 15:23 (revision a577138869ad1d3072630de78ebce39b85303827)
Encoding=UTF-8
EndpointIP=21.0.9.8
EndpointURL=http://c6a0c5487523:8080
TimeZone=Europe/Paris
SystemDate=2020-09-26 11:48:51

## Answer
En liste, un champ "hidden" signifie ne pas afficher la valeur dans la cellule.
car le champ d'une autre ligne peut ne pas être "hidden" = il faut donc la colonne.
On ne peut donc pas réaliser ce que vous demandez de cette manière par visibilité contextuelle à la donnée.

Votre besoin est de spécialiser l'objet en fonction d'une langue, donc contextuellement à l'utilisateur.
Il faut plutôt retirer 1 des 2 champs directement au **postLoad** de l'objet :

```java
if (getGrant().hasResponisibility("X_NOT_ADMIN")) {
  String lang = getGrant().getLang();
  removeField("FRA".equals(lang) ? "fieldEN" : "fieldFR");
}
```

- à ne pas faire pour un profil qui aurait le droit de voir/éditer les 2 champs
- removeField retire le champ de l'objet et de sa zone d'attributs. Il ne sera donc plus affiché du tout nul part pour ce user = aucun besoin de contrainte ou de visibilité liée à la donnée

@Amandine désolé pour le délai de réponse, ce post a été oublié
