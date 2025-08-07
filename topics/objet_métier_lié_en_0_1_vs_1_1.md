# Objet métier lié en 0,1 Vs 1,1

**URL:** https://community.simplicite.io/t/4884

## Question
Bonjour,

Nous avons besoin d'afficher un onglet lorsque le statut d'un dossier passe dans un état.
Le contenu de cette onglet est un objet métier que nous avons lié. 
Tout d'abord avec une cardinalité 0,1 car l'objet métier est obligatoire et unique uniquement à partir d'un statut du worflow . Cela fonctionne mais il y a un bouton switch que nous ne voudrions pas (cf image entourée en rouge). Par défaut le switch est off et donc les données ne sont pas visibles et nous voudrions voir le formulaire sans ce bouton. En fait le comportement attendu est celui que nous avons lorsque nous mettons la cardinalité sur le lien à 1,1. Le problème de cette cardinalité c'est que lors de la création de l'objet dossier il faut aussi crée l'objet dépendant (bon act dans l'exemple) alors que cet objet dépendant n'est obligatoire qu'à partir d'un état.
Est t'il possible de supprimer ce bouton switch et d'avoir l'affichage du formulaire par défaut ?
A quoi sert ce switch ?
Cordialement
Thierry

## Answer
Bonjour,

Dans un lien 0,1, le switch indique si on crée ou on supprime l'objet lié.

Par exemple j'ai une adresse ou pas (lien 0,1). 
Comment savoir qu'il n'y pas d'adresse ?
ou une adresse mais avec champs vides ?

Le cas 1,1, est strict = il y a forcement une adresse en base = pas besoin de switch.

Il faut donc que votre lien soit 0,1 au début du processus.
Puis par hook (`initUpdate` si c'est purement UI ou `postSelect` si c'est aussi pour les appels API en testant la valeur du statut) que vous changiez la cardinalité du Link.

```java
boolean oblig = <condition>;
getLink("object_name","foreign_key_field").setMinOccurs(oblig ? 1 : 0);
```


https://docs.simplicite.io/5/javadoc/com/simplicite/util/Link.html
