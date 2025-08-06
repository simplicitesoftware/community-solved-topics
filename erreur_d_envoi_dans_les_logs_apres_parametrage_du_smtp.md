# Erreur d'envoi dans les logs apres parametrage du SMTP

**URL:** https://community.simplicite.io/t/3792

## Question
Bonjour la team Simplicité !
Nous voilà confrontés à un autre probleme, nous souhaitons pour le projet proposer une solution d'envoi d’e-mail à partir d'un prestataire extérieur qui nous fourni un serveur smtp Microsoft.

Dans Parametres > Mail > nous renseignons les variables pour parametrer l'envoi depuis ce compte,
mais lorsque nous voulons generer l'envoi d'un email, nous avons cette erreur dans les logs : 
```
Votre demande de changement de mot de passe
    com.sun.mail.smtp.SMTPSendFailedException: 554 5.2.252 SendAsDenied; noreply@campus2023mail.onmicrosoft.com not allowed to send as noreply@simplicite.fr; 
```

pourtant dans les valeurs du JSON il n'y a pas noreply@simplicite.fr

## Answer
Pour rappel

https://docs.simplicite.io/documentation/99-misc/email-howto.md
