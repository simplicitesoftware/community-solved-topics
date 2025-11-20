# Erreur sur champ "fantôme" dans les logs

**URL:** https://community.simplicite.io/t/11010

## Question
### Request description

Bonjour,

Nous avons depuis quelques temps une erreur qui revient dans les logs.
Elle survient au moment d'un getCount().

```long nb = linkedObj.getCount();```

Cela n'a pas l'air d'avoir de conséquences concrêtes donc ce ticket n'est pas urgent, mais je n'arrive pas à voir d'où vient le problème.

> ECORED0001|system|com.simplicite.util.engine.ObjectManager|makeFrom||Error Configuration error RciDomBceApp: unable to find the parent field of rciDomfctappAppId.rciAppIsBackup

Pour information, nous avons bien un Object Field rciDomfctappAppId mais il est sur un autre objet ( RciDomFctApp et pas RciDomBceApp).
J'ai essayé de supprimer et recréer la classe, redémarrer Tomcat sans succès.
Je sèche un peu !

Merci d'avance pour vos pistes éventuelles !
Emmanuelle

[Platform]
Status=OK
Version=6.2.18
BuiltOn=2025-10-31 21:07

## Answer
Bonjour Emmanuelle,

Le champ `obf_ref_field_id` est effectivement masqué car contraint par des règles compliquées de compatibilité ascendante avec le nouveau champ reflexif `obj_joined_id` sensé le remplacer à terme.

A date jusqu'en V6 :
- `obf_ref_field_id` sert toujours au chargement des champs référencés en cache, et peut être spécifié dans les "vieux" modules XML
- `obj_joined_id` sert à la UI pour filtrer le choix des champs de l'objet référencé et à afficher un arbre dans le panel des attributs, et pour importer les modules "récents".

On va retirer le propriété `copiable` de `obf_ref_field_id` afin de forcer le recalcul au save en fonction de l'autre.

En attendant, supprime et recrée ces attributs d'objet.
