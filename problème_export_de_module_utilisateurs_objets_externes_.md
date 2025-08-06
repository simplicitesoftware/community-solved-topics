# Problème export de module (utilisateurs + objets externes)

**URL:** https://community.simplicite.io/t/4926

## Question
### Request description

Bonjour,

Nous avons remarqué un problème lors de l'export d'un module en "`Export ZIP (XML)`".
* le code de notre objet externe n'a pas été exporté puisque lors de l'import, nous ne l'avions pas (Solution : nous avons juste copié le code manquant de la DEV vers la PROD)
* Nos utilisateurs sont exportés alors qu'ils ne sont pas sur le module en question. Nous voulons exporter le module `HumanResource` et les utilisateurs sont sur `ApplicationUsers`. ils ne devraient pas être exportés (voici ci-dessous un aperçu d'un utilisateur exporté alors qu'il ne devrait pas) :
```
<data>
	<usp_user_id.usr_login>e.bourgey@siparex.com</usp_user_id.usr_login>
	<usp_param_id.sys_code>FORCE_CHANGE_PASSWORD</usp_param_id.sys_code>
	<usp_value><![CDATA[yes]]></usp_value>
	<usp_param_id.sys_type>PRV</usp_param_id.sys_type>
	<usp_param_id.sys_value><![CDATA[empty]]></usp_param_id.sys_value>
	<usp_param_id.sys_value2/>
	<usp_param_id.sys_desc><![CDATA[Force password change (set at user level)]]></usp_param_id.sys_desc>
	<row_module_id.mdl_name>HumanRessource</row_module_id.mdl_name>
</data>
<data>
	<usp_user_id.usr_login>e.bourgey@siparex.com</usp_user_id.usr_login>
	<usp_param_id.sys_code>HISTORY hr_applicantHome</usp_param_id.sys_code>
	<usp_value><![CDATA[[]]]></usp_value>
	<usp_param_id.sys_type/>
	<usp_param_id.sys_value><![CDATA[empty]]></usp_param_id.sys_value>
	<usp_param_id.sys_value2/>
	<usp_param_id.sys_desc/>
	<row_module_id.mdl_name>HumanRessource</row_module_id.mdl_name>
</data>
```

Voilà la preuve qu'ils sont bien sur `ApplicationUsers` et pas `HumanRessource`.
![image|690x92](upload://5prgaV7LkP3TXOFKjHfPsQA8SeW.png)

Voici la BDD :
![image|690x165](upload://dcKgiqQQBEy1qwYz7EM1kdrWI3e.png)


### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.5
BuiltOn=2022-05-25 15:54
Git=5.2/ecae3b828f4cb7eda5e0e6f6e018fca9b12483d7
Encoding=UTF-8
EndpointIP=10.201.58.89
EndpointURL=http://siparex-simplicite-dev-5475d8459-r9nqn:8080
TimeZone=Europe/Paris
SystemDate=2022-05-31 15:11:44
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Bonjour, 

Il s'agit de l'objet `UserSysParam`, soit les paramètres utilisateur et non pas l'objet `User`
[quote="Elcoco, post:1, topic:4926"]
`UserSysParam`
[/quote]

![image|690x422](upload://3AoYGTJ5fqTV9fjfTqYJcRW5KaE.png)


Edit: vous avez édité votre post pour enelever une info structurante, soit la balise `<name>UserSysParam</name>`
