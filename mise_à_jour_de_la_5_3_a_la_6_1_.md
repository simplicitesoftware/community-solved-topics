# Mise à jour de la 5.3 a la 6.1?

**URL:** https://community.simplicite.io/t/9762

## Question
Bonjour,

Je dois mettre à jour mon instance de la version 5.3 a la version 6.1.27.
Dois-je passer par la version 6.0 (qui n'est plus maintenu) ou je peux passer directement en 6.1.27?

Je vous remercie par avance pour votre réponse.

## Answer
Nous garantissons qu'il soit toujours possible de passer de la v5 **à jour** (actuellement 5.3.66) à la v6 **à jour** (actuellement 6.2.6). Nous testons cette mise à jour à chaque release

Attention, ce test ne présume pas de vos implémentations particulières, donc comme pour tout changement de version majeure, vous devez consulter avec attention les releases notes v6.x pour vérifier que votre code v5 n'est pas impacté par les "compatibility breaking changes" induits par la v6

Tout autre cas de mise à jour n'est plus testé mais un passage de la v5 à jour (5.3.66) à la version mineure legacy 6.1 à jour (6.1.27) ne devrait normalement pas poser de problème

On considère que les versions mineures qui ne sont plus maintenues, comme la 6.0, n'existent plus et ne sont donc jamais un passage obligé pour upgrader depuis la version majeure précédente.

La vraie question est pourquoi visez vous la version mineure **legacy** 6.1 qui est désormais en toute fin de vie (fin de maintenance début mai) et pas directement la version mineure 6.2 qui est la version mineure **actuelle** de la v6 ?
