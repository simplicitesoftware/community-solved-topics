# getNextIdForColumn ne retourne pas la bonne valeur sur un datasource distant

**URL:** https://community.simplicite.io/t/4005

## Question
Bonjour,

depuis la migration de l'application en  V5, j'ai un pb pour récupérer une valeur dans une datasource distante.

L'affichage de la liste fonctionne bien : il y a 47 lignes dans la table. Dernier id utilisé = 49.
Mais quand je veux récupérer le dernier id via :
String n= getGrant().getNextIdForColumn("BLUEWAY_MYSQL_DATASOURCE_REC",getTable(), getField("dematGdaTranscocdrId").getColumn());

je récupère 7. le paramètre datasource n'a pas l'air d'être pris en compte

![image|197x37](upload://80sAZSaOIPCDqePIZyVlrt8aeyE.png)

## Answer
Ok mais c'est tout de même étrange d'utiliser ce verbe à usage "interne" qui incrémente une colonne sur une base distante non-simplicité.

- si `USE_ROWID_TABLE=yes` 
Le correctif ira incrémenter la table distante `m_rowid` sur MySQL, mais elle ne doit pas exister dans Blueway
- si `USE_ROWID_TABLE=no` 
Ca fera un un max+1 dans la table (fonctionnement hérité de la V3)
et s'applique à tous vos accès même en base locale à chaque création (row_id+1)
- Pour les autres bases Oracle ou PostgreSQL cela utilise une vraie sequence auto-comitée

Bref utiliser ce verbe pour des bases non Simplicité semble inapproprié car `getNextIdForColumn` est trop "intelligent" pour gérer tous les cas possible de base.

- il faudrait remettre `USE_ROWID_TABLE=yes` pour utiliser la table `m_rowid` en local (plus performent qu'un max+1 à chaque création)
- et changer votre code pour faire un select max+1 spécifique à votre base distante.

```java
String col = getField("dematGdaTranscocdrId").getColumn();
String n = getGrant().simpleQuery("BLUEWAY_MYSQL_DATASOURCE_REC", "select max("+col+")+1 from "+getTable());
```
