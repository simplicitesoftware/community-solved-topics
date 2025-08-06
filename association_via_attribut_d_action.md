# Association via attribut d'action

**URL:** https://community.simplicite.io/t/6378

## Question
### Request description

Bonjour,

Est-il possible de créer un attribut d'action de type N,N pour pouvoir associer plusieurs valeurs ? Je ne pense pas mais je demande au cas où ^_^

Merci !
Emmanuelle

## Answer
oui tu as les API d'accès à l'ENUM dans ObjectFieldList

```java
ObjectFieldList list = field.getList();
List<EnumItem> items = list.getItems();
items.clear();
list.putItem("code", "value", true, 10);
list.putItem("code2", "value2", true, 20);
```
où les valeurs sont issues d'une requete ou d'un object.search.
