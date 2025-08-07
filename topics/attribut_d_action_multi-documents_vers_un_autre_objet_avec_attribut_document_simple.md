# Attribut d'action multi-Documents vers un autre objet avec attribut document simple

**URL:** https://community.simplicite.io/t/8666

## Question
### Request description

Bonjour,

Je cherche à déposer via une action plusieurs documents via un champ `DocumentSet` multi-doc (attribut d'action) et de les répartir dans des enregistrements distincts d'un autre objet `Content`, où chaque enregistrement contiendra un attribut document unique.

Je rencontre des difficultés à mettre cela en œuvre,avec la doc j'ai réussi à faire le cas nominal d'un docSimple vers un objet avec attribut document simple 
![Capture d'écran 2024-08-27 131239|690x315, 75%](upload://6sbDyIKZqwBylUGgtnN595Fvndc.png)
mais le cas avec un attribut d'action multi-document vers un attribut document simple est compliqué . Pourriez-vous m'indiquer la meilleure façon de procéder pour atteindre cet objectif ? 
![Capture d'écran 2024-08-27 132646|690x294, 75%](upload://12sbiKLKBe9DdDdiS8AQBxg35bv.png)

J'ai essayé de voir au niveau des logs ce que getDocuments() me recupere, il me recupere bien les 2 documents mais sans ID ainsi que 4 autre documents non selectionner avec leurs ID, je dois donc mal utiliser cette méthode

Y-a-il une autre méthode ou un code générique pour ce cas générale.

Merci d'avance pour votre aide sur ce point.

Cordialement,
### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.Code action java

public String addDocumentWithLanguage(Action action) {
		
	    String lang = getGrant().getLang();
	
	    ObjectField multiDocField = action.getConfirmField(lang, "DocumentSetContent");
	    AppLog.info(getClass(), "addDocumentWithLanguage", "multiDocField: " + multiDocField , getGrant());

	    DocumentDB multiDocs = multiDocField.getDocument(); //BON
	    
	    
	    List<DocumentDB> docs = multiDocs != null ? multiDocs.getDocuments() : null;
	    
 		AppLog.info(getClass(), "addDocumentWithLanguage", "Nombre de documents récupérés: " + (docs != null ? docs.size() : 0), getGrant());
 		
 		if (docs != null) {
        for (DocumentDB doc : docs) {
            AppLog.info(getClass(), "addDocumentWithLanguage", "Document path: " + doc.getPath(), getGrant());
            AppLog.info(getClass(), "addDocumentWithLanguage", "Document rowId: " + doc.getId(), getGrant());
		        }
		    }
	   	return null;
	}
2.Log associé dans technical information


4. 

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.1.2
BuiltOn=2024-08-05 20:47
Git=6.1/467048f75ed27520b8cf7eca0ba57eeb2e0e1a0f
Encoding=UTF-8
EndpointIP=100.88.207.56
EndpointURL=http://lbc-77449-app-f4787f7fc-p9r27:8080
TimeZone=Europe/Paris
SystemDate=2024-08-27 17:42:20```
[/details]

[details="Simplicité logs"]
```text
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document rowId: 0
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document path: DOC-MULTI-2.rtf
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document rowId: 0
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document path: DOC-MULTI1.rtf
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document rowId: 18835
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document path: LbcLegalText/DocumentSetContent/0/50/CGU_ID_Connect_FR.rtf
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document rowId: 18858
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document path: LbcLegalText/DocumentSetContent/0/50/CGU_ID_Connect_FR.rtf
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document rowId: 19054
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document path: LbcLegalText/DocumentSetContent/0/50/LEBONN.rtf
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document rowId: 19106
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Document path: LbcLegalText/DocumentSetContent/0/50/LEBONN.rtf
2024-08-27 17:35:38,208|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: Nombre de documents récupérés: 6
2024-08-27 17:35:38,206|SIMPLICITE|INFO||http://lbc-77449-app-f4787f7fc-p9r27:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|addDocumentWithLanguage||Evénement: multiDocField: {"precision":0,"rendering":"MBOX","label":"Document","type":17,"fullinput":"DocumentSetContent","filter":"%","input":"DocumentSetContent","default":"","size":11,"name":"DocumentSetContent","id":"8925","value":"","oldvalue":""}```
[/details]

[details="Browser logs"]
```text
---paste content of the **relevant** browser-side logs---
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Ok si ça fonctionne, mais le code cache des erreurs
- création sans données/clé fonctionnelle puis modification, ce qui semble impossible sauf à avoir un problème de modèle (objet sans champ obligatoire ni clé fonctionnelle)
- pas de validation avant de faire le save pour controler les données, et surtout passer par les hooks pre/postValidate éventuels
- code non thread-safe : si un utilisateur ou un job asynchrone dans cette session utilise la même instance tmp, il faut synchroniser l'usage de l'instance

Exemple de code correct :

```
ObjectDB legalTextContent = getGrant().getTmpObject("LbcLegalTextContent");
synchronized (legalTextContent.getLock()) {
  try {
    // prepare the creation with row_id=0
    legalTextContent.resetValues(true, ObjectField.DEFAULT_ROW_ID);
    // legalTextContent.create(); A retirer car on ne peut pas créer un objet sans sa clé fonctionnelle unique, il y a surement des erreurs en SQL sur la user key
    // Set values
    legalTextContent.setFieldValue("LegalTextIdContent", legalTextId);
    legalTextContent.setFieldValue("LegalTextContentId", content.getRowId());
    // Save = helper pre/postValidate + preSave + pre/postCreate + postSave
    legalTextContent.getTool().validateAndSave(); 
  }
  catch (ValidateException | SaveException e) {
	return "Save error: " + e.getMessage();
  }
}
```
