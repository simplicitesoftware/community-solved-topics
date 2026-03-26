# Problème de mise à jour de BLOB lors du stockage de documents sur S3

**URL:** https://community.simplicite.io/t/11832

## Question
### Bonjour à tous,

Nous rencontrons un comportement étrange lors de la mise en place du stockage de documents sur une base de données S3. Voici une description détaillée du problème :

### Contexte :

* Nous avons configuré l'accès au S3 en nous basant sur le code d'exemple du module Minio.

* Le fichier est bien déposé sur le S3.

* Dans l'interface de paramétrage de l'objet métier, nous voyons bien le document ajouté dans l'onglet "Documents".

* Nous pouvons également télécharger le document sans problème à partir de cette liste, et les logs montrent un appel correct au S3.

### Problème :

Lors de l'upload d'un document, l'IHM renvoie une erreur :

```
blob update failed

```

Les logs système affichent les erreurs suivantes :

```
2026-03-20 11:16:58,486|SIMPLICITE|ERROR||http://XXX/oliv|/oliv|ECOREDB001|system|com.simplicite.util.engine.GrantDirect|updateBlob||Error SQL query: update m_document set dbd_content=? where dbd_path = 'NomvDocuments3/nomvDocFichier/0/19/Bannière 2.png'
    org.postgresql.util.PSQLException: An I/O error occurred while sending to the backend.

2026-03-20 11:16:58,487|SIMPLICITE|ERROR||http://XXX/oliv|/oliv|ERROR|system|com.simplicite.util.tools.DocTool|writeFile||Event: Write error: NomvDocuments3/nomvDocFichier/0/19/Bannière 2.png
    java.io.IOException: BLOB update failed (-1)

2026-03-20 11:16:58,487|SIMPLICITE|ERROR||http://XXX/oliv|/oliv|ECORED0001|a.zoopy|com.simplicite.util.tools.DocTool|upload||Erreur Upload error
    java.io.IOException: BLOB update failed (-1)

```

### Observations supplémentaires :

* La table globale des documents Simplicité est bien mise à jour.

* La suppression d'un document dans la liste envoie bien un appel de suppression au S3.

* Si nous supprimons manuellement un document dans le S3, le téléchargement depuis Simplicité renvoie un fichier vide (0 octet), car Simplicité ne détecte pas la suppression.

### Hypothèse :

Il semble que seul le lien entre l'objet métier et le document déposé pose problème lors de la mise à jour. Tout le reste fonctionne correctement.

### Questions :

* Avez-vous déjà rencontré ce type de problème ?

* Y a-t-il des configurations spécifiques à vérifier pour le stockage des documents sur S3 ?

* Des suggestions pour résoudre ce problème de mise à jour de BLOB ?

Merci d'avance pour votre aide !

## Answer
OK nous avons détecté une anomalie lorsqu'il y a plusieurs platform hooks (d'où ma question sur ce point), on va corriger ça dans la prochaine révision 6.3.7

En attendant vous pouvez soit fusionner temporairement ces 2 classes en une seule, soit (je n'ai pas testé mais ça doit marcher) implementer temporairement les 2 hooks `writeDocument/deleteDocument` avec un simple`return true` dans la classe du platform hook qui ne les contient pas.
