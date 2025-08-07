# Popup de confirmation persistant

**URL:** https://community.simplicite.io/t/5645

## Question
Bonjour,
j'ai un bug apparu avec la version 5.2.25 (j’étais en 5.2.19 initialement), lorsque je clique sur une action, j’ai une popup qui s’ouvre et quand je clique sur “Confirmer”, la popup reste.

**Réponse de François**

Bug connu et corrigé suite à une évolution récente pour ne justement pas le fermer en cas d’erreur de l’action remontée par le back (avant il fallait du coup ressaisir les champs de confirmation).

Peux tu nous donner la définition de l’action et son code back pour analyse ?

* en back : est-ce qu’elle remonte quelque chose et pas null ou dans le genre ?
* en front : quelle est la réponse du call HTTP de l’action ?

Si le popup se ferme pas c’est que le front considère en retour qu’il y a encore qq chose à y faire (peut être à tord si la réponse est un faux positif non traité).

## Answer
[quote="khalil, post:2, topic:5645"]
`public List<String> applyProfilChange (Map<String, String> params)`
[/quote]

Une action remonte un String (un message, une erreur, null, un redirect , un javascript) mais jamais une liste.
Le front reçoit alors le toString de la liste (un tableau vide), et ne doit pas gérer ça comme une réponse OK pour fermer le dialog.

Retourne un String = null ou Message.formatSimpleInfo("Ok");

Ensuite tu peux utiliser directement l'Action en parametre plutôt qu'une Map.
pour accéder aux fields : action.getConfirmField pas forcement textuels
