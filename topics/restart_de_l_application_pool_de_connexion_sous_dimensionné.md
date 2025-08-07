# Restart de l'application/Pool de connexion sous dimensionné

**URL:** https://community.simplicite.io/t/5501

## Question
### Request description

*----description of the request----*
Bonjour,
tous les matins depuis un certain temps, nous constatons un restart du tomcat. Et c'est assez correlé avec une saturation du pool de connexion. Et cela va de pair avec de forts ralentissements.
![dyna_api_connection_pool_2022-11-17|690x178](upload://7tf5lC3uev0Rkahqq7PtivzdClC.png)

Ce qu'on voit dans Dynatrace c'est qu'il semble paramétré à 10

En l'absence de notre tech lead Simplicite, nous aimerions savoir s'il y a un paramétrage pour ça dans Simplicite et où il se trouve.

La requête: SELECT * FROM pg_settings WHERE name = 'max_connections';
donne 400

J'ai regardé la doc tomcat:
![tomcat_active_sessions|690x144](upload://IuYXcdQ8J7e79w0acQPmyiSlCP.png)


Merci par avance de votre assistance.



### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

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
[downloaded-logs-20221117-090852.csv|attachment](upload://oCfhWC6Nx990r78FHiczvjCh7n5.csv) (328.8 KB)

[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonjour,

La configuration du pool de connexion JDBC se fait dans le META-INF/context.xml de la web-app en fonction de votre version de tomcat. Je suppose que par défaut le max est à 10.

Par exemple :

```xml
<Resource
  name="jdbc/simplicite"
  type="javax.sql.DataSource"
  maxTotal="20" maxIdle="10"
  ...
>
```


https://tomcat.apache.org/tomcat-9.0-doc/jndi-datasource-examples-howto.html
https://docs.simplicite.io/documentation/99-misc/root-deploy.md
