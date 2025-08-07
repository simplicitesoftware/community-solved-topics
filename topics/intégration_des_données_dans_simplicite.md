# Intégration des données dans Simplicite

**URL:** https://community.simplicite.io/t/5771

## Question
### Request description
Bonjour,
je vous contacte par rapport à une étude en cours chez nous par rapport à une refonte du processus d'intégration de données à partir des sources diverses.
Nous avons plusieurs questions en rapport avec cette étude.

Une des solution serait de faire alimenter directement la base de données par un ETL externe à Simplicite. D'un point de vue éditeur:

* Est ce que ce type de solution est envisageable ou est ce que ça risque de causer des dysfonctionnements dans le fonctionnement de l'outil?
* D'un point de vue contractuel, est ce que ce type de solution entre en conflit avec le contrat de support existant avec le client?
* Est ce une démarche que vous avez déjà eu à accompagner avec d'autres clients?

J'ai une question supplémentaire.
existe il des interfaces permettant de faire de l'intégration de données en mode bulk dans Simplicite?

Merci de votre support.

Thierry BALLA
*----description of the request----*

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
Alimenter directement la base (quel que soit la manière pour le faire) a l'inconvénient majeur de zapper la couche logique qui, en général, porte les règles de format et de métier (ex: contrôle d'unicité de la clé fonctionnelle, des regex des chaines de caractères, droits, ...) => autrement dit ne pas passer par la couche logique Simplicité vous impose de réécrire toutes ces règles avec les tous les risques que ça comporte, ex: régles incohérentes, régles manquantes, etc.

Il faut aussi veiller à gérer correctement les row ID (notamment vs les séquences associées).

Bref c'est toujours possible mais ce n'est, en général, pas une bonne idée. Sauf éventuellement si on part dans une logique d'accès direct ou de recopie base à base et donc du paramétrage d'objets tapant directement sur les tables de ces bases externes => les objets Simplicité ne correspondent pas forcément aux tables de sa base par défaut. Pour que ça soit envisageable il faut bien entendu avoir des bases de données structurées d'une manière la plus compatible possible avec les principes de Simplicité (i.e. des schemas de base de données pas trop dénormalisés)

En tout cas la manière dont vous chargez vos données n'a pas d'impact contractuel mais ça risque juste de compliquer notre support car cas d'anomalie applicative subtile => on ne pourra pas vous aider sur la partie d'intelligence que vous aurez déporté dans vos processus d'import et l'analyse d'éventuels dysfonctionnements induits au niveau des objets métier ne seront pas forcément évidents à comprendre.

Sur la question:
> existe il des interfaces permettant de faire de l’intégration de données en mode bulk dans Simplicite?

Les modes d'import en masse sont les imports sur le endpoint I/O : soit dans le format historique natif (XML) soit via les adapters standards (JSON, CSV, ...), soit via vos adapters customs. Ces imports passant par les couches logiques 

En conclusion:

Je ne sais pas quels sont les problèmes qui vous amènent à vous poser la question d'éventuels imports "bas niveau" mais je pense que ça vaudrait le coup de prendre du recul pour voir ce qui pourrait être optimisé :
- dans la stratégie d'import:
  -  faire des imports en delta plutôt que du full,
  - faire du fil de l'eau plutôt que du batch,
  - changer de source de données physique si la source est lente (ex: si une base de données distante est très lente à requêter, il peut être plus efficace d'en extraire un fichier CSV et de l'importer via adapter fichier)
  - etc.
- et/ou dans l'optimisation de vos adapters si c'est ce que vous faites (ex: optimiser les paginations de requêtage, cacher en mémoire des données réutilisées fréquemment lors de l'import, etc.)
- et/ou dans l'application de certaines règles couteuses (si vous avez confiance dans la source de données il est possible de "zapper" certains contrôles inutiles = typiquement ne pas passer par le `validate` ou inhiber certaines règles spécifiques codées dans les `pre/postValidate`, etc..)
- etc.

Sans infos précises sur ce qui pose pb, c'est difficile de vous faire des préconisations sur ce qu'il conviendrait de faire
