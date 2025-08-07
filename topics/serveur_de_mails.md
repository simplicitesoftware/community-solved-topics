# Serveur de mails

**URL:** https://community.simplicite.io/t/4114

## Question
Bonjour,
j'aimerai comprendre comment configurer correctement le serveur d'envoi par mails : 
Pour le moment nous sommes sur une instance de test gérée chez vous. Nous migrons vers notre propre hébergeur aujourd'hui.
Quand je fouille dans les param systèmes je retrouve ceci :
![image|690x269](upload://tgdaeKEwftWWpIs1oaXtr9iVpjb.png)

Il semble que les emails envoyés via les Alertes sont envoyés par le noreply@simplicite.fr. Il suffit donc que je remplace par une adresse Siparex le EMAIL_DEFAULT_SENDER ? cela me parait trop simple. 
Je souhaite modifier le MAIL_SERVICE par notre serveur de mail Mailjet. J'ai trouvé cette première partie de réponse : 
![image|690x279](upload://oddAmRknAxrjfDn7QIuyoEmTwmJ.png)

La deuxième sur le code snippet me sert lorsque j'ajoute dans le code source d'un business object les fonctions d'envoie.
Mais lorsque j'utilise les Alertes, simplicité va appeler mon paramétrage MAIL_SERVICE ? ou uniquement EMAIL_DEFAULT ? ou les deux ? 

merci pour votre réponse.:

## Answer
Bonjour,

Le MAIL_SERVICE vous permet de paramétrer les caractéristiques de votre serveur SMTP.
Pour les mails qui sont des alertes paramétrées possiblement déclenchées par un changement d’état, il y a le paramètre BPMALERT_FROM.
Le EMAIL_DEFAULT_SENDER peut vous servir pour les mails envoyés suite à des règles de gestion spécifiques si vous l'utilisez dans le from. .

Cdt,
