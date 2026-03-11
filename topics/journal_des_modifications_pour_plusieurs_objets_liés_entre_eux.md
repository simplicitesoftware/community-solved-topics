# Journal des modifications pour plusieurs objets liés entre eux

**URL:** https://community.simplicite.io/t/7140

## Question
### Request description

Bonjour, j'ai une question concernant le journal des modifications. Je voulais savoir si il était possible qu'il traite plusieurs objets liés entre eux par une relation. J'ai aujourd'hui un objet métier DossiersPme pour lequel j'ai activé le journal des modifications. J'ai un objet DocumentsComplémentaires liés à l'objet DossiersPme, j'aimerais que le même journal des modifications trace les changements sur ces deux objets, malgré mes recherches je ne vois pas comment procéder.
En vous remerciant


### Technical information

[details="Simplicité 5.2.34"]
```text
---paste the content of your-instance.com/health---
```
[/details]

## Answer
Bonjour, 

Votre demande a été passée en feature request : https://community.simplicite.io/t/historique-cascade-sur-les-relations/7142

Sachant que ça sera une fonctionnalité disponible en V6, pour l'instant vous allez devoir paramétrer un objet particulier pour répondre à votre besoin. 

En 6.0 (actuellement beta), sur base de la démo j'ai réussi à répondre à votre besoin en créant un objet `select` affichant la liste des modifications faites aux produits d'un fournisseur donné.

Pour ce faire :
* J'ai créé un objet `ProductRedoLog` qui est une copie du paramétrage de l'objet `RedoLog`
![Capture d’écran 2023-11-08 à 14.05.23|690x416](upload://hLox5GJlIJ2sdImsHfPzmZZGcC2.png)

* Créé un lien virtuel entre `ProductRedoLog` et `DemoSupplier`
* Implémenté le `preSearch` de `ProductRedoLog` afin de valoriser une `searchSpec` permettant de remonter les lignes de `m_redolog` qui concernent les produits du fournisseur :
```java
@Override
public void preSearch() {
	if(isPanelInstance()){//only call when in panel view
		String supId = getParentObject().getRowId();
		//Get ids of the supplier's products
		List<String[]> prdIds = getGrant().query("select row_id from demo_product where prd_sup_id = "+ supId); 
		String whereClause = "";
		for(String[] idRow : prdIds){
			if("".equals(whereClause))
				whereClause += "'DemoProduct:"+idRow[0]+"'";
			else 
				whereClause += ",'DemoProduct:"+idRow[0]+"'";
		}
		//SQL statement used by redo log, updated to use whereClause created above
		String sql = "select t.row_id, t.rlg_index, t.rlg_session_id, t_rlg_session_id.ses_index, t_rlg_session_id.ses_login, t_rlg_session_id.ses_logon_dt, t_rlg_session_id.ses_first_name, t_rlg_session_id.ses_last_name, t_rlg_session_id.ses_user_id, t.rlg_date, t.rlg_object, t.rlg_data, t.rlg_action, t.rlg_html, t.rlg_primary, null from m_redolog t left outer join m_session t_rlg_session_id on (t.rlg_session_id=t_rlg_session_id.row_id)  where t.rlg_object in ("+ whereClause +") order by t.rlg_index desc, t.row_id";
		
		setSearchSpec(sql);
	}
}
```

Le résultat :
![image|690x412](upload://bdFfambi7pfS1KBK485cy5xL8WN.png)


Je pourrai éventuellement tester cette implémentation en 5.2.53 une fois que vous serez à jour
