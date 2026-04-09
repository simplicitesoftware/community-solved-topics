# Preset search sur objet SELECT

**URL:** https://community.simplicite.io/t/11945

## Question
### Request description

Bonjour,
(Ce ticket n'est pas urgent car j'ai un contournement) 
J'ai paramétré une recherche prédéfinie sur un objet SELECT, et la concaténation se fait difficilement.

Paramétrage :
- un objet SELECT
- une vue avec un filtre SQL basée sur une recherche prédéfinie sur l'objet SELECT
-> la requête obtenue n'a pas de WHERE
-> si j'ajoute ```WHERE 1 = 1 ``` dans la search spec, il reste une parenthèse entre ce ```WHERE``` et le ```AND``` de la preset search
-> le ```t``` n'est pas reconnu


*Résultat sans WHERE 1 = 1*
> select * from (((select prd_name from demo_product) and (t.prd_name = 'Classical desktop'))) t limit 10
>     org.postgresql.util.PSQLException: ERROR: syntax error at or near "and"

*Résultat avec WHERE 1 = 1*
> select * from (((select prd_name from demo_product WHERE 1 = 1) and (t.prd_name = 'Classical desktop'))) t limit 10
>     org.postgresql.util.PSQLException: ERROR: syntax error at or near "and"

Pour contourner mon problème, j'ai fait ceci dans le **preSearch**
```
	@Override
	public void preSearch() {
		
		AppLog.info("preSearch " + getSearchSpec(), getGrant());
		
		//Contournement pour les predef Search sur objet SELECT
		String spec = getSearchSpec().replace("WHERE 1 = 1) and", "WHERE 1 = 1 and");
		setSearchSpec(spec);
		
	    super.preSearch();
	}
```

Et ajouté une parenthèse au filtre SQL pour compenser.
```prd_name = 'Classical desktop')```

*Résultat avec contournement*

> select * from (((select prd_name from demo_product WHERE 1 = 1 and (prd_name = 'Classical desktop')))) t limit 10

Ci dessous un objet SELECT et une vue simples sur lesquels j'ai reproduit
[DemoUserHome_4.xml|attachment](upload://h35KcHjElktGAeLsyJtRFqmBGYq.xml) (1.1 KB)
[DemoSelect.xml|attachment](upload://jQzAC0XtWfYU9YF9XCO5awKQDiA.xml) (9.4 KB)


[Platform]
Status=OK
Version=6.3.7-preview
Variant=full
BuiltOn=2026-04-01 18:33

Merci pour votre aide et bonne journée !
Emmanuelle

## Answer
Après analyse, le cas de mettre une search-spec additionnelle dans la search-spec de l'objet `select` via l'item de vue n'avait pas été prévu, car on ne peut pas fusionner un "morceau de where" et une requête select quelconque (avec des unions, des group-by...).

On va faire en sorte de rendre ça possible, mais la requête générée sera encore plus imbriquée, par exemple :

```sql
select * from (
  select * from (
    select prd_name from demo_product      -- the 'select' object
  ) t where (t.prd_name like 'C%')         -- view item search-spec = SQL filter
) t where t.prd_name = 'Classical desktop' -- other user/UI filter
```

Pour un cas simple comme celui-ci ça fonctionne mais on ne peut le garantir pour toutes les BD et toutes les requêtes compliquées. Ce sera livré en 6.3.8 pour tester.

Si cela ne fonctionne pas par imbrication des select/search-spec, il faudra plutôt revoir le design et retirer/déplacer ce filtre de l'item de vue :

- Spécialiser la requête `select` directement au `postLoad` ou `preSearch` sur l'instance particulière (home, panel...) via `setDefaultSearchSpec` pour placer le filtre SQL au bon endroit du 'select' spécifique de l'objet
- ou si le filtre est simple, il faudra le placer directement dans la recherche prédéfinie (au format json), exemple :
 
```json
{
	"demoPrdName": "C%"
}
```

(et sinon il y avait une parenthèse en trop dans le patch fourni, mais ça ne changeait rien au pb)
