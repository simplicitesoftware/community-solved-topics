# Relations "m_async_job_row_id_seq" et "m_log_row_id_seq" already exists

**URL:** https://community.simplicite.io/t/6020

## Question
Bonjour la team Simplicité,

Sur une application en version Simplicité version4.0 patch level P25, nous obtenons en permanence ce logue d'erreur :

ERROR [com.simplicite.util.tools.SQLTool] SIMPLICITE|http://xxx||ERROR|system|com.simplicite.util.tools.SQLTool|getSequence||Evénement: m_async_job_row_id_seq is not created 
    org.postgresql.util.PSQLException: ERROR: relation "m_async_job_row_id_seq" already exists 

ERROR [com.simplicite.util.tools.SQLTool] 
SIMPLICITE|http://xxx||ERROR|system|com.simplicite.util.tools.SQLTool|getSequence||Evénement: m_log_row_id_seq is not created 
    org.postgresql.util.PSQLException: ERROR: relation "m_log_row_id_seq" already exists 

A quoi correspondent-ils ?

Bien cordialement

## Answer
Bonjour Bertrand, 

Désolé pour le délai... Cette log indique que la séquence d'auto-increment et le row_id ne sont pas en phase. Un mécanisme d'auto-correction du déphasage a été mis en place à partir de la 5.2.26. 

Voici, pour info, ce que François avait déclaré au client qui nous a sollicité sur la même question, mais qui ne nous a pas fait de retour par la suite:

[quote="Francois, post:2, topic:5589"]
3. Simplicité cherche a re-créer des séquences qui existent déjà, c’est plus un warning.
les sequences ne devaient pas être en phase avec les row_id de certaines tables livrées non vide ou dans le genre.

* Il faut voir si cette log revient, regardez pour chacune si seq.currval = max(row_id) de la table
et pourquoi vous avez des déphasages de séquence (insert SQL sans passer par Simplicité qui fait des nextval… ?)
* Simplicité tente de recaler tout seul la sequence au premier insert qui plante, ça peut générer des logs pas graves si l’insert se passe bien au retry.
* Simplicité fait aussi un rebuild de toutes les sequences PostgreSQL/Oracle au démarrage il me semble. Est-ce qu’on a les droits de supprimer+créer des sequences sur la base ?
[/quote]
