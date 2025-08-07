# Choix de la clé pour configurer un héritage

**URL:** https://community.simplicite.io/t/3818

## Question
Bonjour,

Pour paramétrer un héritage, je ne parviens pas à configurer correctement le champ "Id Field logical name".
Si je mets le row_id, j'ai une erreur dans les logs me disant que ce champ est technique et réservé.
Si je mets la clé fonctionnelle de mon objet père, mes jointures ne fonctionnent plus car Simplicité essaie de faire un JOIN entre un row_id et une chaîne de caractères.

![image|690x193](upload://j1TdgGMxn9R9xi7jX4sZ9FBH9yb.png)

>     org.postgresql.util.PSQLException: ERROR: operator does not exist: integer = character varying
>      Hint: No operator matches the given name and argument types. You might need to add explicit type casts.

Pouvez vous m'indiquer la bonne façon de faire ? Ou s'il y a un tuto sur le sujet, je n'ai pas trouvé.

Merci ! 
Emmanuelle

## Answer
Pour un héritage entre objets "standards" Simplicité il n'y a pas besoin de configurer cet attribut "Id field".

Pour mémoire celui ci ne sert que quand on configure des objets "atypiques" qui ont un "row ID" qui n'est pas la colonne standard Simplicité `row_id`
