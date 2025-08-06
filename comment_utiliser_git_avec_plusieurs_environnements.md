# Comment utiliser GIT avec plusieurs environnements

**URL:** https://community.simplicite.io/t/9710

## Question
Bonjour, 

je souhaite utiliser Git avec plusieurs environnements. 
J'ai 3 environnements :
- Dev
- Recette
- Prod
Chaque environnement à son répertoire Git.

J'aimerais savoir s'il est possible d'utiliser tout les environnements git entre eux (de push de dev vers Recette)

## Answer
PS: Exemple de settings d'un module avec un repo Git externe de "reference" sur GitHub (+ ses settings de qualimétrie: Linting et Sonar):

```json
{
	"type": "git",
	"origin": { "uri": "git@github.com:myorg/mymodule.git" },
	"maven": {
		"checkstyle": true,
		"jshint": true,
		"eslint": true,
		"stylelint": true
	},
	"sonar": {
		"organization": "myorg",
		"host.url": "https://sonarcloud.io"
	}
}
```

Dans le cas ci-dessus la (ou les) instance(s) de dev ont le droit de lecture et écriture sur le repo GitHub, les instances de recette/preprod/prod ayant, elles, uniquement les droits de lecture

PS du PS: En général les processus de déploiements de modules via répos Git s'accompagnent de l'utilisation des mécanismes d' "importspec",cf. [cette doc](https://docs.simplicite.io/docs/operation/auto-setup)
