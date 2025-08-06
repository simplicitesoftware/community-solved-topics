# Peut-on créer plusieurs formulaires de façon dynamique?

**URL:** https://community.simplicite.io/t/9103

## Question
Bonjour,


Je vais essayer d'être clair :slight_smile:  :
Nous avons un objet métier "t_formulaire_enquete" dans lequel nous avons par exemple 40 objets. Un gestionnaire souhaite créer un ou plusieurs nouveaux formulaires en choisissant parmi les 40 objets ceux qu'il veut voir s'afficher puis il enregistre son choix ainsi qu'un nom.

Ensuite lorsqu'il est avec un client, depuis la vue de la fiche du client, il sélectionne le formulaire qu'il veut utiliser.

En espérant que j'ai été assez précis : Est-ce que c'est possible? 

A disposition pour plus de détails..

Merci

Fabrice Mouttet

## Answer
Bonjour Fabrice,

Comme tu le sais un objet Simplicité contient 
- des attributs stockés dans une table 
- et des relations vers d'autres objets. 

Donc effectivement il va falloir clarifier ton besoin qui ne semble pas standard mais réalisable.

[quote="fabrice, post:1, topic:9103"]
objet métier “t_formulaire_enquete”
[/quote]

ca ressemble pas trop à un nom d'objet métier mais plutôt à une table ?
je comprends que c'est un très "gros" objet à géométrie variable disons `FormulaireEnquete`

[quote="fabrice, post:1, topic:9103"]
dans lequel nous avons par exemple 40 objets
[/quote]

Tu veux dire que la table contient toutes les colonnes des "40 objets" ?
Peux-tu donner des exemples d'objets et leurs contenus ?
Les 40 objets sont définis par qui et comment ?

Dans simplicité soit on a des zones d'attributs pour grouper les champs d'un même objet, si ça contient des listes ce sont forcement des relations n,m. On peut inliner des champs dans le formulaire si la relation est 0,1 ou 1,1 (une seule référence).

[quote="fabrice, post:1, topic:9103"]
il enregistre son choix ainsi qu’un nom
[/quote]

Il faudra modéliser un objet `FormulaireEnqueteTemplate` avec un champ nom unique et qui contient un choix des "40 objets", donc à mon sens il faudra une relation N,N entre des zones d'attributs et le "template" (enfin si on parle d'attributs simples, sinon il faudra lier chaque champ ou chaque link nécessaire).

[quote="fabrice, post:1, topic:9103"]
il sélectionne le formulaire qu’il veut utiliser.
[/quote]

Si j'ai un peu compris il faudra :
- En création que le formulaire `FormulaireEnquete` à l'`initCreate` ne présente que le champ "Choisir un modèle/template" (relation vers un `FormulaireEnqueteTemplate` obligatoire) et les autres champs de clé fonctionnelle (date et numero d'enquete...), et surtout les "60 objets" sont masqués (les fields / areas / links à clarifier)
- Bouton "save"
- puis au rechargement en mise à jour, le hook `initUpdate` ira afficher et masquer les choses en fonction de la définition du template en base

Ca peut marcher si la table peut contenir toutes les colonnes de toutes les enquêtes possibles (combien au total ?), sinon il faudra envisager des objets liés en relation 0,1 au gros objet formulaire.


Autre approche, avoir des héritiers du gros objet plutôt que des templates, mais il faudra que l'admin sache utiliser les fonctions de designer pour se fabriquer ses propres objets Simplicité.
