# SetDefaultSearchSpec : implementation dans un plateformHooks

**URL:** https://community.simplicite.io/t/12244

## Question
Bonjour,

Suite à ma question d'hier :[Filtering d'objet selon l'utilisateur](https://community.simplicite.io/t/filtering-dobjet-selon-lutilisateur/12233) , je sais que je dois surcharger le `postLoad()` d'un objet pour faire un `setDefaultSearchSpec()` avec le bon filtre sql.

Maintenant, je souhaite faciliter l'implémentation en regroupant tout mon code dans un code partagé `plateformhooks` au lieu de surcharger tous les `postLoad()` des objets que je cherche à filtrer. J'ai besoin que le login de l'utilisateur soit disponible car le filtre le prend en compte. 
Quel `plateformhooks` devrais-je surcharger pour cela ?
Je commence à implémenter un test à partir du `postLoadGrant()` mais sans aucune certitude.

cordialement,

## Answer
Bonjour, 

Pour ce cas, vous pouvez créer une classe partagée qui hérite d’ `ObjectDB` puis faire hériter vos classes d’objet métier de cette classe partagée. 
`PlatformHooks` regroupe des hooks spécifiques à une plateforme, notamment l’initialisation, l’authentification et l’intégration de comportements propres.  https://docs.simplicite.io/docs/core/platform-hooks

Cordialement,
