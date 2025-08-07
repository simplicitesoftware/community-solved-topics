# Régression sur les adpateurs implémentant CSVLineBasedAdapter.processValues

**URL:** https://community.simplicite.io/t/6857

## Question
### Request description

Nous avons remarqué une regression sur les adapteurs CSV utilisant la méthode :

CSVLineBasedAdapter.processValues​(long lineNumber, java.lang.String[] values)

![image|690x39](upload://gcEX6RGjoEyrL3MQDAG4VMp7VWW.png)

Le tableau Values semble null, alors que nous ne reproduisons pas le problème sur une version 5.3.11.

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1. Lancer un adapteur implémentant CSVLineBasedAdapter ainsi que la méthode processValues.
2. Intégré une ligne java utilisant Values dans la méthode processValues.
3. Erreur visible dans les logs.

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.13
BuiltOn=2023-09-08 13:14
Git=5.3/fca5758c61ade32f90b9f1401ebe18ec1b6d3e71
Encoding=UTF-8
EndpointIP=xxx
EndpointURL=xxx
TimeZone=Europe/Paris
SystemDate=2023-09-10 14:37:51
```
[/details]

## Answer
Ok donc on va remettre le dernier ";" comme avant si la regex fonctionne de cette manière.

Ce sera relivré en 5.3.14 dans la semaine.
