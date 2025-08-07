# Comportement filtre is null différent de IS NULL sur un champs Date

**URL:** https://community.simplicite.io/t/5595

## Question
### Request description

Bonjour, 
comme indiqué dans le titre du topic, nous avons reçu des plaintes depuis mardi dernier concernant le comportement de l'utilisation du filtre *IS NULL* ayant changé alors que l'utilisation de *is null* nous retourne le bon résultat sur un champs de type Date.
D'après les personnes nous ayant déposé les plaintes, la valeur du champs en majuscule fonctionnait depuis plus de 6 mois et depuis mardi dernier cela ne fonctionne plus.

Pour tester, nous avons essayé de reproduire le test sur l'UI Simplicité ainsi que des appels APIs et le résultat est le même (la valeur en majuscule ne fonctionne pas alors qu'en minuscule cela fonctionne). Nous avons donc pointé du doigt un changement de version. Mais en ayant testé sur un environnement en 5.1.54 (application X) et un autre en 5.2.24 (application Y) et le résultat est une nouvelle fois pareil donc la potentielle cause a été écartée.

Ma question est donc la suivante: Y'a-t-il eu un changement quelconque pour avoir cette divergence en majuscule ou en minuscule sur une même valeur d'un champs de type Date au niveau Simplicité?

Merci d'avance

## Answer
Suite à analyse, cette syntaxe n'a jamais été supportée pour les dates, vous devez confondre avec autre chose ou un usage spécifique.

On a tout de même fait en sorte de gérer l'uppercase dans une prochaine livraison.

![image|690x152](upload://yf0DJnlepqKuFNSphq3XcXzClIY.png)
