# Domaine ouvert par défaut pour un profil donné

**URL:** https://community.simplicite.io/t/5090

## Question
Bonjour la team Simplicité,
Simplicité v4 patch level P25,
Peut-on paramétrer l'ouverture d'un domaine par défaut sur un groupe de profils ?
Bien cordialement,

## Answer
Bonjour,

[quote="bminisclou, post:1, topic:5090"]
Peux t’on paramétrer l’ouverture d’un domaine par défaut sur un groupe de profils ?
[/quote]

Non, cela se paramètre au niveau de chaque User, pas au niveau d'un groupe de droits.
- Vous pouvez forcer la valeur de `usr_menu_defdomain_id` dans le `postSave` si vous utilisez un héritier du User lors de la création d'un utilisateur.
- Ou passer une requête SQL qui met à jour en masse cette colonne dans m_user en fonction des responsabilités dans m_resp du style :

```sql
update m_user 
set usr_menu_defdomain_id = (select row_id from m_object where obj_name='MyDomainName')
where row_id in (select r.rsp_login_id from m_resp r, m_group g where r.rsp_gorup_id=g.row_id and g.grp_name='MY_PROFILE' ...)
```

- Sinon au runtime, le row_id du domaine par défaut d'un user est chargé au logon dans la variable suivante : `grant.getData().m_menu_domain_id`

Vous pouvez le forcer dans les GrantHooks (en V4, et PlatformHooks en V5) en fonction des responsabilités chargées donc au `postLoadGrant` :

```java
if (grant.hasResponsibility("MY_PROFILE")) {
   grant.getData().m_menu_domain_id = ObjectDB.getObjectId("MyDomainName");
}
```
