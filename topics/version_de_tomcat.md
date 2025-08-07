# Version de tomcat

**URL:** https://community.simplicite.io/t/10142

## Question
Bonjour,

Quelle est la version de tomcat la plus récente qui est compatible avec Simplicité 6.2 et les futures 6.x ?

Dans la doc, ca parle de webapp 4.0 donc Tomcat 9 seulement : https://docs.simplicite.io/docs/compatibility/#application-servers

Merci

## Answer
Simplicité embarque un certain nombre de librairies tierces dont certaines qui n'étaient pas encore compatibles avec JakartaEE en date de la release initiale de la v6, donc Tomcat 10 et 11 ne peuvent pas être utilisées => la v6 de Simplicité est donc destinée à tourner sur Tomcat 9

Le passage à Tomcat 11 est prévu pour la v7 (prévue à horizon de fin 2025 / début 2026), ce changement de socle technique avec ses impacts potentiels sur le code applicatif ne peut se faire que dans le cadre d'une version majeure.
