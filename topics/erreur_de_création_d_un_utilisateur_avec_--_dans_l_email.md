# Erreur de création d'un utilisateur avec "--" dans l'email

**URL:** https://community.simplicite.io/t/8914

## Question
### Request description

Bonjour,

Nous avons un problème lors de la création d'un utilisateur particulier dont l'adresse e-mail contient un double trait d'union `--`.

Le compte utilisateur n'est pas créé dans simplicité, et dans les logs on peut voir l'erreur :
```
2024-10-17 09:17:36,473|SIMPLICITE|ERROR||https://dev-sim:10838/suividspbreizhgo|/suividspbreizhgo|ERROR|system|com.simplicite.util.SessionInfo|syncUser||Evénement: Unable to update user testemail: ERR_EMAIL:Email#ERROR#usr_email
```

Nous avons d'abord constaté l'erreur sur une application en attente de migration (encore en simplicité v4 avec crowd comme fournisseur d'identités), mais après vérification le problème existe aussi sur une autre application en v6.0.23 qui utilise keycloak, avec le même message (c'est l'application d'où vient le log ci-dessus).

## Answer
Les EMAIL sont des types de champ dont la regexp est livrée comme ceci  :

`^\w+(['\.\+-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$`

Libre à vous de l'adapter à vos besoins.
