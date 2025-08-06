# Conservation des SelectedIds

**URL:** https://community.simplicite.io/t/5874

## Question
### Request description

Bonjour,

Mon contexte est le suivant : j'ai implémenté un setSearchSpec dans mon InitRefSelect pour une association via Pillbox entre un objet A et B.

Sur une instance de A, j'associe une valeur de B.
Sur une autre instance de A, mon setSearchSpec ramène donc des lignes différentes de B ; mais la valeur précédemment associée reste cochée.
Je me retrouve donc avec 0 lignes alors que je devrais avoir des valeurs possibles.

![image|690x296](upload://5ABlqDZ2soxe2rzw13dSQ2GNQj4.png)

Faut-il forcer par défaut le reset des SelectedIds avant une recherche quand j'ai un setSearchSpec?
Il me semblait qu'ils étaient déselectionnés avant une nouvelle recherche.

Merci d'avance pour votre réponse !
Emmanuelle


[details="Instance /health"]
[Platform]
Status=OK
Version=5.2.28
BuiltOn=2023-01-20 16:43
Git=5.2/863cfad4c8c21998884a167b5f88de0c00e7d44d
[/details]

## Answer
Bonjour,

Un setSearchSpec ne déclenche pas de recherche filtrée, il faut donc à priori ajouter un `resetSelectedIds()` dans votre `initRefSelect`, tout comme vous pourriez y pré-cocher certaines lignes (via listSelectAll ou setSelectedIds..) avant d'afficher la liste des références.

Mais votre cas est différent, car il garde un filtre sur le row_id directement.
Cela a été corrigé dans la version 5.2.30. Il faudrait mettre à jour l'instance et voir si ça persiste (on est actuellement en 5.2.31).
