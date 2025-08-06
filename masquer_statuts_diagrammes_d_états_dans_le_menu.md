# Masquer statuts diagrammes d'états dans le menu

**URL:** https://community.simplicite.io/t/3775

## Question
Bonjour, 
J'aimerai masquer sur mon menu, le diagramme d'état qui s'ouvre (Inactif, Actif etc.).
![image|267x192](upload://20ANRTO9oFWKGWr2nqXUmAD3UOG.png)
Je suis sur un objet personnalisé hérité de m_user. 
Il me semble que cela est possible sur la configuration de l'objet mais je ne retrouve plus où se trouve ce paramétrage. 
Version : 5.1
Merci pour votre aide,
Ophélie

## Answer
Pour masquer le sous menu des états il faut appeler `setMenuStates(false);` dans le `postLoad` de votre objet.
