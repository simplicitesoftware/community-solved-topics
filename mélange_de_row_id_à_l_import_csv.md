# Mélange de row_id à l'import CSV

**URL:** https://community.simplicite.io/t/7785

## Question
### Request description

Bonjour, 

Je rencontre un problème à l'import de lignes via l'interface Csv Import.
L'import termine en erreur, voici un extrait du log de flow

```
2024-02-20 16:11:36,234 INFO  [] Start import object RciApplication:
2024-02-20 16:11:36,234 INFO  []   Found field rciAppCtyGrpId.isoCtygrpCode = []
2024-02-20 16:11:36,234 INFO  []   Found field rciAppVersion = [1]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppDivision = [LOCAL]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppCmdbTechno = []
2024-02-20 16:11:36,234 INFO  []   Found field rciAppState = [PROJECT]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppTechnicalId = [APP-2528]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppCorp = [-]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppContractType = []
2024-02-20 16:11:36,234 INFO  []   Found field rciAppOrgdomId.rciOrgDomName = []
2024-02-20 16:11:36,234 INFO  []   Found field rciAppCtyId.isoCtyCode2 = [IT]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppComments = []
2024-02-20 16:11:36,234 INFO  []   Found field rciAppRosierId = [NA]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppName = [**TBC_Sinistri Mach1**]
2024-02-20 16:11:36,234 INFO  []   Found field rciAppIdentifier = []
2024-02-20 16:11:36,234 INFO  []   Found field rciAppCriticality = [STANDARD]
2024-02-20 16:11:36,236 INFO  []   New record key row_id
2024-02-20 16:11:36,236 INFO  []   Action: INSERT
2024-02-20 16:11:36,511 INFO  []   Save ok.
2024-02-20 16:11:36,511 INFO  [] line 110: Imported
2024-02-20 16:11:36,511 INFO  [] Start import object RciApplication:
2024-02-20 16:11:36,511 INFO  []   Found field rciAppCtyGrpId.isoCtygrpCode = [Iberian]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppVersion = [1]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppDivision = [LOCAL]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppCmdbTechno = [MAINFRAME]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppState = [INSTALLED]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppTechnicalId = [ES050]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppCorp = [-]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppContractType = []
2024-02-20 16:11:36,511 INFO  []   Found field rciAppOrgdomId.rciOrgDomName = []
2024-02-20 16:11:36,511 INFO  []   Found field rciAppCtyId.isoCtyCode2 = [ES]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppComments = []
2024-02-20 16:11:36,511 INFO  []   Found field rciAppRosierId = []
2024-02-20 16:11:36,511 INFO  []   Found field rciAppName = [SIN (RCI ES)]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppIdentifier = [IRN-55138]
2024-02-20 16:11:36,511 INFO  []   Found field rciAppCriticality = [STANDARD]
2024-02-20 16:11:36,523 INFO  []   Found internal key row_id = **6218**
2024-02-20 16:11:36,530 INFO  []   Action: UPDATE
2024-02-20 16:11:36,532 ERROR [] Validation error: [ERR_USERKEY:SIN (RCI ES) ]
2024-02-20 16:11:36,532 ERROR [] line 111: Import error
````
La 2ème ligne est en erreur ERR_USERKEY alors qu'elle n'est pas en doublon. On voit dans les logs que le row_id matché est celui de la ligne précédente :

Found internal key row_id = **6218**

-> 6218 est le row_id de la dernière création.

En regardant les logs de Simplicité en mode debug, je vois que pendant le traitement de la ligne 2, Simplicité est en train de créer l'indexe pour la ligne 1. J'ai l'impression qu'un setFilter pour la création d'indexe de la ligne 1 s'applique également sur la recherche pour UPSERT de la ligne 2.



**--> Création d'indexe ligne 1**
```
2024-02-20 16:11:36,519|SIMPLICITE|INFO||http://simplicite-poc-78bcfc499-d5ctb:8080||SQLUSER|system|DBAccess|SQL|query|SQL=jdbc/simplicite: select t.idx_key, t.idx_object, t.idx_row_id, t.idx_ukey, t.idx_all from m_index t where (idx_key='RciApplication:6218') order by t.idx_key asc Hosts=
```
**-> Requête pour UPSERT ligne 2 avec row_id ligne 1**
```
2024-02-20 16:11:36,523|SIMPLICITE|DEBUG||http://simplicite-poc-78bcfc499-d5ctb:8080||DCOREDB001|system|com.simplicite.util.engine.ObjectManager|query||SQL query: jdbc/simplicite: select t.row_id, t.rci_app_bce_doms, t.rci_app_funct_doms, t.rci_updates_log, [...] t.created_dt, t.created_by, t.updated_dt, t.updated_by from rci_application t left outer join rci_application t_rciAppOriginAppId on (t.rci_app_origin_app_id=t_rciAppOriginAppId.row_id) left outer join rci_application_type t_rciAppTypeId on (t.rci_app_type_id=t_rciAppTypeId.row_id) left outer join iso_country t_rciAppCtyId on (t.rci_app_cty_id=t_rciAppCtyId.row_id) left outer join iso_country_grouping t_rciAppCtyGrpId on (t.rci_app_cty_grp_id=t_rciAppCtyGrpId.row_id) left outer join m_user t_rciAppCmsiRit on (t.rci_app_cmsi_rit=t_rciAppCmsiRit.row_id) left outer join m_user t_rciAppCmsiRm on (t.rci_app_cmsi_rm=t_rciAppCmsiRm.row_id) left outer join m_model t_RciApplication_Model_id on (t.rciapplication_model_id=t_RciApplication_Model_id.row_id) left outer join m_model t_rciAppDataflowsModelId on (t.rci_app_dataflows_model_id=t_rciAppDataflowsModelId.row_id) left outer join m_model t_rciAppDataflowsMacroModelId on (t.rci_app_dataflows_macro_model_id=t_rciAppDataflowsMacroModelId.row_id) left outer join m_model t_rciAppFlowsModelId on (t.rci_app_flows_model_id=t_rciAppFlowsModelId.row_id) left outer join rci_security_auth t_rciAppCcaIntUsrAuthId on (t.rci_app_cca_int_usr_auth_id=t_rciAppCcaIntUsrAuthId.row_id) left outer join rci_security_policy t_rciAppCcaIntSecurityPolicyId on (t.rci_app_cca_int_security_policy_id=t_rciAppCcaIntSecurityPolicyId.row_id) left outer join rci_security_auth t_rciAppCcaExtUsrAuthId on (t.rci_app_cca_ext_usr_auth_id=t_rciAppCcaExtUsrAuthId.row_id) left outer join rci_responsible_entity t_rciAppRspEntId on (t.rci_app_rsp_ent_id=t_rciAppRspEntId.row_id) left outer join iso_country t_rciRspEntCtyId on (t_rciAppRspEntId.rci_rsp_ent_cty_id=t_rciRspEntCtyId.row_id) left outer join rci_org_domain t_rciAppOrgdomId on (t.rci_app_orgdom_id=t_rciAppOrgdomId.row_id) where (t.row_id=?) order by t.updated_dt desc, t_rciAppTypeId.rci_app_type_name asc, t.rci_app_name asc, t.row_id asc
2024-02-20 16:11:36,523|SIMPLICITE|DEBUG||http://simplicite-poc-78bcfc499-d5ctb:8080||DCOREDB002|system|com.simplicite.util.engine.ObjectManager|query||Host: column [1] value (6218)
```
-> l'heure correspond au log Found internal key row_id = **6218** et à l'erreur de duplicate.

A noter que malgré l'erreur, mon objet ligne 2 est quand même créé.
Et si je désactive les indexes pour cet objet, je n'ai plus d'erreur.

Merci d'avance pour votre aide,
Emmanuelle

## Answer
Bonjour,

- Il est impossible que la ligne soit créée si la log indique un update en erreur, le traitement à du être lancé 2 fois ou apparaitre 2 fois dans le fichier.
- L'indexation d'objet est asynchrone mais le thread est synchronisée sur une autre instance d'objet, donc il n'y a pas de collision possible de filtres.

Il faut plutôt faire un select en base pour voir :
- Ce que contient exactement le record row_id = 6218
- Idem pour "TBC_Sinistri Mach1"
- Chercher s'il n'y a pas un autre "SIN (RCI ES)" en base, ou regarder s'il n'y pas des doublons en base
- Voir si l'objet a des search-spec qui font qu'on ne voit pas les doublons en base ou un pb de clé fonctionnelle partielle.
