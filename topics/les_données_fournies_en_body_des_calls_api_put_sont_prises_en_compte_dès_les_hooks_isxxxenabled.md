# Les données fournies en BODY des calls API (PUT) sont prises en compte dès les hooks isXXXEnabled

**URL:** https://community.simplicite.io/t/3777

## Question
Bonjour,

Version=5.1.0 BuiltOn=2021-09-01 18:40 (et probablement toutes les précédentes)

En cas de PUT sur une API rest mappée, les données fournies par le client sont déjà prises en compte dans les hooks isXXXEnabled (i.e. reportées dans les values de row ou accessibles via getFieldValue) . Ceci met en défaut nos règles d'activation des droits lorsqu'elles s'appuient sur les dernières valeurs validées lors du save précédent.

Exemple : Un attribut "recordOwner" est renseigné pour limiter la modification à "recordOwner". Un client pourrait pousser une nouvelle valeur de "recordOwner" pour transgresser la règle.

Le contournement mis en place pour l'instant est de ne pas faire référence à **getFieldValue**(...) mais **getFieldOldValue**(...) dans les hooks isXXXEnabled pour garantir un comportement équivalent entre les cas d'usage UI et API.

## Answer
Merci beaucoup pour ces éclairages (et pour l'historique).

La consigne est passée : Dans les hooks **isUpdate|DeleteEnable**, utiliser **getFieldOldValue** qui contient les dernières **valeurs validées** à la place de getFIeldValue (ou row qui contient les mêmes valeurs) qui pourra contenir des valeurs proposées à la mise à jour.
