# Surcharge du created by et update by

**URL:** https://community.simplicite.io/t/4383

## Question
Bonjour,

est ce possible de remplacer les valeurs created by et updated by par d'autres valeurs ?

Contexte :
Depuis un UI externe nous mettons à jour des données en faisant un appel des apis avec un utilisateur générique webservice. Nous voudrions remplacer le nom de cet utilisateur api par un autre.
Code :
J'ai mis le code 
```
                BusinessObjectTool objT = this.getTool();
                try {
                    if (isCreate) {
                        setFieldValue("created_by", nomprenom[0] + " " + nomprenom[1]);
                        setFieldValue("ladDossiersUserCreation", nomprenom[0] + " " + nomprenom[1]);
                    } else {
                        setFieldValue("updated_by", nomprenom[0] + " " + nomprenom[1]);
                    }

                    objT.validateAndSave();
                } catch (Exception e) {
                    AppLog.error("Erreur lors du changement d'auteur de l'action", e, g);
                }
```

dans le hook postCreate et postUpdate mais j'ai une erreur

> com.simplicite.util.exceptions.UpdateException: ERR_EXCEPTION:StackOverflowError postUpdate (null)
	at com.simplicite.util.tools.BusinessObjectTool.update(BusinessObjectTool.java:752)

Merci pour votre retour.
Cordialement

## Answer
Il y a des débat actuellement pour avoir une offre commerciale plus adaptée au cas fréquent d'un frontend externe où les utilisateurs doivent interagir ponctuellement avec le backend Simplicité de manière nominative et authentifiée (au sens où cet utilisateur est connu de Simplicité en tant que user déclaré). Je vous laisse vous rapprocher de nos équipes commerciales pour trouver une solution commerciale adaptée qui vous évite de partir dans un contournement de la licence techniquement risqué et contractuellement discutable.

Sinon pour en revenir au `created/updated_by` : c'est un mécanisme technique de la plateforme qui n'est de toute façon pas sensé être surchargé/contourné (ces attributs contiennent le login du user qui a réalisé l'opération, il ne sont pas faits pour stocker autre chose). Si vous avez besoin de stocker des éléments d' "identification" associé à vos données je vous suggère de le faire dans des attributs métier ad hoc (quitte à le mettre en "forbidden" si vous voulez que ça ne soit manipulable que du coté serveur). typiquement à valoriser dans le hook preValidate (sans faire de save surabondant)
