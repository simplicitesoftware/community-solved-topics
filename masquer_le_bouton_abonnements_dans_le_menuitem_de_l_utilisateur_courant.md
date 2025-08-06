# Masquer le bouton "Abonnements" dans le menuItem de l'utilisateur courant

**URL:** https://community.simplicite.io/t/9031

## Question
### Request description

Bonjour, Dans le cadre de mon projet, nous souhaitons retirer à certains utilisateur l'accès à une partie des fonctionnalités natives Simplicité. 

Parmi ces fonctionnalités, nous souhaiterions retirer l'accès à la partie "Social activities". Le fait de basculer le paramètre système USE_SOCIAL_ACTIVITIES à "no" m'a suffit à retirer la quasi totalité des éléments que je souhaitais masqué pour les utilisateurs concernés. Cependant, je constate que le bouton "Abonnements", présent dans le menu en haut à droite du HEADER, en cliquant sur le nom de l'utilisateur, ne disparaît pas. 
![image|690x111, 75%](upload://kBzd0MGXnEO1FwIyN1WARD5U1kS.png)

### Steps to reproduce

Je suis sur une instance en V6.1.12.

1. J'ai créé un utilisateur auquel j'ai attribué des responsabilités propre à mon appli (consultation des objets métiers relatifs à mon appli). Ces responsabilités ne sont pas reliées aux groupes SOCIAL_ADMIN et SOCIAL_USER.
2. Le paramètre système USE_SOCIAL_ACTIVITIES a pour valeur "no" (pas de valeur remplacée)
3. Constatant que le bouton Abonnement ne disparaissait pas, j'ai tenté d'ajouter le paramètre utilisateur du même nom USE_SOCIAL_ACTIVITIES avec la valeur "no".
--> Le bouton "Abonnements" est toujours visible

### Questions annexes

* Mon application n'étant qu'à destination d'utilisateurs Français, nous souhaitons aussi masquer les drapeux avec le choix de langue. Y a-t-il un élément de conf qui permette de le faire sans passer par une surcharge des styles complémentaires de mon thème (ressource *addon.less*) ?
Aujourd'hui, ma solution est d'appliquer un display: none sur les deux \<img> correspondantes. Solution ok mais est-il possible de masquer cette option par de la configuration Simplicité ?
* Même chose concernant l'option "copier le lien" dans le menu en haut à droite de chaque vue liste/formulaire. Je n'ai pas su trouver d'option dans la config d'un objet métier pour masquer cette option

## Answer
Bonjour,

- Si vous regardez la définition de ce raccourcis, il est habilité à `NOTI_ADMIN` et `NOTI_READER`.

- Copier le lien = je pense que vous parlez du flag `USE_DEEPLINKS`

- Les langues sont données par la liste de valeurs `LANG` mais l'anglais est forcé en plus des autres langues. du coup je pense qu'on est obligé de masquer le bouton par CSS. On ne peut pas définir les langues possibles pour un utilisateur donné. Il faudrait disposer d'un paramètre `USE_LANGS` pour conditionner ce switch, on va l'ajouter en 6.1+.
