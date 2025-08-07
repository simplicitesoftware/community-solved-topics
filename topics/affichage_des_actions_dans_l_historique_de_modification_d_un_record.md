# Affichage des actions dans l'historique de modification d'un record

**URL:** https://community.simplicite.io/t/9414

## Question
### Request description

Bonjour ,

Nous avons un objet avec différentes actions,nous aimerions que lorsqu'un utilisateur les exécute, elles apparaissent dans l'historique de modification (notamment l'import de document et les transitions d'état). Nous avons réfléchi aux solutions possibles pour assurer l'affichage dans l'historique pour ses deux cas précis :

**Action import de document :**

L'action d'import permet de déposer des documents dans un objet `Content` ayant une relation N:N avec notre objet A. Étant donné que l'enregistrement se trouve dans un autre objet, j'ai pensé à ajouter un attribut non visible (persisté ?) dans l'objet A, qui serait mis à jour avec le nom de l'action exécutée. 

Cela permettrait de conserver une trace de l'action dans l'historique des modifications.
Je me demande si cette approche est viable, voire la plus adaptée, ou s'il existe une meilleure méthode pour afficher cette action dans l'historique.

**Action de transition d'état :**

Ses actions liées aux transitions d'état apparaissent bien dans l'historique, probablement parce qu'elles modifient directement le record.

Cependant, l'une des transitions d'état (de **Draft** vers **Validé**) est liée à une action back-end qui effectue une mise à jour en base de données pour définir la date d'application via une requête SQL:
![image|690x354, 50%](upload://kCxAqHO4LokwmvDe16zzQoj6UeN.png)

Ici, le set de la date ne s'affiche pas dans l'historique de modification,
![image|690x486, 50%](upload://vgspS88YWr52igDufbyAyrYnNS0.png)
peut-être en raison du fait que je mets à jour directement la date en base de données sans utiliser les méthode de l'API Simplicité.., Voici le code de l'action : 
[details="Action transtion draft vers validé"]
```text
public String updateDraftToValidate(Action action) {
	    String legalTextId = getRowId();
	    String lang = getGrant().getLang();
	    String legalTextStatut = this.getFieldValue("LegalTextStatut");
	
	    ObjectField applicableFromField = action.getConfirmField(lang, "lbcConfirmAdaptationApplicableFrom");m
	    String applicableFrom = applicableFromField != null ? applicableFromField.getValue() : null;
	    String currentDateStr = Tool.getCurrentDate(); // Format interne "yyyy-MM-dd"

	
	    try {
	        if (applicableFrom != null && !applicableFrom.isEmpty()) {
	            String applicableFromInternal = Tool.dateFromFormat(applicableFrom, "yyyy-MM-dd");
	
	            if (applicableFromInternal.compareTo(currentDateStr) <= 0) {
	                String errorMessage = "FRA".equals(lang)
	                    ? "Impossible : Choisissez une date supérieure ou égale à la date du jour."
	                    : "Impossible: Choose a date greater than or equal to today's date.";
	                return errorMessage; 
	            }
	        } else {
	            return "Erreur : La date d'application n'est pas renseignée.";
	        }
	    } catch (Exception e) {
	        AppLog.error(getClass(), "updateDraftToValidate", "Erreur lors de la gestion des dates: " + e.getMessage(), null, getGrant());
	        return "Erreur : Impossible de traiter la date.";
	    }
	
	    try {
	        if (applicableFrom != null && !applicableFrom.isEmpty()) {
	            String updateSql = "UPDATE lbc_legal_text SET legal_text_applicable_from = '" + applicableFrom + "' WHERE row_id = " + legalTextId;
	            getGrant().update(updateSql);
	        }
	    } catch (Exception e) {
	        AppLog.error(getClass(), "updateDraftToValidate", "Erreur lors de la mise à jour de LegalTextApplicableFrom: " + e.getMessage(), null, getGrant());
	        return "Erreur : Impossible de mettre à jour la date d'application.";
	    }
	
	    return null; 
	}```
[/details]



En synthèse, auriez-vous des recommandations pour ses 2 type d'actions à afficher dans l'historique pour :

1. Garantir que toutes les actions, y compris celles sur des objets liés soient visibles dans l'historique de modification ?

2. S'assurer que les mises à jour effectuées directement en base soient correctement prises en compte dans l'historique ?(utiliser un setFieldValue au lieu d'update peut-être )

Merci d'avance pour vos retours et suggestions :slight_smile: 

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.1.20
BuiltOn=2025-01-16 10:03
Git=6.1/d9a92766ff23ed5933a93a0d0f4811903b25cad1
Encoding=UTF-8
EndpointIP=100.88.233.23
EndpointURL=http://lbc-77449-app-576fdf68f5-6qtpc:8080
TimeZone=Europe/Paris
SystemDate=2025-01-21 16:40:11

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=304
EnabledUsers=10
LastLoginDate=2025-01-21 14:44:52---
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

Pour s'assurer que l'exécution d'une action sur un objet lié soit correctement enregistrée dans l'historique de l'objet parent, je pense qu'ajouter un attribut invisible dans l'objet parent et de modifier sa valeur à chaque déclenchement de l'action est une bonne solution. Il faudra utiliser [BusinessObjectTool.validateAndSave(true, true)](https://platform.simplicite.io/6.1/javadoc/com/simplicite/util/tools/BusinessObjectTool.html#validateAndSave(boolean,boolean)) pour créer l'historique. 

Concernant le deuxième point, il est fortement déconseillé de manipuler directement la base de données, `setFieldValue` sera toujours la solution recommandée, avec toujours le param `undoredo` a `true` dans le `validateAndSave` pour créer l'historique.
