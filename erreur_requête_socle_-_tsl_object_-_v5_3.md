# Erreur requête socle - tsl_object - V5.3

**URL:** https://community.simplicite.io/t/8895

## Question
### Request description

Bonjour,
Je pense qu'il y a eu un mauvais backportage de la version 6.0 vers la version 5.3. suite à la migration d'une version 4.0 en 5.3. Nous rencontrons le log d'erreur suivant  :

> 2024-10-15 22:25:44,907|SIMPLICITE|ERROR||http://XXXXXX:8080/simplicite|/simplicite|ECOREDB001|system|com.simplicite.util.engine.GrantManager|query||Erreur SQL requête: select distinct obj.obj_name,obj.obj_dbtable,t.tsl_value,fld.fld_name,fld.fld_dbname,fld.fld_required,obf.obf_cascad,ref.obj_dbtable,t.tsl_lang from m_object ref inner join m_objfield obf on (ref.row_id = obf.obf_ref_object_id and obf.obf_ref_field_id is null) inner join m_object obj on (obj.row_id = obf.obf_object_id) inner join m_field fld on (fld.row_id = obf.obf_field_id) left outer join m_translate t on (t.**tsl_object**='ObjectInternal:'||obj.row_id) where ref.obj_name='ProjetReal'
> 
> java.sql.SQLSyntaxErrorException: ORA-00904: "T"."TSL_OBJECT": invalid identifier
> https://docs.oracle.com/error-help/db/ora-00904/

Nous n'avons pas de champ tsl_object dans le métamodel.

Pour moi, ce champ arrive dans la version 6.0 :
> Translation refactored link 
> All Translation objects has a new field tsl_object to address any translatable entity.

https://docs.simplicite.io/versions/release-notes/v6-0

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.48
BuiltOn=2024-09-13 14:47
Git=5.3/eabe8a342a09dc94a30086ecc233891e8b706ef7
Encoding=UTF-8

[Server]
ServerInfo=Apache Tomcat/9.0.87.redhat-00003

[JavaVM]
Version=17.0.11

[Database]
Vendor=4
VendorName=oracle
ProductName=Oracle
ProductVersion=Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production

```
[/details]

Cordialement,

## Answer
Vérification faite c'est la raison d'être de la révision corrective express 5.3.49 qui est arrivée le lundi 16/09 suite à la 5.3.48 buguée du vendredi 13/09.
