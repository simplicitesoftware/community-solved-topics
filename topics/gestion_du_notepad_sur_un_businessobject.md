# Gestion du Notepad sur un BusinessObject

**URL:** https://community.simplicite.io/t/13431

## Question
### Request description

Bonjour , 
afin d'anticiper la dépréciation de `BusinessObjetTool`, quelle serait la méthode recommandée pour ajouter une entrée de bloc-notes avec la nouvelle API `BusinessObject` ? 

Je n'ai pas trouvé de méthode similaire à `getField()` dans la nouvelle api. 

Je fournis ici un exemple simplifié sur le module Démo (sur le sim en 6.3): 

avec `getTool()` : 
```
@BusinessObjectAction
	public String increaseStock(Map<String, String> params) {
		try {
			int inc = Tool.parseInt(params.get(INCREMENT_FIELDNAME), DEFAULT_INCREMENT);
			if (inc > 0) {
				ObjectField s = getField(STOCK_FIELDNAME);
				s.setValue(s.getInt(0) + inc);
				getField("demoPrdComments").addNotepad(getGrant().getFullName(), "Stock was increased");
				getTool().validateAndSave();
				// Log
				AppLog.log("DEMO_INFO", getClass(), "increaseStock", "Stock for " + getFieldValue(REFERENCE_FIELDNAME) + " is now " + s.getValue(), getGrant());
				// User message
				return Message.formatSimpleInfo("DEMO_PRD_STOCK_INCREASED", s.getValue());
			} else {
				return Message.formatSimpleError("DEMO_PRD_ERR_INCREMENT", String.valueOf(inc));
			}
		} catch (Exception e) {
			return Message.formatSimpleError(e);
		}
	}
```
avec BusinessObject API :
```
@BusinessObjectAction
	public String increaseStock(Map<String, String> params) {
		try {
			int inc = Tool.parseInt(params.get(INCREMENT_FIELDNAME), DEFAULT_INCREMENT);
			if (inc > 0) {
				String rowId = getRowId();
				int updatedStock = getField(STOCK_FIELDNAME).getInt(0) + inc;
				try (com.simplicite.util.BusinessObject bo = getGrant().getBusinessObject(getName())) {
					bo.forUpdate(rowId)
						.withValue(STOCK_FIELDNAME, String.valueOf(updatedStock))
						/** Tentative non-concluante */
						.then(obj -> {
							obj.getField("demoPrdComments").addNotepad(getGrant().getFullName(), "Stock was increased");
						})
						/* */
						.validateAndSave();
				}
				// Log
				AppLog.log("DEMO_INFO", getClass(), "increaseStock", "Stock for " + getFieldValue(REFERENCE_FIELDNAME) + " is now " + updatedStock, getGrant());
				// User message
				return Message.formatSimpleInfo("DEMO_PRD_STOCK_INCREASED", String.valueOf(updatedStock));
			} else {
				return Message.formatSimpleError("DEMO_PRD_ERR_INCREMENT", String.valueOf(inc));
			}
		} catch (Exception e) {
			return Message.formatSimpleError(e);
		}
	}
```

## Answer
_No answer provided._
