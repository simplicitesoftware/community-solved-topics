# Edition en liste (contexte : Treeview)

**URL:** https://community.simplicite.io/t/8955

## Question
### Request description

Bonjour je souhaiterai pouvoir "editer en liste" lors de la consultation de la liste dans un treeview. 
Ici : 
![image|690x50](upload://mffI3RqBF5QefHO14KwFi5Md8X9.png)

Pourtant : 
![image|402x366](upload://mDLacg4gAGMYrW8EZMYDcaE2sE3.png)

et ca fonctionne sur la liste "généraleé et aussi sur la liste d'un panel :
![image|690x95](upload://gFtvYPkHQBhMWq6MCcgwoeyxIzX.png)


je n'arrive pas à le faire figurer sur cette liste dans le contexte treeview. 
Si j'ai bien compris, `isActionEnable` est applicable que pour les actions customs, alors j'ai tenté ça : 
 ```
@Override
	public void initList(ObjectDB parent) {
		if (isTreeviewInstance()){
			setListEditable(true);
		}
	}
```
Y-a-t-il des éléments spécifiques à configurer ou une autre méthode ou hooks à implémenter pour avoir cette action ?

## Answer
Bonjour,

Effectivement, les mises à jour de liste ne sont prévues que pour les instances :
- Main : liste principale du menu
- Panel : liste fille d'un formulaire père
- Home : liste en page d'accueil ou accueil de domaine

Il faudrait donc que la liste filtrée qui s'ouvre depuis un Treeview soit l'instance Main pour récupérer les bonnes metadata en front. Les instances Treeview sont juste dédiées à gérer ce que s'affiche dans l'arbre ou dans les API du treeview.

On va regarder pour changer ce comportement à la prochaine livraison.
