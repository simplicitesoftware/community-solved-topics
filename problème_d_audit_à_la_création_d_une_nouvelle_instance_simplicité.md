# Problème d'audit à la création d'une nouvelle instance Simplicité

**URL:** https://community.simplicite.io/t/4897

## Question
### Request description

Bonjour,

Comme nous avions plusieurs problème d'audit sur notre instance DEV sur des modules natifs, nous avons installé une nouvelle instance temporaire pour pouvoir réexporté ces modules (System, Documents...) de la nouvelle instance vers l'instance DEV.

Nous avons cependant remarqué quelque chose. Il y a 2 problèmes d'audit par défaut à la création de cette nouvelle instance :
![image|690x190](upload://yfGvivSYom1zjRs2it46EEdRSJy.png)

**Est-ce normal ?**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.3
BuiltOn=2022-05-10 18:31
Git=5.2/75384808e0fc7f992d50959bdc3fb75a79deac57
Encoding=UTF-8
EndpointIP=10.201.117.42
EndpointURL=http://siparex-simplicite-tmp-85f76d87b-vzznf:8080
TimeZone=Europe/Paris
SystemDate=2022-05-23 11:48:01
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Ok, les 2 audits seront effacés dans la prochaine release.

Pour supprimer un warning ou une erreur si un de vos paramétrages est un faux positif (un choix fait exprès pour de bonne raison), il faut savoir que le process d'audit utilise une instance particulière nommée **audit_XXX** donc on peut filtrer sur le nom de l'instance pour changer de comportement pour passer les tests.

Exemple pour **ModuleCommit** qui est un vrai-faux objet avec des champs logiques et dont le code surcharge le "search" pour ne pas utiliser la base mais le repo GIT et qui n'a donc pas besoin de clé physique. Au niveau du postLoad on a ajouté :

```java
// False positive: AuditTool needs a persistent key
if (this.getInstanceName().startsWith("audit_")) {
	ObjectField f = getField("mdl_git_id");
	f.setFunctId(true);
	f.setColumn("mdl_git_id"); // dummy column = not created in local DB
	setFunctId(); // rebuild the full user-key
}
```
