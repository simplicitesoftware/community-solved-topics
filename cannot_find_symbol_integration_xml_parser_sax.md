# Cannot find symbol Integration.XML_PARSER_SAX

**URL:** https://community.simplicite.io/t/5002

## Question
Bonsoir,

J'ai un message d'erreur après être passé en version 5.2.8 :

![image|690x100](upload://xs93xRJH6xU9t4jBhUpYtaZtsCd.png)

Je n'ai rien trouvé de spécifique dans la javadoc.

XML_PARSER_SAX n'existe plus ou il a été remplacé ?

Merci d'avance,

Benoît

## Answer
La méthode que vous utilisez est deprecated en 5.2+, les constantes utilisées par l'argument `parser` de cette méthide ont été abusivement supprimées,  elles auraient dû être laissées en deprecated aussi... les 2 constantes seront restaurées (et marquées @deprecated) dans la prochaine révision.

En attendant de refactorer votre code pour utiliser une méthode `importXML` non deprecated, vous pouvez toujours passer `null` à la place de la constante disparue car l'argument `parser` n'est de toute façon plus utilisé dans ce qu'appelle cette méthode deprecated (celle ci génèrera un warning de deprecation).
