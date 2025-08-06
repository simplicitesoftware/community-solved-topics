# Conflits sur des Contraintes de même effets avec un ordre différent

**URL:** https://community.simplicite.io/t/4855

## Question
### Request description

Bonjour,

J'ai une contrainte avec un effet **back-end** et un **ordre de 100** qui vérifie que les champs ne soit pas `null` en les rendant **Obligatoire**:
![image|690x286](upload://41SHJVvbRy2Q5suX5WdKX1eoq9a.png)

J'ai une deuxième contrainte avec un effet **back-end** et un **ordre de 110** qui change la **valeur du champ** :
![image|690x350](upload://crDQDLo0VkPwAs13flP4QSBkZEO.png)

Mon objectif était que l'objet vérifie d'abord que le champ n'est pas vide, puis si il n'est pas vide il change la valeur de ce champ.

Sauf que la première contrainte (ordre 100) ne fonctionne pas car pour l'objet, le champ n'est pas vide car je remplace sa valeur dans la contrainte suivante (ordre 110). La preuve est que si je rends inactif la contrainte d'ordre 110, la contrainte d'ordre 100 refonctionne.

C'est selon moi pas logique car la contrainte d'ordre 100 devrait d'abord s'exécuté puis ensuite celle d'ordre 110. Il ne devrait pas y avoir de lien entre ces 2 contraintes qui devraient être indépendante l'une de l'autre.

**Avez-vous une idée du problème ?**

**PS :** Les 2 contraintes fonctionnent séparément, mais ensemble celle d'ordre 110 ne fonctionne pas.

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.3
BuiltOn=2022-05-10 18:31
Git=5.2/75384808e0fc7f992d50959bdc3fb75a79deac57
Encoding=UTF-8
EndpointIP=10.201.117.57
EndpointURL=http://siparex-simplicite-dev-557d978ccf-xvkwk:8080
TimeZone=Europe/Paris
SystemDate=2022-05-13 16:09:44
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
**Pour clôturer ce sujet (si d'autre utilisateurs veulent la solution) :**

[quote="nathalie, post:9, topic:4855, full:true"]
Comme dit il fallait tester que votre champ n’est pas vide et cela fonctionne.
Il n’y a pas d’étoile rouge car le champ est obligatoire lors de la transition d’état.
J’ai mis un exemple sur evlValInitEvalComment
[/quote]

[quote="Elcoco, post:10, topic:4855"]
Merci, par contre je rencontre un bu visuel (peut être normal).
[/quote]

Il fallait tester que la valeur ne soit pas `null` avant de remplir la valeur du champ dans la contrainte d'ordre 110.

Pour le bug, @nathalie m'a indiqué que lorsqu'on a des impacts qui s’exécutent en back uniquement il vaut mieux employer des expressions qui s’exécutent en back aussi.

Voici donc un exemple d'expression utilisé dans la contrainte d'ordre 110 (remplir les champs automatiquement) :
```
!Tool.isEmpty([VALUE:evlValDafComment])&& [OLDSTATUS].equals("REVIEWED_MANAGER") && [STATUS].equals("REVIEWED_DAF")?[VALUE:evlValDafComment] + "--" + [LOGIN] + " - " + [DATE]: [VALUE:evlValDafComment]
```
