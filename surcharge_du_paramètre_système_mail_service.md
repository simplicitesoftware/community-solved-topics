# Surcharge du paramètre système MAIL_SERVICE

**URL:** https://community.simplicite.io/t/9794

## Question
Bonjour,

Notre équipe Sécurité nous a demandé de ne plus stocker de secrets dans la configuration système, afin qu’ils ne soient pas visibles dans l’interface graphique.

Dans ce contexte, nous souhaitons extraire l’attribut "password" du paramètre système `MAIL_SERVICE` et l’injecter d’une manière différente, de sorte que le mot de passe ne soit plus exposé dans l’outil.

Nous avons envisagé d’injecter la configuration SMTP directement dans le fichier `META-INF/context.xml`. Cependant, d’après votre documentation, cette méthode ne semble pas compatible avec la version 5.3 :

> **WARNING** As of version 5.x this context-level is **not possible anymore** as the `javax.mail.*` package has been replaced by the new `jakarta.mail.*` which is not compatible with this legacy approach.
[https://docs.simplicite.io/docs/misc/email-howto/#legacy-tomcat-context-level-configuration](https://docs.simplicite.io/docs/misc/email-howto/#legacy-tomcat-context-level-configuration)

Est-il possible de créer des instances des objets `Mail` ou `MailTool` avec une configuration alternative à celle définie dans les paramètres système par défaut ?
À défaut, quelles sont les bonnes pratiques recommandées par l’éditeur Simplicité pour gérer ce type de besoin ?

Merci d’avance pour votre aide.

Cordialement

## Answer
Bonjour, 

Dans la dernière version de la 5.3.67 (qui sera releasée aujourd'hui), il est possible de passer la valeur en variable d'environnement : https://docs.simplicite.io/versions/release-notes/v5-3/#version-5.3.67

Cf : https://docs.simplicite.io/docs/operation/docker#mail-service pour la syntaxe
