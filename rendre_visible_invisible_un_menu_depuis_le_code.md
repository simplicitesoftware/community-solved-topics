# Rendre visible/invisible un menu depuis le code

**URL:** https://community.simplicite.io/t/4560

## Question
Bonjour,

Je possède le menu suivant : 
![image|271x190](upload://eu6aee14oZROaczkTXszlUDane4.png)

J'aimerais depuis le code rendre invisible ou visible dans certain cas le menu `Equipe` ou le menu `Fond`.

J'ai consulté la documentation, et il est effectivement possible de récupérer les `MenuItem` et de boucler sur leurs noms pour récupérer le bon menu. Mais dans la documentation, il n'y a pas de méthode `setVisible()` ou `isVisible()`.

**Auriez-vous une solution ?**

## Answer
Vous avez la notion d'héritage de groupes ou d'union de droits par le paramétrage de profils.
Si un utilisateur d'une équipe a plus de droits il peut  être dans un groupe habilité à la fonction de lecture  du domaine Information et DDV_EMPLOYEE n'a pas de droits sur le domaine.
Si vous voulez changer les accès au menu par code vous le ferez forcément dans PlatformHooks.
