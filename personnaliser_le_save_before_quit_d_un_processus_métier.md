# Personnaliser le "SAVE_BEFORE_QUIT" d'un processus métier

**URL:** https://community.simplicite.io/t/9183

## Question
Bonjour, 

Nous avons actuellement depuis la 6.1.16 sur simplicité cette fonctionnalité lorsque l'utilisateur tente de quitter un processus sans l'avoir terminé : 
![image|558x180](upload://bEU5c07xFKLjOBTkLO5ikMChfXb.png)

Nous aimerions pouvoir custom ce message afin de l'adapter aux  besoins métier et aux exigences UX. :slight_smile: dont un des rendu spécifié est le suivant :

![image|689x355, 50%](upload://pfFz3BXuvEUbKDVN8QQptP0nNO9.jpeg)

* Pour personnaliser les boutons, je prévois de mettre un coup de css pour ne garder que 2 boutons, mais je n'ai pas encore trouvé une approche propre et efficace pour implémenter cela. (ou mettre cette ressource dans la responsive5 ou une autre ?..)

* Les styles sont applicables dans le thèmes chargés ce n'est pas bloquants.

* Existe-t-il aussi une méthode dans l'API Simplicité pour personnaliser le texte ?


La fonctionnalité vient de sortir, nous essayons de prendre les bonnes pratiques dès le départ concernant cette nouvelle feature :)


Merci d'avance pour vos retours et conseils !

[details="Instance /health"]
```text
--- [Platform]
Status=OK
Version=6.1.16
BuiltOn=2024-11-29 13:53
Git=6.1/4d1040b907ab4a5824903e1a31d91364f29ce7f6
Encoding=UTF-8
EndpointIP=100.88.233.215
EndpointURL=http://lbc-77449-app-6cf56d9fd-frqh9:8080
TimeZone=Europe/Paris
SystemDate=2024-12-04 16:09:58

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=302
EnabledUsers=23
LastLoginDate=2024-12-04 15:55:03

[Server]
ServerInfo=Apache Tomcat/9.0.97
ServerType=WEB
ServerActiveSessions=1
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
[quote="Hamza, post:4, topic:9183"]
`MutationObserver`
[/quote]

Bonjour,

Merci pour ton partage. Utiliser un MutationObserver est pratique pour ajouter du code sur des événements du DOM s'il n'y a pas de hook ou handler prévu. Mais bon c'est assez lourd à maintenir.

Vous pouvez utiliser `$grant` au lieu de `$ui.getGrant()`.

Sinon il serait plus simple de passer par du simple CSS mais il manque un élément de contexte pour cibler ce dialogue sur ce processus.
On devra ajouter un `data-context` au dialogue avec le nom du processus ou de l'objet.
Cela devrait vous permettre d'alléger votre code avec du pur CSS, comme par exemple :

```css
#dlgmodal_saveBeforeQuit[data-context=MyProcessName] .btn-SAVE{ display: none }
#dlgmodal_saveBeforeQuit[data-context=MyProcessName] .btn-QUIT { display: none }
#dlgmodal_saveBeforeQuit[data-context=MyProcessName] .btn-CANCEL_PROCESSUS > span { display: none }
html[lang=en] #dlgmodal_saveBeforeQuit[data-context=MyProcessName] .btn-CANCEL_PROCESSUS::before {
   content: "Abandon"
}
html[lang=fr] #dlgmodal_saveBeforeQuit .btn-CANCEL_PROCESSUS::before {
   content: "Abandonner"
}
```

Sinon il suffit de mettre le `SCRIPT` dans votre module au lieu de `UI`.
Nous ne le relivrons jamais puisqu'il est vide par défaut.

On va également ajouter un autre message `SAVE_BEFORE_QUIT_PROCESS` que vous pourrez changer.
