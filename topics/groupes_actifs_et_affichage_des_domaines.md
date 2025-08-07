# Groupes actifs et affichage des Domaines

**URL:** https://community.simplicite.io/t/10216

## Question
### Request description

Bonjour,

Ceci est une question non urgente suite au déroulement du tuto Simplicité sur la 6.2.11.
Elle semble rejoindre la question posée [ici](https://community.simplicite.io/t/tutoriel-aide-au-demarrage/7569/5).

Le paramétrage du group actif sur la page d'accueil FormationScope semble désactiver l'accès au menu Mon Application.

Le menu Mon application est habilité au groupe TRN_SUPERADMIN
![image|448x299](upload://7pa75Y0JaD2x1pmG95qpH7Dv26v.png)
![image|236x500](upload://kTlpUN3X1rW3EVUGznaStTBpisY.png)

La home page a comme groupe assigné et comme groupe actif TRN_SUPERADMIN
![image|459x500](upload://eNEeEvtHaPZ9Twlvq9SGSZoav1t.png)

![image|421x500](upload://kPnQBJEGTCQXUfkvA3jPIIaQD5J.png)

Si je switch sur cette Home page
![image|565x500](upload://bTr08TPZxnrYc0N8AE07x3d8gME.png)

J'ai bien accès aux objets, mais plus au menu
![image|436x261](upload://zPbhHIK7SLd4fIkdBzP44MBml1I.png)

Si je supprime la ligne Groupe actif, je retrouve l'accès au menu
![image|435x292](upload://j4VOI381SvYWBCL2614YxN9EiB0.png)

Le tuto est déroulé sur l'instance mise à disposition https://hbrahamli.demo.simplicite.io/ui

A-t-on manqué quelque chose ?

Merci à vous !
Emmanuelle

## Answer
Bonjour Emmanuelle,

Il y a une nouvelle règle qui dit que si un domaine est tout seul dans le menu, il n'est plus affiché pour ne voir que ses items directement à la racine du menu.

Je ne sais pas si ça correspond à ton cas ?
