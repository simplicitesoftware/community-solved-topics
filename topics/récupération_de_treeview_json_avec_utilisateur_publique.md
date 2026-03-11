# Récupération de treeview json avec utilisateur publique

**URL:** https://community.simplicite.io/t/2923

## Question
Bonjour 

Nous avons des documents consultable par les utilisateurs publiques, 

depuis une mise a jours du module System, l'affichage de ses documents ne fonctionne plus, 

la fonction incriminée semble etre la récupération de la treeview json : 
String reponse = JSONToolHelper.getObjectAsJsonTreeview(getGrant().getTmpObject("ComACOPV"), params.getParameter("id"), treeview);

En effet, cette fonction retoune bien un objet json correcte pour un utilisateur connecté, 

Mais retourne "[1]" pour un utilisateur publique, ce qui entraîne la non génération du document.

## Answer
Bonjour Théo, 

Je viens de comparer rapidement la prod et la dev/qual et il semblerait que le code de ComActionCommerciale ne soit pas tout à fait le même surtout au niveau du postLoad. 

Ce n'est donc pas lié à l'import du module Systeme mais bien à ce bout de code. La searchspec empechait l'utilisateur public de consulter le record.
