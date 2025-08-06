# Contrainte sur la visibilité d'une action

**URL:** https://community.simplicite.io/t/4434

## Question
Bonjour,

J'ai une action et j'aimerais qu'elle ne soit visible que pour un certain groupe **ou** si l'utilisateur responsable est l'utilisateur actuel de la session.

Pour le groupe, j'ai mis une habilitation sur les groupes dont je souhaite pouvoir voir l'action et exécuter l'action.
![image|690x323](upload://dw0WIXS2UfFEro9D0lYb2r5Bqw9.png)

Cependant, pour la deuxième condition si l'utilisateur responsable est l'utilisateur actuel de la session, j'ai créé une contrainte :
![image|690x263](upload://4Wxkuux9HirZDBVFcVZaO0vy6Sw.png)
Cette contrainte ne fonctionne pas car je ne sais pas comment appeler la méthode `getSessionInfo()` et de plus `get("rowId")` retourne `null` quand j'utilise `AppLog.info` dans le code pour l'afficher.

Mes 2 questions sont les suivantes :
* Comment appeler dans une contrainte l'ID utilisateur de la session actuel ?
* Est-ce qu'il y aura des conflits entre l'habilitation de la fonction et la contrainte ou est-ce que les 2 font fonctionner de paire sans problème ?

## Answer
Du coup, voici la solution pour laquelle j'ai opté:
`[USERID] == [VALUE:hrEmpSrvId.HrService_User_id] || [HASRESP:HR_SUPERADMIN]`
![image|690x297](upload://udM1xuMHjJxk1ctiXbQUY9cZq8Q.png)

Tout fonctionne. Merci pour votre aide
