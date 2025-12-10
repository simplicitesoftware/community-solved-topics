# Message d'erreur lié au relation d'objet

**URL:** https://community.simplicite.io/t/11153

## Question
### Request description

Bonjour,

Nous avons une question concernant la **gestion des relations d’objets** et la **personnalisation du message d’erreur** lorsque la cardinalité empêche la création d’un nouveau lien.

###  **Contexte fonctionnel**

Nous avons configuré un objet externe (ex : `Link : linkedLegalTextId`) avec une **relation de cardinalité 0,1** vers un objet enfant (`LbcLegalTextToExternalRef`).

L’objectif fonctionnel est de garantir qu’**un seul lien maximum** puisse exister pour un enregistrement donné du parent (`LbcLegalText`).
![image|689x248, 50%](upload://lc8JmbpCPab3Mg9HD8HSdmSfs5Z.png)


### 🔍 **Comportement actuel**

Lorsque l’utilisateur tente de créer un deuxième lien, Il voit le message standard :

> **“Creation limited for: Linked Legal text (1)”**


![image|690x215, 50%](upload://h1ao7yAp2q2wPRbgz3dx7sXl7Z0.jpeg)

Ce message est correct techniquement, mais pas compréhensible pour l’utilisateur final.


###  **Objectif souhaité**

Nous aimerions **remplacer ou enrichir ce message** afin de :

1. Indiquer **qu’un lien existe déjà** ;
2. **Rediriger l’utilisateur vers le record existant** (ajout d'un lien dans le message d'erreur).

###  **Notre question**

Avant d’implémenter cette logique, nous nous demandions quelle est la **meilleure pratique spécifique aux relations d’objet** dans Simplicité .
Y a-t-il un moyen natif de **surcharger le message système** lié à la cardinalité ? 
Hook spécifique ?

Merci d’avance pour vos retours et recommandations ! 

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
Bonjour,

[quote="Hamza, post:1, topic:11153"]
Creation limited for
[/quote]

C'est le libellé du texte statique générique `ERR_MAXLIMIT`.
Ensuite c'est suivi du nom de la relation et de la cardinalité maximale.

En terme d'UX il faudrait masquer le/les boutons "créer" si le max est déjà atteint :
- `initList` : `setListAccessNewForm` et/ou `setListAccessNewLine` si select count<1
- et/ou mettre une aide contextuelle sur la liste pour dire qu'il ne peut y en avoir qu'un s'il est déjà présent `setCtxHelp(ObjectCtxHelp.CTXHELP_PANELLIST, "Only one record is permitted")`

Sinon pour afficher autre chose au create, il faudra agir avant le save/create qui check les cardinalités : retourner votre message d'erreur spécifique au `pre/postValidate`, avec éventuellement un `Call to action` pour permettre à l'utilisateur d'ouvrir le record existant. En soit il a juste un clic à faire sur la liste donc c'est assez redondant.
