# Changement authent 5.1

**URL:** https://community.simplicite.io/t/3897

## Question
Bonjour,

On a constaté une regression en 5.1 qui plante toute notre CI:
![image|689x131](upload://tnHbP3qaCKuIAQqRvoqOwfQIGlB.png)

On utilise toujours le couple designer:simplicite pourtant. Quand on passe sur l'image 5.0.x, ça fonctionne de nouveau sans changer les paramètres en entrée. Y'a-t-il un changement en 5.1 sur l'authent ?

## Answer
Certains contrôles d'accès ont été renforcés en 5.1 suite à différents audits de sécurité.

Notamment, depuis la révision 5.1.3 (cf. la release note) on n'autorise plus l'accès au endpoint I/O via username/password par un user qui est encore dans le statut où il doit changer son mot passe. Etes vous dans ce cas là ?

Si oui vous devez passer un mot de passe I/O via la variable d'environnement `IO_PASSWORD` (ou la property JVM `io.password`) ex: `docker run ... -e IO_PASSWORD=<a very strong password> ...` et l'utiliser sur le endpoint I/O à la place du password "normal" (qui pourra être utilisé une fois qu'il aura été modifié).
