# Ajout objet métier dans vue

**URL:** https://community.simplicite.io/t/3261

## Question
Bonjour,

Actuellement nous rencontrons le problème suivant : 

Nous avons une page d'accueil qui pointe sur une vue, elle-même composé d'un objet externe et d'une recherche sur un objet métier standard.

Lorsque nous accédons à l'objet métier via le burger menu, aucun problème, par contre lorsque nous cliquons sur une ligne de la liste via la page d’accueil nous avons systématiquement le message aucun résultat à la recherche, uniquement la première fois. Les autres fois marche sans aucun problème.

Après vérification le code ne semble pas en être la cause.

De ce fait, quelle est la bonne pratique pour intégrer un objet métier dans une vue ?

Actuellement nous avons une 'Recherche' avec l'utilisateur Designer, et le filtre egal à : {}, avec le réglage public sur 'oui'. 

Merci d'avance,

Benoît

## Answer
Qu'entendez vous par burger menu ?
NO_ROW_FOUND indique que le select du row_id n'a rien ramené : problème de droit ou de filtres.

L'instance d'objet d'une page d'accueil est particulière, son nom est "home_ajax_xxx" afin de pouvoir spécialiser son comportement, il n'y a rien d'autre de particulier :
- quand on clique sur une ligne de cette recherche cela ouvre l'instance main "the_ajax_xxx" sur le row_id sélectionné
- exactement comme si on cliquait sur la liste de l'objet (via le menu principal qui travaille déjà sur the_ajax_xxx).

Vous devez avec un filtre ou une search-spec mal positionnée sur votre objet ou certaines instances.
Vous pouvez debugger le select qui ne ramène rien en activant les traces LOG_SQL_USER=yes.
Vous verrez le "where" qui filtre trop strictement, et remonter à votre code ou paramétrage qui le positionne.
