# Modification de la façon d'exporter

**URL:** https://community.simplicite.io/t/9480

## Question
Bonjour,
J'aimerais savoir s'il est possible de modifier les possibilités d'export par exemple ne pouvoir exporter qu'en fichier excel sur un type d'objet.
Et en plus de ça j'aimerais savoir s'il est possible de rajouter un role pour ne l'autoriser qu'à certaine personne.

Merci d'avance pour votre réponse

## Answer
Une solution est de créer un code partagé 

````
public class MyObjectDB extends com.simplicite.util.ObjectDB
````
 implémentant les hooks partagés et de faire hériter vos objets de cette classe.
