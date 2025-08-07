# Stocker de byte[] en base de données

**URL:** https://community.simplicite.io/t/4699

## Question
Simplicité 5.1.37

Bonjour,

Toujours dans les problématique de chiffrage AWS, je cherche comment stocker proprement des tableau de byte en base de données ? A l'issue du chiffrement avec aws on obitent un` byte[]` et la méthode de déchiffrement prend en entré ce même tableau de byte.

J'ai essayé en utilisant les methodes updateBlob et simpleBlob en transformant le` byte[]` en InputStream avant de persister et inversement en récupérant le record mais il semblerait que le` byte[]` que j'obtiens depuis la bdd soit différent du` byte[]` que je stocke.

J'ai essayé aussi de le stocker sous forme de chaine de charactère bien que ce ne soit pas conseillé mais je me suis heurté a des problèmes d'encodage.

## Answer
2 approches pour stocker du contenu binaire:

1) Attribut de type texte long avec encodage/décodage du `byte[]` en base 64 
2) Attribut document 

Dans votre contexte la première approche me semble à priori plus simple
