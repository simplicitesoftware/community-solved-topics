# API REST – Support de la clé fonctionnelle

**URL:** https://community.simplicite.io/t/11473

## Question
Bonjour,

Dans le cadre de l’exposition de nos objets métier via les API REST Simplicité, nous sommes aujourd’hui limités à l’utilisation du `row_id` comme identifiant technique dans les endpoints.

Or, pour certains objets métier, nous disposons d’une **clé fonctionnelle stable**, connue des systèmes consommateurs et déjà utilisée comme clé d’unicité métier.

Dans notre cas concret, nous avons l’objet **`LbcLegalText`**, dont la clé fonctionnelle est portée par l’attribut **`LegalTextId`**.

👉 **Besoin fonctionnel**

Permettre aux consommateurs de l’API de **retrouver, lire, mettre à jour ou supprimer une ressource directement à partir de sa clé fonctionnelle**, sans avoir à effectuer au préalable une recherche pour récupérer le `row_id`.

Cela permettrait d’exposer des endpoints plus lisibles et plus alignés avec le modèle métier, par exemple : functionalkey =legalTextId

```
GET /legalTexts/{functionalkey}
```

en + de :

```
GET /legalTexts/{row_id}
```

👉 **Question ouverte sur les possibilités Simplicité (choix d’implémentation)**

Nous avons identifié **deux approches possibles côté framework**, et souhaiterions avoir votre avis sur celle à privilégier, ou sur l’existence d’un mécanisme natif équivalent. 

**1️⃣ Approche “path param étendu”**

* Autoriser un endpoint du type :

```
GET /legalTexts/{functionalKey}
```

* Avec une résolution interne du `functionalKey` vers le `row_id` (via recherche sur la clé fonctionnelle).
* Le format pourrait être reconnu implicitement ou via une configuration spécifique au niveau de l’objet.Cette solution est dégradé (en réflexion, dans l'hypothèse qu'on saura patcher la requete).

**2️⃣ Approche via `URI_MAPPING` / routage personnalisé**

* Déclarer un mapping spécifique reconnaissant un format de path dédié
(ex : `/legalTexts/by-functional-key/{key}`)
* Déclencher automatiquement un `search` ou un `select` basé sur la clé fonctionnelle.



👉 **Points de réflexion complémentaires**

* **Objets avec plusieurs clés fonctionnelles** :
Existe-t-il une recommandation pour gérer ce cas de manière standard (mapping explicite, configuration par objet, priorité d’une clé) ?


* **Tables d’association exposées en API** :
pour les objets d’association, le `row_id` n’a généralement pas de sens métier et les clés sont souvent **composites**.
Dans notre cas, nous avons les objets `LegalText` et `Content`, liés via la table d’association `lbcLegalTextContent`, exposée en API.
Fonctionnellement, l’unicité d’un contenu n’est pas portée par un `contentId` technique (équivalent au `row_id`), mais par le **`LegalTextId` associé et la langue du contenu**.

Dans ce contexte, nous souhaiterions exposer l’association via une clé fonctionnelle composite dans l’API (par exemple) : {functionalkey} = {legalTextId} - {contentLanguage}

```
GET /legalContent/{functionalkey}
```

Existe-t-il des bonnes pratiques ou mécanismes recommandés dans Simplicité pour exposer ce type de **ressource d’association par clé fonctionnelle**, ou via des sous-ressources REST  ?

L’objectif n’est pas de remplacer le `row_id`, mais de **d'ajouter un accès REST plus métier et optionnel**, tout en restant compatible avec les standards Simplicité et les évolutions futures.

Merci d’avance pour votre retour et vos recommandations.

Cordialement,

## Answer
A la réflexion il semble plus cohérent de se s'appuyer de la notion existante de "permalinks" (introduite en v6). Pour rappel ce mécanisme sert pour gérer des liens directs vers les formulaires de la UI mais sa généralisation à la couche d'API pourrait être une bonne chose.

On va livrer dans le cadre de la 6.3.2 un 1er jet de ce que ça pourrait donner en se focalisant à ce stade **uniquement sur les APIs mappées**

Dans ce 1er jet on est soumis à **une contrainte de nommage forte** = il faut **impérativement** configurer le permalink de l'objet au format `/<nom mappé de l'objet>-[USERKEY]` (ce qui exclue mécaniquement des mappings sur plusieurs noms).

Par exemple sur la démo avec l'objet `DemoSupplier`, qui est mappé sur une API mappée en tant que `suppliers`, si on configure ce permalink:
![image|690x333](upload://dd96DjBFOpB4826TTeweBBjhNNP.png)
On a alors la possibilité d'accéder au record du supplier "BIM" via l'API mappée sur la clé `[USERKEY]` à savoir ici `bim` ou `BIM`(les permalinks sont case-insensitive)
![image|594x500](upload://eHPdz5DeaWWg8sY50XtmSNNVhXl.png)

A noter que la conversion générique des valeurs d'attributs en snake case utilisée par les permalinks a un effet sur certaines valeurs, ex: le `[USERKEY]` du produit "REF006" du fournisseur "LLED" donne `lled-ref-006` (à noter le `-` ajouté entre `ref`et `006`).

Si ça va dans le bon sens on verra pour faire évoluer ça vers plus de souplesse.
