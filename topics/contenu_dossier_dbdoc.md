# Contenu dossier dbdoc

**URL:** https://community.simplicite.io/t/10476

## Question
Bonjour,

Lors de la migration d’une version à l’autre du moteur Simplicité, nous nous sommes rendu compte que des fichiers sont stockés sur notre serveur dans le dossier du template (dans le dossier dbdoc).

Concrètement, notre dossier template-5-3-41 faisait plusieurs centaines de gigaoctets, et quand nous sommes passés en 5.3.71, ce même dossier dbdoc a recommencé a augmenter en taille (à la vitesse en les utilisateurs envoient leurs fichiers dans notre application.

Etant donné que lors d’un changement de version du moteur Simplicité, nous changeons complètement nos liens, plus aucun accès à ces fichiers n’est possibles, et pourtant aucune anomalies est rencontrée dans l’application. 

Les fichiers sont de ce style là : 

![image|644x108](upload://qrkAYXfUb9e13qCSFu95hUHWEPt.png)

Est-ce que vous auriez une idée de pourquoi ces fichiers restent à cet emplacement?

Merci

## Answer
Merci pour ces précisions.

Si `DOC_DIR=BLOB` alors c'est bien la base qui stocke les fichiers.
Le contenu du `DOC_LOCAL_DIR` sert 
- de fallback si pas trouvé en base, on prend celui sur le disque en le remettant en base au passage
- et à serialiser un fichier si on y accède autrement que par un InputStream, via des appels API du genre `obj.getField("myFieldDoc").getDocument(getGrant()).getFile()`

Dan ce cas, Simplicité doit écrire le fichier dans `DOC_LOCAL_DIR` pour retourner sa version `java.util.File` avec un path physique.

Il faut identifier dans le code applicatif ce genre d'accès, pour n'utiliser que des DocumentDB.getInputStream, ou des copies physiques dans un répertoire temporaire supprimé en fin de traitement.

Vous pouvez voir un exemple de fabrication de ZIP à partir de documents mis dans /temp, sans laisser de trace physique une fois terminé:

[cf doc](https://docs.simplicite.io/docs/core/basic-code-examples/#write-zip-file)
