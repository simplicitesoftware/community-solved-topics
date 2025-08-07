# Editer en liste en appelant une méthode 1 seul et unique fois

**URL:** https://community.simplicite.io/t/4602

## Question
Bonjour,

J'ai une méthode qui permet d'avertir par email des responsables.
Cette méthode est appelé lorsque tous les responsables ont validé (Champ `ddvPowValidate = 'Yes'`).

Le problème, c'est que en plus de l'édition classique à l'intérieur du formulaire, les responsables peuvent aussi valider en éditant la liste comme ci-dessous :
![image|690x338](upload://op9RTNc5GAe65LlWKDIvrvZewSM.png)

Du coup, pour chaque ligne modifiée, la méthode `preValidate()` est appelé. Par conséquent, ma méthode d'envoie d'email aux responsables sera appelé plusieurs fois (2 fois dans la capture d'écran ci-dessus).

**Existe-il un moyen d'appelé 1 seul et unique fois une méthode lorsqu'on sauvegarde en éditant la liste ?**

## Answer
Une façon de répondre à ce besoin serait donc de regarder après un save si le nombre de lignes à "Oui" correspond au nombre total de lignes. Et peut être stocker au niveau du parent le fait qu'une notification a été envoyée - de manière à ne pas renvoyer une notification si jamais une des lignes est modifiée à nouveau.
