# Cron et Changement heure hiver/été

**URL:** https://community.simplicite.io/t/4568

## Question
### Request description

Bonjour,

J'ai des tâches planifiées (crontab Simplicite) qui s'exécutent quotidiennement entre 2h et 3h.

Que va-t-il se passer pour elles ce WE ?

Merci.

## Answer
Bonjour,

La cron Simplicité se base sur le composant **org.quartz** qui gère normalement le changement d'heure. Ca doit dépendre de l'expression cron (periodique, à date fixe...).
Le deamon de la cron s'endort jusqu'à la tache suivante en se servant du verbe `getFireTimeAfter` qui donne l'heure de prochain passage en fonction du TZ système.

Vous pouvez faire un test de votre expression CRON en vous positionnant juste avant le changement d'horaire pour savoir quelle heure de passage sera retournée/planifiée :

```
// A mettre dans un hook une méthode action back
Date currTime = new Date(); // ou samedi soir...
CronTrigger tr = new CronTrigger();
tr.setCronExpression("0 0 23 3,18 * ? *");
Date nextFireAt = tr.getFireTimeAfter(currTime);
AppLog.info("Reference time: " + currTime, null);
AppLog.info("Next fire after reference time: " + nextFireAt, null);
```

Sinon par sécurité décalez votre cron en dehors de la plage 2h-3h cette nuit là.
