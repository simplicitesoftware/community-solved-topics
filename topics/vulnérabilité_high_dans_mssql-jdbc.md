# Vulnérabilité high dans mssql-jdbc

**URL:** https://community.simplicite.io/t/11534

## Question
### Request description

Bonjour,

Grype nous remonte une vulnérabilité high dans la lib mssql-jdbc présente dans Simplicité 6.3.2.
Celle-ci était déjà présente dans la version 6.2, en 6.3 toutes les libs avec une vulnérabilité high ont été mis à jour sauf celle-ci. Est-ce qu'il y a une raison particulière ?

```
[2026-02-05T09:23:08.059Z] NAME             INSTALLED  FIXED-IN      TYPE          VULNERABILITY        SEVERITY 
[2026-02-05T09:23:08.060Z] mssql-jdbc       13.2.1     13.2.1.jre11  java-archive  GHSA-m494-w24q-6f7w  High  
```

## Answer
Bonjour

Ca semble être un faux positif car nous embarquons bien la bonne version du driver JDBC:
![image|690x141](upload://j1m6iA5PFo69MAc0v30hALP1BKn.png)
![image|645x178](upload://88Z6BFEB3LHGqc2g20bGGHWkX6g.png)
Et c'est bien ce JAR qu'on retrouve dans les images 6.2 et 6.3:
![image|690x162](upload://taDlHOX4MfMbYnAfabDFFii6Tu9.png)

PS: Si vous n'utilisez pas de base SQLServer vous pouvez supprimer ce driver de l'image Docker
