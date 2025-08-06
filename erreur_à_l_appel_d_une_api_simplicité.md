# Erreur à l'appel d'une API Simplicité

**URL:** https://community.simplicite.io/t/4565

## Question
### Request description

Bonjour,

Nous rencontrons récemment une erreur à l'appel d'une API. L'appel fonctionne via l'interface /api de Simplicité mais en ligne de commande j'ai l'erreur suivante :

Cannot read field "m_objects" because "this.m_data" is null

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and those are the steps to reproduce it:*

1. Ouvrir un CMD
2. Obtenir un token curl -s -k -u <login>:<mdp> "<URL>/login?_output=json"
3. Appeler l'API curl -X GET "<URL>" -H "Authorization: Bearer <TOKEN>"

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=4.0.P25
BuiltOn=2022-02-22 00:16 (revision 39f36d20ad611794a99815948a8f09f3bd7c4e19)
```
[/details]

[details="Simplicité logs"]
```text
Pas d'erreur dans les logs.
```
[/details]

## Answer
Commencez par un clear cache global et/ou un stop/start histoire d'être sûr que ce n'est pas un effet de cache. Dans mes tests sur mon API custom de test je n'ai pas constaté de pb de cet ordre mais on ne sait jamais d'autant que vous n'êtes à priori pas parfaitement à jour.

Ensuite je ne vois pas de raison qu'un appel depuis la page API tester ou depuis un `curl` se comportent différemment (en tout cas si les deux sont bien effectués avec le même user et depuis la même machine cliente et sur la même URL). Pendant mes tests j'ai fait les deux sans pb sur mon API custom de test (ici avec le même token):

![image|690x323](upload://5c3yu4lqqHZsgywlJXtnycNqxB6.png)
![image|690x104](upload://qlMIV5m5sTsgmZ5Xqq9La9wUON1.png)

Vous pouvez tester sur l'instance en question si besoin, elle est encore active: https://testdaz40.demo.simplicite.io designer/simplicite

Pour ce qui est de débugger au niveau où l'appel à la méthode `get` est effectué, ce n'est pas possible car on est dans les classes système et il n'y a pas de log events pour augmenter le niveau de trace.
