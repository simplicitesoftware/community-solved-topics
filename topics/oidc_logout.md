# OIDC logout

**URL:** https://community.simplicite.io/t/11675

## Question
### Request description

Après être authentifié dans l’instance via OIDC,lorsque je me déconnecte en cliquant sur le bouton “quitter”, je suis redirigé vers une page blache où je peux lire dans la barre : “[https://Nom](https://Nom) du fournisseur/auth/realms/intradef/protocol/openid-connect/logout?id_token_hint=eyJhb…….
Comment réaliser le paramétrage pour revenir sur la page d’accueil de l’instance et non sur cette page blanche ?

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
Merci cela fonctionne avec l’uri
