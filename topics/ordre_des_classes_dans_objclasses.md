# Ordre des classes dans OBJCLASSES

**URL:** https://community.simplicite.io/t/12301

## Question
### Request description

Bonjour,
J'ai un souci que je n'arrive pas à analyser avec des classes JS héritées.

J'ai 3 objets SELECT avec chacun une ressource JS de nom CLASS.
Les 3 héritent d'une classe JS commune.

Dans la ressource générée OBJCLASSES, j'ai une erreur sur une d'entre elles (la dernière créée) :

```Uncaught TypeError: Class extends value undefined is not a constructor or null```

![image|690x133](upload://mkruhnxNqhgrGjiFctNqYv7sJxM.png)

J'ai l'impression que c'est un problème d'ordre d'écriture dans le fichier JS, car les deux autres classes héritées apparaîssent après celle du père et n'ont pas l'erreur.

Quel est le critère de tri des classes dans le fichier ?

Merci pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.9
Variant=full
BuiltOn=2026-05-08 12:11

## Answer
A la relecture, l'algo exporte bien pour chaque objet l'ordre topologique, des parents aux enfants.

L'algo se base sur les `getObjectLocation(name)` construit à partir de la définition des objets donc de l'héritage déclaré dans l'object internal (et donc pas issu du code java ou js).

Sinon si tu ne veux pas d'héritage fonctionnel mais que technique, il faudra essayer de déclarer la classe JS parente comme un shared script / JS partagé.
