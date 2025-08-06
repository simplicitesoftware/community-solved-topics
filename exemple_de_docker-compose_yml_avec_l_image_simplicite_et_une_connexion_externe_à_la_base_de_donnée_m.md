# Exemple de docker-compose.yml avec l'image simplicite et une connexion externe à la base de donnée MariaBD

**URL:** https://community.simplicite.io/t/2976

## Question
Bonjour,

Est-il possible de mettre à disposition un exemple de Docker-Compose avec une connexion externe à MariaDb comme vous l'avez fait dans vos exemples ci-dessous ?

## [docker](https://github.com/simplicitesoftware/docker)/[examples](https://github.com/simplicitesoftware/docker/tree/master/examples)/[docker-compose](https://github.com/simplicitesoftware/docker/tree/master/examples/docker-compose)/**docker-compose-mariadb.yml** 

Je vous remercie par avance.

Laurent.

## Answer
Il suffit de partir de cet exemple et de retirer ce qui concerne le container MariaDB, genre:

```yaml
version: "3"
services:
  simplicite:
    image: simplicite/platform:<tag, e.g. 5-latest>
    restart: always
    container_name: myapp
    environment:
      DB_SETUP: "true"
      DB_VENDOR: "mysql"
      DB_HOST: "<your database server hostname or IP address>"
      DB_PORT: "<your database server port>"
      DB_USER: "<your database username>"
      DB_PASSWORD: "<your database password>"
      DB_NAME: "<your database name>"
      DB_WAIT: 100
    ports:
     - 127.0.0.1:8080:8080
     - 127.0.0.1:8443:8443
    volumes:
    - myapp-git:/usr/local/tomcat/webapps/ROOT/WEB-INF/git
volumes:
  myapp-git:
```

Bien entendu il faut vous assurer que la base en question est bien atteignable au sens réseau depuis l'intérieur du container, c'est de la pure "tuyauterie" classique Docker, rien de specifique à Simplicité ici (le piège classique c'est si vous mettez "localhost" en hostname => depuis l'intérieur du container "localhost" c'est le container lui même, pas la machine hôte)
