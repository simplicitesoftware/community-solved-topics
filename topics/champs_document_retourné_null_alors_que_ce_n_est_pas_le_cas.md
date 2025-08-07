# Champs document retourné null alors que ce n'est pas le cas

**URL:** https://community.simplicite.io/t/4692

## Question
### Request description

Bonjour,

J'ai un champ document appelé `hrEmpMutuellejustification`.
![image|690x270](upload://bDxq0u0XaIZSnVTzKRp975zzHLo.png)

Dans mon formulaire, j'ai bien enregistré un PDF comme on peut le voir ci-dessous :
![image|309x94](upload://jDWfnMA0qVJyqqKJArHmHQSYGFP.png)

Dans la méthode `postSave()`, j'affiche le document, mais il est `null` alors que ça ne devrait pas être le cas.
```
public String postSave(){
	if(getOldStatus().equals("DATA_SHEET_SENT") && getStatus().equals("DATA_SHEET_COMPLETED") && !getFieldValue("hrEmpMutuellejustification").equals("") && getFieldValue("hrEmpMutuellejustification") != null){
		AppLog.info("============ document mutuelle : " + getField("hrEmpMutuellejustification").getDocument(), getGrant());
		this.notifyMutuel();
	}
	
	return null;
}
```
Voici le résultat :
![image|690x18](upload://xKsCjKivKG3RoxtrHEj1IjoyUJo.png)

**Une idée du problème ?**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.37
BuiltOn=2022-04-05 11:19
Git=release/0d9c19594e35d74bd1dead5960d3b31b37337814
Encoding=UTF-8
EndpointIP=10.201.117.1
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-11 12:14:25
```
[/details]

[details="Simplicité logs"]
```text
2022-04-11 12:12:16,731|SIMPLICITE|INFO||http://siparex-simplicite-dev-745fcf686c-ptkfp:8080||INFO|designer|com.simplicite.objects.HumanRessource.HrNewEmployee|postSave||Evénement: ============ document mutuelle : null
```
[/details]

## Answer
Bonjour, **j'ai une idée** ;) 

Utilisez plutôt la méthode : `public DocumentDB getDocument​(Grant g)`
Qui "Load and get the document's extended data"
