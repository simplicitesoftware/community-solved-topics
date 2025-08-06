# Roulement des logs catalina

**URL:** https://community.simplicite.io/t/4936

## Question
Simplicité 5.1.44

Bonjour,

en fouillant un peu dans l'image, et notamment dans les conf de **tomcat** (pas le log4j), le roulement des logs catalina est par défaut valorisé à 28. Sachant que nos logs partent tous dans cloudwatch, on souhaite passer ce paramètre à 1 jour pour éviter de stocker des fichier sur le container inutilement. Est-ce que vous y voyez une contre-indication ?

Merci d'avance.

## Answer
Non pas de contrainte, vous pouvez faire ce que vous voulez au niveau des logs Tomcat.

NB: Au niveau des logs Simplicité (Log4J) vous pouvez aussi faire ce que vous voulez mais le composant legacy "System logs" risque d'être impacté car il lit les dernières lignes du fichier `simplicite.log` (les remontées de logs via websocket ne sont, en revanche, pas impactées par la config Log4J)
