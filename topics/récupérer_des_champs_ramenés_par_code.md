# Récupérer des champs ramenés par code

**URL:** https://community.simplicite.io/t/4836

## Question
### Request description

Bonjour,

J'ai l'objet métier ci-dessous :
![image|410x348](upload://rIwxfdZH7UbvPOP2VbOGYMhRGcy.png)

Dans le code, je crée un nouvel objet `DdvFndPart` et je set les 2 ID `ddvFndpartPartId` et `ddvFndpartFndId`. Le reste ne sont que des champs ramenés.

Le problème, c'est que ces champs, ne sont pas ramenés dans 95% des cas même avec le `populate(true)`. Il y a que quelques exception ou ils sont ramenés (étrange).

Voici ce que j'obtiens :
![image|690x91](upload://6CCTXra5SLlSivjYyzoP3ETQuMb.png)
Voici ce que je devrais obtenir :
![image|690x91](upload://uJgNPWOGXtCHIGPxWJgRwCElwFc.png)

Le **nom** et l'**ID** du fond sont correcte, donc je ne comprends pas pourquoi le nom de l'équipe et de la SGP ne sont pas ramenés.

Voici le code :
```
ObjectDB inv = g.getTmpObject("DdvFndPart");
BusinessObjectTool invOt = inv.getTool();
	
String fundId = getGrant().simpleQuery("SELECT row_id FROM ddv_fund WHERE ddv_fund_key = '" + rs.getString(1) + "'");
	
if(!fundId.equals("") && fundId != null){
	
	invOt.getForCreateOrUpdate(new JSONObject().put("ddvFndpartFndId", fundId).put("ddvFndpartPartId", o.getRowId()));
	
	inv.setFieldValue("ddvFndpartPartId", o.getRowId());
	inv.setFieldValue("ddvFndpartFndId", Integer.parseInt(fundId));
	
	inv.populate(true);
	
	invOt.validateAndSave();
}
```

Quelle peut être l'origine du problème selon vous ?

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.2
BuiltOn=2022-04-29 15:38
Git=5.2/a2c69b2ee78658770a248e617730e607252990ca
Encoding=UTF-8
EndpointIP=10.201.58.66
EndpointURL=http://siparex-simplicite-dev-777bcd4cfc-dqxdr:8080
TimeZone=Europe/Paris
SystemDate=2022-05-10 10:02:31
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
[quote="Elcoco, post:4, topic:4836"]
```java
String fundId = getGrant().simpleQuery("SELECT row_id FROM ddv_fund WHERE ddv_fund_key = '" + rs.getString(1) + "'");
```
[/quote]

Vous récupérez le row_id du Fond en faisant une recherche sur `ddv_fund_key`, cette requête va retourner la première ligne qu'il trouve, en l'occurence, le record auquel vous n'avez plus accès. 

Oui vous pouvez faire un  `DELETE FROM ddv_fund`
