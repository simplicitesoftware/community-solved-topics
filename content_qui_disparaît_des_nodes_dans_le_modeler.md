# Content qui disparaît des Nodes dans le Modeler

**URL:** https://community.simplicite.io/t/4706

## Question
### Request description

Bonjour,
Je constate une régression dont je ne trouve pas l'origine dans l'utilisation du Modeler : je n'ai plus le contenu des Nodes à l'affichage de mon Model.

### Steps to reproduce

1. Paramétrer un modèle template avec des Content sur un des Model Template Object
2. Vider le cache
3. Générer un modèle basé sur ce template
4. Le content du premier node traité est visible à l'ouverture du modèle puis disparaît quelques secondes après - les autres nodes n'ont pas de content
5. Fermer et rouvrir le modèle
6. Même juste à l'ouverture, le content ne s'affiche plus

A l'ouverture (après vidage de cache)

![image|690x148](upload://mn6RRLX665EFXoHENUokEoU7SKh.png)

Quelques secondes après

![image|690x164](upload://s3X6ioMRltNCMGxFcnkz4yFLG60.png)



### Technical information

Voici mon paramétrage

![image|690x102](upload://sVrLnyGLMx0TnvATtrUzRBi5QPT.png)

En activant les logs SQL, je vois passer la requête pour mon Content et elle ramène bien un résultat.
Je n'ai pas d'erreur.
En debuggant dans la console juste après un vidage de cache je vois que mon Node est correct avec les items.

![image|543x381](upload://aPF8hSEjXrWyf8J32Xl5fU7O8YL.png)


[details="Instance /health"]
```text
[Platform]
Status=OK
Version=4.0.P25
BuiltOn=2022-03-18 11:41 (revision d81c6d369cb003b957136e8ed8d42cb7e2bbe62e)
```
[/details]

## Answer
Bonjour,

Merci pour ces précisions, ça doit donc être une limitation du modeleur qui ne gère que des objets distincts dans les contenus. On ne fera pas d'évolution en V4, mais on peut voir pour supporter cette fonctionnalité en V5.

En attendant, pour ne pas fusionner les search-spec, vous pouvez essayer de créer un héritier pour le modeleur, juste pour avoir 2 noms d'objets différents dans les contenus.
