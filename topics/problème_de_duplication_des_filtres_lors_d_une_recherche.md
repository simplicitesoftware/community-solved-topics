# Problème de "duplication" des filtres lors d'une recherche

**URL:** https://community.simplicite.io/t/11419

## Question
### Request description

Bonjour Je rencontre un problème lors de l’utilisation des filtres dans une recherche sur l’objet **SubPurposeTags**. Voici le contexte :

#### **Modèle de données :**

* J’ai trois objets manipulés : **FamilyTags**, **PurposeTags** et **SubPurposeTags**.

* Ces trois objets héritent tous de l’**objet LbcTags**.

* Une des propriétés de l’**objet LbcTags** est qu’il peut avoir un parent du même type (**LbcTags**).

* Dans mon cas, **SubPurposeTags** a comme parent **PurposeTags**, et **PurposeTags** a comme parent **FamilyTags**.

### Steps to reproduce

![ModelTags|690x492](upload://fqAbjiIokOVJmDZtRmZ86qOQ5RJ.svg)

### 

#### **Problème rencontré :**

Lorsque je fais une recherche sur l’**objet SubPurposeTags** et que je sélectionne un **PurposeTags** comme élément de filtre, je constate que les filtres sont dupliqués sur deux champs de l’**objet FamilyTags**. Cela fausse logiquement les résultats de la recherche.

NB: A l’inverse je ne constate pas ce comportement lorsque je sélectionne un **FamilyTags**

![image|690x179](upload://66dns6LxhcngADRqolfmiXsEeB6.png)

#### **Question :**

Est-ce un comportement attendu ou s’agit-il d’un bug ? Si c’est un comportement attendu, comment puis-je configurer mon modèle ou mes recherches pour éviter cette duplication des filtres et obtenir des résultats corrects ?

Merci d’avance pour votre aide et vos éclaircissements !

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.20
BuiltOn=2026-01-02 22:59
Git=6.2/247648a272030a5c6026aa4c146866d268d8b124


[Server]
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true

[JavaVM]
HeapFree=154732
HeapSize=462848
HeapMaxSize=4747264
TotalFreeSize=4439148

[Cache]
ObjectCache=281
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=0
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Healthcheck]
Date=2026-01-20 12:48:34
ElapsedTime=8
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

[quote="JordanSO, post:7, topic:11419"]
configuration qui me permettrait de retirer cette loupe
[/quote]

On ne peut pas sélectionner un objet si on n'a pas de droit de lecture sur cet objet lié.
Sinon ce n'est pas prévu côté front, car c'est sensé fonctionner si on a les droits.
Masquer ce bouton reste un contournement temporaire.

La fonction "loupe de recherche d'une référence" a changé de comportement en V6.3. Il est maintenant possible de choisir plusieurs références, et seul le champ recherché sera renseigné 
- par une égalité stricte ou un `in(...)`
- et non plus par la foreign-key + tous les champs liées, ce qui était ambiguë dans votre cas de lien réflexif sur 3 niveaux

On va backporter temporairement cette fonctionnalité en 6.2 mais toujours en "mono-sélection", ça devrait corriger votre problème.

__Note__ La 6.2 est désormais en maintenance court-terme, il va falloir envisager de passer en 6.3 LTS.
