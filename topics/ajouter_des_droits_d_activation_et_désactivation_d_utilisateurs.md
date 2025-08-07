# Ajouter des droits d'activation et désactivation d'utilisateurs

**URL:** https://community.simplicite.io/t/5913

## Question
Bonjour,

Je voudrais créer un utilisateur dont le rôle est de gérer les autres utilisateurs, et notamment de les activer et désactiver, comme pourrait faire le designer avec son attribut usr_active ou son bouton d'action : 

![image|690x75, 75%](upload://6tt841EbJVHIxTId6q9Q4N5m7kL.png)
 et
![image|530x153, 75%](upload://pdbJSkdZ5LmR2OTjk8I3pjaeKVp.png)

Au niveau du designer je ne constate aucune habilitation qui donnerait le droit au changement d'action, donc je ne peux pas accorder à mon superadmin les mêmes droits.

Pour résoudre ça j'ai créé 2 habilitations - qui permettent à mon utilisateur de disposer des deux action ACTIVATE et DISABLE sur l'interface utilisateur. Ci-dessous l'habilitation pour le statut ACTIVATE, et j'en ai créé un deuxième pour le statut DISABLE.
![image|690x203](upload://wT9TbG8vs478nKW06on1Er4woZA.png)
L'ajout de ces habilitations me donne ceci lorsque je me connecte en temps qu'utilisateur superadmin : 
![image|690x193](upload://wEGpW1HxA1dTK2dPOR7ZEkRaJTH.png)

Ce changement d'état n'est relié à rien car cliquer sur le bouton "Activer" affiche un message de confirmation sans que rien ne se passe.

Auriez-vous une idée sur ce que j'aurai manqué de faire, car  logiquement si le designer a le pouvoir de changer les status, n'importe qui d'autre avec les bons droits peut le faire, mais malheureusement je ne trouve rien qui relie le rôle designer avec ce changement d'état.

Bien Cordialement,

Clément

## Answer
Bonjour Clément, 

Il suffit d'habiliter les transitions d'état `USER-1-0-Disable` et `USER-0-1-Activate` au Groupe concerné

![Capture d’écran 2023-02-20 à 15.27.38|690x463](upload://8ul9BGj8NjUZDtR4PrCO0x28qrO.jpeg)
