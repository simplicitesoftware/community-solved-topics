# Boucle infinie dans getTargetObject sur un objet inliné

**URL:** https://community.simplicite.io/t/11903

## Question
### Request description

Bonjour,
J'ai un cas très particulier qui génère une boucle infinie à l'affichage d'un form :
- avoir un business objet A
- avoir un business objet B inliné attaché à A
- dans getTargetObject de B, pointer vers A
-> à l'affichage du form de A, B s'affiche en mode "inception"

![image|690x335](upload://ahsW3euO2cC39kNLTFvx0Lunsak.png)

J'ai contourné en vérifiant le nom de l'instance pour que getTargetObject ne se déclenche qu'en "vraie" liste, donc ce n'est pas urgent pour nous.

Merci d'avance pour votre aide !
Emmanuelle

```
	@Override
	public String[] getTargetObject(String rowId, String[] row) {
	    
	    String target = "DemoMain";
	    
	    AppLog.info("getTargetObject getinstance " + getInstanceName(), getGrant());
		
	    String t[] = new String[3];
	    t[0] = target; // target object
	    t[1] = "the_ajax_"+target; // target instance
	    t[2] = getFieldValue("demoInlinedDemoMainId"); // target id
	    return t;

	}
```
[Platform]
Status=OK
Version=6.3.7-preview
Variant=full
BuiltOn=2026-04-01 18:33

## Answer
Bonjour,

C'est joli. Je ne comprends pas le comportement attendu puisque ton paramétrage est par construction une boucle infinie.

Le formulaire de A affiche la liste B en relation 0,1 inliné, donc la UI refait un `get` du record de B dont le `getTargetObject` redirige vers l'affichage de A... 

Fut un temps la UI ne permettait pas de parcourir/afficher récursivement les liens de l'objet inliné. Mais on avait du faire cette évolution pour adresser des besoins de voir dans la boite de pandore les "objets inlinés d'objets inlinés" ou de "panels en liste d'objets inlinés".

Bref sortir de la boucle ne peut effectivement se faire que par code au niveau du `getTargetObject` pour qu'à un moment donné B soit B.
