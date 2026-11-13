# Erreur SQL "missing FROM-clause entry" lors de l'utilisation d'un SQL spécifique dans un lien de relation

**URL:** https://community.simplicite.io/t/13583

## Question
Bonjour à tous,

Je rencontre un problème lors de l’utilisation d’un **SQL spécifique** (filtre) sur un lien de relation, et je ne parviens pas à identifier l’origine de l’erreur.

**Environnement :**

* Simplicite : **6.3.19**
* Base de données : PostgreSQL

**Contexte :** J’ai une table dee_collaborateur_projet qui sert de **table de liaison** entre :

* cpj_projet (via dee_clp_pjt_id)
* m_user (via dee_clp_user_id)

J’ai besoin d’ajouter un filtre spécifique sur la relation dee_clp_pjt_id. Pour ce faire, j’ai saisi le SQL spécifique 1=1 dans les paramètres du lien (afin de tester).

**Le problème :** Quand j’exécute la requête, le moteur Simplicite génère le SQL suivant, qui lève l’erreur : ERROR: missing FROM-clause entry for table "t_deeclppjtid"

**Requête générée par Simplicite :**

```sql

select t.row_id, 
       t.dee_clp_pjt_id, 
       t_deeClpPjtId.cpj_pjt_titre,   -- ⚠️ Colonne demandée
       t.dee_clp_user_id, 
       t_deeClpUserId.usr_login, 
       t_deeClpUserId.usr_email, 
       t.dee_clp_droit_en_ecriture, 
       t.dee_clp_droit_automatique, 
       t.created_dt, t.created_by, 
       t.updated_dt, t.updated_by 
from dee_collaborateur_projet t 
left outer join m_user t_deeClpUserId 
       on (t.dee_clp_user_id=t_deeClpUserId.row_id)
       -- ❌ MANQUE : left outer join cpj_projet t_deeClpPjtId on (t.dee_clp_pjt_id=t_deeClpPjtId.row_id)
where (1=1) and (t.dee_clp_pjt_id=?) 
order by t.dee_clp_pjt_id asc, t.dee_clp_user_id asc, t.dee_clp_droit_automatique asc, t.row_id asc 
limit 20

```

**Analyse :** Le SELECT demande bien la colonne cpj_pjt_titre via l’alias t_deeClpPjtId, mais le JOIN correspondant à la table cpj_projet est **absent** de la clause FROM/JOIN.

Je ne sais pas si c’est :

1. Un bug dans la génération du SQL ?
2. Une mauvaise configuration de ma part dans le modèle (déclaration de la relation, champ de la relation, etc.) ?
3. Une limitation connue en version 6.3.19 ?

Merci d’avance pour votre aide !

## Answer
_No answer provided._
