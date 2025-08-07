# SMTP connexion : couldn't connect to host

**URL:** https://community.simplicite.io/t/4450

## Question
Bonjour,

Essayant de mettre en place un envoi automatique d'e-mail, je souhaite utiliser un serveur d'envoi SMTP.
Dans mon contexte, nous utilisons GCP comme Cloud provider donc le port 25 (mis part défaut dans Simplicité ( System parameter > MAIL_SERVICE > "mail.smtp.port" ).
GCP bloque ce port et est à priori branché sur le port 587, j'ai donc modifié ce port pour m'adapter.
Cependant, à l'envoi du mail (classiquement > méthode : mail.send(); / bibliothèque util.Mail & util.tools.MailTool) la connexion est toujours refusée

**"Couldn't connect to host, port: localhost, 587; timeout -1;"**

Sauriez-vous me guider pour résoudre ce problème ? :slight_smile: 

P.S. : Sur une instance "vierge" j'ai reussi à exécuter des envois d'e-mail avec l'utilisation du port 25 (par defaut)

## Answer
Non désolé nous ne pouvons pas vous aider sur ce sujet qui est purement au niveau infra (config de vos serveurs/services réseau, firewall, etc.)

Vous devez configurer le `MAIL_SERVICE` pour pointer sur votre serveur SMTP.  Simplicité n'embarque pas de serveur SMTP mais utilise un serveur SMTP externe.

Celui-ci doit donc être accessible depuis le serveur/container qui exécute Simplicité. Si possible testez d'abord en dehors de Simplicité depuis ce serveur/container (ex: en ligne de commande), si ça ne marche pas à ce niveau il n'y a aucune chance que ça puisse marcher dans la webapp Simplicité.

Des exemples ici: https://docs.simplicite.io/documentation/99-misc/email-howto.md, à adapter à votre cas.
