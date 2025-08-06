# Création d'un workflow pour un nouveau référentiel dans Simplicité

**URL:** https://community.simplicite.io/t/6367

## Question
### Request description

Bonjour,
nous nous sommes lancé dans la création d'un nouveau référentiel chez Renault et on nous a demandé s'il était possible d'intégrer un workflow utilisable directement depuis l'instance Simplicité. Je suis allé regardé la documentation directement mais je n'ai rien trouvé de satisfaisant. S'il est possible de créer ce workflow, a-t-il des limites quant à son utilisation ou de ses features?
Merci d'avance.

AISSANI Saïd

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
Dans Simplicité il est possible de paramétrer différents types de workflows mettant en action les objets métier: workflows d'états, workflows d'activités persistants ou non persistant. Les transitions d'état ou d'activité étant habilités à des profils, etc.

Selon le besoin c'est l'un ou l'autre (ou parfois les deux) qui est le plus pertinent.

Pour vous conseiller il faudrait nous exprimer votre besoin métier sans raisonner "solution" (la solution étant la réponse au besoin, ce n'est pas le besoin).

Peut être qu'un échange en visio serait plus efficace car ce forum n'est pas le support idéal pour échanger sur des besoins.

PS : Connaissez vous le cas d'usage de la démo qui met en œuvre les 2 types de workflows sur des cas d'usage très simples autour de la notion métier de "commande"
