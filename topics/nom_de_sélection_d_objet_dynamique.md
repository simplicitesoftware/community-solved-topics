# Nom de sélection d'objet dynamique

**URL:** https://community.simplicite.io/t/13388

## Question
Bonjour,

Je souhaite donner à un objet sur l'écran de sélection un nom particulier.

Exemple, dans Commande, je veux au lieu d'afficher "Sélectionner une personne" au lieu de "Sélectionner Client", lorsque je clique sur la loupe du code client.

j'ai ajouté dans le code de DemoClient le hook initRefSelect

```
	@Override
public void initRefSelect(ObjectDB parent) {
    setDisplay("une personne");
}
```

Lorsque je clique sur la loupe, rien ne change :

![image|690x177](upload://xTOGYsjXg3MW78F1q0kLoU1HLiH.png)

mais lorsque je clique une seconde fois cela fonctionne :

![image|690x175](upload://1oXLglsny5ajzqwHufYM5lSAf4J.png)

Dans mon besoin métier, j'ai 2 références dans mon formulaire qui pointent vers le même objet (PsmUser qui hérite de User). Je modifie avec un setDisplay dans le initRefSelect de PsmUser le nom que je souhaite afficher en fonction du Parent et de la clé technique qui référence PsmUser.

```
	@Override
	public void initRefSelect(ObjectDB parent) {
	     setSearchSpec("t.usr_active = '1'");

	    // Vérifier si la sélection provient d'un objet parent spécifique
	    if (parent != null && "PsmProjet".equals(parent.getName()) && "prjPusrIdChefPrj".equals(getParentObjectRefField())) {
	        // Redéfinir le libellé d'affichage de l'objet pour cette instance de sélection
	        setDisplay("Chef de projet AMOE");
	    }
	    else if (parent != null && "PsmProjet".equals(parent.getName()) && "prjPusrIdChefSect".equals(getParentObjectRefField())) {
	        // Redéfinir le libellé d'affichage de l'objet pour cette instance de sélection
	        setDisplay("Chef de section");
	    }
	}
```

Si je m'amuse à sélectionner l'un puis l'autre, aucun nom n'est correctement synchronisé avec mon choix car j'ai un "clic de retard" pour l'affichage.

Autre point qui rentre sans doute dans le sujet, j'ai créé un objet N,N qui lie Mon Projet (PsmProjet) avec un utilisateur (PsmUser). via la sélection en pillbox je peux associer plusieurs utilisateurs à mon projet, mais dans ce cas la surcharge du nom de s'effectue pas, alors que je rentre bien dans mon hook (j'ai testé avec un applog sur PsmUser). 

![image|353x266](upload://aR2RXfVGN4SvDps0OcbdU1BoY92.png)

Je n'ai mis aucune condition à cette surcharge de nom, simplement le hook avec un setDisplay("Nom modifié") dans PsmUser.

Je suis en version 6.3.19

## Answer
_No answer provided._
