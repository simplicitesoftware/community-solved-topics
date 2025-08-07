# Docker registry - erreur d'authentification

**URL:** https://community.simplicite.io/t/7229

## Question
Bonjour,

Voici le message d'erreur 
"
docker login https://registry.simplicite.io
Username: ####
Password: ####
Error: authenticating creds for "registry.simplicite.io": pinging container registry registry.simplicite.io: Get "[https://registry.simplicite.io/v2/":](https://registry.simplicite.io/v2/%22:) authenticationrequired
"

alors que l'authentification fonctionne avec l'UI
https://registry-ui.simplicite.io/containers

Auriez-vous une idée ?

## Answer
Bonjour David,

Merci pour ta réponse.
Après étude des flux il s'agit d'un problème de proxy de notre côté.
