# Créer une copie de formulaire via une action

**URL:** https://community.simplicite.io/t/8902

## Question
Bonjour,

J'ai besoin de dupliquer un formulaire avec certaines conditions :

1. Certaines valeurs sont copiées telles quelles
2. Certaines valeurs sont supprimées sur la copie
3. Certaines valeurs sont placées dans d'autres champs
4. Certaines valeurs sont définies par l'utilisateur au lancement de la copie (par exemple l'année concernée, la date d'acquisition, etc.)

Actuellement j'ai la méthode initCopy qui me permet les points 1-3, mais il faut que je rajoute le point 4 et je pense que ça passe par une action.

Est-ce que je peux déclencher le initCopy via une action?

```
	@Override
	public void initCopy(){
		AppLog.info(getClass(), " le initCopy a été appelé :::::  ", getFieldValue("ParticipationTitreAnnee") ,  getGrant());
	    calculTitreId();
	    valeurParDefautCopie();
	
	}

```

```
	public void valeurParDefautCopie(){
		AppLog.info(getClass(), " la définition des valeurs par défaut à la copie a été appelée", null ,  getGrant());
		
		//défini l'année suivant celle du titre copié
 	    String annee = getFieldValue("ParticipationTitreAnnee");
 	    int newyear = Tools.nouvelleAnnee(1,annee);
        setFieldValue("ParticipationTitreAnnee",newyear);
        
    	setFieldValue("ParticipationTitreNbTitreVille",getFieldValue("ParticipationTitreNbTitreVilleTotal"));
        setFieldValue("ParticipationTitreSoldeAu1",getFieldValue("ParticipationTitreSoldeActuel"));
        setFieldValue("ParticipationTitreEtatFinFondsPropresN1",0);
        setFieldValue("ParticipationTitreReevDep",0);
        setFieldValue("ParticipationTitreCours",0);
        setFieldValue("ParticipationTitreMontantDivAnneePrec",getFieldValue("ParticipationTitreMontantDiv"));
        setFieldValue("ParticipationTitreMontantDiv",0);
        setFieldValue("ParticipationTitreTauxRendementAnneePrec",getFieldValue("ParticipationTitreTauxRendement"));
        setFieldValue("ParticipationTitreValeurVenaleSubstAnneePrec",getFieldValue("ParticipationTitreValeurVenaleSubst"));
        setFieldValue("ParticipationTitreValeurVenaleBoursiereAnneePrec",getFieldValue("ParticipationTitreValeurVenaleBoursiere"));
        setFieldValue("ParticipationTitreEcartVvVc0101",getFieldValue("ParticipationTitreEcartVvVc3112"));
        setFieldValue("ParticipationTitreEcartVnVc0101",getFieldValue("ParticipationTitreEcartVnVc3112"));
	}

```

Merci d'avance

Fabrice

## Answer
Bonjour,

[quote="fabrice, post:3, topic:8902"]
Une fois la copie réalisée, tous les champs du formulaire original sont verrouillés
[/quote]

Plutôt qu'une action qui va réinventer la roue, il faut à mon avis pour gérer cette notion de "versionning" de record :

- positionner un champ/verrou dans une colonne sur votre précédent record lors de la création par recopie au `postCreate`
- ce champ sera utilisé par le hook `isUpdateEnable` pour interdire la mise à jour.

Par exemple :

```java
public String postCreate() {
  // Lock the original record
  String originId = getCopyId();
  if (isCopied() && !Tool.isEmpty(originId)) {
     getGrant().update("update mytable set myrecordlock='1' where row_id="+Tool.toSQL(originId));
  }
  return super.postCreate();
}

public boolean isUpdateEnable(String row[]) {
   // Denied locked records
   if ("1".equals(getFieldValue("myRecordLock", row)))
     return false;
   return super.isUpdateEnable(row);
}
```
