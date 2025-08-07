# Mise à jour d'un attribut de liste de valeur en erreur de validation

**URL:** https://community.simplicite.io/t/4318

## Question
Bonjour,
Un traitement cron doit mettre à jour un attribut de liste énuméré dans certains cas.
La mise à jour ne fonctionne pas suite à une erreur de validation 
```
com.simplicite.objects.ladnext.LadDossiers|ValidateException||Evénement: ERR_ENUM: Statut

```

La valeur ABANDON existe : 

|Liste|Code|Ordre|Description|
|---|---|---|---|
|LADSTATUTACT|ATTENTE| 1|En attente|
|LADSTATUTACT|NOUVEAU| 2|Nouveau|
|LADSTATUTACT|INELIGIBLE| 3|Inéligible|
|LADSTATUTACT|ABANDON| 4|Abandon|
|LADSTATUTACT|NON_CONFORME| 5|Non conforme|
|LADSTATUTACT|ACCEPTE| 6|Accepté|


J'ai testé avec les autres valeurs j'ai le même résultat, la seule valeur qui semble fonctionné est la valeur de départ.

la valeur est sur la classe fille (LadDossierAct) et la recherche se fait sur l'objet parent LadDossiers.

Code :

```
        String target = "";
        String statut = "";
        switch (type){
            case "ACT": target = "LadDossierAct"; statut = "ladDossierActStatut";break;
            case "PMFP": target = "LadDossierPmfp";statut = "ladDossierPmfpStatut"; break;
            case "PME": target = "LadDossierPme"; statut = "ladDossierPmeStatut";break;
            case "OBS": target = "LadDossierFuneraire"; statut = "ladObsStatut";break;
        }

        ObjectDB messageObj;
        BusinessObjectTool messageTool;
        messageObj = getGrant().getProcessObject(target);
        //messageObj = getGrant().getProcessObject("LadDossiers");
        messageTool = messageObj.getTool();
        try {
            messageTool.getForUpsert(
                    new JSONObject()
                            .put("row_id", rowId));

            messageObj.setFieldValue(statut, statutDossier);

        } catch (GetException e) {
            AppLog.error(getClass(), "GetException", e.getMessage(), null,
                    getGrant());
        }
        try {
            messageTool.validateAndUpdate();
        } catch (ValidateException ev) {
            AppLog.error(getClass(), "ValidateException", ev.getMessage(), null, getGrant());
        } 
```

Merci pour votre aide

Version 5.1.22

Thierry

## Answer
Si votre attribut est un diagramme d'état les mises à jour doivent respecter les transitions autorisées sur le diagramme d'état (y compris les éventuelles règles additionnelles custom dans les hooks, genre dans `isStateTransitionEnable`) et le user utilisé pour faire la transition doit être habilité à effectuer cette transition.

Il n'y a rien de particulier dans le cadre d'une mise à jour effectuée tâche cron  (ou via un appel d'API ou un import I/O) => ça reste une mise à jour par un user désigné donc ça respecte les règles.
