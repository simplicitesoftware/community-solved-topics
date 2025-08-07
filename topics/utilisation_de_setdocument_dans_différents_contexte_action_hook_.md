# Utilisation de setDocument dans différents contexte ( action, hook...)

**URL:** https://community.simplicite.io/t/9765

## Question
### Request description

Bonjour,

Nous rencontrons un comportement étrange concernant l’utilisation de la méthode `setDocument`.

Contexte fonctionnel :

* Nous avons deux objets métiers ,LegalText(objetA) qui peut avoir plusieurs  `LbcContent`(objetB).

* Lors d’une **action de montée de version de LegalText**, nous dupliquons le record, et à cette occasion, nous dupliquons aussi ses contenus en copiant les documents via `setDocument(...)`. Dans ce cas, **tout fonctionne parfaitement** : les documents PDF et DOCX sont bien copiés dans les nouveaux contenus et  relié au contenu du new LegalText ,

 [details="code lancé depuis action"]

```
    ObjectDB oldContent = g.getTmpObject("LbcContent");
	     if (!oldContent.select(oldContentId)) {
	            AppLog.error(getClass(), "duplicateContentsFromLegalText", "Contenu introuvable (ID=" + oldContentId + ")", null, g);
	            continue;
	        }	
	    String contentLanguage = oldContent.getFieldValue("ContentLanguage");
		DocumentDB docPdf = oldContent.getField("ContentDocPdf").getDocument(g);
		DocumentDB docRtf = oldContent.getField("ContentDocRtf").getDocument(g);

     ObjectDB newContent = g.getTmpObject("LbcContent");
			newContent.resetValues(true);
			newContent.setFieldValue("ContentLanguage", contentLanguage);
			
			// Traitement du PDF 
			if (docPdf != null) {
			    String fileName = docPdf.getName();
			    byte[] fileBytes = docPdf.getBytes(true); 

			    newContent.getField("ContentDocPdf").setDocument(newContent, fileName, fileBytes);
			    AppLog.info(getClass(), "duplicateContentsFromLegalText", "PDF copié : " + fileName, g);
			}
```
[/details]

* En revanche, dans un autre cas d’usage où un `LegalText` est publié( changement de status), nous créons automatiquement des record du `LegalText`depuis le hook `postSave` . Ces records doivent également récupérer les contenus via duplication (`setDocument(...)`) dans un nouveau `LbcContent` à chaque fois.

* Dans ce deuxième cas (hook `postSave`), les objets `LbcContent` sont bien créés, les champs métiers sont correctement remplis, **mais les documents PDF et DOCX ne sont jamais définis** malgré l’appel explicite à `setDocument(...)`.
* Nous avons vérifié via `AppLog` que :
  * Les objets sources contiennent bien des documents valides ( avec un docID)
  * `setDocument` est bien appelé avec les bons paramètres.
  * Aucun message d’erreur ne s’affiche, mais les documents ne sont pas enregistrés dans la nouvelle instance de `LbcContent`.
  
 [details="logs entre sourceContent et copyContent lancé depuis un hook"]
```text
Content dupliqué pour adaptation 772 | Langue : fr
2025-04-03 16:35:09,714|SIMPLICITE|INFO||http://lbc-77449-app-767f4598f6-zbqpx:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|createContentsForAdaptation||Evénement: COPY content (ID=1178) :
    - Langue : fr
    - ContentDocPdf :
    - ContentDocRtf :
    - ContentSPId :
    - ContentSP :
    - ContentLocalProductName :
2025-04-03 16:35:09,714|SIMPLICITE|WARN||http://lbc-77449-app-767f4598f6-zbqpx:8080||WARN|p124722|com.simplicite.objects.RenaultLBC.LbcContent|postSave||Evénement: Aucun fichier à envoyer vers SharePoint
2025-04-03 16:35:09,704|SIMPLICITE|INFO||http://lbc-77449-app-767f4598f6-zbqpx:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|createContentsForAdaptation||Evénement: SOURCE content (ID=1158) :
    - Langue : fr
    - ContentDocPdf : 48649
    - ContentDocRtf : 48648
    - ContentSPId : f6427d83-0593-4f40-bbfd-87babeb442f5
    - ContentSP : https://grouperenault.sharepoint.com/sites/

```

[/details]

Nous nous demandons donc si ce comportement est :

1. **Lié à l’utilisation d’un hook** pour effectuer la duplication d'un document ?

3. Ou si c’est une limitation ou différence de contexte d'exécution ?

5. Ou bien s’il y a des considérations spécifiques pour les documents binaires dans ce type de logique métier ?

À noter également : nous avions déjà observé des comportements similaires dans des tests passés, où **des actions asynchrones** échouaient elles aussi à définir des documents avec `setDocument(...)`.

Merci d’avance pour votre éclairage sur ce point. 

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
```
[/details]

[details="Simplicité logs"]
```text
---paste the content of the **relevant** server-side logs---
```
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
Bonjour,

Une action asynchrone est lancée dans un thread du pool asynchrone.
Donc rien ne garantit que les données du popup de l'action soit encore en mémoire au moment où le job y accède. 

Dans le cas d'une action avec document, le fichier posté est stocké temporairement sur le serveur, il faut passer par `doc.getUploadFile()` pour y accéder. Simplicité évite au maximum de monter les fichiers en mémoire de la JVM (getBytes sera surement vide).

Le bon design pattern est effectivement de rendre l'action synchrone pour lire les données saisie en front, et d'y lancer un job asynchrone, par exemple :

```java
// Action paramétrée en synchrone
public String myAction(Action action) {
  // Action data from UI
  ObjectField myDocField = action.getConfirmField("myDocField");
  DocumentDB doc = myDocField!=null ? myDocField.getDocument() : null;
  final java.io.File tmpFile = doc!=null ? doc.getUploadFile() : null;

  if (tmpFile!=null) {
    // Launch a job
    JobQueue.push("myJob", new Runnable() {
      @Override
      public void run() {
         // do something with the file (using a stream)
         // finally delete the tmp file
         tmpFile.delete();
      }
    });
  }
  return null;
}
```

on peut aussi utiliser un  `AsyncTracker` pour que l'utilisateur suive la progression de l'import : le job doit écrire dans le tracker, et le front affichera la progression, l'utilisateur pourra demander l'arrêt, etc.

cf
https://docs.simplicite.io/docs/core/custom-actions-examples
