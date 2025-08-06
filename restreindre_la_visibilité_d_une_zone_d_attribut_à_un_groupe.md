# Restreindre la visibilité d'une zone d'attribut à un groupe

**URL:** https://community.simplicite.io/t/7006

## Question
### Request description

Bonjour, Dans le cadre d'une action sur un objet en réflexif, on souhaiterai faire apparaitre la zone que pour certain gestionnaires, ceux qui aurait les droit du bouton d'action, et donc masquer aux autre utilisateurs qui aurait la visibilité sur l'objet en question.

Version 5.3.15

## Answer
Bonjour, 

Vous pouvez implémenter ce besoin grâce à une Contrainte avec un Impact qui a comme cible la zone d'attributs concernée. L'expression de l'Impact sera la vérification de si l'utilisateur appartient à un groupe particulier (ou toute autre RG)

![image|690x305](upload://nGnUn0WDBApFDNJNjrFNhE3Zu7q.png)


Si cette approche ne répond pas à votre besoin, vous avez toujours la possibilité de jouer sur la visibilité d'une Zone d'attributs avec la méthode `setVisible(true|false)` de [FieldArea](https://platform.simplicite.io/5/javadoc/com/simplicite/util/FieldArea.html#setVisible(boolean)) 

Exemple : `getFieldArea("MyFieldArea").setVisible(true|false)`
