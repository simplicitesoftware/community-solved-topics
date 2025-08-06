# Erreur sur la modification d'un champ : "Création limitée pour XXX"

**URL:** https://community.simplicite.io/t/4571

## Question
Bonjour,

J'ai un objet métier `Service`. Lorsque je créer un service, je dois rentrer 3 informations :

* Nom du service
* Code du service
* Responsable du service

Je peux sans problème créer un service. Cependant, lorsque je veux modifier le responsable de service d'un service existant, j'ai cette erreur lorsque j'enregistre :
![image|690x201](upload://wCNDq7EmzRZfdf96yaFpHyC3lk8.png)

Il n'y a rien dans les logs.
Je suis persuadé qu'il s'agit d'un problème de configuration de notre coté, mais je sais pas lequel.

Voici ma relation entre l'objet métier `Service` et `User` :
![image|690x298](upload://g0Ul1JxotJwG7fNM6HbaPr8TWAZ.png)
*(HrSalarie extends SimpleUser)*

**Auriez-vous une idée du problème ?**

## Answer
CQFD, vous êtes limités à 1 Service maximum par Salarié.

Dans votre test "e.arlet" a déjà un Service, vous ne pouvez l'attacher à un autre service si la cardinalité vaut 1,1 :

- min 1 = on ne peut pas supprimer au delà de 1 lien minimum
- max 1 = on ne peut pas associer plus d'une fois l'entité
.
