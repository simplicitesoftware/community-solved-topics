# Error: cannot find symbol

**URL:** https://community.simplicite.io/t/6728

## Question
### Request description

Bonjour, soudainement dans ma class SitesCommon il ne trouve plus aucune des mes autres classes alors qu'elles existent 


### Technical information

[details="Instance /health"]
``Status=OK
Version=5.3.8
BuiltOn=2023-07-10 20:23
Git=5.3/4502a60a63d445a5ec961e13b5f62415953c5056
Encoding=UTF-8
EndpointIP=172.17.0.4
EndpointURL=http://f0201638d3b5:8080
TimeZone=Europe/Paris
SystemDate=2023-08-01 12:12:14

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=14.7
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.6.0
DBDate=2023-08-01 12:12:14
DBDateOffset=0
DBPatchLevel=5;P03;bc4366987393580404a47f28cbc198d5
UsingBLOBs=true
```
[/details]

[details="Simplicité logs"]
```
2023-08-01 12:07:11,048|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesAssignment: checks definition and script compilation.

2023-08-01 12:07:10,986|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesAssignmentHistoric: checks definition and script compilation.

2023-08-01 12:07:10,938|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesManufacturingLines: checks definition and script compilation.

2023-08-01 12:07:10,877|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesTopologyElement: checks definition and script compilation.

2023-08-01 12:07:10,838|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesCertificates: checks definition and script compilation.

2023-08-01 12:07:10,643|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesRealEstateSite: checks definition and script compilation.

2023-08-01 12:07:10,595|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesAccessPointHistoric: checks definition and script compilation.

2023-08-01 12:07:10,502|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesAccessPoint: checks definition and script compilation.

2023-08-01 12:07:10,446|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesRealEstateAssetIdentifierValueHistoric: checks definition and script compilation.

2023-08-01 12:07:10,385|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesRealEstateAssetIdentifierValue: checks definition and script compilation.

2023-08-01 12:07:10,334|SIMPLICITE|ERROR||http://f0201638d3b5:8080||ERROR|designer|com.simplicite.util.engine.CoreCache|instantiateObject||Event: Class not found for SitesDocument: checks definition and script compilation.
```
[/details]

![image|690x388](upload://2mrHOt7qbufTGL5CyM77PMx4vG3.png)

## Answer
Bonjour

Sans plus d'éléments c'est compliqué pour nous d'investiguer le pb que vous décrivez.
Nous n'avons pas connaissance de cas de compilations qui ne fonctionnent plus sans raison.

Quelques pistes à creuser de votre coté:

- Les sources des classes induisant les erreurs sont ils toujours présents ? Vous pouvez le vérifier via l'éditeur de code ou directement sur les items de paramétrage concernés (le fichier source est visible en vue étendue)
- Peut être y a-t-il une première erreur de compilation qui induit les erreurs visibles dans votre copie d'écran et les traces logs fournies (qui ne disent rien sur leur cause) ?
- Peut être y a-t-il des traces pertinentes dans les logs en amont de votre compilation  (ex: erreur système type file system full, pb ponctuel d'accès en base, pb de mémoire, ...) ?
- Etc.
