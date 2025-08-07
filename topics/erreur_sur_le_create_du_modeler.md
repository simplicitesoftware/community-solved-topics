# Erreur sur le Create du modeler

**URL:** https://community.simplicite.io/t/9720

## Question
### Request description

Bonjour,

Nous avons une erreur à la création d'un diagramme par code via le Modeler.
J'ai l'impression que ça se produit depuis la migration de 5.3 vers 6.2.

![image|690x71](upload://aQlTxwxF0PlIzNsx1intG3Yd5Yu.png)

L'erreur semble se produire dans diagram-bundle. L'appel au Create a un cbk et un then, je ne sais pas si c'est voulu, mais ça passe dans le callback avant d'avoir reçu le résultat du call. ( _hasCallback renvoie true )

![image|690x368](upload://czWHDHiPeDblUO3PKNlaHr4aiiH.jpeg)

Je n'ai pas de méthode sûre pour reproduire, mais si ce que j'indique n'est pas suffisant dites moi, je vais essayer de voir pourquoi cela se passe sur ce diagramme en particulier.

Merci à vous 
Emmanuelle

[Platform]
Status=OK
Version=6.2.3
BuiltOn=2025-03-07 12:29
Git=6.2/de139c86150da2a84599aa6c14b51d1e06a2e118

## Answer
oui c'est un erreur, à cause du 1er paramètre (ancienne syntaxe) ça ne retourne pas de promesse.
On va corriger
