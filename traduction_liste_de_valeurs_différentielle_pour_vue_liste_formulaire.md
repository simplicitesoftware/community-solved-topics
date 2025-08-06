# Traduction liste de valeurs différentielle pour vue liste / formulaire

**URL:** https://community.simplicite.io/t/5108

## Question
Bonjour,

J'aurais souhaité savoir s'il existait un moyen d'avoir une traduction différentielle, pour les valeurs d'une liste de valeurs, entre la vue en formulaire et la vue en liste. En effet, je me retrouve avec un de mes champs qui est de type "enumerate". Cependant, les valeurs de cette liste ont des traductions assez longues. Est-il possible, pour l'affichage en liste, de raccourcir cette traduction ou de rendre possible le retour à la ligne ?

## Answer
Bonjour, 

Il n'existe pas en standard un mécanisme de "libellé court" pour la valeur d'un énum (ça existe pour les en-tête de colonne). 
À votre place, si vous ne pouvez pas vous passer d'une longue valeur de liste, je passerai par un objet métier référentiel qui porte les valeurs de votre liste avec un attribut "Traduction courte" et un attribut "Traduction longue". 
Votre objet initial aura donc un lien vers cet objet (au lieu d'un champ énum), et vous pourrez choisir d'afficher le champ ramené "Traduction courte" dans la liste et l'attribut "Traduction longue" dans le formulaire. 

Dans le cadre du module de la démo (disponible depuis l'AppStore de votre instance), ça revient à afficher le code du Fournisseur sur la liste des Produits et le nom complet du Fournisseur sur le formulaire.
