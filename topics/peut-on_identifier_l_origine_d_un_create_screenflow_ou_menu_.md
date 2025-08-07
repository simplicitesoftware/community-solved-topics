# Peut-on identifier l’origine d’un create (screenflow ou menu)?

**URL:** https://community.simplicite.io/t/4270

## Question
Bonjour,
Je voudrais savoir s’il était possible d’identifier l’origine d’un create dans un business object.

Je m’explique, dans la V5, nous avons maintenant la possibilité de créer un objet depuis une liste d’une étape select.

Je voudrais donc savoir dans le postCreate de l’objet, si ce create vient d’une étape d’un process ou d’un create « normal » depuis l’objet lui-même (au niveau de la liste par exemple).
Voici ce que je fais dans le postCreate de l'objet :
````
	var g = this.getGrant();
	var pcs ="ImmoCreateLease";	
   	var p = g.getProcessus(pcs, null);
	var af = p.getCurrentActivity();
	if (af!=null) {
	    var step = af.getActivity().getStep();  
		console.log("step = " + step); 
		if (step == 'P-LEASE-120-PRO-SEL') console.log("l'utilisateur crée un bien depuis le process");
	} else console.log("l'utilisateur crée un bien en dehors du process"); 	
````

Mais je me rends compte que ceci n’est pas fiable à 100%. Je donne un exemple :

Dans mon process (Screenflow), je demande la sélection d’un bien dans une liste, si l’utilisateur ne le trouve pas, maintenant, avec la V5, il peut cliquer sur « Créer » tout en restant dans le process. 

Du coup, mon contrôle de provenance dans le postCreate est presque parfait car nous avons un process en cours et on est sur le bon step (sélection des bien). 

Or, tant qu’on n’a pas enregistré ce nouveau bien, et tant qu’on est dans l’étape select du process, si l’utilisateur ouvre un autre écran est créé un bien via l’objet, sans passer par le process, le postCreate considèrera toujours qu’il vient d’un process car mon contrôle est toujours bon, or ce n’est pas le cas.

J’espère que ma question est assez clair

Merci d’avance pour votre retour.
Abed.

## Answer
Bonjour,

Il n'y aucune raison d'avoir une activité de Synchronisation dans un screenflow.
Elle sert aux processus longs qui ont des branches d'activité en parallèle. Il ne peut pas y avoir une seule activité courante dans un processus qui comporte des branches instanciées en parallèle. Ce type d'activité est purement technique et sert de "join" en attendant la réalisation de toutes les branches (activité de parallélisation / split).

A quoi sert l'activité en question ?
Essayez de la remplace par une simple activité de Condition (pour le code dans les hooks avec une seule sortie à la condition toujours vraie), ou de la retirer et de mettre son code dans le preLock de l'activité suivante.
.
