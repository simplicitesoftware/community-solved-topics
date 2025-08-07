# Groupes de responsabilité + Paramètres utilisateurs + visibilité du menu lors de la connexion

**URL:** https://community.simplicite.io/t/9170

## Question
### Request description

Besoin actuel : La connexion des utilisateurs de notre application se fait par SSO. Dans le platformHooks.java, nous avons donc souhaité dans l'ordre : 
1. Récupéré les groupes de responsabilité liés au token utilisateur
2. Set les paramètres utilisateurs en fonction du/des groupes de responsabilités de l'utilisateur
3. Rendre visible ou non le menu principal (menu sur la gauche de l'écran) de Simplicité en fonction du/des groupes de responsabilités de l'utilisateur.

### Steps to reproduce

Nous avons commencé par implémenté ces 3 étapes dans le hook **preLoadGrant(Grant g)**.
1. `Grant.addResponsibility(Grant.getUserId(g.getLogin()), respGroupToSet, Tool.getCurrentDate(-1), null, true, MODULE_USERS);`
--> Fonctionne : Les groupes de responsabilités sont bien visibles dans le profil de utilisateur
2. `if (getGrant().hasResponsiblity(respGroupToSet)) { Grant.getSystemAdmin().setUserSystemParam(g.getLogin(), userParamToDisable, "no", true);}`
--> Ne fonctionne pas car le `hasResponsibility(respGroupToSet)` retourne *false*
3. `if (getGrant().hasResponsiblity(respGroupToSet)) { [Mise à jour du champ usr_menu pour l'utilisateur courant, dans la table m_user];}`
--> Ne fonctionne pas car le `hasResponsibility(respGroupToSet)` retourne *false*

Nous avons tenté d'implémenter les étapes 2. et 3. dans les hooks **preLoadProfile()** et **postLoadProfile()**, sans succès car le `hasResponsibility(respGroupToSet)` retourne *false*.

Seul le postLoadGrant() permet d'obtenir un `hasResponibility(respGroupToSet)` = *true*. Cela permet effectivement de set les paramètres utilisateurs (2.) mais concernant la visibilité du menu principal (3.), bien que le champ *usr_menu* soit passé à la valeur attendu ("0" ou "1"), cela n'affecte pas la visibilité du menu car le switch de la valeur n'a pas été prise en compte pour display l'écran d'accueil. 

Si on tente une seconde connexion, cela résout le problème car la valeur de *usr_menu* est déjà bonne pour l'utilisateur courant avant exécution du **postLoadGrant()**

### Question
Nous souhaiterions savoir s'il y a une bonne pratique à appliquer (hooks à utiliser, ...) pour l'implémentation de ces différents besoins au moment de la connexion d'un utilisateurLo'bjectif est qu'au moment du display de l'écran d'accueil, toutes ces modifs soient réalisées et prises en compte.

### Technical information

Simplicité V6.1.15.

## Answer
Bonjour,

Les responsabilités sont bien accessibles après avoir été chargées, donc en général pour ne pas se poser de question, on change les responsabilités au `postLoadGrant` = le dernier hook pour ajouter/retirer les groupes en base/session en regard du profil remonté du SSO, forcer des paramètres...

Pour changer le flag menu, inutile de le changer en base, il suffit de le changer en mémoire au `postLoadGrant` ou après profile :

```java
grant.getData().m_showMenu = false;
```
