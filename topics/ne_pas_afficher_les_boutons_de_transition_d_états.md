# Ne pas afficher les boutons de transition d'états

**URL:** https://community.simplicite.io/t/5588

## Question
Bonjour
je suis à la recherche d'un moyen  permettant de ne pas afficher les boutons de transition d'états : 
![image|690x82](upload://d6hjbYeSNxAHxsdVPRD4cj9DRtY.png)
sans pour autant inhiber ces mêmes transitions d'états. 
Je pensai simplement rajouter une ressource de type stylecss sur mon objet avec le fichier suivant : 
button.btn.btn-transition.action-not-xs { visibility: hidden;}
mais sans succès, est ce la bonne méthode ?

Frédéric
Ps : je suis en version 5.2.24 Bootstrap 4

## Answer
Bonjour,

Les boutons de transition d'état sont des actions de transition d'état. 
Il vous suffit de retirer l'action et  les personnes habilitées pourront réaliser la transition via la liste de valeurs. 

![image|690x232](upload://o0NipJb3JT5KB9P7PmAjldCAMx2.png)
