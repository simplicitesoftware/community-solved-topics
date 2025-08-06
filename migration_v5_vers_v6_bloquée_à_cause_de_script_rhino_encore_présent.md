# Migration V5 vers V6 bloquée à cause de script Rhino encore présent

**URL:** https://community.simplicite.io/t/8198

## Question
### Request description
Bonjour, 
nous sommes en train d'effectuer une migration de la version 5 vers 6. Cependant lorsque nous changeons la version, nous avons un message nous disant qu'il reste des scriptes rhinos. Nous avons supprimé les scripts JS de nos modules, mais le message persiste.
Reste-t-il une trace dans la base de données ? Avez-vous une idée d'où je peux orienter la recherche ?

```text
2024-05-14 10:39:45,275|SIMPLICITE|INFO|Database is ready
2024-05-14 10:39:45,535|SIMPLICITE|INFO|Platform version = 6, patch level = 0, patch level files MD5 hash = 25f4b5d3d1be83f90e311332b7d41816
2024-05-14 10:39:45,538|SIMPLICITE|INFO|Current database version = 5, patch level = 3, patch level files MD5 hash = d51efda09a57e3a95ffd4ec5469862b2, revision = 37
2024-05-14 10:39:45,539|SIMPLICITE|INFO|Platform needs to be updated
2024-05-14 10:39:45,698|SIMPLICITE|WARN|ZZZ ScriptUsage is deprecated, Rhino script must be refactored to Java class thru ObjectDB inheritance.
2024-05-14 10:39:45,699|SIMPLICITE|FATAL|UPGRADE FAULT
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
This version 6 does not support Rhino script anymore to implements Hooks.\n==> All legacy Rhino scripts have to be refactored to more efficient Java classes.
==> Rhino scripts are only dedicated to expressions, calculated fields and constraints.
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
2024-05-14 10:39:45,712|SIMPLICITE|ERROR|Unable to unregister the platform management bean

```

## Answer
Bonjour

Il faut regarder quels scripts partagés sont encore attachés à des objets métiers. 
Cette table doit être vide :

`select * from m_script_usage`

Il y a peut-être des dead links en base : plus aucun script rhino mais cette table N,N encore peuplée, donc à vider à la main via un `delete from m_script_usage` avant de migrer.

Par ailleurs, il faut également qu'il n'y ait plus de scripts Rhino qui implémentent les hooks des entités, donc aucun fichier `*.js` pour : Object internal | external | disposition | process | adapter
