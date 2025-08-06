# Comment rendre un bouton non-cliquable en JavaScript de manière persistante?

**URL:** https://community.simplicite.io/t/5966

## Question
Bonjour,

Je suis actuellement confronté à un problème avec un bouton (action). Je souhaite rendre ce bouton non cliquable à l'aide d'un script JavaScript qui désactive le bouton en utilisant la propriété "disabled" selon le profil. De la manière suivante je réussi à rendre le bouton non clickable : 

> if(app.grant.responsibilities.includes('...Profil...')){
>    button.disabled = true;".
> }

Cependant, j'ai remarqué que le script ne s'exécute qu'une seule fois, au chargement de la page. Lorsque je rafraîchis la donnée, le bouton redevient cliquable car le script n'est pas réexécuté. Je suis donc à la recherche d'une solution pour rendre ce bouton non cliquable même après un rafraîchissement de donnée (via le fil d'Ariane par exemple).

Je suis ouvert à toutes vos suggestions et je vous remercie d'avance pour votre aide.

Mounir


> [Platform]
> Status=OK
> Version=5.2.31
> BuiltOn=2023-02-09 18:48
> Git=5.2/***********************
> Encoding=UTF-8
> EndpointIP=10.144.56.222
> EndpointURL=http://*********************
> TimeZone=Europe/Paris
> SystemDate=2023-03-01 17:07:05

## Answer
Où est affiché sur le bouton d'action ? Sur la liste ou formulaire ?

Dans mon exemple, c'est le hook onload du formulaire qui est implémenté, il est donc exécuté à chaque affichage du formulaire de l'objet - c'est donc applicable à un bouton sur formulaire.
[quote="Alistair, post:6, topic:5966"]
```
p.form.onload = function(ctn, obj, params) {
				var disabled = !app.getGrant().hasResponsibility("DEMO_ADMIN")
				$('[data-action="DEMO_INCSTOCK"]').prop("disabled", disabled); // Increase stock button disabled for users not in DEMO_ADMIN Group 
			};
```
[/quote]

Si votre bouton est affiché en liste, il faut implémenter le hook onload de la liste.

```javascript 
p.list.onload = function(ctn, obj, params){
	...	
}
```
