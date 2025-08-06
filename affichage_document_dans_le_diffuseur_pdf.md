# Affichage document dans le diffuseur PDF

**URL:** https://community.simplicite.io/t/9174

## Question
### Request description

Bonjour, nous avons un objet **Content** qui gère des documents PDF et RTF. 


* Si je dépose un **RTF**, un document pdf est  généré et s'affiche correctement dans le diffuseur.
![Capture d'écran 2024-12-03 101012|690x171, 75%](upload://iz3su5ugRnFTzw6X9ZthHirkK51.png)
![Capture d'écran 2024-12-03 101053|690x307, 75%](upload://AluJBX8mB6Xp8x2mSVNSe8PCHov.png)

* Si je dépose directement un **PDF** dans content ("ici le pdf "testImportDepuisContent"), le document est téléchargé, un document rtf est généré et le pdf est bien afficher dans le diffuseur pdf.
![Capture d'écran 2024-12-03 101209|690x167, 75%](upload://7yqWYYQOKxKLPuVXBCOoLcOLegd.png)
![Capture d'écran 2024-12-03 101225|690x172, 75%](upload://umH9zxAz77oipQ5c42Eua1ST85d.png)


Cependant, lorsque nous utilisons une **action dans un autre objet** pour créer un **Content** et y associer un document :

1. Pour un fichier **RTF**, le document est bien généré en PDF et s'affiche correctement dans le diffuseur.
![Capture d'écran 2024-12-03 103224|654x500, 50%](upload://yGNFIC8SgcaQeJOYXKza8yRXWdu.png)
![Capture d'écran 2024-12-03 104521|690x138, 50%](upload://9PD4kLhReNkzzlezOXqc7zpmPjG.png)

2. Pour un fichier **PDF**, bien qu'il soit téléchargeable via la liste ou les détails de l'objet, le diffuseur retourne une **erreur 404**.


![Capture d'écran 2024-12-03 104637|690x402, 50%](upload://mpkh0xSSi8daFTHXS6lwzSPVEvu.png)
![Capture d'écran 2024-12-03 104702|690x156, 75%](upload://o4DsPFWiiruc10OJ0SwduIbswfq.png)
![Capture d'écran 2024-12-03 104710|690x159, 75%](upload://rWU5We98KFCNmkbIVdyM5EOpCLk.png)

J'ai essayé de visualiser depuis la liste completes des documents avec les paths, le diffuseur ne marche toujours pas. 
![image|690x221, 75%](upload://4lQpa4YYJ5Oa6mZfBPw4dAdmEbw.png)

J'ai aussi comparer la div iframe dans l'inspection web c'est bien configurer avec id de l'attribut et du doc..
Ainsi que dans la bd entre un pdf  ou le diffuseur marche et non,pas d'anomalie :
![image|690x78](upload://vZEREFncyWDHyE2HpUlEdYW1382.png)

voici la log lorsque le diffuseur est en 404



```text
--- 2024-12-03 11:15:16,681|SIMPLICITE|ERROR| |http://lbc-77449-app-6cf56d9fd-kd9df:8080||ERROR|p124722|com.simplicite.webapp.servlets.ui.DocumentServlet|service||Evénement: Unknown message ---
```

Tous ces tests m'indiquent que peut être il y a un probleme au niveau du path du pdf déposé depuis l'action, c'est une piste mais pas sur.. auriez-vous d'autres pistes à me conseiller ?
### Technical information

[details="Instance /health"]
```text
---[Platform]
Status=OK
Version=6.1.16
BuiltOn=2024-11-29 13:53
Git=6.1/4d1040b907ab4a5824903e1a31d91364f29ce7f6
Encoding=UTF-8
EndpointIP=100.88.207.16
EndpointURL=http://lbc-77449-app-6cf56d9fd-kd9df:8080
TimeZone=Europe/Paris
SystemDate=2024-12-03 11:17:39

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=1
TotalUsers=301
EnabledUsers=22
LastLoginDate=2024-12-03 11:00:03

[Server]
ServerInfo=Apache Tomcat/9.0.97
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30
CronStarted=true
---
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
Hello David, merci pour ton retour.

Nous avons trouvé la solution en retraçant la facon de recuperer le document, et son path, cela nous as permis de trouver une facon de set le document quand c'est un pdf et une autre facon quand c'est un rtf, 

Ca marche impecable, nous pouvons à présent importer un document RTF ou PDF via cette meme action  :slight_smile:
