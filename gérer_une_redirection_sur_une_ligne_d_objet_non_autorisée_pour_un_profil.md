# Gérer une redirection sur une ligne d'objet non autorisée pour un profil

**URL:** https://community.simplicite.io/t/5140

## Question
Bonjour ce post fait suite à celui ci-après :

https://community.simplicite.io/t/redirection-sur-objet-externe/5139

J'ai réussi à faire une redirection sur un objet avec la logique codé côté front.

Cependant dans le cas ou l'utilisateur rentre une référence d'objet sur laquelle il n'est pas habilité (setSearchSpec en Back), le message ci après apparait :

![image|478x193](upload://upYNAYW7vaKtdAuNOti4uXKfqVB.png)

Y a t'il moyen de gérer ces cas ? Ou à minima de pouvoir personnaliser le message ?

Merci d'avance,

Benoît

## Answer
Bonjour Benoît, 

Dans la callback de la méthode search, tu devrais pouvoir gérer le cas où la recherche ne retourne rien, ou un record que l'utilisateur n'a pas la droit de voir.

Par exemple dans la Démo, si je positionne une searchSpec pour l'objet `DemoSupplier`
```java
public class DemoSupplier extends ObjectDB {
	private static final long serialVersionUID = 1L;
	
	@Override
	public void postLoad() {
		setSearchSpec("sup_code = 'LLED'");
	}
}
```

Et que je fais une recherche sur cet objet via l'API Ajax : 
```javascript
var app = $ui.getApp();
var supplier = app.getBusinessObject("DemoSupplier", "DemoSupplierSearch");
supplier.search(function(res){
	console.log(res);
}, 
{
	demoSupCode:"BIM",
});
```

Il n'y aura rien dans la variable `res` qui est le résultat du `search` passé à la méthode de callback.
