# Erreurs de validation avec objets inlinés

**URL:** https://community.simplicite.io/t/11863

## Question
### Request description

Bonjour, c'est encore moi :grimacing:
J'ai un nouveau cas d'usage avec des objets inlinés : en cas d'erreur de validation sur l'objet père, j'ai l'impression qu'on essaie quand même de créer les fils (avec du coup une clé vers le père vide)

Mode opératoire :
- avoir un objet principal avec par exemple un champ obligatoire
- et un objet inliné en 1,1
- créer une instance du père sans remplir le champ obligatoire
-> le fils remonte également avec une erreur "clé vers le père manquante"

*1- erreur champ obligatoire
2- erreur sur le fils*
![image|690x160](upload://2x1wZBeKkwCyGclAWe5YXBndEEu.png)



*Create sans erreur de validation, la clé vers le père est renseignée*
![image|690x298](upload://zJbvWN50uuAvJzfqANrUlmekahn.png)


*Create avec erreur,la clé vers le père est vide*
![image|690x304](upload://1hrsVoSThOJXYWzGpGZFO7FKvSe.png)

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.6
Variant=full
BuiltOn=2026-03-12 16:20

## Answer
Ce sera livré en 6.3.7.

Du coup puisque dans ce cas le fils n'est pas créé, si le fils avait aussi des erreurs de validation back, elles ne seront visibles que lorsque la parent aura été créé / création en 2 temps si l'utilisateur fait n'importe quoi.

Il n'est pas possible de distinguer des erreurs qui relèvent de la création ou juste des données sans ajouter de la complexité déjà bien garnie.

Les liens 0,1 inlinés gérés par le front viendront a être remplacés par des objets composites générés par la back pour décharger la UI d'une combinatoire de plus en plus complexe. L'idée étant de fournir au front 1 seul objet, le mapping avec les objets liés/physiques devra se faire en back.
