# SSL problems avec GIT

**URL:** https://community.simplicite.io/t/10347

## Question
Bonjour,

Sur le premier *push* de mon projet sur GitLab j'ai le message suivant 
`https://xxx.picsel.xxx/ZPN_XXX/afimo.git: Secure connection to https://xxx.picsel.xxx/ZPN_XXXafimo.git could not be established because of SSL problems`

**Step pour reproduire**
Je viens de créer un module Simplicité pour commencer un nouveau POC. 
Côté GitLab, j'ai créé un projet vierge (avec le Readme.md uniquement). J'ai créé une branche "develop" (branche par défaut et protégée).
Dans les settings de mon module j'ai bien déclaré et **sauvegardé** mon repo distant :
{
	"origin": {
		"uri": "https:// `xxx.picsel.xxx/ZPN_XXX`/afimo.git"
	},
	"type": "git",
	"branch": "develop"
}
J'avais d'abord ajouté au settings "username" et "password" au même niveau que "uri".
J'ai testé enfin en déclarant sous forme de variables d'environnement le username/password git avec les clefs : REMOTE_GIT_USERNAME et REMOTE_GIT_PASSWORD.

Je créé mon premier commit (il apparait bien dans Modules > Module : afimo > Git repository). Quand je clique sur *Push* j'ai le message d'erreur plus haut.

USE_GIT est bien à yes.

Hors Simplicité, je me suis assurée de pouvoir : 
- cloner le projet sur ma Vm locale (Windows)
- créer un nouveau fichier, le commiter et le pusher sur mon repo distant

Merci pour votre aide

## Answer
OK il faudrait que la JVM qui fait tourner Simplicité coté serveur connaisse cette CA interne comme "trusted CA", je pense que ça ne doit pas être le cas (la JVM gère sa propre base de certificats, elle n'utilise pas celle de l'OS d'où la différence de comportement je pense)

S'agit il d'un déploiement en container Docker ou d'un déploiement "classique" ?

NB: une autre approche possible, passer par des URI Git en protocole SSH (en git://) avec idéalement authent par clé SSH, ça évite les problèmes SSL
