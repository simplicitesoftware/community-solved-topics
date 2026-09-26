# Document : Comportement des bibliothèques et stockage des attributs multi-documents

**URL:** https://community.simplicite.io/t/13245

## Question
### Request description

Bonjour,

Sur **Simplicité 6.3.15**, nous avons identifié deux comportements autour des attributs document. Nous souhaitons savoir s’il s’agit d’anomalies ou du fonctionnement attendu.

**1. Sélection de la bibliothèque associée à un attribut document**

Contexte :

* Objet métier : `DemoProduct`
* Attribut document : `demoPrdBrochure`
* Une bibliothèque `B-demoPrdBrochure` est créée automatiquement.
* Les bibliothèques supplémentaires utilisent le même objet et le même attribut métier.

Scénario observé :

1. Un document est ajouté dans l’attribut `demoPrdBrochure`.
2. Il apparaît dans la bibliothèque initiale.
3. Nous créons manuellement une deuxième bibliothèque, `DemoSecond`, associée au même attribut.
4. Les documents apparaissent alors dans cette nouvelle bibliothèque.
5. Nous supprimons `DemoSecond` : le document se retrouve temporairement sans bibliothèque.
6. Nous créons manuellement une troisième bibliothèque : le document existant y apparaît.
7. Si nous ajoutons ensuite un nouveau document depuis l’attribut métier, celui-ci apparaît dans la première bibliothèque automatique et non dans la dernière bibliothèque créée.

Questions :

* Peut-on officiellement associer plusieurs bibliothèques au même attribut, ou faut-il n’en conserver qu’une seule ?
* Si plusieurs bibliothèques sont supportées, comment Simplicité choisit-il celle qui reçoit les nouveaux documents ?
* Le comportement observé après la suppression et la recréation d’une bibliothèque est-il normal ou s’agit-il d’une anomalie ?



 **2. Stockage SQL d’un attribut multi-document**

Constat reproductible sur le même attribut `demoPrdBrochure` :

* Avec l’affichage **document unique**, le `doc_id` est enregistré dans la colonne `prd_brochure`.
![image|598x152, 50%](upload://elagRxfzM73uiwKfSz02UWqkvDg.png)

* En changeant uniquement l’affichage du même attribut vers **multi-documents** (liste ou miniatures), la colonne devient vide,
![image|495x217, 50%](upload://27SLraCsWZ4GCi8zhwYtJOF1k8a.png)
![image|616x439, 50%](upload://n2gfVC92iAVGmdYPqFH9JlPYCLe.png)
 même si les documents restent accessibles dans `m_document`.

Est-ce le comportement attendu ou une anomalie ? Pourquoi les identifiants ne sont-ils pas enregistrés sous la forme `doc_id1;doc_id2`, comme pour une énumération multiple ? Quelle est la méthode pour récupérer les documents associés à un attribut multidoc ?

Je sais que cela fait beaucoup de questions pour un seul post, mais comme les deux sujets concernent directement les attributs document et les bibliothèques associées, je préfère tout centraliser ici 🙂 

Merci d’avance pour vos éclaircissements.

## Answer
_No answer provided._
