# Les appels POST sur les API mappées (RESTMappedObject) n'exécutent pas le hook initCreate

**URL:** https://community.simplicite.io/t/3539

## Question
Bonjour,

Version=4.0.P25
BuiltOn=2021-06-22 18:31 (revision 2f12327fd6f2e0e735a1c1fa852147d8f6006fa8)

Il semble que le hook initCreate ne soit plus exécuté dans le cadre des appels POST sur les API mappées. La création est néanmoins réalisée (mais il manque l'application des règles définies dans l'initCreate).

Dans le cadre d'une création va la UI, le hook est bien exécuté.

## Answer
Merci beaucoup pour ce refresh... en effet, depuis ma formation en 2017, j'ai largement eu le temps de "corrompre" ce dont j'ai pu me souvenir... le passage en revue de tous les initXXX sera l'occasion de remettre les éventuelles règles "hors la loi" dans le droit chemin.
