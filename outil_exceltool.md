# Outil ExcelTool

**URL:** https://community.simplicite.io/t/5643

## Question
Bonjour, 
je souhaite mettre à jour mes fonctions utilisant ExcelPOITool vers ExcelTool, mais je ne trouve aucun tutoriel sur cette classe.

Je penses avoir réussi à créer une "sheet" mais je ne vois pas comment ajouter des lignes comme je le faisais sur l'ancienne classe.
```
ExcelTool ex = new ExcelTool(true);
var sheet = ex.addSheet("Reporting");
int line = 0;
//
for(String[] row : fin_info.search()){
	// sheet.addFullRow(line++, row); // avec ExcelPOITool
}
```

Bonne journée,
Paul-alexandre

## Answer
Bonjour, 

Il y a un exemple de l'utilisation d'ExcelTool dans le module Demo disponible sur l'App Store. 

```java
[...]
ExcelTool xls = new ExcelTool(true); // true = XLSX format
Sheet sheet = xls.addSheet("Contacts");
for (int i = 0; i < rows.size(); i++) {
	ExcelRow r = new ExcelRow(i);
	String[] row = rows.get(i);
	for (int j = 0; j < row.length; j++) {
		r.add(xls.newCell(j, row[j]));
	}
	xls.addRow(sheet, r);
}
[...]
```
