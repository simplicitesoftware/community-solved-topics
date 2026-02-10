# Objet service contenant un champ d'objet associé à un modèle d'état -> erreur relation service does not exists / searchGroupBy

**URL:** https://community.simplicite.io/t/11558

## Question
### Request description

*Erreur dans la log système suite à l’affichage de la liste d’un objet service (basé sur une API REST). Cet objet contient notamment un champ associé à un modèle d’état. Dans la configuration, pas de groupBy, pas de menu bannette, pas d’état visible dans le menu, pas de tableau de bord.*

![image|690x207](upload://AgrnjCn24nlazHbkTJzACFSr6H4.png)

J’ai l’impression que l’objet service ne tient pas compte de cette configuration car les états sont visibles dans le menu et l’erreur suivante est générée dans la log système :

![image|690x281](upload://19MaaVTE7ohC8qBPoMkZSpmzPyS.png)

```
2026-02-09 11:00:38,929|SIMPLICITE|ERROR||http://bca-71077-cron-86ddd46c5d-bmnhg:8080||ECOREDB001|system|com.simplicite.util.engine.ObjectManager|query||Error SQL query: jdbc/simplicite: select * from (select null as c0, null as c1, null as c2, t.legal_text_statut as c3, null as c4, null as c5, null as c6, null as c7, null as c8, null as c9, null as c10, null as c11, count(*) as count from service t group by t.legal_text_statut) t0 order by t0.c3 asc
    org.postgresql.util.PSQLException: ERROR: relation "service" does not exist
     Position: 207
     at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2734)
     at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2421)
     at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:372)
     at org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:518)
     at org.postgresql.jdbc.PgStatement.execute(PgStatement.java:435)
     at org.postgresql.jdbc.PgPreparedStatement.executeWithFlags(PgPreparedStatement.java:196)
     at org.postgresql.jdbc.PgPreparedStatement.executeQuery(PgPreparedStatement.java:139)
     at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:123)
     at org.apache.tomcat.dbcp.dbcp2.DelegatingPreparedStatement.executeQuery(DelegatingPreparedStatement.java:123)
     at com.simplicite.util.engine.DBAccess.query(DBAccess.java:683)
     at com.simplicite.util.engine.DBAccess.query(DBAccess.java:520)
     at com.simplicite.util.engine.ObjectManager.searchGroupBy(ObjectManager.java:762)
     at com.simplicite.util.engine.ObjectDirect.searchGroupBy(ObjectDirect.java:339)
     at com.simplicite.util.ObjectDB.searchGroupBy(ObjectDB.java:1051)
     at com.simplicite.util.tools.JSONTool.list(JSONTool.java:3429)
     at com.simplicite.webapp.tools.JSONServletTool.search(JSONServletTool.java:787)
     at com.simplicite.webapp.ObjectJson.search(ObjectJson.java:410)
     at com.simplicite.webapp.tools.JSONServletTool.businessObjectService(JSONServletTool.java:567)
     at com.simplicite.webapp.servlets.AbstractJSONServlet.process(AbstractJSONServlet.java:155)
     at com.simplicite.webapp.servlets.AbstractJSONServlet.service(AbstractJSONServlet.java:129)
     at javax.servlet.http.HttpServlet.service(HttpServlet.java:623)
     at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:199)
     at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:144)

```

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```

[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```

[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```

[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*

[/details]

## Answer
Il n'y a pas d'attribut paramétrable pour dire d'avoir ou non un sous menu des états pour un objet ayant un diagramme d'états :
- l'attribut booléen _Menu banettes_ ne joue que sur la présence ou pas de la bannette dans le sous menu
- l'attribut enum multiuple _Vue des états du menu_/_List de tableaux de bord_ ne joue que sur les capacités de dashboarding associées à l'objet avec diagramme d'état, notamment  la présence du dashdoard du sous menu (cf. l'aide de l'attribut)

Il faut donc le dire via code au niveau du `postLoad`, ex:

```java
@Override
public void postLoad() {
    setMenuStates(false);
}
```
@Francois que penses tu d'ajouter la possibilité d'inhiber le sous menu des états au niveau du paramétrage de l'objet ? (à moins que ça ne soit déjà possible autrement...)

En tout cas, dans le cas d'un objet service, utiliser `setMenuStates(false)` fait bien disparaitre les erreurs SQL indiquées.

On va tout de même essayer de rendre les choses plus malignes pour éviter de générer des requêtes SQL inappropriées
