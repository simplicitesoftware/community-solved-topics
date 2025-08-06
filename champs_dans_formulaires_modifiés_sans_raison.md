# Champs dans formulaires modifiés sans raison

**URL:** https://community.simplicite.io/t/3147

## Question
Bonjour,

J'ai remarqué un bug assez embêtant. 
Il y a des champs dans des formulaires qui se remplissent automatiquement, alors qu'il n'y a pas de code sensé le permettre (il n'y a aucun setFieldValue ou autre sur ce champ).

![bugModif|690x348](upload://fDLIelg8Hgtuxtnf2mKmU1EFqvc.png) 

Sur cet exemple, le champ de commentaire "Observation interne" est rempli, alors que comme le montre l'historique des modifications, aucune modification n'a été faite sur ce formulaire (ce champ est bien vide par default, et n'a pas été modifié).
La valeur de ce champ est similaire à celle dans un autre formulaire du même objet, qui lui, avait été modifié manuellement (ces deux formulaires n'ont aucun lien entre eux).
Il y aurait une sorte de transfert de données aléatoire entre les différents formulaires.
Avez vous une solution ou une piste contre ce problème ?

Ps : Je ne sais pas à quel moment ce déclenche ce problème. Peut être qu'un utilisateur a des formulaires différents ouverts dans plusieurs onglet et qu'une seule sauvegarde modifie tout ?

## Answer
A quoi correspond l'objet `personne` ? 
Je ne vois pas de `create` dans votre code.

Si vous créez l'objet `personne` appelez un `personne.resetValues()` avant les `setFieldValue()`.
