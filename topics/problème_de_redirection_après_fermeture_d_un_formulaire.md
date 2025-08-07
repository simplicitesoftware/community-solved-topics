# Problème de redirection après fermeture d'un formulaire

**URL:** https://community.simplicite.io/t/5800

## Question
### Request description

Bonjour à tous,

Je rencontre un problème de redirection lorsque j'utilise la barre de recherche de mon application. Lorsque je tape une référence, le formulaire de la référence s'ouvre comme prévu. Cependant, lorsque je clique sur le bouton "fermer" pour fermer ce formulaire, je suis redirigé vers la page d'accueil plutôt que vers la liste des références.

Je souhaiterais savoir s'il était possible que, lorsque je clique sur le bouton "fermer" du formulaire de la référence, je sois redirigé vers la liste des références afin de pouvoir continuer à naviguer.

### Steps to reproduce

1. Nous avons sur la page d'accueil une barre de recherche pour trouver une référence, on entre une référence et on tape sur la touche "entrer"

2.Voici la capture d'écran de la page du formulaire vers laquelle je suis redirigé. Quand je clique sur le bouton "Fermer", je suis alors redirigé vers la page d'accueil. 
![image|690x372](upload://mgFHpvwwxrpEjRD6u1xZfo55VIZ.png)


3. Voici la capture d'écran de la page contenant la liste des références vers laquelle j'aimerais être redirigé après avoir cliquer sur le bouton "fermer" du formulaire.
![image|690x333](upload://6MiEAdHzDJ9pscQBdVLIWIwqcFW.png)


Auriez-vous des suggestions pour résoudre ce problème de redirection ?

Merci d'avance pour votre aide.

Cordialement,
Elyass

### Technical information
[Health check]

[Platform] 
Status=OK 
Version=5.1.54
BuiltOn=2022-10-31 15:49 
Git=5.1/06cc2793ebaaa50ddf3f3dee2251b397d7bdc09b 
Encoding=UTF-8 
EndpointIP=172.20.112.121 
EndpointURL=http://mla-api-58c6f4c4db-tqsrb:8080 
TimeZone=Europe/Paris 
SystemDate=2023-01-27 15:42:17

## Answer
Tu peux aussi utiliser le hook front `onclose`

```
p.form.onclose = function(ctn, obj) {
	$ui.displayList(ctn, "MyObject", {nav:'add'});
}
