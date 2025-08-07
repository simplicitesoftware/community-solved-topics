# Service Mail Name

**URL:** https://community.simplicite.io/t/8302

## Question
Bonjour, ils nous ai demandé d'afficher sur une api nos différents services.
Tel que le service mindefconnect(authentification), BDD, servicemail, espace de stockage.
Pour les deux premiers on a répliqué le code d'une autre appli en l'adaptant.
utilisation de Java.net avec la classe httpURLConnection pour le service d'authentification.
Javax.sql avec la Datasource pour le sgbd.
Pour le service mail on voulais utilisé jakarta mail, mais on ne connais pas le nom du service on a testé :"java:/comp/env/mail/simplicite" comme la valeur était définit à un endroit du template mais le nom de ce service n'est pas connu, le service mail est définit seulement dans le MAIL_SERVICE et non dans le serveur context.xml du serveur Tomcat.
Actuellement en 5.3.37.

## Answer
Finalement on a laissé la définition du service mail dans le MAIL_SERVICE et on a instancié un service mail avec les paramètres du MAIL_SERVICE afin de pouvoir le pinger.
