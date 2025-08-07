# Trier après un getSelectedIds()

**URL:** https://community.simplicite.io/t/9558

## Question
### Description

Bonjour,

Suite à mon précédent post, je me permet de republier la première partie.

https://community.simplicite.io/t/echange-sur-les-bonnes-pratiques/9548

J’ai réalisé une librairie Excel à la région pour exporter les données rapidement - apporter une modularité simple et factoriser le code pour le rendre plus lisible. Lorsqu’on utilise une méthode Java pour une publication, j’ai vu qu’on pouvait utiliser la fonction getSelectedIds() pour récupérer les ids des lignes sélectionnés, cela fonctionne très bien pour moi. Maintenant, j’aimerais ajouter un tri côté client - imaginons un simple tri alphabétique sur un champ - dois-je réaliser le tri en dur (en java) à partir des ids - et sélectionner chaque id pour faire mon tri ? ou je peux utiliser quelque chose comme : this.getField(“XXX”).setOrder(10) ?

Voici la fonction jusqu’à ce jour :

Etat du code

```
//Côté serveur
public List<String> getSelectedIds(ObjectDB obj) {
    // Recupération des ids
    List<String> ids = new ArrayList<>();

    if (Tool.isEmpty(obj.getSelectedIds())) {
        List<String[]> rows = new ArrayList<>();
        ObjectFieldSearch[] filters = obj.getFilters(); // Keep filters
        obj.setFilters(filters);
        rows = obj.search(false);
        for (String[] row : rows) {
            ids.add(row[0].toString());
        }
    } else {
        ids = obj.getSelectedIds();
    }

    return ids;
}

//Côté client
List<String> ids = excelUtils.getSelectedIds(this);
// Ajout d'un tri ici 
``` 
Merci d'avance et belle journée

## Answer
Dans ce cas, vous pouvez implémenter dans le `postLoad` un mécanisme qui définit les ordres de tri selon une instance particulère : 
```java
@Override
public void postLoad() {
	if (getInstanceName().contains("MyCustomExcelInstance")) {
		resetOrders(); // retirer les tris configurés
		getField("fieldToOrder1").setOrder(1);
		getField("fieldToOrder2").setOrder(2);
		getField("fieldToOrder3").setOrder(3);
	}
}
```

Et adapter votre méthode `getSelectedIds` 
```java
ObjectDB obj = getGrant().getObject("MyCustomExcelInstance", "MyObject");
obj.resetFilters();

if (Tool.isEmpty(getSelectedIds())) {
    if (this.isFiltered(true)) { // true dans le cas d'une liste liée (filtre sur le parent id)
        this.getFields().stream()
                   .filter(ObjectField::isFiltered)
                   // ajouter à l'instance custom les filtres UI
                   .forEach(f -> obj.getField(f.getName()).setFilter(f.getFilter())); 
    }
} else {
    obj.setFieldFilter("row_id", " in (" + String.join(", ", this.getSelectedIds()) + ")");
}

List<String[]> rows = obj.search(false);
List<String> ids = rows.stream().map(row -> row[0]).toList()
```

[quote="availlant, post:1, topic:9558"]
```
ObjectFieldSearch[] filters = obj.getFilters(); // Keep filters
        obj.setFilters(filters);
```
[/quote]

Le problème avec ça, c'est que `obj.getFilters()` contient aussi les ordres de tri.
