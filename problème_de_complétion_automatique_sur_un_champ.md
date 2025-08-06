# Problème de complétion automatique sur un champ

**URL:** https://community.simplicite.io/t/6675

## Question
### Request description
Bonjour,

J'ai un business process de création d'un objet métier. Dans ce processus, l'utilisateur doit remplir plusieurs champs, dont l'un d'entre eux concerne le département juridique. Je souhaite que ce champ soit prérempli lorsque l'utilisateur arrive sur la page de création, car la table des départements ne comporte qu'un seul élément.
![image|539x197](upload://n4IdjynCq5f4YRKv4gRdCDipjiL.png)
(*Champ du département juridique*)


Pour atteindre cet objectif, j'ai configuré le champ en activant l'option "Auto-select" dans la section "Auto-complétion" des paramètres de champ. Cependant, lorsque j'arrive sur le formulaire de création, le champ n'est pas automatiquement prérempli. Lorsque je clique dessus, une pop-up s'affiche avec la possibilité de choisir l'unique élément de la table des départements.
![image|278x92](upload://ukJgKMyWT0BWS0YkHnu6KwJcH3K.png)
(*section "Auto-complétion" des paramètres de champ*)

![image|690x160](upload://xRUW7A2GsvVRD7cwbxz3Ymco9Sg.png)
*(popup qui s'affiche après avoir cliqué que le champ)*


Je me demande donc d'où pourrait venir le problème et pourquoi la complétion automatique ne fonctionne pas comme prévu. Ai-je manqué quelque chose dans ma configuration ou y a-t-il d'autres paramètres que je dois prendre en compte ?

Toute assistance ou suggestion pour résoudre ce problème serait grandement appréciée.

Merci beaucoup !

Cordialement,
Elyass

### Technical information
[Platform]
Status=OK
Version=5.3.8
BuiltOn=2023-07-10 20:23
Git=5.3/4502a60a63d445a5ec961e13b5f62415953c5056
Encoding=UTF-8
EndpointIP=149.202.171.75
EndpointURL=http://renault.simplicite.io:10488
TimeZone=Europe/Paris
SystemDate=2023-07-13 17:47:13

## Answer
Vous pouvez essayer en rajoutant un `populate(true)` après le `setFieldValue` ?
