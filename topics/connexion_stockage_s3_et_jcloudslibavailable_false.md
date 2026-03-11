# Connexion stockage S3 et jcloudsLibAvailable() false

**URL:** https://community.simplicite.io/t/11684

## Question
### Bonjour,

Nous essayons d’appliquer l’exemple du module minio mais nous obtenons une page de log d’erreur.
Cette page fini par     Caused by: java.lang.ClassNotFoundException: org.jclouds.blobstore.options.PutOptions
J’ai testé ensuite globals.jcloudsLibAvailable() et cela me renvoi nulle. S’agit-il d’une erreur d’installation ?

Cordialement,

## Answer
Vérification faite, les libs JClouds (qui sont utilisées notamment pour accéder aux buckets S3) ne sont effectivement pas disponibles dans la variante "light" de la plateforme dont vous disposez.

Nous allons intégrer ces libs à la variante "light" dans la prochaine révision car c'est effectivement désormais légitime qu'elles y soient.

En attendant nous allons soit vous mettre à disposition la variante "full" soit vous rebuilder la variante "light" avec ces libs. @olivier du coup il va falloir ré-upgrader le SIM avec un nouveau `template-6.tar.gz` (qui sera forcément plus gros que le précédent), te te préviens quand celui-ci est disponible.
