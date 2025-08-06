# Obtenir les emails de tous les utilisateurs d'un groupe

**URL:** https://community.simplicite.io/t/4344

## Question
Bonjour,

J'ai 2 utilisateurs qui ont chacun leurs adresses email. Ces 2 utilisateurs ont le même groupe qui leur est associé que nous appellerons "G1".
J'aimerais en java récupérer sous forme de liste les adresses email de ces utilisateurs à partir du groupe "G1".

J'ai consulté la Javadoc, et je peux récupérer un groupe, mais je n'arrive pas à récupérer les adresses email des utilisateurs de ce groupe.

Auriez-vous une solution ? Merci d'avance.

## Answer
Il y a plusieurs approches possibles. 

Le plus "propre" est d'utiliser les APIs Java des objets métier => l'objet `Responsability` filtré sur l'attribut ramené du nom du groupe `rsp_group_id.grp_name` pour récupérer la liste des row IDs des utilisateurs affectés au groupe puis l'objet `User` pour récupérer, pour chacun de ces row IDs, la valeur attribut email `usr_email`. Cette approche induira N+1 requêtes SQL s'il y a N utilisateurs (si N est faible ce n'est pas grave) mais ça sera didactique sur l'usage des APIs Java des objets métier.

Le plus "sale" mais le plus performant (1 seule requête SQL) c'est de faire directement la requête en base genre:
```sql
select u.usr_email
from m_user u, m_resp r, m_group g
where u.row_id = r.rsp_login_id
and g.row_id = r.rsp_group_id
and g.grp_name = 'MYGROUP'
```
