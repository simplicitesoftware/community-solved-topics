# Suppression d'un objet comportant attribut type Document entraîne la suppression du document en base

**URL:** https://community.simplicite.io/t/4045

## Question
Bonjour,

Version de Simplicite : 5.1.5.

Données concernées : 
- Objet métier Justificatifs comportant, entre autres, un attribut pieceJustificative de type Document
- Objet métier DossierTypeA
- Objet métier DossierTypeB
- Objet métier DossierTypeC
L'objet Justificatifs est relié aux objets parents DossierTypeA, DossierTypeB et DossierTypeC par une relation 1,N.
L'alimentation de l'objet Justificatifs est conditionné par le type de dossier (A, B ou C) et aussi certains champs du dossier B par exemple.

Fonctionnalité mise en place :
Pour éviter de stocker des documents en doublon, nous avons mis en place une récupération d'anciens documents pour un client donné. Exemple : Un client Lambda a renseigné une pièce d'identité dans un dossier A. Plus tard, il monte un dossier B et la pièce d'identité est aussi demandée. Le traitement va chercher tous les dossiers (A, B et C) du client Lamba et renseigner, par défaut, la dernière pièce d'identité utilisée dans le champ pieceJustificative type "pièce d'identité" du dossier B, en cours de saisie.

Technique utilisée pour mettre en place la fonctionnalité :
Pour un attribut de type Document, on a vu que sa valeur, en base de données, est un champ de type String correspondant au row_id de la table m_document du document ajouté.
Dans les hooks postCreate et postUpdate des objets DossierTypeA, DossierTypeB et DossierTypeC, on charge l'objet Justificatifs. Et à ce moment-là aussi, via une requête SQL, on va chercher la liste des attributs pieceJustificative déjà utilisés par un client Lambda dans d'autres dossiers créés auparavant. Via cette requête, on récupère le row_id du dernier document utilisé. Ensuite, on set l'attribut pieceJustificative de l'objet Justificatifs avec la valeur du row_id récupéré.

Constat :
A la création d'un objet DossierType*, tout se passe bien. La dernière pieceJustificative utilisée remonte bien. En revanche, pour le dossierTypeB, lorsque l'on met à jour un champ particulier et qu'on enregistre le formulaire, l'objet lié Justificatifs se met à jour. On fait une suppression (via un getForDelete du BusinessObjectTool) de l'objet Justificatifs précédent la mise à jour du champ particulier et on initialise un nouvel objet Justificatifs.
Et c'est à ce moment là qu'un problème arrive. A savoir, que la suppression de l'objet Justificatifs entraine ceci (constaté fonctionnellement et via les logs en activant les logs SQL) :
- la suppression de la ligne de la table m_document correspondant au row_id renseigné dans l'attribut pieceJustificative de l'objet supprimé Justificatifs
- mise à null de l'attribut pieceJustificative de l'objet Justificatifs du dossier où avait été récupérée la pièce d'identité la plus récente

Hypothèse :
La suppression, via le getForDelete(), d'un objet comportant un attribut de type de Document entraîne la suppression du document dans la table m_document. Comme, dans notre cas, la ligne m_document supprimée n'est pas rattachée à l'attribut pieceJustificative de l'objet supprimé, il y a un traitement qui tourne derrière pour aller mettre à null la valeur de l'attribut auquel était rattaché la ligne m_document qui vient d'être supprimée. Probablement un traitement de conformité pour éviter des liens cassés entre des enregistrements "en vie" et des enregistrements "morts".

Questions :
1) Est-ce bien le "getForDelete" qui est responsable de la suppression du document et de la mise à null de l'attribut de l'objet créé de référence ?
2)  Existe-t-il un moyen de contourner ce problème ?
3) Peut-être que notre technique utilisée n'est pas la bonne ?

J'espère ne pas vous avoir perdu dans ma tentative d'expliquer le problème :slight_smile: 

En vous remerciant.

Bruno

## Answer
Bonjour,

Oui il y a une bijection entre m_document et le champ de l'objet.
Si on supprime un record, ça supprime les documents (enfin ça les mets en 40aine dans recyclebin pour permettre le Undo de l'utilisateur dans sa session).

Pour mutualiser votre document entre plusieurs dossiers, il faut donc créer une relation N,N et non 0,N entre vos dossiers et vos justificatifs.

Vous pourrez ainsi :
- Utiliser la fonction d'Association sur le lien pour lier en masse des documents déjà existants à un dossier
- Supprimer la relation et pas le document partagé.
- Au postDelete de la relation N,N, il faudra tester s'il n'y a plus de lien pour supprimer le justificatif orphelin.

Bien sur, cela impacte votre modèle physique, et il faudra prévoir une reprise de données si votre application est en production pour alimenter la table N,N.
