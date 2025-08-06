# Filtre sur un champ d'objet en fonction d'un autre champ

**URL:** https://community.simplicite.io/t/3042

## Question
Bonjour
j'ai un objet "Requête" qui a deux champs : le créateur et le validateur.
Je souhaiterais pouvoir filtrer les requêtes automatiquement validées càd créateur = validateur.

J'ai essayé de créer un attribut calculé mais la recherche sur cet attribut ne fonctionne pas.
Existe t-il une façon d'écrire ce filtre (par exemple : [VALUE:FieldCreator]) ?
Dois-je faire un champ persistant ?

Quelle est la meilleure solution ?

Cordialement

**[Platform]**
Status=OK
Version=4.0.P25
BuiltOn=2021-03-11 12:27 (revision 87c63edc550691b4a0f402a31d3841429a9e0476)
Encoding=UTF-8
EndpointIP=21.0.9.3
EndpointURL=http://0843d6d81cfb:8080
TimeZone=Europe/Paris
SystemDate=2021-03-25 15:58:55

## Answer
Bonjour Amandine,

Voici un exemple de paramétrage qui permet l'utilisation d'un filtre de recherche booléen.

Sur l'objet, paramétrer un champ `demoSupIsBimSupplier` **calculé** (donc pas de nom physique, pas de colonne en base), **invisible** (donc n'apparaissant pas dans les listes et formulaires) et **recherchable** (donc apparaissant dans les champs de recherche).

[details="Exemple de paramétrage Simplicité"]

```xml
<?xml version="1.0" encoding="UTF-8"?>
<simplicite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.simplicite.fr/base" xsi:schemaLocation="http://www.simplicite.fr/base https://www.simplicite.io/resources/schemas/base.xsd">
<object>
	<name>Field</name>
	<action>upsert</action>
	<data>
		<fld_name>demoSupIsBimSupplier</fld_name>
		<fld_dbname/>
		<fld_visible>0</fld_visible>
		<fld_updatable>0</fld_updatable>
		<fld_required>0</fld_required>
		<fld_research>1</fld_research>
		<fld_researchreq>0</fld_researchreq>
		<fld_type>8</fld_type>
		<fld_size>1</fld_size>
		<row_module_id.mdl_name>Demo</row_module_id.mdl_name>
	</data>
</object>
<object>
	<name>ObjectFieldSystem</name>
	<action>upsert</action>
	<data>
		<obf_object_id.obo_name>DemoSupplier</obf_object_id.obo_name>
		<obf_field_id.fld_name>demoSupIsBimSupplier</obf_field_id.fld_name>
		<obf_order>330</obf_order>
		<obf_area_id.ofa_name>DemoSupplier-1</obf_area_id.ofa_name>
		<obf_area_id.ofa_position>1</obf_area_id.ofa_position>
		<row_module_id.mdl_name>Demo</row_module_id.mdl_name>
	</data>
</object>
<object>
	<name>TranslateField</name>
	<action>upsert</action>
	<data>
		<tsl_typeField>F</tsl_typeField>
		<tsl_id.fld_name>demoSupIsBimSupplier</tsl_id.fld_name>
		<tsl_lang>ENU</tsl_lang>
		<tsl_value>BIM only ?</tsl_value>
		<tsl_simplehelp/>
		<tsl_short_value/>
		<tsl_placeholder/>
		<tsl_listhelp/>
		<row_module_id.mdl_name>Demo</row_module_id.mdl_name>
		<tsl_tooltip/>
	</data>
</object>
<object>
	<name>TranslateField</name>
	<action>upsert</action>
	<data>
		<tsl_typeField>F</tsl_typeField>
		<tsl_id.fld_name>demoSupIsBimSupplier</tsl_id.fld_name>
		<tsl_lang>FRA</tsl_lang>
		<tsl_value>BIM uniquement?</tsl_value>
		<tsl_simplehelp/>
		<tsl_short_value/>
		<tsl_placeholder/>
		<tsl_listhelp/>
		<row_module_id.mdl_name>Demo</row_module_id.mdl_name>
		<tsl_tooltip/>
	</data>
</object>
</simplicite>
```
[/details]

Sur le code de l'objet, ajouter le code sur le hook `preSearch`

```java
public class DemoSupplier extends ObjectDB {
	private static final long serialVersionUID = 1L;
	
	@Override
	public void preSearch() {
		setSearchSpec(getDefaultSearchSpec() + (
			Tool.isTrue(getFieldFilter("demoSupIsBimSupplier")) 
			? " and sup_code='BIM'" 
			: " and 1=1"
		));
	}
}
```

Aviez-vous résolu votre problème? Cela répond-t-il à votre question?
