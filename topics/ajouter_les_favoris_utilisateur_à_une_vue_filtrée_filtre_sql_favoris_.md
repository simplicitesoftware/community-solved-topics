# Ajouter les favoris utilisateur à une vue filtrée (Filtre SQL + favoris)

**URL:** https://community.simplicite.io/t/10418

## Question
### Request description
👋 Bonjour,

Je souhaite créer une **vue filtrée** dans mon objet qui affiche :

1. les enregistrements **créés par l'utilisateur connecté**
2. ou **dont il est contributeur** (via les colonnes `legal_text_person_id`, `legal_text_publisher_id`, ou des champs texte comme `legal_text_juridique_contributor`, `legal_text_business_contributor` qui peuvent contenir plusieurs row_id séparés par `;`)

4. **et également ses favoris**, même s’il n’est pas contributeur ni créateur.

### 🔍 Pour les contributeurs et créateurs, voici le filtre SQL que j’utilise dans le champ `Filtre additionnel SQL` (`vwi_search_spec`) :
![image|690x228, 50%](upload://5EBMVJOI68ozas8K3mtVDSV9wRC.png)

```
(
  t.created_by = [LOGIN]
  OR t.legal_text_person_id = [USERID]
  OR t.legal_text_publisher_id = [USERID]
  OR t.legal_text_juridique_contributor LIKE CONCAT('%', [USERID], '%')
  OR t.legal_text_business_contributor LIKE CONCAT('%', [USERID], '%')
)
```

Ce filtre fonctionne correctement.

### ❓ Problème :

Je voudrais **ajouter les favoris** de l'utilisateur **même si le record ne correspond pas aux critères ci-dessus**.

Or :

* Les favoris ne sont pas stockés dans les colonnes de l’objet 
* Ils sont gérés côté UI, via les préférences utilisateurs (icône étoile)
* Et comme vu dans les paramètres utilisateur, chaque **vue d’accueil** a ses propres favoris

---

### 📷 Voici ce que je constate :
  ![image|297x500, 50%](upload://l3onvFsh9IPpOG6wz7sTXGyyvv6.jpeg)

* Les favoris sont bien visibles quand je consulte la **liste complète (non filtrée)** et les bons records filtré sont aussi en favoris dans la liste filtré
* Mais dès que j’applique un **filtre SQL**, seuls les enregistrements correspondant au filtre apparaissent, **meme cas pour les favoris** 

Auriez-vous une idée de comment gérer ce besoin de filtre sur un objet avec en + les favoris lié au user ?

En attente d'un retour, à bientot !


### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.2.10
BuiltOn=2025-05-23 10:17
Git=6.2/db71f45b7b47f1aea2d669dc5b22c5369ec75d92
Encoding=UTF-8
EndpointIP=100.88.228.130
EndpointURL=http://lbc-77449-app-8ddbc79cf-cl52t:8080
TimeZone=Europe/Paris
SystemDate=2025-07-28 15:52:17

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://ldm-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=2
TotalUsers=304
EnabledUsers=16
LastLoginDate=2025-07-28 15:44:26

[Server]
ServerInfo=Apache Tomcat/9.0.105
ServerType=WEB
ServerDevMode=false
ServerCompiler=true
ServerActiveSessions=2
ServerSessionTimeout=30
CronStarted=true
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
[quote="Hamza, post:1, topic:10418"]
`t.created_by = [LOGIN]`
[/quote]

Cette syntaxe me semble invalide car LOGIN est un String donc plutôt à mettre entre quote, mais peut être que le parser est malin et les ajoute en escapant le login en SQL.

`t.created_by = '[LOGIN]'`

Sinon pour avoir les bookmarks, ils sont persistés en base au niveau des paramètres du User par scope/accueil, et monté en session dans un objet JSON qu'on peut convertir en SQL

![image|690x243](upload://nsWuTObl1jOwP3l5b98J7tXGDmR.png)
 
Par exemple 

```java
// convert JSON bookmarks to 't.row_id in (10,23,543...)'
String bm = "";
// object bookmarks in current session/scope
JSONObject o = getGrant().getBookmarks().find(obj.getName());
// List of bookmarks
JSONArray a = o!=null ? o.optJSONArray("b", null) : null;
if (a!=null) {
	for (int i=0; i<a.length(); i++) {
		if (i>0) bm += ",";
		bm += a.getJSONObject(i).optString("id");
	}
}
// add to searchspec / additionnal search spec / view filters...
if (bm.length()>0)
   obj.setSearchSpec("... or t.row_id in (" + bm + ")");
```
