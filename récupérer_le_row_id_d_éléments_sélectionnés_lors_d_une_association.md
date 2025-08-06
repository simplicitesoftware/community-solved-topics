# Récupérer le row_id d'éléments sélectionnés lors d'une association

**URL:** https://community.simplicite.io/t/7480

## Question
Bonjour,
Meilleurs voeux pour 2024

Nous utilisons Simplicité 5.1.66.
Nous effectuons une associations entre deux tables (A et B) dans une troisième (la table C).

Au clic sur le bouton "Associer éléments", un ensemble d'éléments de la table A sont choisis, pour les associer avec des éléments de la table B.
Au sein de la table C, nous affichons cette association et souhaitons appliquer une méthode sur ces éléments associés. 

Pour se faire, nous avons besoin de récupérer le row_id des éléments de la table A sélectionner pour l'utiliser dans la méthode développée dans le code java de l'objet C.

Nous avons pensé récupérer l'instance de l'objet A en cours pour appliquer une méthode *getSelectedIds*. En vain.

Auriez-vous une façon de procéder à nous conseiller ?

Bien à vous,
VML

## Answer
[quote="victormehdileguet, post:6, topic:7480"]
méthode asynchrone que doit être appelée une seule fois, après la création de l’ensemble des C
[/quote]

Actuellement, l'associate revient conceptuellement à créer les NN en boucle à la main, c'est géré dans le front et non dans le back, et à ce titre, il n'y pas de hook `postAssociate`. 

Partant de ce constat, plusieurs options s'offrent à vous:
1. faire un workflow
2. coder en JS l'équivalent d'un associate, mais avec un appel final à l'action asynchrone
  > $ui.selectObject multiple de B
  > $ui.displayForm éventuel des valeurs par défaut des champs obligatoires de la NN
  > boucle ajax de create NN pour chaque B sélectionné
  > puis update ajax final…
3. **Revoir votre conception pour que votre algo de traitement postCréation soit unitaire**. Par curiosité, quels sont lea traitements qui sont réalisés uniquement dans le cas de l'association et non lors de la création de C par formulaire? ***(option conseillée!)***

----

Pour revenir à votre approche initiale, dans le cas étudié, **je pense que vous n'arrivez pas à récupérer les IDs car vous ne visez simplement pas la bonne instance de A (instance de sélection de références)** . En effet, en 5.3.25, j'ai bien la liste des IDs dans ce test:
- relation NN sur C configurée comme suit: **A <-- C --> B**
- étant sur B, dans le panel de C, je clique sur "Associate".
- je sélectionne dans la liste de "A" et clique sur "Select"
- dans le `postCreate` de C, je peux récupérer la liste des IDs de A via l'instance de sélection de références `getGrant().getRefObject("A").getSelectedIds()`

> **ATTENTION:** cette solution est donnée pour cesser de tergiverser et répondre à la question initiale, mais ce n'est probablement pas la bonne approche. Il reste en effet à répondre à la question de l'exécution de votre algo si l'utilisateur n'est pas passé par l'associate, mais que getSelectedIds n'est pas vide car il contient une sélection passée...
