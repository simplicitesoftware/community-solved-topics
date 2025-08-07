# Problème d'affichage des libellés des actions dans un formulaire

**URL:** https://community.simplicite.io/t/8818

## Question
### Request description

Bonjour,

Je rencontre un problème d'affichage des libellés des actions dans mon formulaire d'objet.
Les actions sont bien visibles avec l'icon mais sans le titre : 
![Capture d'écran 2024-09-30 113632|690x180, 75%](upload://drK5hUct9OIYUdXK8L5SOzi80Kp.png)

Lors de l'édition d'un objet dans mon template, les titres des actions s'affichent correctement avant la sauvegarde.
![Capture d'écran 2024-09-30 113741|658x460, 50%](upload://rLOYBAvPG23PQhkKaI6713zE2R1.png)
 Cependant, une fois la sauvegarde effectuée, ces titres disparaissent et seules les icônes restent visibles.
![Capture d'écran 2024-09-30 113754|690x381, 50%](upload://wmR8vI2JSalubCfCmPfB8qt2hcT.png)

J'ai aussi essayer de surcharger sur l'action sur la couleur du text mais toujours pas 
![Capture d'écran 2024-09-30 114427|690x324, 75%](upload://OXSTWQbGZ7LGqMZmpCQPI7SD1p.png)


Y a-t-il une solution pour l'affichage des libellés des actions dans une formulaire,ou bien me manque-t-il une étape ?

 En attente d'un retour, à bientôt :)

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.1.6
BuiltOn=2024-09-13 16:21
Git=6.1/dfa6a2c301a0b79b7667cb2f921b3c5a38f0d51c
Encoding=UTF-8
EndpointIP=100.88.204.156
EndpointURL=http://lbc-77449-app-846c7ffb59-g486c:8080
TimeZone=Europe/Paris
SystemDate=2024-09-30 11:46:30

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=302
EnabledUsers=21
LastLoginDate=2024-09-30 11:30:31
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

L'évolution pour afficher les onglets à gauche n'est pas disponible en 6.1.6.
On a backporté cette évolution en 6.1.9.

Vous avez dû mettre du CSS pour masquer le libellé des tabs, et il y a surement une portée trop grande ?
