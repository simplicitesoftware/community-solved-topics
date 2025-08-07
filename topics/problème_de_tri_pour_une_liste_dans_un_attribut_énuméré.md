# Problème de tri pour une liste dans un attribut énuméré

**URL:** https://community.simplicite.io/t/9266

## Question
### Request description

Bonjour,je rencontre un souci avec un attribut de type "Enuméré multiple" dans mon module. Voici le contexte :

### Steps to reproduce

1. **Liste de valeurs utilisée** : `LBC_LIST_COUNTRY`, qui contient les pays triés par code.
![image|657x499, 50%](upload://7ooJnodV8nVctoTUlO74mo02ovQ.png)



2. **Comportement attendu** : En vue de liste, je voudrais afficher tous les pays triés par **ordre** dans l'ordre croissant, sans distinction.
3. **Comportement actuel** :Liste pas dans l'ordre établi
![image|152x347, 50%](upload://bSoXi1Oo6WT2YlGUYazViJhw05I.png)


  * Les pays importateurs (provenant de `LBC_LIST_COUNTRY_IMPORTER`) s'affichent en premier.
  * Ensuite, les pays filiales (provenant de `LBC_LIST_COUNTRY_SUBSIDIARY`) apparaissent, mais l'ordre global n'est pas respecté.

Cela vient peut etre du fais que l'attribut legaltextGeographicalZone est set de base sur la liste de valeur `LBC_LIST_COUNTRY` mais dans notre processus métier en fonction d'un autre attribut, la liste est updaté dans le processus métier soit par la liste de pays filiales ou importateurs. Et au final cela se traduit par l'affichage de ses lignes en sommes pour les valeurs 
![image|690x102, 75%](upload://qafford4HoTpicpnUxRyLyakBf4.png).

J'ai aussi essayé de voir dans le hook initlist les logs concernant le nom de la liste et les valeurs mais c'est bien la liste global qui est sur cette attribut. 

J'ai essayé, de voir au niveau des parametre de tri de la liste mais rien de change.
J'utilise aussi cette liste dans un autre objet 'utilisateur' et je n'ai pas ce conflit la liste est bien trié par ordre.
![image|427x353, 50%](upload://g8hE38AP0m2UUdxn5pvK4tdQv1j.png)




### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```
[/details]

[details="Simplicité logs"]
```text
---
2024-12-18 11:17:22,824|SIMPLICITE|INFO||http://lbc-77449-app-7cc8cb8f44-xbc86:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|initList||Evénement: List :{"name":"LBC_LIST_COUNTRY","items":[{"code":"DZ","readonly":false,"value":"ALGERIE","enabled":true},{"code":"AR","readonly":false,"value":"ARGENTINE","enabled":true},{"code":"AU","readonly":false,"value":"AUSTRALIE","enabled":true},{"code":"AT","readonly":false,"value":"AUTRICHE","enabled":true},{"code":"BE","readonly":false,"value":"BELGIQUE","enabled":true},{"code":"BR","readonly":false,"value":"BRESIL","enabled":true},{"code":"BG","readonly":false,"value":"BULGARIE","enabled":true},{"code":"CA","readonly":false,"value":"CANADA","enabled":true},{"code":"CL","readonly":false,"value":"CHILI","enabled":true},{"code":"CO","readonly":false,"value":"COLOMBIE","enabled":true},{"code":"HR","readonly":false,"value":"CROATIE","enabled":true},{"code":"CZ","readonly":false,"value":"REPUBLIQUE TCHEQUE","enabled":true},{"code":"DK","readonly":false,"value":"DANEMARK","enabled":true},{"code":"EE","readonly":false,"value":"ESTONIE","enabled":true},{"code":"FO","readonly":false,"value":"FEROE, ILES","enabled":true},{"code":"FI","readonly":false,"value":"FINLANDE","enabled":true},{"code":"FR","readonly":false,"value":"FRANCE","enabled":true},{"code":"DE","readonly":false,"value":"ALLEMAGNE","enabled":true},{"code":"GB","readonly":false,"value":"ROYAUME-UNI","enabled":true},{"code":"GR","readonly":false,"value":"GRECE","enabled":true},{"code":"GP","readonly":false,"value":"GUADELOUPE","enabled":true},{"code":"HU","readonly":false,"value":"HONGRIE","enabled":true},{"code":"IS","readonly":false,"value":"ISLANDE","enabled":true},{"code":"IN","readonly":false,"value":"INDE","enabled":true},{"code":"ID","readonly":false,"value":"INDONESIE","enabled":true},{"code":"IE","readonly":false,"value":"IRLANDE","enabled":true},{"code":"IL","readonly":false,"value":"ISRAEL","enabled":true},{"code":"IT","readonly":false,"value":"ITALIE","enabled":true},{"code":"JP","readonly":false,"value":"JAPON","enabled":true},{"code":"KR","readonly":false,"value":"COREE REPUBLIQUE DE","enabled":true},{"code":"LV","readonly":false,"value":"LETTONIE","enabled":true},{"code":"LT","readonly":false,"value":"LITUANIE","enabled":true},{"code":"LU","readonly":false,"value":"LUXEMBOURG","enabled":true},{"code":"MY","readonly":false,"value":"MALAISIE","enabled":true},{"code":"MA","readonly":false,"value":"MAROC","enabled":true},{"code":"MU","readonly":false,"value":"MAURICE","enabled":true},{"code":"MX","readonly":false,"value":"MEXIQUE","enabled":true},{"code":"NL","readonly":false,"value":"PAYS-BAS","enabled":true},{"code":"NC","readonly":false,"value":"NOUVELLE-CALEDONIE","enabled":true},{"code":"NZ","readonly":false,"value":"NOUVELLE-ZELANDE","enabled":true},{"code":"NO","readonly":false,"value":"NORVEGE","enabled":true},{"code":"PH","readonly":false,"value":"PHILIPPINES","enabled":true},{"code":"PL","readonly":false,"value":"POLOGNE","enabled":true},{"code":"PT","readonly":false,"value":"PORTUGAL","enabled":true},{"code":"RE","readonly":false,"value":"REUNION","enabled":true},{"code":"RO","readonly":false,"value":"ROUMANIE","enabled":true},{"code":"RU","readonly":false,"value":"RUSSIE","enabled":true},{"code":"SG","readonly":false,"value":"SINGAPOUR","enabled":true},{"code":"SK","readonly":false,"value":"SLOVAQUIE","enabled":true},{"code":"SI","readonly":false,"value":"SLOVENIE","enabled":true},{"code":"ZA","readonly":false,"value":"AFRIQUE DU SUD","enabled":true},{"code":"ES","readonly":false,"value":"ESPAGNE","enabled":true},{"code":"SE","readonly":false,"value":"SUEDE","enabled":true},{"code":"CH","readonly":false,"value":"SUISSE","enabled":true},{"code":"TU","readonly":false,"value":"TURQUIE","enabled":true},{"code":"AE","readonly":false,"value":"EMIRATS ARABES UNIS","enabled":true},{"code":"US","readonly":false,"value":"ETATS-UNIS","enabled":true}]}
2024-12-18 11:17:22,823|SIMPLICITE|INFO||http://lbc-77449-app-7cc8cb8f44-xbc86:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|initList||Evénement: ListName :LBC_LIST_COUNTRY
```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonjour,

Effectivement la recherche du champ lié concatène tous les codes possibles de l'ensemble des listes liées possibles (sauf si un filtre a déjà été positionné sur le champ père). 

Cette concaténation ne se préoccupe pas de l'ordre global, mais juste du "distinct" pour ne pas afficher un même code 2 fois.

Dans votre cas d'usage, si les listes liées sont toutes des pays, ça aurait du sens de les re-trier globallement.

Mais dans un cas général, il n'est pas forcement intelligible de mélanger/réordonner les sous-listes qui n'auraient pas la même sémantique. Par exemple les sous-listes de rendering par type de champ n'ont rien à voir entre elles.

En terme d'UX, il conviendrait de plutôt afficher dans le `select` un niveau `<optgroup>` qui indiquerait que pour telle valeur du père, il a certaines valeurs liées possibles.


Essayez de voir ce que contient la liste ENUM de tous les item à l'`initList` :

```java
List<EnumItem> list = getField("x").getList().getAllItems();
```
Par code vous devriez pouvoir les trier comme vous le souhaitez si elle contient bien tous les pays.
