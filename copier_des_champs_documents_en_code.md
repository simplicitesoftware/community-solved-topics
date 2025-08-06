# Copier des champs documents en code

**URL:** https://community.simplicite.io/t/4737

## Question
### Request description

Bonjour,

Sur ce topic, je souhaitais copier les champs d'un objet dans un autre : https://community.simplicite.io/t/copier-lintegralite-dun-objet-metier-via-le-code-sans-copier-les-champs-1-par-1/4730

La solution marchait pour tous les champs que j'avais sauf 1 type de champ : les champs documents. Ces champs là ne sont pas copiés.

**Une idée du problème ?**

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.1.39
BuiltOn=2022-04-13 18:24
Git=release/e929cbae23c2441b4cb0a66b9501de0159ee7c92
Encoding=UTF-8
EndpointIP=10.201.117.43
EndpointURL=http://siparex-simplicite-dev-745fcf686c-ptkfp:8080
TimeZone=Europe/Paris
SystemDate=2022-04-20 10:29:26
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Bonjour Corentin, 

Vous pouvez intégrer à votre code les éléments suivants (lorsque vous bouclez sur les attributs à copier) :
```java
if(f.isMultiDocuments()){
	DocumentDB copiedDocs = copyAndGetDocuments(this, f, getRowId(), targetRowId);
	obj.getField(f.getName()).setDocument(copiedDocs);
	obj.getField(f.getName()).setValue(""); // cross reference not used
}
```

Avec `copyAndGetDocuments(...)` comme suit : 
```java
private DocumentDB copyAndGetDocuments(ObjectDB obj, ObjectField f, String rowId, String targetRowId){
	
	DocumentDB currentDocs = DocumentDB.getDocuments(obj, f, rowId);
	DocumentDB newDocs = new DocumentDB(true); //instantiate a multi-doc DocumentDB object
	if (currentDocs!=null) {
		List<DocumentDB> list = currentDocs.getDocuments();
		if (list!=null)
			for (DocumentDB d : list){
				try{
					DocumentDB newDoc = new DocumentDB(null, d.getName(), d.getBytes(true), getName(), f.getName(), targetRowId); //create a new DocumentDB per document found in list
					newDoc.setStatus(DocumentDB.STATUS_TO_UPLOAD);
					newDocs.add(newDoc); //add to list of documents
				}
				catch(IOException e){
					//handle IOException
				}
			}
	}
	return newDocs;
}
```
