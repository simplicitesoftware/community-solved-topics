# Field type image

**URL:** https://community.simplicite.io/t/8662

## Question
### Request description

Bonjour,

Nous aimerions ajouter un champ de type image dans le formulaire et avons quelques questions à ce sujet :
- Quelle est la taille maximale d'une image que l'on peut joindre en pièce jointe ?
- Quels sont les impacts sur la base de données ?
- Y a-t-il d'autres directives à suivre pour ce type de champ ?

Merci d'avance pour votre retour.

## Answer
Bonjour

Les images sont des documents donc :

- la limite d'upload est celle définie globalement par le paramètre système `MAX_UPLOAD_SIZE` (100Mb par défaut). NB: cette limite peut ne pas être atteinte si d'autres limites sont définies en amont (i.e. niveau Tomcat et/ou niveau de vos reverse proxies)
- Le contenu est stocké soit en base sous forme de BLOB soit en file system en fonction de la configuration du paramètre système `DOC_DIR`.
  - Si vous stockez en BLOB en base il faut donc prévoir une taille de stockage appropriée pour la base
  - Si vous stockez en file system il faut prévoir une taille de stockage appropriée pour ce file system + garantir la persistence de ce file system (ex: un montage de volume persistant en Docker) + avoir un mécanisme de sauvegarde garantissant l'intégrité de la base **et** de ce file system (i.e. sauvegarder les deux de manière synchrone)

Bref, de manière générale avec les données de type fichiers (images et/ou autres) il faut donc bien estimer l'espace de stockage et de sauvegarde requis pour ne pas risquer des incidents pour cause d'espace de stockage saturé.

C'est aussi vrai pour les autres données en base mais les documents induisent rapidement beaucoup plus de volume.

Veillez aussi à prévoir le vidage régulier de la corbeille des documents si vous la rendez persistante.
