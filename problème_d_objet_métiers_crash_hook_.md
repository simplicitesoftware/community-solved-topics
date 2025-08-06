# Problème d'objet métiers (crash/hook)

**URL:** https://community.simplicite.io/t/4619

## Question
Bonjour,

J'ai fait une boucle infini sur un objet métier : j'ai fait un `save()` dans `preValidate()`.

Le problème, c'est que j'ai arrêté la boucle puis je l'ai enlevé et maintenant mon objet métier ne fonctionne plus.
Quand je sauvegarde mon objet, les infos sont sauvegarder, mais je ne passe même plus par mon code. Aucun Hook n'est appelé :
Mon message `"passe par pre validate power"` ne s'affiche pas dans les logs.
![image|690x270](upload://5nU1ZGjNu87KyB3HXCHShC436ya.png)

Tous les autres objets métiers fonctionnent.

J'ai demandé de redémarrer le serveur mais j'ai toujours le problème.

**Une idée du problème ?**

## Answer
Bonjour,

Lorsque vous créez un nouveau sujet sur le forum, il y a un template de sujet qui a sa raison d'être: sans les informations techniques, il est difficile de vous assister. Merci de le respecter. (s'il ne s'affiche pas pour vous, merci de me contacter par MP)

![Simplicité_Software_Community_Forum|676x500](upload://gsGAmIBDySNFrgQHgFJd5pZxKLz.jpeg)


---

Pour votre exotique problème, essayez de 
1. copier le contenu du code
2. supprimer le code (cf screenshot)
3. ajouter un nouveau code
4. y recoller le contenu

![Simplicité®|690x482](upload://xDBGWu0PZIrQkYbE4b3hO8rkrfK.jpeg)
