# Lien virtuel sur un objet récursif / réflexif

**URL:** https://community.simplicite.io/t/3069

## Question
Bonjour,

J'ai dans mon application des Domaines qui peuvent avoir des Domaines enfants de façon récursive.
Un Domaine peut être lié à une ou plusieurs applications (relation NN).
Je voudrais, pour chaque domaine, faire un lien virtuel qui liste toutes les applications de TOUS ses domaines enfants (pas que celui du dessous). J'ai tenté de faire une requête SQL récursive mais quand je la teste dans DB access j'ai l'erreur suivante

> Error: A result was returned when none was expected.

Ma requête

```sql
WITH RECURSIVE child_doms AS (
	SELECT
		row_id,
		rci_dom_dom_id
	FROM
		rci_domain
	WHERE
		row_id = 1
	UNION
		SELECT
			dom.row_id,
			dom.rci_dom_dom_id
		FROM
			rci_domain dom
		INNER JOIN child_doms cdom ON cdom.row_id= dom.rci_dom_dom_id
) SELECT * FROM	child_doms;
```

> Version=4.0.P25
> BuiltOn=2021-03-24 00:20 (revision 0ab578dff484419fee9205b41be7f805473ce9a4)

Merci d'avance pour votre aide !
Emmanuelle

## Answer
L'accès DB Access permet d'exécuter des `select` simples ou des mises à jour directes (`insert`, `update`, `delete`). Il ne doit pas gérer ce genre de syntaxe spécifique à PostgreSQL.

Pour tester ta requête, il faut passer par un autre accès, via psql ou autre client PostgreSQL, ou alors faire commencer ta requête par un `select * from (...sous requête...)`.


Au delà de ça, il faudra voir comment cette search-spec peut être placée dans un lien virtuel sous forme de "exists" ou "in" (intégrée au where du select des objets fils).
