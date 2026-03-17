# Bouton Action liste et menu plus

**URL:** https://community.simplicite.io/t/11641

## Question
### Request description

*Bonjour, je constate que la configuration de l’affichage d’un bouton d’action en liste dans un menu “plus” sur la version 5.3.84 n’a pas le comportement attendu.*


Configuration action :

![image|690x243](upload://xKeT13ovrnQY2OfNJpPkDKnCr3Z.png)

Resultat UI (sans code, juste configuration précédente) : 
![image|690x92](upload://4SxgmuRC9T1B9ns4NJjleEbEm49.png)

J'ai réussi par le code dans le hook `initList` (ne fonctionne pas dans le `postLoad` mais logs identiques) mais j'ai l'impression qu'il y a quand même un bug/régression car on peut constater dans les logs que :

* le bouton est censé être dans le menu “plus” car `action.isDefaultPlus()` = true

* mais bizarrement `action.isPlus()`  = false

* après un `action.setPlus(true)`

* `action.isPlus()` devient true

**Suis-je obligé d'implémenter la surchage "codée" en 5.3  ? (car en 6.2 ou 6.3, la configuration suffit ) Ou il y a effectivement une régression sur la version 5.3.84 ?**

### Technical information

[details="Simplicité logs" open]
```text
initList||Event: 3 isPlus() true
initList||Event: 2 isPlus() false
initList||Event: 1 isDefaultPlus() true
```
[/details]

## Answer
Bonjour, 

En nous excusant pour le délai de réponse, je ne reproduis pas le problème sur une instance 5.3.84.

[details="Détails"]
### v6.3.5 OK

![demo63_-_Imports_supervisor|584x193](upload://e6LVKXEXJDyFOQBbd1daVhFGc0P.png)

### v5.3.84 OK

![demo53|591x348](upload://uMbS5WBJKL8cpiXBKzXSuQZE5GE.png)
[/details]

Avez-vous essayé de vider les préférences utilisateur pour cet objet?

![demo53|541x500](upload://vZAsvDAN233u1z15224Q4f27sRf.png)

Si le problème persiste, il va nous falloir des informations supplémentaires: logs navigateur, logs serveur, etc.
