# Simplicité et les blocs synchronized

**URL:** https://community.simplicite.io/t/4937

## Question
Simplciité 5.1.44

Bonjour,

dans notre code, nous avons utilisé des blocs "synchronized" pour éviter 2 modifications concurrentes sur un même BO, par exemple :

```
  candidature.select(candidatureId)
  synchronized (candidature) { // thread-safe
                    candidature.setFieldValue("xx", "xx");
                    candidature.setFieldValue("yy", "yy");
                    candidature.update();
                }
```


Aujourd’hui on se rend compte que ces blocs sont un peu inutiles dans la mesure ou l'objectif d'architecture est d'avoir 4 instances simplicité différentes sur une même BDD.

On réfléchi aujourd'hui a sauter ses blocs synchronzied pour éviter des blocages inutile et on se pose donc la question de comment simplicité traite les accès concurrent sur un même record ?

Merci d'avance.

## Answer
Bonjour,

Il y a 2 sujets à mon avis vous les confondez :

### Thread safe

Il faut utiliser une synchronisation au sein d'une même session, c'est à dire que dans une même session/tomcat,  plusieurs threads peuvent accéder à une instance d'objet de l'utilisateur. Typiquement : un hook qui accède à une instance getTmpObject(), qui serait également utilisée par du code d'une action asynchrone lancée par ce même user en //.

Ce n'est donc en aucun cas une synchronisation de mise à jour pour tous les users. C'est purement un accès concurrent en mémoire de la session à cette instance particulière.

D'ailleurs en 5.2, la syntaxe est plutôt 
`synchronized (candidature.getLock())`
car il convient de poser un verrou sur un membre de l'objet, et non pas l'objet lui-même.

Si vous retirez le synchronized = il faut vous assurez que l'instance qui travaille est bien unique dans la session, du genre utiliser un 

`getGrant().getObject("MonInstanceParticuliereXYZ","MyObject")`

Là aucun autre thread (system, UI ou cron...) n'ira utiliser cette instance d'un nom inconnu.
Ce prendra juste plus de mémoire, alors qu'un synchronized permet de réutiliser l'instance, et dans des cas rares, faire patienter les accès d'une même session.

### Concurrence d'accès à un record

Que ce soit N serveurs, ou N sessions au sein d'un même serveur, c'est la même chose : c'est le mode de verrouillage logique via le **timestamp** qui est utilisé pour l'accès concurrent à un record.
- En mode bloquant, le verrou de celui qui utilise un record est stocké en base.
C'est donc couteux (timeout pour déverrouiller...) et à limiter aux objets "mono-user"
Sur le formulaire, l'utilisateur voit "qui" a ouvert l'objet et donc peut s'attendre à un accès concurrent, sauf s'il voit qu'il a l'icone "verrou" sur son avatar.
- En général on utilise un timestamp non-bloquant / controle de timestamp au save (updated_dt)
