# Modifier dynamiquement une zone de texte

**URL:** https://community.simplicite.io/t/4584

## Question
Bonjour,

J'ai une zone de texte comme ci-dessous :
![image|690x115](upload://1IR8ELwXSkWzHGGvKmLRRAs4mpw.png)

J'aimerais pouvoir modifier ce texte dynamiquement depuis le code en Java.

J'ai pu voir sur le forum que c'était assez peu pratique : https://community.simplicite.io/t/cacher-une-zone-de-texte-dans-un-hook/3073/5
Cependant ce topic date d'il y a un an.

Voici donc mes questions :
* **Est-il possible de modifier la zone de texte depuis le code en Java assez facilement (aussi facile que modifier un champ par exemple) ?**
* **Si ce n'est pas possible, serait-il possible d'avoir une documentation sur comment modifier dynamiquement le Template HTML via du JavaScript ?**

## Answer
[quote="Alistair, post:7, topic:4584"]
attribut non persisté
[/quote]

Oui, si le champ est read-only et de type HTML vous pouvez l'alimenter au postSelect.

```java
if (isMainInstance())
   selFieldValue("myTextField", "<p>contenu compliqué</p>");
```

Et on peut aussi n'afficher que la valeur (sans le label) dans le template editor.
data-display="input"

![image|283x314](upload://A4RnlsJzRrPBDkTyiBwSRyw2eb6.png)
