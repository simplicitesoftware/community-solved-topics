# Copier l'intégralité d'un objet métier via le code (sans copier les champs 1 par 1)

**URL:** https://community.simplicite.io/t/4730

## Question
### Request description

Bonjour,

J'ai un objet métier. Lorsque je sauvegarde cet objet métier, je veux copier l'intégralité de l'objet dans un autre.

**Exemple :** L'objet métier Evaluation. Lorsque je sauvegarde une Evaluation, je veux copier cette Evaluation dans d'autre Evaluation (selon la date de campagne).

J'ai essayé avec : `evlInstance = this`. **Mais ça ne fonctionne pas**.

Voici le code complet (sachant que j'arrive bien jusqu'à la ligne `evlInstance = this`) :
```
String idPart = getGrant().simpleQuery("SELECT m.row_id FROM evl_participation m INNER JOIN evl_investment i ON i.evl_prt_id = m.row_id INNER JOIN evl_valuation v ON v.evl_val_inv_id = i.row_id WHERE v.row_id = " + this.getRowId());
		
String dateCnp = getGrant().simpleQuery("SELECT c.evl_cpn_date FROM evl_campain c INNER JOIN evl_valuation v ON v.evl_val_cpn_id = c.row_id WHERE v.row_id = " + this.getRowId());
	
ObjectDB cmpInstance = getGrant().getTmpObject("EvlCampain");
	
synchronized(cmpInstance){
	
	cmpInstance.resetFilters();
	cmpInstance.setFieldFilter("evlCpnDate", dateCnp);
	
	java.util.List<String[]> camps = cmpInstance.search();
	AppLog.info("==================== campsSize : " + camps.size(), Grant.getSystemAdmin());
	for(String[] camp : camps){
		
		cmpInstance.setValues(camp);
		AppLog.info("==================== cmpInstance : " + cmpInstance.getFieldValue("evlCpnName"), Grant.getSystemAdmin());
		ObjectDB evlInstance = getGrant().getTmpObject("EvlValuation");
		
		evlInstance.resetFilters();
		evlInstance.setFieldFilter("evlValCpnId", cmpInstance.getRowId());
		
		java.util.List<String[]> evals = evlInstance.search();
		AppLog.info("==================== evalsSize : " + evals.size(), Grant.getSystemAdmin());
		for(String[] eval : evals){
		
			evlInstance.setValues(eval);
			
			String newIdPart = getGrant().simpleQuery("SELECT m.row_id FROM evl_participation m INNER JOIN evl_investment i ON i.evl_prt_id = m.row_id INNER JOIN evl_valuation v ON v.evl_val_inv_id = i.row_id WHERE v.row_id = " + evlInstance.getRowId());
			
			AppLog.info("==================== newIdPart : " + newIdPart, Grant.getSystemAdmin());
			AppLog.info("==================== idPart : " + idPart, Grant.getSystemAdmin());
			if(newIdPart.equals(idPart)){
				AppLog.info("==================== OK", Grant.getSystemAdmin());
				evlInstance = this;
				evlInstance.save();
			}
		}
	}
}
```

Je n'ai pas envie de copier les champs 1 par 1.

**Avez-vous une solution ?**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.39
BuiltOn=2022-04-13 18:24
Git=release/e929cbae23c2441b4cb0a66b9501de0159ee7c92
Encoding=UTF-8
EndpointIP=10.201.117.43
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-19 09:30:28
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
[quote="Elcoco, post:4, topic:4730"]
`evlInstance.setValues(eval);`
[/quote]
A priori, ça vous n'en avez pas besoin, parce que vous les écrasez avec `evlInstance.setFieldValue(name, val);` 

J'ai lu vite et donc je n'avais pas vu qu'on était dans le cadre d'une mise à jour d'un record existant. 
Dans ce cas, à votre place je chercherai l'id du record à mettre à jour et après un `.select(id)` j'appellerai la boucle qui set la valeur des champs.

```
public void copyRecord(){
	ObjectDB obj = getGrant().getTmpObject("MyObject");
	if(obj.select(targetRowId)){// targetRowId is the row id of the record you want to override
		for(ObjectField f : getFields()){
			if(!f.isTechnicalField()){
				String val = f.getValue();
				String name = f.getName();
				obj.setFieldValue(name, val);
			}
		}
		obj.save();
	}
}
```

Essayez avec ça et en rajoutant le `if(!f.isTechnicalField())` pour ne pas copier les timestamp et row_id
