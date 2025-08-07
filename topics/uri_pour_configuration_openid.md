# URI pour configuration OPENID

**URL:** https://community.simplicite.io/t/5912

## Question
### Request description

Bonjour,
Nous allons migrer vers un protocole de connexion avec OPENID connect.
Nous avons besoin pour cela des URI redirect et logout.
J'ai trouvé dans [la doc](https://docs.simplicite.io/documentation/91-authentication/tomcat-oauth2.md) l'information pour redirect `<base URL>/oauth2callback`, mais pas pour le logout. Pouvez vous m'éclairer ?

Merci d'avance,
Emmanuelle

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
1) L'URL de logout à configurer coté Simplicité est l'URL de logout de votre IdP.
2) L'URL de logout à configurer coté IdP est `<base URL>/logout`

Les deux approches correspondent à des mécanismes de logout différents qui ne sont pas forcément pertinents dans tous les cas mais qui peuvent coexister:

1) un logout initié depuis la session apllicative (ex: via le bouton "Deconnecter") met fin à la session IdP 
2) un logout de la session IdP met fin aussi à la session applicative
