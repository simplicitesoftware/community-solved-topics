# Gestion des paramètres systèmes

**URL:** https://community.simplicite.io/t/3003

## Question
Bonjour,

Nous avons un paramètre système avec une url sur un ws. Cette url est la même pour toutes les applications (ne contiennent qu'un module) qui font appel à ce ws selon l'environnent (https://vali-ws-... ou https://test-ws-....ou https://ws-.... )

Que conseillez-vous de faire :

* un paramètre système par module
* un paramètre système dans un module qui ne contiendrait que ce paramètre
* une autre possibilité?

Merci

## Answer
Oui.
Vous pouvez aussi 
* Créer votre module VDLConfig avec l'url de test 
* L'exporter et le sauvegarder en VDLConfig_TEST 
* Modifier l'url en url de production et exporter/sauvegarder le module en VDLConfig_PROD
Importer le modules VDLConfig_TEST sur l'environnement de test, le module VDLConfig__PROD sur l'environnement de production

Puis importer le module applicatif sur vos 3 environnements dans lequel est **absent** le paramètre système VDL_WS.
