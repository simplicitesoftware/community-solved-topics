# Fichier simplicite.log absent (Error: Missing file path)

**URL:** https://community.simplicite.io/t/3088

## Question
Bonjour,

Je n'arrive pas à visualiser la log dans la nouvelle instance en 5.1 : 

![2021-04-02 10_48_47-System log|501x133](upload://9kWjMxlkeJEaQaolLbcP07q5syH.png) 

En plus, le répertoire tomcat/webapps/ROOT/WEB-INF/log est vide sur le serveur

Aurais-je oublié un paramètre ?

![simpli|690x87](upload://vkgEoEQtgGen867SNfp27SC5UOx.png) 

Merci d'avance
Abed.

## Answer
OK c'est ça le pb, il n'était pas/plus dans le template 5.1, il y a été remis.
Faites un `sim refresh` pour mettre à jour le template.
