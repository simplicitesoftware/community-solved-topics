# Problème de redirection au logout

**URL:** https://community.simplicite.io/t/6604

## Question
### Request description

Bonjour,

Quand on clique sur le bouton Quitter, la redirection me renvoie une erreur 500 qui disparait lorsqu'on rafraichit la page.
Il semble que la redirection de l'URL de base vers l'URL de connexion LDAP ne fonctionne pas au moment du Quit.

Pouvez-vous nous aider ?

Merci.

Julien

### Technical information

[details="Instance /health"]
```text
Status=OK
Version=5.3.4
BuiltOn=2023-06-03 17:10
```
[/details]

## Answer
OK vu, un test sur la session manquait et ça pouvait finir en NPE quand celle-ci n'était pas initialisée.

Ce sera corrigé en 5.3.10
