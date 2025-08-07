# Ajouter une action de redirection vers une URL externe depuis le domaine ou une page d'accueil

**URL:** https://community.simplicite.io/t/10398

## Question
### Request description

Bonjour,

Nous aimerions ajouter une action permettant de rediriger l’utilisateur vers une URL externe (par exemple un portail d’aide), soit :

* directement via le **menu principal du domaine**,
![image|191x213](upload://sf4wniPQYJ0zz20yR2hxrYd11AN.png)

* soit via un **bouton ou une action visible sur la page d'accueil**.
![image|690x167](upload://k2DWCiW2ZRQU5R1yT3vFSgtwXLV.jpeg)


#### Objectif :

Permettre un accès rapide à une ressource externe (type portail d’aide/documentation) sans passer par un objet métier.

#### Questions :

* Quelle est la meilleure pratique pour cela dans Simplicité ? J'ai pensé à une action mais celle-ci doit etre lié à un objet pour etre mise dans un domaine. Pareil dans la Landing page mais pas la possibilité de mettre des actions.

Merci d’avance pour vos conseils !

### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.2.10
BuiltOn=2025-05-23 10:17
Git=6.2/db71f45b7b47f1aea2d669dc5b22c5369ec75d92
Encoding=UTF-8
EndpointIP=100.88.208.82
EndpointURL=http://lbc-77449-app-58fb86f965-h4jw8:8080
TimeZone=Europe/Paris
SystemDate=2025-07-22 17:53:43

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://ldm-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=0
TotalUsers=304
EnabledUsers=16
LastLoginDate=2025-07-22 15:29:53

[Server]
ServerInfo=Apache Tomcat/9.0.105
ServerType=WEB
ServerDevMode=false
ServerCompiler=true
ServerActiveSessions=0
ServerSessionTimeout=30
CronStarted=true---
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
Bonjour Hamza,

Vous pouvez ajouter l'action via [des objets externes](https://docs.simplicite.io/make/userinterface/externalobjects/uicomponent).

**Pour l'ajouter dans le menu** :
1.  Avec le champ URL pour ouvrir le portail au sein de l'interface utilisateur.
2.  Via la ressource JavaScript pour une redirection complète.
```
async render(params, data = {}) {
	let url ='https://docs.simplicite.io/';
	document.location.replace(url);
}
```
3. Ajouter l'objet dans le menu
![image|690x423](upload://4HNe6lGzewLjIpzcomuGWInRPjt.png)


**Depuis la page d'accueil** : Vous pouvez créer votre encart en HTML, CSS et JavaScript via les ressources , puis l'ajouter à votre page d'accueil.

![image|690x370](upload://tf2LQi2wGYTChlpLKF9if7ySHZy.png)
![image|681x500](upload://zM8rFigDCKslidwQ8NdDRJg5NYL.png)

De plus, la notion de **raccourcis** pourrait correspondre à votre besoin :

![image|689x440](upload://1kxTYcBFO33ZcR0qD7N0r53Tt2N.png)

1. L'URL de votre portail.
2. Afficher le raccourci dans le menu en haut à droite.
3. Afficher le raccourci dans l'en-tête (5).
5. Afficher le raccourci dans l'encart des raccourcis des pages d'accueil.
Dans une vue, vous avez la possibilité d'afficher les raccourcis habilités pour l'utilisateur.
![image|597x500](upload://133wwqWD7f9c7RniVlZaFceQSKr.png)
