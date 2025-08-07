# MAJ en masse problème de temps de chargement (objet rapporté / héritage)

**URL:** https://community.simplicite.io/t/5609

## Question
Bonjour,

Nous souhaitons mettre à disposition une limitation sur la fonctionnalité de modification en masse sur l'ensemble des objets auprès des utilisateurs de l’application.

Pour cela, nous utilisons le Hook preUpdateAll dans une classe commune qui, en fonction de l'utilisateur, instaure une limite avec un nombre de donnée modifiable specifique à chaque utilisateur (en utilisant "hasResponsability("...")).

Jusqu'ici tout allait bien pour l'ensemble des objets métier, la limitation se fait bien, une pop-up est directement retourné avec un message d'erreur (le return du preUpdateAll en l'occurrence, sauf pour un cas de figure.

Nous rencontrons un problème dans le cas d'un objet dont son code et son template sont hérité (l'objet métier n'a pas d'attribut d'objet à lui mais proviennent tous de l'objet hérité). 

Le problème ici est qu'il y a un temps de chargement plutôt long (de calcul des champs peut être ?) avant d'exécuter le preUpdateAll qui après un certain temps s'exécute bien et empêche la MAJ en masse si la limitation est dépassé (pop-up apparait et pas de modification). Cependant pour environs 1300 lignes sélectionnés il y a un temps de chargement d'environs 46s avant que la pop-up de restriction ne s'affiche à l'utilisateur (lui faisant croire probablement que la modification se fait, et je ne parle pas du cas où le nombre de ligne sélectionner est encore plus grand...).

*P.S. : Version=5.1.54*

Merci pour vos conseils.

Mounir

## Answer
[quote="Mounir_ELOUARIACHI, post:3, topic:5609"]
nb = search(false).size();
[/quote]

faites un simple `count()` qui fait un simple  "select count(*) ... where ...filters..."
car search(false) donc non paginé ramène toute la table en mémoire (une liste de `String[]`)
que comptez vous exactement ?
