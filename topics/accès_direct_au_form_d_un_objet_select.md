# Accès direct au FORM d'un objet SELECT

**URL:** https://community.simplicite.io/t/11883

## Question
### Request description

Bonjour,
Est-il possible d'accéder directement à une instance d'un objet SELECT sans être passé par la liste au préalable ?
J'ai un objet Business en liste avec un getTargetObject qui envoie vers un object SELECT, mais j'ai le même souci que dans [ce ticket](https://community.simplicite.io/t/acces-form-sur-un-objet-select-en-page-daccueil/11564/4) (le get renvoie des valeurs nulles)
J'ai aussi testé avec un accès par copy link avec le même résultat (valeurs nulles)

Si ce n'est pas un usage prévu, je ferai autrement.

Merci !
Emmanuelle

```
	@Override
	public String[] getTargetObject(String rowId, String[] row) {
	    
	    String act = getFieldValue("cdpPdtActivityId.cdpActActivityId.cdpActtypName");
	    String target = "Cdp" + act.substring(0, 1) + act.substring(1).toLowerCase() + "ProductView";
	    
	    				AppLog.info("getTargetObject " + target + "rowId " + rowId, getGrant());

	    
	    String t[] = new String[3];
	    t[0] = target; // target object
	    t[1] = "the_ajax_"+target; // main target instance
	    t[2] = rowId; // target id
	    return t;
	}
```

[Platform]
Status=OK
Version=6.3.6
Variant=full
BuiltOn=2026-03-12 16:20

## Answer
Bonjour Emmanuelle, 

Le fix de François dans le [ticket](https://community.simplicite.io/t/acces-form-sur-un-objet-select-en-page-daccueil/11564/9) force un `search` de l'objet select dans le cas où l'instance est autre que `main`.

Dans ton hook, il suffit de remplacer le nom de l'instance pour forcer le search :
```diff
-    t[1] = "the_ajax_"+target; // main target instance
+    t[1] = "ref_"+target; // ref target instance
```
