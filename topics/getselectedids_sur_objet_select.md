# getSelectedIds sur objet SELECT

**URL:** https://community.simplicite.io/t/12341

## Question
### Request description

Bonjour,

Est-il prévu de pouvoir utiliser le getSelectedIds sur un objet SELECT ?
J'ai essayé mais je me retrouve avec des valeurs qui ne correspondent pas au champ row_id dedans.

Merci !
Emmanuelle

[Platform]
Status=OK
Version=6.3.9
Variant=full
BuiltOn=2026-05-08 12:11

## Answer
Bonjour,

Aucune idée, les `selectedIds` sont normalement issus du premier champ de l'objet mais c'est peut être forcé à un test `row_id` quelque part.
Quel est le premier champ de l'objet ? 

un objet `SELECT` n'a pas de `row_id` ni aucune obligation de ramener des records uniques, ça peut être un `group by`, une `union` de plusieurs tables, etc.

Bref il faut à minimal que l'objet contiennent une "clé" en premier qui permet de retrouver de quoi on parle ensuite par code : objet, id... Il faut mapper le `row_id` si l'objet `SELECT` correspond bien à des records d'une table.

**UPDATE**
Après vérification, les `selectedIds` sont placés par le front via le champ clé de l'objet :
`obj.getRowIdFieldName()` =  `obj.metadata.rowidfield || "row_id"`

Donc il faut bien définir un champ clé ou avoir le champ `row_id` dans l'objet, et le placer en premier par convention.
