# Erreur : "Unable to get row ID 2009 for object Domain"

**URL:** https://community.simplicite.io/t/6341

## Question
Erreur lors de la création d'un Nouveau Module

Bonjour, je suis actuellement en train de me former sur Simplicité, après avoir fait le Tutoriel d'apprentissage, j'ai voulu me re-tester sur ce lien :  https://training.simplicite.io/training/business-objects-configuration/a010-create-a-module/
Mais si en apparence la création de mon nouveau module se passe, la création de Groupe et de nouveau Domaine me renvoie sur la même anomalie.

Je n'ai pas un Background de dev très développé ^^'. J'ai bien lu les réponses apportées dans le Forum pour ce type d'anomalie mais je n'ai pas réussi à trouver le lien avec mon cas. A savoir que je suis toujours sur le compte test "Designer" auquel l'on m'a donné accès et sur lequel j'ai déjà fait le tutoriel, il y a t'il une limite en terme de création d'Objects sur ce compte ?

### Etape 1 création Module 
![CreationMyModule|690x263](upload://rtkDVa0lJVhfzaYzbkW266ia8F4.png)

### Etape 2 Création Group avec Erreur "Unable to get row ID 55 for object Group"
![errGetrowID55forobjectGroup|690x347](upload://m32ikStcBtzlnVUYYLG6vrQVzzL.png)

### Etape 3 Création Domaine avec Erreur "Unable to get row ID 2009 for object Domain"
![UnableToGetRowID2009forObjectDomain|690x345](upload://ytbvY6AcvISQAep7AaD7x8gPV97.png)

Si j'insiste j'ai un message m'informant que clé fonctionnelle Domaine existe déjà : 
![CleFonctioExisteDeja|690x352](upload://h0JDWiPp5wSXTiV4b0ofHla5obP.png)

Mais en revenant dans ma liste de Domaines, je n'ai que celui de mon Tutoriel : 
![MaisNonLeMyDomainIlestpaslà|690x348](upload://xTKA0WwKmAyXlxIeh0eSG0qODSR.png)

Je vous remercie d'avance pour toutes réponses à ce sujet.

## Answer
Bonjour,

La version à jour du tutoriel se trouve ici: https://docs2.simplicite.io Où avez-vous trouvé le lien vers l'ancien?

En haut à droite de l'application, un bouton est surligné en jaune, qui indique que le filtrage de module a été activé, probablement suite à la création d'un nouveau module. C'est la source de vos problèmes, vous enregistrez dans "MyModule" mais vous avez activé un filtrage global sur "Training".
