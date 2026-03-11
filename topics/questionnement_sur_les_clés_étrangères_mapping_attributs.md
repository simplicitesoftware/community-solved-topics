# Questionnement sur les clés étrangères, mapping, attributs

**URL:** https://community.simplicite.io/t/6310

## Question
Bonjour,

Suite à une montée en version en 5.2, beaucoup d'erreurs sur les clés étrangères sont ressorties (comme dit dans votre documentation sur la complétude des clés étrangères en version 5.2).

**Après lecture de la documentation et du training**, j'ai plusieurs questions :

- Tout d'abord, je ne comprends pas très bien la différence entre les attributs et les attributs d'objet. Est ce le fait que l'attribut objet est un attribut associé à un objet ? Si oui, qu'est ce qu'un attribut non associé à un objet ?

- Deuxièmement, pouvez vous m'expliquer plus en détail la notion de mapping et à quel moment faut il l'utiliser ?

- Troisièmement, pour une clé étrangère (cf première image), la bonne méthode est bien de créer l'attribut objet (trnSupName) dans TrnProduct avec pour champs référence (trnPrdSupId) et avec comme objet lié TrnSupplier ?

![Capture51|690x425](upload://ZIInFVXnK02qgRK1Bst8hY5S7B.png)



- Enfin, pour notre projet il est important d'avoir la possibilité d'accéder à un même attribut via deux tables différentes (chemins jaune et vert, cf image2).

![Capture52|690x409](upload://amddpMnY6XMVV37zZGYaFcMuOhQ.png)


 Cependant, lorsque j'essaye d'appliquer les méthodes que j'ai cru tirer de la documentation, pour implémenter le chemin jaune, la solution simplicité me sort l'erreur (cf image 3), savez vous comment résoudre ce problème et pourquoi l'erreur apparait ?
![Capture53|533x168](upload://rak2DEU40bbuQ8zZyOIqbTGC8D3.png)


Merci d'avance

## Answer
Bonjour, 

Pour ne pas mélanger les sujets, merci de créer un autre post pour votre sujet "implémenter le chemin jaune".

[quote="OumamaK, post:1, topic:6310"]
Tout d’abord, je ne comprends pas très bien la différence entre les attributs et les attributs d’objet. Est ce le fait que l’attribut objet est un attribut associé à un objet ? Si oui, qu’est ce qu’un attribut non associé à un objet ?
[/quote]

Comme indiqué dans la [documentation](https://docs2.simplicite.io/lesson/tutorial/configuration/attribute) : l'objet Attribut d'objet est un objet du méta-modèle Simplicité qui représente la relation **N-N entre un Objet métier et un Attribut**. Un Attribut peut être associé à d'autres objets du méta-modèle (Process, Action, Timesheet, Agenda, etc.)

[quote="OumamaK, post:1, topic:6310"]
Deuxièmement, pouvez vous m’expliquer plus en détail la notion de mapping et à quel moment faut il l’utiliser ?
[/quote]

Si vous parlez du mapping de relation, il existe un exemple dans le module Demo qui permet, dans l'objet Contact de filtrer la liste des Commandes du Client sélectionné.

[quote="OumamaK, post:1, topic:6310"]
Troisièmement, pour une clé étrangère (cf première image), la bonne méthode est bien de créer l’attribut objet (trnSupName) dans TrnProduct avec pour champs référence (trnPrdSupId) et avec comme objet lié TrnSupplier ?
[/quote]
Je vous incite fortement à passer par le **template editor** ou via le **modeler** pour créer vos relations et non à le faire manuellement en créant un élément dans la liste des Attributs d'objets.
