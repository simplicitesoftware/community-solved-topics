# Savoir si un utilisateur à accès à une fonction

**URL:** https://community.simplicite.io/t/4065

## Question
Bonjour,


Je suis connecté sur un objet externe et je souhaiterais savoir si le role actuel à accès à une fonction.

Comment simplement savoir si le role actuel dispose de l'accès à cette fonction ?Du genre : canExecuteFunction("maFonction") ?

Je pourrais passer par le hasResp par exemple mais si la liste des rôles associés a cette fonction évolue, je devrait la répercuter la modification dans le code également.

Merci d'avance

## Answer
Il faut utiliser les méthodes `getGrant().access*`, ex: [accessCreate](https://docs.simplicite.io/5/javadoc/com/simplicite/util/GrantCore.html#accessCreate(java.lang.String))
