# Ecriture des logs

**URL:** https://community.simplicite.io/t/7021

## Question
### Request description

j'ai plein d'applog.info() dans le code que je ne souhaite pas voir dans le fichier simplicite.log
(j'ai un problème que je n'arrive pas à identifier, qui fait des tonnes de logs et fait planter le serveur à cause du fichier simplicite.log trop lourd.)
je ne trouve pas dans les paramètres system, celui qui me permet de gérer ça.

## Answer
Idealement il faudrair refactorer ces `AppLog.info(...)` en `AppLog.log("<log event>", ...)` afin de pouvoir activer/désactiver ce log event uniquement quand vous en avez besoin.
