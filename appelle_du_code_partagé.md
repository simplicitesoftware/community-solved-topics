# Appelle du code Partagé

**URL:** https://community.simplicite.io/t/9507

## Question
Bonjour,

j'essaye de de créer du code partagé afin de factoriser du code dans plusieurs object. J'ai deux questions :
- A quoi sert la partie "Utilisation code partagé" ?
- Faut-il que j'extends le code partagé dans chaque object qui l'utilise ou tout se fait à partir de la partie code partagé ?

Merci d 'avance

## Answer
Bonjour, 

Vous créez une méthode statique dans le code partagé. 
Vous devez définir autant de fonctions qu'il y a d'objets qui utilisent l'action. 
(L'action est lié à l'objet par la fonction.)
La méthode de l'action doit être dans chaque classe d'objets et appeler la méthode statique du code partagé.
