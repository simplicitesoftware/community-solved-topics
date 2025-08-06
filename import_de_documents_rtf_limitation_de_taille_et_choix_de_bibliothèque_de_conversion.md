# Import de documents RTF : Limitation de taille et choix de bibliothèque de conversion

**URL:** https://community.simplicite.io/t/8648

## Question
### Description

Bonjour,

Nous travaillons sur un projet où nous avons un cas d'utilisation nécessitant l'import de documents au format RTF. Nous avons remarqué qu'il est possible de contraindre l'import de RTF et de limiter le nombre de documents dans Simplicité. Cependant, il semble qu'il n'y ait pas de contrainte concernant la taille maximale des documents ( nous souhaiterions limiter la taille des fichiers à 50 MB maximum dans notre cas).
![Capture d'écran 2024-08-22 153004|690x172, 75%](upload://hXk0YW2L4UovKJfXtRn9Yk2pVcd.png)

Pourriez-vous nous indiquer s'il existe un moyen d'ajouter cette contrainte de taille dans Simplicité via l'interface ou bien dois-on passer par le code ?

De plus, en explorant les options disponibles pour parser des fichiers RTF et les convertir en HTML, nous avons identifié les bibliothèques **iText-RTF** et une librairie liée à **Tika-Parser** pouvez-vous nous aider à choisir la meilleur libraire pour ce use case, nous n'avons pas trouvé d'informations dans la documentation Java à ce sujet en v6.1.

Pourriez-vous nous conseiller sur la bibliothèque la plus pérenne et utile sur le long terme pour répondre à ce besoin ?

Merci d'avance pour votre aide.

## Answer
Bonjour

La limite d'upload est globale et positionnée par défaut à 100Mb (vous pouvez surcharger cette valeur selon votre besoin):

![image|690x311](upload://pUGlkVM1oIPwWoSHZvJKGbTFNdo.png)

**Attention** je précise qu'on parle bien ici d'une limite au niveau Simplicité, selon les installations/configurations de votre Tomcat et/ou de votre reverse proxy il se peut que des limites plus basses aient été configurées en amont de Simplicité auquel cas la limite définie au niveau Simplicité ne pourra pas être atteinte.

S'agissant de la conversion RTF => HTML nous n'avons aucune expérience sur ce genre de choses et ne pouvons donc pas trop vous conseiller sur quelle lib utiliser. 

NB: La lib iText que nous embarquons toujours actuellement est une version ancienne (la dernière avec une licence libre), nous envisageons de toute façon de supprimer cette lib obsolète à court terme au profit de l'outil PDFBox. Les versions plus récentes d'iText sont soumises à une licence d'utilisation commerciale que vous devez acquérir par ailleurs si vous souhaitez l'ajouter dans vos projets. Bref je pense qu'il vaut mieux vous orienter vers l'ajout d'une une autre solution (ex: https://github.com/bbottema/rtf-to-html)
