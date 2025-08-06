# Refactoring User

**URL:** https://community.simplicite.io/t/3499

## Question
Contexte : Permettre aux administrateurs de l'application d'accèder à la liste des utilisateurs.

Nos utilisateurs ne sont pas modifiable depuis l'application car c'est synchronisé avec un annuaire Azure AD.

Actuellement on a ajouté des champs sur l'objet User.
![image|690x120](upload://zEPOrQ5kimketpoNJnDdRcn1YSV.png)

J'ai donc créé un objet qui hérite de SimpleUser et ça répond en grande partie au besoin.

2 Question découlent :
- Comment afficher ces attributs dans notre Objet Final
- Peut-on utiliser le template editor pour gerer l'affichage de cet objet et si oui de quelle manière? J'ai créé un template pour gérer l'affichage mais ça ne change rien. Je dois passer par le platform  hooks pour cacher des champs mais pas possible de gerer la disposition.

## Answer
Vous devez mettre au niveau de `SimpleUser` ce qui est utile à la fois dans le `User` système et dans votre user "simplifié".  Ca dépend donc de votre besoin en customisation du user.

Par contre je ne comprend pas ce que vous voulez dire par "empêche l'utilisation du template", décrivez nous ce qui vous pose pb exactement. 

Comme pour tout objet qui hérite d'un autre il n'est pas possible de modifier au niveau du fils ce qui est défini au niveau du père, c'est logique. SimpleUser comprend des attributs associés à une zone d'attribut `SimpleUser-1` => celle ci n'est donc pas éditable via le template editor sur objet qui hérite de `SimpleUser`.  C'est ça qui vous pose pb ?

En tout état de cause utiliser le template editor drag&drop n'est jamais obligatoire, c'est juste un outil visuel additionnel => vous pouvez toujours directement éditer manuellement le HTML des templates de formulaires et de vues et des zones d'attributs si besoin (c'est ce qu'il fallait faire avant l'arrivée du template editor visuel).
