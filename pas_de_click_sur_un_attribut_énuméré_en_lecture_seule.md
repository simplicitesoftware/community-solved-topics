# Pas de 'click' sur un attribut énuméré en lecture seule

**URL:** https://community.simplicite.io/t/5157

## Question
Bonjour,
Je souhaite ajouter du code JS sur le click de certains attributs qui sont en lectures seules.
J’arrive à le faire sur les attributs décimaux (exemple ci-dessous : Solde dû) ou textes :
 
![image|690x116](upload://nqkhdPy3ARNxhBTxrkfbgheYEcy.png)

Mais je n’arrive pas avec un attribut énuméré (exemple ci-dessous : Documents complets), je n’ai pas de click sur ce champ :

![image|690x122](upload://dHsVxzsOv4flfmWn9hHTGxmZihP.png)
 
 Est-ce normal ? comment le contourner ?

Merci d’avance pour votre aide,
Abed.


[Platform]
Status=OK
Version=5.2.11
BuiltOn=2022-07-22 22:18
Git=5.2/bc1f6e720f5df119336af65fa1b502bd40ac47d4
Encoding=UTF-8
EndpointIP=149.202.173.228
EndpointURL=http://e3m.simplicite.io:10118
TimeZone=Europe/Paris
SystemDate=2022-08-17 10:53:34

## Answer
Visiblement le `click` n'est pas implémenté sur le un UIField select2...

J'ai réussi à contourner le problème en bindant le click sur la div qui porte la select2

```javascript
$("[data-field='myField']").on('click', function () {
    //do something
});	                
```
