# Debug du push GIT

**URL:** https://community.simplicite.io/t/10932

## Question
### Request description

Bonjour,
Nous avons un souci avec un push de module vers GIT qui affiche un succès mais n'est pas effectif (rien sur le GIT).
Les logs nous donnent peu d'informations.

Push "succès" non effectif
![image|690x33](upload://wvDi0vVD2eOkuhJ9VoKuxguvVZB.png)

Push effectif
![image|690x51](upload://mSulgQ20WCTLByHKbHuXdZ7RpbJ.png)

Pourriez-vous m'indiquer comment avoir plus d'informations sur ce qu'il se passe lors du push ?
L'instance est bien mise à jour mais pas l'origin.

Merci d'avance pour vos pistes
Emmanuelle

[Health check]
[Platform] Status=OK Version=6.2.17 BuiltOn=2025-10-02 18:05

## Answer
L'action _push_ est un push Git de base = la même chose que si on fait un `git push` manuel dans le repertoire Git du module (i.e. dans `/usr/local/tomcat/webapps/ROOT/WEB-INF/git/<nom du module>/` dans le container)

Ici j'ai l'impression que le push sur votre remote y force en fait la création d'un "merge request" ce qui n'est pas un mécanisme Git standard et donc quelque chose qui n'est pas géré par Simplicité (= vu de Simplicité le push est OK, on ne peut pas deviner que ce qui a été fait coté remote est en fait autre chose qu'un simple push)

Bref, plutôt que pousser directement sur votre remote depuis l'instance Simplicité je vous suggère donc de cloner le repo Git de l'instance localement, d'y puller vos commits et d'y faire les push vers votre remote, vous aurez alors plus de visibilité sur ce qui se passe effectivement du coté de votre remote
