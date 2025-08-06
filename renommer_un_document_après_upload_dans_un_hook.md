# Renommer un document après upload dans un hook

**URL:** https://community.simplicite.io/t/9859

## Question
### Request description

Bonjour,

Je rencontre un souci lors de la tentative de renommage dynamique de documents lié à un objet `Content`, déclenché par un changement sur un objet parent `LegalText`.

---

### 🔍 Contexte :

* Chaque `Content` contient deux documents : un `.docx` (`ContentDocRtf`) et un `.pdf` (`ContentDocPdf`).

* Une méthode `setDocumentName(String ext)` génère dynamiquement un nom correct pour chaque document.

* J'appelle cette logique dans une méthode `renameAssociatedDocuments()` (appelée dans `initUpdate()` de `LegalText`).

---

### 🧪 méthode dans l'initUpdate :

```
private void renameAssociatedDocuments() {
		String sql = "SELECT legal_text_content_id FROM lbc_legal_text_content WHERE legal_text_id_content = " + getRowId();
		String[] contentIds = getGrant().queryFirstColumn(sql);
	
		if (contentIds == null || contentIds.length == 0) return;
	
		LbcContent content = (LbcContent) getGrant().getTmpObject("LbcContent");
	
		for (String contentId : contentIds) {
			content.resetValues();
			if (content.select(contentId)) {
				try {
					
					String docxName = content.setDocumentName("docx");
					String pdfName = content.setDocumentName("pdf");
	
					AppLog.info(getClass(), "renameAssociatedDocuments", "Renommage Content ID=" + contentId + " → " + docxName + " / " + pdfName, getGrant());
					if (content.getField("ContentDocRtf").getDocument() != null) {
						String oldDocxName = content.getField("ContentDocRtf").getDocument().getName();
											 content.getField("ContentDocRtf").getDocument().setName(""+docxName+"");
						String newDocxName = content.getField("ContentDocRtf").getDocument().getName();
					
						AppLog.info(getClass(), "renameAssociatedDocuments",
							"\n[Content ID=" + contentId + "]" +
							"\nDOCX avant : '" + oldDocxName + "'" +
							"\nDOCX après : '" + newDocxName + "'",
							getGrant());
					}
					// PDF
					if (content.getField("ContentDocPdf").getDocument() != null) {
						String oldPdfName = content.getField("ContentDocPdf").getDocument().getName();
						content.getField("ContentDocPdf").getDocument().setName(pdfName);
						String newPdfName = content.getField("ContentDocPdf").getDocument().getName();
					
						AppLog.info(getClass(), "renameAssociatedDocuments",
							"\n[Content ID=" + contentId + "]" +
							"\nPDF avant : '" + oldPdfName + "'" +
							"\nPDF après : '" + newPdfName + "'",
							getGrant());

					}
					content.setFieldValue("ContentLocalProductName","TestDocName");
					AppLog.error("content value 0001:"+	content.getFieldValue("ContentLocalProductName"), e, getGrant());
					content.update();


				} catch (Exception e) {
					AppLog.error(getClass(), "renameAssociatedDocuments", "Erreur lors du renommage du content " + contentId, e, getGrant());
				}
			}
		}
	}
```

---

### ✅ Logs Simplicité :

Les logs indiquent que le nouveau nom est bien défini, **mais** lors du téléchargement depuis l’interface, **le nom n’a pas changé** : on retrouve toujours `document_sharepoint.docx` ou `documentPDF_sharepoint.pdf`( qui est le nom du doc en dur recuperer depuis un callAPI).
![image|690x229, 75%](upload://fZOdSJFkoD3Jx9Eek2n8js7pitF.png)

Le setFieldValue sur un attribut String est bien pris en compte dans le record ( vérification entre cette string et le nom d'un document pour retirer ce doute)
```
2025-04-25 12:39:43,725|SIMPLICITE|ERROR||http://lbc-77449-app-689d875dcc-p6r84:8080||ERROR|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|renameAssociatedDocuments||
Evénement: content value 0001:TestDocName
2025-04-25 12:39:43,725|SIMPLICITE|INFO||http://lbc-77449-app-689d875dcc-p6r84:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|renameAssociatedDocuments||
Evénement:
    [Content ID=1301]
    PDF avant : 'documentPDF_sharepoint.pdf'
    PDF après : 'M - Alpine - Conditions of use - MyDaciaWeb - 2025-04-22.pdf'
2025-04-25 12:39:43,725|SIMPLICITE|INFO||http://lbc-77449-app-689d875dcc-p6r84:8080||INFO|p124722|com.simplicite.objects.RenaultLBC.LbcLegalText|renameAssociatedDocuments||
Evénement:
    [Content ID=1301]
    DOCX avant : 'document_sharepoint.docx'
    DOCX après : 'M - Alpine - Conditions of use - MyDaciaWeb - 2025-04-22.docx'
```


---

### ❓ Question :

Est-ce que l’appel à `setName()` sur `getField(...).getDocument()` est **la bonne manière de renommer un document** ? 

Faut-il appeler une autre méthode pour forcer la mise à jour du nom ? Ou est-ce que cela ne fonctionne que **lors de l’injection initiale du fichier via `setDocument(...)`** ? 

En attente d'un retour à bientot :slight_smile: 

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

A priori le "save/update" de l'objet ne changera pas le nom d'un document ce cette manière.
Il faut plutôt forcer un upload d'un nouveau document basé sur l'ancien, du style :

```java
DocumentDB a = getField("fieldName").getDocument();
DocumentDB b = new DocumentDB("0", "newName.pdf", a.getInputStream(), "ObjectName", "fieldName", rowId);
getField("fieldName").setDocument(b);
update();
```
