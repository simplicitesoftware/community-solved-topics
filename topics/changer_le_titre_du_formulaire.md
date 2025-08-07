# Changer le titre du formulaire

**URL:** https://community.simplicite.io/t/3528

## Question
Bonjour,
J'ai vu dans un post qu'il était possible de modifier le titre du formulaire avec `getUserKeyLabel`. Je n'ai pas trouvé d'exemple en JAVA dans la doc. Pouvez-vous m'en donner un?

Merci
Fabrice

## Answer
Bonjour, 

Vous pouvez surcharger le titre du formulaire en utilisant l'attribut "Titre complémentaire" d'un objet métier :

![Image_08_07_2021_09_24_collée|690x302](upload://6G8eC4vbLsrAIt8fQoaPxOvQOB9.png)

Vous pouvez également utiliser la méthode `getUserKeyLabel` comme suit :
```
/** Hook override: custom short label */
	@Override
	public String getUserKeyLabel(String[] row) {
		return getFieldValue("myField", row);
	}
```
