# Problème persistant de complétion automatique sur un champ

**URL:** https://community.simplicite.io/t/6694

## Question
Bonjour,

Suite à une question que j'avais déjà posée à l'équipe concernant le préremplissage d'un champ dans mon business process de création d'un objet métier, la dernière réponse a effectivement résolu le problème initial.

Cependant, je me suis rendu compte que j'avais rencontré un nouveau problème lié à ce préremplissage du champ. Malgré le succès du préremplissage initial, le système continue de considérer le champ 'direction' comme obligatoire lors de la soumission du formulaire pour créer l'objet. Ce comportement inattendu bloque la création de l'objet malgré la valeur préremplie dans le champ. (cf capture d'écran ci-dessous)

![image|690x373](upload://gG5PBBoii4yCH76vskgpG1WAfhO.png)

J'ai entrepris plusieurs actions pour résoudre ce nouveau problème, notamment la vérification des règles de validation et l'emplacement du `setFieldValue()` . Cependant, malgré ces vérifications, le problème persiste et je ne parviens pas à identifier la source de l'erreur.

Merci pour votre support continu.


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
SystemDate=2023-07-20 15:25:28

## Answer
Merci pour votre réponse.

Je me suis rendu compte que c'était une fk intermédiaire (en rouge) qui était valorisée au lieu de la fk principale (en vert) ce qui était la cause de mon problème : 

![image|690x402](upload://d7da4eLcqky46a2DCsjDHJsHwX1.png)


A présent, tout fonctionne correctement. Merci pour votre aide !

Cordialement, 
Elyass
