# Mise en oeuvre du concept de "Notification" par un canal "Spécifique" configurant une méthode ad-hoc

**URL:** https://community.simplicite.io/t/9940

## Question
### Request description

*Bonjour, j'essaye sans succès de mettre en oeuvre le concept de "Notification" par un canal "Spécifique" configurant une méthode ad-hoc. Sur la base des éléments de configuration partagés ci-dessous, je n'arrive jamais à l'exécution de la méthode implémentée. J'ai testé la même configuration sur une 5.3, une 6.1 et une 6.2 "à jour". J'ai peut-être mal configuré les choses. Quoi qu'il en soit, ça ne fonctionne pas...*

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it: [https://bruno.renault2.simplicite.io/ui](Instance de démo sur sim2 Renault) -> user te00001 (mdp transmis par MP).*

1. un simple objet métier avec un seul champ text court comme clé fonctionnelle
2. deux notifications sur les événements de create/update configurées sur le canal "Spécifique" mentionnant la méthode "pushToDigitalBackBone"
3. implémentation de la méthode dans le code de l'objet (public String pushToDigitalBackBone() { ... }) -> ce code ne fait pour l'instant que loguer "Here we are" dans la log système...
4. créer / modifier des enregistrements dans l'objet test
5. rien dans la log (la méthode n'est pas exécutée)

J'ai tenté plusieurs interfaces pour la méthode, sans plus de succès (public String, public void, ... sans paramètre).


### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonjour Bruno, 

Il faut définir en paramètre de la méthode l'objet `Notification`

```java
public void pushToDigitalBackBone(Notification n) {
    // Récupérer l'objet qui a déclenché la notification :
    ObjectDB obj = n.getObject();
}
```

Le tutoriel + doc sur cette fonctionalité est en cours de rédaction.
