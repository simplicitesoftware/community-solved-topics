# URL perdue après connexion

**URL:** https://community.simplicite.io/t/5729

## Question
### Request description

Bonjour,

Nous avons un paramétrage de connexion via LDAP (paramètre LDAP_AUTH_CONFIG).
Quand on accède à Simplicité via une URL, par exemple le lien d'un objet, après l'écran de LOGIN, on est directement dirigé vers la page d'accueil.
J'ai vu que ceci a été implémenté pour [SAML](https://community.simplicite.io/t/url-pour-acceder-directement-a-une-objet-metier-dans-une-alerte-email/2732) mais j'ai l'impression que ça ne marche pas avec LDAP ?

Merci !
Emmanuelle


### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.26
BuiltOn=2022-12-20 22:00
```
[/details]

## Answer
C'est fait, en 5.2+ l'authentification via un provider LDAP conservera bien les deeplinks et le scope.
 
Ce sera livré avec la prochaine révision 5.2.28 qui sera releasée d'ici la fin de la semaine.
