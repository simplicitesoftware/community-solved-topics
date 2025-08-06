# Create object List from select

**URL:** https://community.simplicite.io/t/3652

## Question
Bonjour,

* Comment créer une liste d'objet métier à partir d'un Id connus dans l'attribut

* Comment créer des instances d'objet métier avec l'aide d'un "for" ? 

Exemple : j'ai une table Commande qui contient l'id du Client. L'id du client se retrouve sur une autre table PreferenceMaterielClient. Chaque fois que je crée une commande je souhaite créer automatiquement les Produits contenus dans la table PreferenceMaterielClient dans ma Commande (object n-n Produits_Commande)

Commande javascript code (hook postCreate): 
------------------------------

```java
public String postCreate() {
		String clt_Id = getFieldValue("ClientId");
		List <String> produitList = select ProduitId from PreferenceMaterielClient where clientId :=clt_Id
                for (prdt in produitsList ) {
                            create Produit_Commande (commande = commandId , Produit = prdt);
                }
		return null;
	}
```

## Answer
```java
public String postCreate() {
	String commandId = getRowId();
	String[] produitList = getGrant().queryFirstColumn("select ProduitId from PreferenceMaterielClient where clientId="+getFieldValue("ClientId"));
	ObjectDB prdCmd = getGrant().getTmpObject("Produit_Commande");
	for (prdt_id in produitsList) {
		synchronized(prdCmd){
			prdCmd.resetValues();
			prdCmd.setFieldValue("commande_id",commandId);
			prdCmd.setFieldValue("produit_id", prdt_id);
			try{
				(new BusinessObjectTool(prdCmd)).validateAndCreate();
			} catch(Exception e){
				AppLog.error(getClass(), "postCreate", "Error creating object", e, getGrant());
			}
		}
	}
	return null;
}
```
