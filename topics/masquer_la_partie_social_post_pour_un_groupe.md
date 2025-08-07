# Masquer la partie "social post" pour un groupe

**URL:** https://community.simplicite.io/t/3859

## Question
Continuing the discussion from [Module Social - masquer le module social pour un groupe](https://community.simplicite.io/t/module-social-masquer-le-module-social-pour-un-groupe/2911/2):

Bonjour,
je cherche à masquer la partie "social post" pour un groupe, seulement il n'est ni directement ni indirectement associé à Social_users : 
![image|690x191](upload://35QNdIRE83ff2EiAgBKu1L5uLbZ.png)
![image|690x267](upload://3tX1ZE18M2L4GCMXzI6T3C4xZUQ.png)
![image|690x323](upload://iPp3WcW3XmuhG8HDoqUVhJTg3XN.png)


merci

## Answer
Bizarre on va vérifier s'il n'y a pas une régression sur cette gestion de droit.

- Avez vous du code dans les codes partagés `PlatformHooks` (ou `GrantHooks` en V4) ?
car on peut y forcer des groupes à l'ouverture de session.

- Sinon il y a un hook au niveau de l'objet métier, pour dire s'il est ou non social (paramétrage au niveau de la définition de l'objet), c'est peut être ça qui est prioritaire sur le groupe SOCIAL_USER, donc un autre moyen serait de mettre dans  le `postLoad` de l'objet :

```java
if (getGrant().hasResponsibility("HR_APPLICANT"))
   setSocial(false);
```

Mais bon sans SOCIAL_USER, le flag social de l'objet ne devrait pas être pris en compte. On va vérifier.
