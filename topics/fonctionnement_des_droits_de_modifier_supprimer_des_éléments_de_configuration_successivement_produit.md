# Fonctionnement des droits de modifier/supprimer des éléments de configuration successivement produits par plusieurs développeurs

**URL:** https://community.simplicite.io/t/3312

## Question
Bonjour,

le problème que je rencontre est peut-être lié à nos mauvaises pratiques antérieures (dont l'usage du user designer pour développer) mais je constate que depuis l'upgrade en v5 d'une instance, je n'ai plus la main sur les éléments de configuration réalisés par un ancien membre de l'équipe qui est parti depuis.
La seule solution que j'ai trouvée consiste à forcer en base un UPDATE de la colonne created_by de tous les records associés à son login (ou au user designer)  avec mon propre login.

Ce problème n'est évidemment pas rencontré si je suis loggué en tant que designer mais uniquement lorsque je me connecte avec mon propre login.

Ce n'est a priori pas un problème d'habilitation (j'ai les responsabilités  ADMIN, APP_ADMIN, APP_DESIGNER et DESIGNER ainsi que le paramètre utilisateur ADMIN_SYSTEM=yes et pas de MODULE_FILTER positionné).

Comment est-ce censé fonctionner ? (notamment en cas de turnover dans l'équipe)

## Answer
Une règle de visibilité est soit une search-spec, soit un accès limité à create/update/delete associé à une fonction CRUD de groupe. On s'en sert peu car on préfère souvent coder les search-spec ou les isUpdateEnabled...

Si vous avez mélangé du paramétrage fait par un designer de ADMIN, c'est normal que quelqu'un de APP_DESIGNER ne puissent pas y toucher (cf visibilité des fonctions de ce groupe sur Update et Delete).

- Retire tous les groupes à scope réduit de ton user sauf ADMIN. 
- ou alors (XOR) ne met que APP_DESIGNER = on ne peut modifier ou supprimer qu'une entité créée par quelqu'un de APP_DESIGNER = dans ce cas il faut remettre tous les created_by de votre module sur qq'un de ce groupe

L'option 1) est plus simple si vous avez changé de stratégie en cours de route.
