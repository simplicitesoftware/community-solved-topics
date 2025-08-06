# Customisation du menu principal + l'ordre des colonnes des listes

**URL:** https://community.simplicite.io/t/5972

## Question
### Request description

Bonjour à tous,

* Customisation du menu principal

* Choisir l'ordre des colonnes des lists de façon définitive pour tous les users et selon les lists

J'en profite pour avoir quelques petites infos en plus, sur des sujets moins complexes ^^" j'ai pris le temps de chercher ici tous les articles que je pouvais trouver sur le menu principal mais j'ai rien vu sur le changement de son nom et de son icône associée (ici, l'icon et données de référence) :

![cap_menu_principale|333x342](upload://yFx64HsltDGW9Jl0tWWReW8Bi8q.png)

J'ai trouvé comment choisir quoi afficher ( accueil/ clients / lignes de crédit / alertes) dans l'objet domain mais je m'attendais a voir plus d'options ici concernant le titre et les icons (un peu comme dans les objects métier avec leur menu => interface / options / boutons)

Ensuite, concernant les listes qui représente les attributs d'un object : 

![cap_ordre_colones|690x75](upload://4NS6xyHziGTcuSMXYcrt6KuKaUY.png)

J'ai vu qu'on chaque utilisateur peut configurer dans les options de listes selons ses préférences, l'ordre des colonnes :

![cap_ordre_col|628x500](upload://7HiJHQz2OPonJuKzrMI2m23WgtO.png)

Pour moi le but est d'interdire ce choix, j'imagine quand désactivant l'accès au préférence dans le bouton ?
Mais pour pouvoir configurer "en dur" l'ordre des colonnes ? 
Et différentes selon la vue qui les affiches ?
Pour que chaque utilisateur qui se connecte, est le même ordre et pas la possibilité de la changer !

Merci d'avance

## Answer
[quote="Jonathan, post:4, topic:5972"]
[
Cap_domain1505×822 49.6 KB
](https://community.simplicite.io/uploads/default/original/2X/0/07b9b4e92d1696fa6cf1b38fc44d9fe7d12cd2da.png)

Quand je clique sur retirer, il m’affiche une icône dossier par default. Je souhaiterais n’avoir aucune icone a gauche de menu, je le cache en CSS ? display none ?
[/quote]

Tu peux spécifier une icône `blank` qui est une icône transparente. Ou passer par du CSS au niveau de la disposition `responsive5` :
```css
[data-domain="DomainCode"]{
	.ico{
		display:none; 
/*ou*/
        visibility:hidden;
	}
}
```

[quote="Jonathan, post:4, topic:5972"]
J’aimerais pouvoir faire en sorte de choisir moi même (en temps que designer) l’ordre des colonnes par object affichés dans les listes
[/quote]
L'odre des colonnes est défini par l'ordre de la zone d'attribut dans laquelle se trouve l'attribut d'objet **et** l'ordre de l'attribut d'objet (cf aide sur le champ Ordre de l'attribut d'objet). Les attributs dans une Zone d'ordre `1` seront affichés avant les attributs dans une Zone d'ordre `2`. L'ordre des attributs au sein d'une même zone est défini par le paramétrage de l'attribut `ordre`
![Capture d’écran 2023-03-02 à 16.24.16|689x407](upload://yobUyGXaLWAO7GahhvouuG9p5NH.png)
