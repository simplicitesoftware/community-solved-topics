# Impossible de joindre un document à un mail

**URL:** https://community.simplicite.io/t/5312

## Question
Bonjour, je cherche à joindre des documents dans des mails, ceux-ci sont issus d'un champs de type "document" de simplicité. Le mail part bien, mais il n'y a pas de pièce jointe.
![image|385x88](upload://mc0qWv8jN1IYAbU5WAFifRQJ9oZ.png)

j'utilise ce code :
[...]
ObjectDB users = getGrant().getTmpObject("HrSalarie");
mail.addAttach(users,users.getField("hrSalPlanning"));
[...]
mail.send

Cordialement

## Answer
Je reproduis bien le fait qu'en l'état ça n'envoie pas la pj.
Ça fonctionne si tu rajoutes un `users.select(users.getRowId())` après ton `.setValues()`
