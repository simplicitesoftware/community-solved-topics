# Affichage d'erreur "Unable to get row ID" après perte de droits par SearchSpec

**URL:** https://community.simplicite.io/t/4627

## Question
### Request description

Bonjour,

J'ai un objet métier qui possède plusieurs enregistrements (2 dans le cas ci-dessous):
![image|690x321](upload://3W6kTTRKx3Chqz7ttn5RhYsZxHt.png)

Si un utilisateur n'appartient pas au groupe administrateur, il voit uniquement les enregistrements qui le concerne (ceux dont il est le responsable). Exemple ci-dessous:
![image|690x293](upload://dg6D39tP1ctAMySZGh9OuvG3Wxd.png)

Le problème, c'est que cet utilisateur doit pouvoir changer le responsable si besoin. En changeant de responsable, il ne doit plus pouvoir voir l'enregistrement car il n'en est plus responsable. 

Le problème, c'est que du coup, comme il n'en a plus la visibilité, au moment où il enregistre, il obtient cette erreur ci-dessous (**Thomas GERAUD** change le responsable. Ce n'est plus lui, mais **Florent LAUZET**):
![image|690x336](upload://dWxJU0ax2hJVLFwtD3yvxdfAXg0.png)

Voici comment les droits de visibilités sont gérés :
```
@Override
public void postLoad() {
	if(!getGrant().hasResponsibility("DDV_SUPERADMIN") && !getGrant().hasResponsibility("DDV_ASSISTANT")){
		if(getGrant().hasResponsibility("DDV_MANAGER")){
			setDefaultSearchSpec("t.ddv_pow_responsible IN " + this.getAllResponsibleOfFundForTeamManager());
		} else {
			setDefaultSearchSpec("t.ddv_pow_responsible = " + getGrant().getUserUniqueId());
		}
	} else{
		setDefaultSearchSpec("t.ddv_pow_responsible IS NOT NULL");
	}
}
```

**Avez-vous une idée de comment résoudre ce problème ?**

**PS :** Je précise que l'enregistrement est bel et bien sauvegardé malgré l'erreur.

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.36
BuiltOn=2022-03-25 23:37
Git=release/8329db12a092c6c91775901c9f207681792bbea1
Encoding=UTF-8
EndpointIP=10.201.117.42
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-01 10:41:18
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Le fonctionnement sera amélioré au prochain build 5.1.38 :

Depuis un update en formulaire :
- Affiche les messages (ou applique les HTMLTool.javascriptStatement / HTMLTool.redirectStatement) issus du hook `postSave` ou `postUpdate`
- Sinon par défaut, affiche un toast "L'accès à l'objet ne vous est plus autorisé" + redirect vers la liste de l'objet

Depuis un update en liste (fille ou non) :
- aucun message affiché / ni redirect
- ignore les messages des hooks car la ligne n'existe plus pour les afficher
- la ligne disparait simplement de la liste actualisée au save
