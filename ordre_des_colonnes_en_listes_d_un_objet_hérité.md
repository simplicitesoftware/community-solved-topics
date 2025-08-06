# Ordre des colonnes en listes d'un objet hérité

**URL:** https://community.simplicite.io/t/6063

## Question
### Request description

Bonjour, 

Nous reprenons ce ticket : https://community.simplicite.io/t/surcharger-lordre-des-colonnes-dun-objet-herite/6044

Car nous ne trouvons de solution à notre besoin.
Nous devons garder extend of code, car nous avons besoins d'accéder aux éléments de l'objet père, notamment les links.
Nous avons essayé de réorganiser les colonnes : 
- en surchargeant l'ordre dans le paramètrage
- en utilisant les methodes `this.getField("...").setOrderInObject(...)` et `this.getFieldArea("...").moveField(5,1);` dans le postLoad et le initList
- en surchargeant le template de l'objet hérité avec l'ordre souhaité

mais aucunes de ces méthodes ne fonctionnent en liste mais nous donnent un résultat dans le formulaire.
En liste nous continuons d'avoir l'ordre de l'objet père.
Par contre quand nous surchargeons d'autres paramètres notamment la visibilité cela fonctionne en liste et dans les formulaires.

Pouvez-nous indiquer une solution pour changer l'ordre en liste d'un objet hérité ?

Merci d'avance pour votre aide

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.32
BuiltOn=2023-02-20 14:50
```
[/details]

## Answer
On a revu le loader pour déplacer tous les champs ré-ordonnées par héritage, et pas seulement les nouveaux champs ajoutés au niveau de l'objet hérité. Ce sera livré en 5.2.35

[quote="julienroy03, post:1, topic:6063"]
setOrderInObject
[/quote]

C'est un simple accesseur pour changer la valeur, mais ça n'agit pas sur la liste des fields.

[quote="julienroy03, post:1, topic:6063"]
getFieldArea("...").moveField(5,1);
[/quote]

Ca change l'ordre au sein d'une zone, mais si l'objet n'a pas de zone, cela ne changera rien au niveau de la liste principale des champs getFields().
