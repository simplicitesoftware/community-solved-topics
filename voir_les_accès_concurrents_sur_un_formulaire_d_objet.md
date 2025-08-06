# Voir les accès concurrents sur un formulaire d'objet

**URL:** https://community.simplicite.io/t/4853

## Question
Simplicité 5.1.44

Bonjour,

je ne trouve pas de documentation concernant le réglage de la politique sur les accès concurrents sur les records, avez vous une page qui le décrive ?
![image|320x77](upload://d7pAt3aZilW2Ch80JJgIoWvAG2.png)

Comment fonctionnent exactement ces réglage ? On a testé le non-blocking:
User 1 prend la maint sur le record
User 2 consulte le record, l’icône de U1 apparait en haut de page du record de U2 et vice versa.
U1 sauvegarde ses modifications et se retrouve sur la page du record, l'icone U1 disparait de la page d'U2 et U1 n'a pas d’icône d'U2 sur la page du record alors qu'ils sont en accès concurrent.

## Answer
Bonjour,

Lors du "save" front, le navigateur enregistre les modifications en back, puis recharge le formulaire avec les données à jour retournées par la back.

Donc normalement :
- Le déchargement de la page supprime l'usage de l'objet pour cet utilisateur
- Et le rechargement le ré-ajoute en base (car on pourrait rediriger ailleurs après un save, comme pour un save&close ou save&copy)

Dans votre cas, les 2 événements asynchrones s'inversent et du coup l'avatar se vide.
On va corriger.

On peut voir les usages ici : Menu étendu "Operation / Object usages"
