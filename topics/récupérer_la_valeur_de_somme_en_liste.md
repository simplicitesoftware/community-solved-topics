# Récupérer la valeur de somme en liste

**URL:** https://community.simplicite.io/t/1989

## Question
Existe-t-il une méthode Java, ou bien un nom d'attribut qui permet de récupérer la valeur de somme en liste pour un attribut via .getField?
Image ci-dessous :

![image|470x391](upload://3rtT8ePMXzr1nOykz7tBIUjRp0I.png) 

Merci !

## Answer
Bonjour,

oui via `object.getField("xxx").getListOperatorValue()` qui est valorisé au moment du `count()` de la liste. Donc suivant où vous aurez besoin de cette somme, il faudra peut être refaire un `object.getCount()` sur l'objet avant d'utiliser cet accesseur.


Cette méthode retourne un String car potentiellement ça peut être un min/max de date par exemple.
Il faudra un Double.parseDouble() si vous voulez vous en servir en numérique.
