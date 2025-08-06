# Recherche globale de type 'contains'

**URL:** https://community.simplicite.io/t/8048

## Question
### Request description

Bonjour,

Nous avons un champ identifiant indexé de type 'IRN-XXXXX'.
La recherche globale fonctionne si on cherche IRN-XXXXX mais pas si on cherche seulement XXXXX.
J'ai trois questions :
- l'utilisation de wildcard sur le début d'un terme impacterait-elle trop les performances ?
- sinon, est-ce paramétrable sans évolution ?
- et sinon, est-ce que créer un champ caché indexé de cet identifiant sans le 'IRN-' serait une bonne solution de contournement ?

Merci d'avance,
Emmanuelle

## Answer
En simplifiant :

Avec un mot complet (ici la ref d'un produit de la démo):

```sql
SELECT idx_object, idx_row_id, idx_ukey, idx_all
FROM m_index
WHERE to_tsvector('simple', idx_all) @@ to_tsquery('REF001:*')
AND idx_object = 'DemoProduct'
```
On trouve bien le seul record qui matche:
![image|690x481](upload://gbWgpa9taicIgPYr1KJZdKfLcQL.png)

Mais effectivement avec une fin de mot on ne trouve rien:

```sql
SELECT idx_object, idx_row_id, idx_ukey, idx_all
FROM m_index
WHERE to_tsvector('simple', idx_all) @@ to_tsquery('001:*')
AND idx_object = 'DemoProduct'
```

![image|690x239](upload://tEn1ihddJKMTqqtp91NobVOaA7u.png)

NB : Par contre avec un début de mot on trouve bien tous les records qui matchent (ici tous les produits):

``` sql
SELECT idx_object, idx_row_id, idx_ukey, idx_all
FROM m_index
WHERE to_tsvector('simple', idx_all) @@ to_tsquery('REF00:*')
AND idx_object = 'DemoProduct'
```

De ce que je comprends de la mécanique de la recherche fulltext PostgreSQL il n'y a pas moyen d'exprimer un "ends with" ou un "contains", mais uniquement un "more or less equals" qui se comporte notamment comme une sorte de "starts with". Je ne suis pas non plus expert de ce type de recherche...

Bref, à ce stade, pour répondre à un besoin de recherche de type "contains", je ne vois pas d'autre solution que de ne pas utiliser la recherche fulltext en passant le param système `USE_FULLTEXT_INDEXES` à `no`, les recherches se feront alors avec des `like %...%` ce qui correspond à du "contains" mais sera moins précis/souple pour des recherches plus ciblées, comme par exemple utilisant des recherches avec combinaisons de mots:
![image|577x88](upload://Ad9CGd7vfn0645D49tZ8Um8Qv0W.png)
