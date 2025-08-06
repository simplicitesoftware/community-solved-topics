# Problème de sauvegarde edition en liste initRefSelect

**URL:** https://community.simplicite.io/t/5415

## Question
Bonjour, nous avons détecté un bug lié au initrefselect,
lorsque l'on édite en liste un objet soumis au initref, si on modifie plusieurs champs avant de sauvegarder, seul le dernier est sauvegardé. 


référence à ce post, peut etre que le bug vient du fix?
https://community.simplicite.io/t/initrefselect-ne-fonctionne-pas-pour-ledit-list/5387/9?u=paul-alexandre

## Answer
Après analyse, il n'est pas possible de rappeler l'initRefSelect au save.
Si vous devez absolument utiliser une search-spec, il faudra la retirer dans le preSelect pour que lorsque Simplicité cherche à savoir si l'enregistrement existe en back, il n'y ait plus le filtrage contextuel pour la UI :

```
@Override
public void initRefSelect(ObjectDB parent) { 
	if (parent!=null && parent.getName().equals("RheCmplvCol"))
		setDefaultSearchSpec("t.rhe_cmplv_cmp_id = " + parent.getFieldValue("rheCmplvcolCmpId"));
}
@Override
public void preSelect(String rowId, boolean copy) {
	setDefaultSearchSpec("1=1");
	super.preSelect(rowId, copy);
}
```
