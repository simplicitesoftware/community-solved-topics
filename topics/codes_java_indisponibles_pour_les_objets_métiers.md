# Codes java indisponibles pour les objets métiers

**URL:** https://community.simplicite.io/t/4803

## Question
### Problem description

*----description of the problem----*
Bonjour,
lorsque j'essaie d'accéder au code d'un objet depuis notre instance de production, ceux-ci apparaissent vide : 
![image|603x297](upload://neAHt63k9bUlc1Chj07i5GAiZFH.png)


### Steps to reproduce

*I have reproduced the problem on an **up-to-date** Simplicité instance
and those are the steps to do it:*

1. Récupérer un objet qui possède déjà un code java
2. Ouvrir le code
RAS dans les logs

### Technical information

[details="Instance /health"]
```text
Status=OK
Version=5.1.41
BuiltOn=2022-04-21 18:53
Git=5.1/272235adb3ca4075dc9520bcbd806e5ea044184c
Encoding=UTF-8
EndpointIP=10.201.117.14
EndpointURL=http://siparex-simplicite-prod-564764f4d6-2pjw8:8080
TimeZone=Europe/Paris
SystemDate=2022-05-03 14:58:54
```
[/details]

[details="Simplicité logs"]
```text
2022-05-03 14:58:53,129|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||ICORED0001|public|com.simplicite.util.Grant|init||Info: public connected, session ID: 60C2623A6D3FBC9709E92A3C0CD2EB7D, timeout: 5 min , user agent: Zabbix
2022-05-03 14:58:25,431|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================false
2022-05-03 14:58:25,431|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:58:25,430|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:58:25,430|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:58:25,430|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:58:25,429|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:58:25,429|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:58:25,428|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================false
2022-05-03 14:58:25,428|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================false
2022-05-03 14:58:25,428|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================false
2022-05-03 14:58:25,427|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================false
2022-05-03 14:58:25,427|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:58:25,426|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||INFO|system|com.simplicite.objects.Evaluator.EvlValuation|initUpdate||Event: ====================true
2022-05-03 14:57:50,876|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||ICORED0001|public|com.simplicite.util.Grant|init||Info: public connected, session ID: 0553B4FD37CF6F1BDAAA806610031203, timeout: 5 min , user agent: Zabbix
2022-05-03 14:56:47,967|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||ICORED0001|public|com.simplicite.util.Grant|init||Info: public connected, session ID: F2C172A51143732DB41C14B3E501DEC8, timeout: 5 min , user agent: Zabbix
2022-05-03 14:55:45,325|SIMPLICITE|INFO||http://siparex-simplicite-prod-564764f4d6-2pjw8:8080||ICORED0001|public|com.simplicite.util.Grant|init||Info: public connected, session ID: 417E28F8DC4AA6803F61E531F38D6257, timeout: 5 min , user agent: Zabbix
```
[/details]

[details="Browser logs"]
```text
ICORETM009|system|com.simplicite.util.engine.ProcessScheduler|manageDeadlockActivity|System param ACTIVITY_LOCK_LIMIT = 3600s
ui-bundle.js?_=41:604 ICORETM005|system|com.simplicite.util.engine.ProcessScheduler|manageDeadlineActivity|found 0 activity(ies)
ui-bundle.js?_=41:604 ICORECM005|system|com.simplicite.util.CronJob|run|Result of job deadlineActivity : 
ui-bundle.js?_=41:604 ICORECM005|system|com.simplicite.util.CronJob|run|Result of job deadlockActivity : 
ui-bundle.js?_=41:604 ICORECM004|system|com.simplicite.util.CronJob|run|Execute job deadlineState at 2022-05-03 15:00:01
ui-bundle.js?_=41:604 INFO|system|com.simplicite.util.engine.CronManager|run|Event: Next cron job: ObjectFullGC at Tue May 03 15:03:00 CEST 2022
ui-bundle.js?_=41:604 INFO|system|com.simplicite.util.engine.CronManager|run|Event: Cron manager is sleeping for 0:02:58...
ui-bundle.js?_=41:604 ICORECM005|system|com.simplicite.util.CronJob|run|Result of job deadlineState : 
```
[/details]

[details="Other relevant information"]
Notre hébergeur nous indique qu'il est de plus en plus long de redémarrer le serveur. 
[/details]

Merci

## Answer
Vu avec Ophélie : 
Valoriser le champ à "Nom du document unique", enregistrer, supprimer la valeur et enregistrer à nouveau a solutionné le problème d'affichage du code.
