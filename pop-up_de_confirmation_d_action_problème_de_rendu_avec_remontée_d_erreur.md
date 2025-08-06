# Pop-up de confirmation d'action : Problème de rendu avec remontée d'erreur

**URL:** https://community.simplicite.io/t/10330

## Question
### Request description

Je souhaite configurer une action avec pop-up de confirmation.
Lors du déclenchement de cette action, certains checks sont faits et une erreur peut-être remontée. 

Je souhaite que ma pop-up de confirmation, au déclenchement de mon action, se présente de façon standard avec le message "Etes-vous sûr de vouloir exécuter cette action ?" et les boutons "Oui" et "Non"

Si, lors de l'exécution de mon action, une erreur est remontée, je souhaite afficher le message d'erreur de manière standard avec le bouton "Ok" qui, au click, ferme la pop-up et redonne la main à l'utilisateur sur le formulaire courant.

Problème : Lorsque je ne surcharge pas le template UI de l'action, je me retrouve avec un message de confirmation comprennant le message standard suivi de la traduction de l'action.

![image|690x431, 75%](upload://hL2YwfQQRicnAqiJ92uQZmihkRe.png)

**Question 1 : Est-il normal d'obtenir ce rendu ? (ajout de la traduction de l'action pour suffixer le message de confirmation standard)**

Suite à cela, lorsque je confirme l'exécution de l'action, je remonte une erreur et j'obtiens alors le rendu souhaité (pop-up avec message d'erreur et le bouton standard "Ok")

![image|690x426, 75%](upload://7EVahZTHTfv0VnM2J1ATvOdyMzq.png)

Pour contourner cela, j'ai surchargé le template ui de l'action comme suis : 
```
<div class="text" data-text="Etes-vous sûr de vouloir exécuter cette action ?"> 
```

J'obtiens alors la pop-up de confirmation suivante : 
![image|632x500, 75%](upload://idVFHPZb0qfuQ66z7G6qccb6pVU.png)

**Question 2 : Sans surcharge supplémentaire de l'action, est-ce normal que l'intitulé des boutons "Oui" et "Non" standards change pour "Confirmer" et "Annuler" ?**

Le rendu me convient, malgré le changement d'intitulé des boutons. Cependant, lors de l'exécution de mon action, lors de la remonté du message d'erreur, je souhaiterai de nouveau avoir simplement accès au bouton "Ok" permettant de fermer la pop-up. Au lieu de ça, je retrouve juste sous le message d'erreur le message de confirmation de la pop-up d'action ainsi que les deux boutons "Confirmer" et "Annuler".

![image|600x500, 75%](upload://4YK3M3jMGipwxShCyLtFQwsHONH.png)

**Question 3 : Ce comportement est-il standard et si oui, comment configurer de façon standard mon action pour qu'en cas d'erreur, je n'affiche plus ni le message de confirmation, ni les boutons associés ?**

### Technical information

je suis en Simplicité v6.2.2, reproduit en v6.2.12

## Answer
Bonjour, 

[quote="JoffreyB96, post:1, topic:10330"]
Question 1 : Est-il normal d’obtenir ce rendu ? (ajout de la traduction de l’action pour suffixer le message de confirmation standard)
[/quote]

Oui, c'est normal. Le message par défaut est la concaténation du texte statique "CONFIRM_ACTION" et du libellé de l'action.

[quote="JoffreyB96, post:1, topic:10330"]
Question 2 : Sans surcharge supplémentaire de l’action, est-ce normal que l’intitulé des boutons “Oui” et “Non” standards change pour “Confirmer” et “Annuler” ?
[/quote]

Oui, c'est normal aussi. Si l'action est considérée comme "custom" à savoir, continent un Template UI ou des attributs d'actions, les boutons deviennent "Confirmer" et "Annuler"

[quote="JoffreyB96, post:1, topic:10330"]
Question 3 : Ce comportement est-il standard et si oui, comment configurer de façon standard mon action pour qu’en cas d’erreur, je n’affiche plus ni le message de confirmation, ni les boutons associés ?
[/quote]

Oui c'est normal, a partir du moment où l'action est considérée custom (template ui), on considère que l'utilisateur pourrait avoir une action à mener sur les éléments remplis dans l'action : cas d'attributs d'actions qui ne passeraient pas une validation.

Pour avoir le comportement attendu, à priori il faudra retirer le template UI et surcharger la valeur du texte statique `CONFIRM_ACTION` dans `PlatformHooks`
