# Problème de récupération d'un attribut d'action Choix multiple selon le format

**URL:** https://community.simplicite.io/t/6393

## Question
### Request description

Bonjour,

Sur une action j'ai configuré un attribut d'action de type Choix multiple dont je génère les items dynamiquement.

![image|690x135](upload://qCeSoD7iFBflcuzPHFwVgmUcUh.png)


```	@Override
	public void initAction(Action action) {
		String lang = getGrant().getLang();
		
		if (action.getName().equals("createApp"))
		{
			ObjectField f = action.getConfirmField(lang, "rciCreateAppCountries");
			
			ObjectDB sub = getGrant().getTmpObject("RciSubsidiary");
			sub.resetFilters();
			sub.getField("rciSubScope").setOrder(1);
			
			List<String[]> subList = sub.search();
			
			for (int i = 0 ; i < subList.size() ; i++)
			{
				sub.setValues(subList.get(i));
				f.getList().putItem(sub.getRowId(), sub.getFieldValue("rciSubScope"), true);
			}
			
		}
		
		super.initAction(action);
	}
```
A l'exécution je récupère sa valeur de la façon suivante

```String[] countries = action.getConfirmField(getGrant().getLang(),COUNTRY_FIELDNAME).getCodes();```

J'ai un résultat différent selon le rendering de mon attribut :
- en Select with search (Pillbox) je récupère les valeurs sélectionnées par le user (comportement attendu)
- en Cases à cocher horizontales, je ne récupère que le code du premier item, même s'il n'est pas coché (comportement pas attendu)

Ai-je fait une erreur ?
Merci !
Emmanuelle

### Technical information

[details="Instance /health"]
```text
Version=5.2.39
BuiltOn=2023-05-02 12:08
```
[/details]

## Answer
Problème non reproduit/

Sur la démo, j'ai ajouté "grp_type" dans l'action qui incrémente les stock d'un produit (c'est un enum multiple des types de groupe de droits). On a bien les valeurs cochées avec getValue ou getCodes.

```java
ObjectField type = action.getConfirmField(getGrant().getLang(), "grp_type");
AppLog.info("type value = " + type.getValue(), null);
AppLog.info("type codes = " + String.join(",", type.getCodes()), null);
```

Et si on replace la liste dynamiquement l'enum dans l'initAction :

```java
ObjectField type = action.getConfirmField(getGrant().getLang(), "grp_type");
type.getList().getItems().clear();
type.getList().putItem("A", "text a", true);
type.getList().putItem("B", "text b", true);
type.getList().putItem("C", "text c", true);
type.getList().putItem("D", "text d", true);
```

Si on coche b+c+d, on obtient bien "B;C;D" et "B,C,D" dans les logs / testé avec rendering checkbox horizontal et vertical.

Quelques idées :
- il manque le "clear" pour faire un annule et remplace à chaque fois
- les valeurs cochées par défaut sont issues de la valeur par défaut du champ, car le formulaire d'une action est comme une création, il faut utiliser setDefaultValue pour proposer une valeur (setValue n'est pas utilisé).
