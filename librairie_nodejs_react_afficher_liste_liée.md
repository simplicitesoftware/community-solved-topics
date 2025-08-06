# Librairie NodeJs / React / Afficher liste liée

**URL:** https://community.simplicite.io/t/4300

## Question
Bonjour,

J'aimerais savoir s'il y'a une possibilité de récupérer une liste liée à une liste énuméré provenant du même objet métier, en utilisant la librairie npm de Simplicité.

Exemple :
1ere liste (document type) 
2ème liste (document sub type)

Lorsque je sélectionne la valeur "30", sur ma 2ème liste je souhaiterais voir apparaître la liste filtrée pour cette valeur. Plus précisément pouvoir récupérer la liste liée "DOCPROPERTYSUBTYPE"

![image|690x360](upload://kvIxWAVpBXMyn4mD2thzHWXla3e.jpeg)

Pour le moment, j'ai uniquement réussi à récupérer ces deux listes de façon globale à partir de ce code : 

```
const immoDocProperty = await app.getBusinessObject('ImmoDocProperty');
const immoDocPropertyMeta = await immoDocProperty.getMetaData();

const typeList = await immoDocProperty.getField("DocPropertyImmoDocId__documentType").listOfValues;    
const subTypeList = await immoDocProperty.getField("DocPropertyImmoDocId__documentSubType").listOfValues;

```

Merci d'avance pour votre aide.
Paul

## Answer
Ca a été ajouté dans la version 2.2.18 de la lib npm, cf. [getFieldLinkedList](https://simplicitesoftware.github.io/nodejs-api/module-simplicite-BusinessObject.html#getFieldLinkedList)

Exemple d'usage

```javascript
const list = await ctc.getFieldLinkedList('myField', 'myLinkedField', 'MYCODE1');
for (const item of list.items)
	console.log(`${item.code} (${item.value})`);
```
