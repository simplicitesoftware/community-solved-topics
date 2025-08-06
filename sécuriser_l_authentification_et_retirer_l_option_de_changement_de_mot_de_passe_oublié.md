# Sécuriser l'authentification et retirer l'option de changement de mot de passe oublié

**URL:** https://community.simplicite.io/t/6804

## Question
### Request description

Bonjour, nous souhaiterions pouvoir augmenter la sécurité lors de la connexion à l'application.

Actuellement, nous avons deux possibilités, une authentification interne (OpenID Connect), et l'authentification basique provider internal.

Le souhait, serait de ne laisser la possibilité qu'au profil "designer", de pouvoir s'authentifier avec un password, suivi d'un code unique MFA. Pour ce faire, nous avons fait un test en supprimant les passwords de chaque utilisateur, et en surchargeant :

```
@Override
public String generatePassword(Grant sys) {
	return null;
}
```

L'approche entreprise est elle correcte ?

Nous avons remarqué la nécessité d'inhiber la fonctionnalité de password oublié :

![image|348x175](upload://13XTzZJCvfks6zlhkQkZLEdmJVT.png)

Existe-t-il un moyen de le faire, pour empêcher quelqu'un de pouvoir redéfinir un password ?

Merci d'avance pour vos réponses,

Benoît 

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.11
BuiltOn=2023-08-07 15:27
Git=5.3/015368bc51913a479e8d682d65ea405c12b45951
Encoding=UTF-8
EndpointIP=xxx
EndpointURL=xxx
TimeZone=Europe/Paris
SystemDate=2023-08-24 11:06:06
```
[/details]

## Answer
Bonjour,

[quote="Benoit, post:1, topic:6804"]
`generatePassword null`
[/quote]

- null ou "" ne passera pas la validation du mot de passe par défaut (de mémoire minimum 8 chars)
- il faut plutôt gérer un mot de passe dédié/identifiable (genre forcer "NOPWD") et donc surement revoir le hook suivant pour dire ok si égal "NOPWD", ou retourner une erreur au logon... :

`public List<String> validatePassword(Grant g, String password)`

[quote="Benoit, post:1, topic:6804"]
désactiver password oublié
[/quote]

On peut désactiver l'option via le paramètre système :

`USE_FORGOT_PWD = no`
