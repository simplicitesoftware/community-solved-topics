# Actualiser des champs du formulaire sans reload complet quand une liste/pillbox N,N change

**URL:** https://community.simplicite.io/t/10254

## Question
### Request description

Bonjour,

J'ai un objet sur lequel on a des champs et des pillboxs mis à jour lors de la modification d'une autre pillbox embeddée sur cet objet.
J'aimerais pouvoir recharger ces champs / pillbox en cas de mise à jour de ma pillbox sans recharger tout le formulaire.
Le reload complet agace les utilisateurs et si ils mettent à jour un champ avant de modifier la pillbox, ils ont le message de confirmation "Voulez vous quitter" et ne comprennent pas ...

Est-il possible 
- d'accéder aux nouvelles valeurs des champs sans reload
- de les mettre à jour à l'affichage ?

Merci !
Emmanuelle

[Health check]
[Platform] Status=OK Version=6.2.10 BuiltOn=2025-05-23 10:17

## Answer
Si tu as besoin de ton code back pour calculer la valeur de l'avancement, car trop compliqué à faire en front, et si tu ne veux pas "tout" recharger : il faut nécessairement faire un appel Ajax depuis le front pour rafraichir la valeur du parent.

- la pillbox Simplicité appelle un save/delete de la N,N
- en back ton hook postSave/Delete fait le recalcul de l'avancement du parent
- si save/delete N,N ok => Simplicité en front ajoute/retire un li à la pillbox (trigger un change de la vue, etc)
- ton code observer en front doit faire un `get` ajax / via instance tmp de l'objet pour pas perturber le formulaire/main => pour remonter l'avancement à jour
- then => changer la progressbar
