# Erreur 404 pour télécharger un document déposé

**URL:** https://community.simplicite.io/t/3827

## Question
Nous avons migré en Aout une application de V3 vers V4
Pour cette migration, nous avons fait une reprise des données (postgres vers mysql) et aussi copié les documents déposés par les utilisateurs sur la nouvelle instance.

Lorsque nous essayons de télécharger les documents, ça fonctionne pour certains mais pas pour d'autres = Erreur 404.

![image|690x213](upload://lZzyfUaZprCqYQj01EZfPgY7oO7.png)

J'ai vérifié en base, les référénces dans m_document sont correctes :
![image|689x47](upload://Aq3LV4ZqF2g35770kpFSghX6LuT.png)

j'ai vérifié sur le serveur, le document est bien présent :
![image|534x106](upload://4ETXTcy2syETdkbpWcQkNPCeRcS.png)

requête envoyée :
https://region.bretagne.bzh/eqlyc/ui/document?object=CrbEqlDemandePj&field=eqlDemandePjDoc&row_id=40036&doc_id=63411&_=4b75e331329a5018f5504996ce9c3fe498350469_20210901022448

## Answer
Ok,
si le doc est bien téléchargeable directement depuis l'objet système Documents et sans passer par l'objet métier, c'est que tout est bien câblé techniquement. Il faudrait maintenant comparer l'URL pour télécharger le doc depuis tous les points d'accès (document, liste et formulaire).

Si ce sont les mêmes c'est certainement un problème de droits de lecture sur le record de l'objet qui contient des documents. Quand on demande un document d'un record :
- simplicité vérifie que le doc existe (dans la table m_document avec les bonnes références + path)
- et que le "select" avec les droits utilisateur ramène bien le record avant de servir le document. 

A tester avec plusieurs profils, et voir s'il y a des filtres/search-spec sur l'objet métier qui limitent l'accès aux enregistrements qui ne servent pas les documents.
