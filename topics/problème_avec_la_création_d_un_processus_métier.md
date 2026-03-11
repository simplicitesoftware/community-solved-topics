# Problème avec la création d'un processus métier

**URL:** https://community.simplicite.io/t/11116

## Question
Bonjour,

Je voudrais savoir comment obtenir plus de documentation concernant les processus métiers.

Je suis actuellement en train d’essayer de créer un processus métier similaire au processus métier de création d’un utilisateur.

![image|347x118](upload://yIuwuwLqswkUD3RyFqsKQkkyiKp.png)

Mais lorsque je clique sur le processus j’ai juste une fenêtre vide qui apparaît comme on peut le voir ci-dessous:

![image|635x321](upload://nGy4N8khKOIQh0i47mS2aTO42gm.png)

J’ai suivi la documentation disponible: https://docs.simplicite.io/make/businessprocess/business-process

Où pourrais-je trouver un tutoriel plus en détail concernant les processus métiers ?

Merci d’avance pour votre aide.

## Answer
Bonjour, 

Êtes-vous sûr qu'il ne s'agit pas d'une relation N:N entre votre l'objet commande et l'objet produit ?
Auquel cas, vous devez passer par le hook `postValidate` du processus pour implémenter votre besoin et créer l'objet qui lie un produit à une commande. S'il ne s'agit pas d'une N:N, il faudra tout de même passer ce hook, pour mettre à jour les produits sélectionnés dans le process.

Exemple : 
```java
@Override
public void postValidate(ActivityFile context) {
	String step = context.getActivity().getStep();
	if ("ORDER-CREATE".equals(step)) { // étape de sélection des produits
		// récupérer les lignes produit sélectionnées
		String[] selectedIds = getContext(getActivity("PRD-SELECT")).getDataFile("Field", "row_id" , true).getValues();
		String orderId = context.getDataValue("Field", "row_id");
		for (String prdId : selectedIds) {
			// Object N:N
			ObjectDB nn = getGrant().getTmpObject("OrderPrd");
			try {
				nn.getTool().getForCreate();
    			nn.setFieldValue("orderId", orderId);
    			nn.setFieldValue("productId", prdId);
    			nn.getTool().validateAndCreate();
			} catch (GetException | ValidateException | SaveException e) {
				AppLog.error(e, getGrant());
			}
		}
	}
}
```
