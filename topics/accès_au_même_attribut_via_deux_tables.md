# Accès au même attribut via deux tables

**URL:** https://community.simplicite.io/t/6320

## Question
Bonjour,  

Suite à une montée en version en 5.2, beaucoup d’erreurs sur les clés étrangères sont ressorties (comme dit dans votre documentation sur la complétude des 
clés étrangères en version 5.2).
Pour notre projet il est important d’avoir la possibilité d’accéder à un même attribut via deux tables différentes (chemins jaune et vert, cf image 1).


![Capture52|690x409](upload://amddpMnY6XMVV37zZGYaFcMuOhQ.png)


Cependant, lorsque j’essaye d’appliquer les méthodes que j’ai cru tirer de la documentation, pour implémenter le chemin jaune, la solution simplicité me sort
 l’erreur (cf image 2), savez vous comment résoudre ce problème et pourquoi l’erreur apparait ?
![Capture53|533x168](upload://rak2DEU40bbuQ8zZyOIqbTGC8D3.png)

Merci d'avance

## Answer
Bonjour, 

Vu que vous empruntez 2 chemins différents pour récupérer le libellé de la région `namRegLibelleRegion` il devrait appraitre 2 fois dans l'objet  `NamCommune`

Dans capture d'écran, l'attribut est ramené via `namDepRegId` soit le chemin jaune.

Il manque donc l'attribut ramené via `namComDepId`

Difficile de vous aider d'avantage au vu des éléments que vous nous fournissez.
