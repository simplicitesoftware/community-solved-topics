# Configuration d'un stockage S3

**URL:** https://community.simplicite.io/t/11611

## Question
### Request description

*Dans le cadre de notre déploiement de solution, nous avons comme obligation de déposer les données versées sur notre applicatif sur un serveur S3.* Nous souhaitons obtenir un exemple d’implémentation (objet, hook, code Java, etc.)

### ***1 - Ajout et gestion de tags***

 Ajout automatique de tags lors du dépôt d’une pièce jointe, les tags sont issues de certains attributs du module dans lequel le document est déposé et d’autres tags issues d’une table de référence en fonction du type de document (date d’archivage, date suppression….).

***2-  Versement vers un stockage S3***

Le bouton de dépôt permettrait de générer les tags du document et flécher les dossiers vers une organisation dans le bucket (arborescence, nommage)

## Answer
# 1) gestion de "tags"

Dans Simplicité un document n'existe pas tout seul => Il n'existe qu'en tant qu'attribut d'un objet métier.

Donc ce que vous appelez "tag" peuvent donc simplement être d'autres attributs de l'objet métier qui porte le document : des attributs dates valorisées selon les règles de gestion souhaitées, un statut, des classifications, etc.

A la lumière de ce que vous exprimez je créerait donc un objet métier `MyDocument` avec un attribut de type document et les autres attributs qui correspondent à vos besoins.

Ce faisant vous aurez tout ce qu'il faut pour rechercher vos documents via les attributs ("tags") en question depuis la UI ou via API, comme pour tout objet métier.

# 2) stockage physique de documents sur S3

Nous vous avons mis à disposition un module d'exemple dans lequel il y a un exemple complet de stockage d'attributs de type "document" dans un bucket S3 : https://github.com/simplicitesoftware/module-minio

_NB: dans cet exemple c'est un serveur S3 Minio mais ça se généralise facilement à d'autres types de serveurs S3_

La partie intéressante c'est ce source contenant les platform hooks `readDocument/writeDocument/deleteDocument`: https://github.com/simplicitesoftware/module-minio/blob/master/src/com/simplicite/commons/Minio/PlatformHooksMinio.java 

**Attention**:

Ce n'est qu'un exemple **basique** où nous avons, par exemple, opté pour une stratégie '"à plat" de nommage des documents dans le bucket S3 en transformant les paths technique des documents en nom unique, ex: `MyObject/myField/0/194/mydoc.pdf` => `MyObject~myField~0~194~mydoc.pdf`

D'autres logiques peuvent être mises en place selon **vos besoins** et **vos choix de structuration de votre bucket** à partir des paths techniques car leur syntaxe est `<nom de l'objet métier>/<nom de l'attribut document de l'objet>/<subdivision que vous pouvez ignorer>/<row ID du record de l'objet>/<nom du fichier>`. Ce qui est impératif c'est de faire en sorte que le nom de chaque document soit strictement unique (et stable dans le temps) dans le bucket donc un nommage utilisant d'une manière ou d'une autre le triplet (nom de l'objet, nom de l'attribut, row ID) est la bonne approche dans tous les cas.

Par ailleurs, dans notre exemple nous utilisons le nom de l'objet métier pour déterminer si le document est stocké dans S3 ou si il est stocké conformément à la stratégie par défaut de la plateforme (i.e. en BLOB en base ou sur filesystem local). En l'occurrence seuls les objets dont le nom commencent par `TestMinio` voient leurs documents stockés sur le bucket S3

Voici ce que ça donne une fois déployé:

Ce record de l'objet `TestMinio`:
![image|690x421](upload://sSiYphoPgdebzcEtfb8Co1PVoZ8.png)
A son attribut document physiquement stocké dans le bucket S3 configuré:
![image|690x421](upload://a2yAp8wSTuAjcOG75MobNbOKpkO.png)
La configuration du bucket est dans l'exemple dans un param système ad hoc:
![image|690x421](upload://84RMpVH9jwLgxOIcUge7KOLnrFv.png)
Les variables d'environnement utilisées dans ce param système étant définies dans mon test de déploiement Docker dans le `docker-compose.yml`:

```yaml
services:
  minio:
    image: quay.io/minio/minio:latest
    container_name: ${COMPOSE_PROJECT_NAME}_docs
    restart: unless-stopped
    command: [ "server", "--console-address", ":9001", "/data" ]
    ports:
      - 127.0.0.1:9001:9001
    volumes:
      - docs:/data
  simplicite:
    image: registry.simplicite.io/platform:6-latest
    container_name: ${COMPOSE_PROJECT_NAME}
    restart: unless-stopped
    user: simplicite
    ports:
      - 127.0.0.1:8443:8443
    volumes:
      - db:/usr/local/tomcat/webapps/ROOT/WEB-INF/db
      - dbdoc:/usr/local/tomcat/webapps/ROOT/WEB-INF/dbdoc
    environment:
      MINIO_ACCESSKEY: "minioadmin"
      MINIO_SECRETKEY: "minioadmin"
      MINIO_ENDPOINT: "http://minio:9000"
      MINIO_BUCKET: "sandbox"
volumes:
  db:
  dbdoc:
  docs:
```

PS: Sur un serveur SIM les variables d'environnement peuvent se définir dans le fichier `.simplicite` de l'instance (syntaxe `export MYENVVAR="myvalue"`, sinon vous pouvez aussi mettre "en dur" les valeurs dans le paramètre système
