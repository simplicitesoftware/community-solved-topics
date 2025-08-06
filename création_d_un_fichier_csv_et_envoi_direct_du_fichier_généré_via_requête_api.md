# Création d'un fichier CSV et envoi direct du fichier généré via requête API

**URL:** https://community.simplicite.io/t/6235

## Question
### Création d'un fichier CSV et envoi direct du fichier généré via requête API

Bonjour, comme indiqué en titre de ce poste, j'ai besoin de conseils concernant la méthode à appliquer afin de créer un fichier CSV dans mon adapter puis d'envoyer directement ce fichier via un POST d'API. L'adapter qui est déjà fonctionnel permet de charger des fichiers CSV contenant des données monétaires. 
Je souhaite via cette adapter créer un second fichier CSV qui ne contiendra que les données monétaires d'un pays en particulier. Une fois ce fichier généré, je souhaite l'envoyer via une requête API.

### Solutions testées

J'ai déjà essayé de créer un fichier CSV via un ByteArrayOutputStream() ou encore via un objet File mais sans succès lors de l'envoi de ces derniers via API. Je soupçonne que la génération du fichier pour ces 2 méthodes n'est pas accomplie puisqu'en essayant de log, je tombe sur un objet java du type java@.....
Je me suis alors demandé si je pouvais utiliser une librairie du type OpenCSV et si une librairie extérieure était implémentable dans Simplicité.
Je vous remercie d'avance pour vos conseils.

AISSANI Said

## Answer
Un "adapter" sert à inserer des donées dans Simplicité, là je pense que vous parlez d'une publication ?

PS: A nouveau, vous n'indiquez pas les infos de version etc. du template de demandes de support. Ce sont des informations sont nous avons **IMPRETIVEMENT** besoin pour vous aider. **Merci de respecter le template des demandes de support**
