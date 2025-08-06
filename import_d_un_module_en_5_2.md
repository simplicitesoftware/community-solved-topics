# Import d'un module en 5.2

**URL:** https://community.simplicite.io/t/4820

## Question
### Request description

Bonjour, 
Je tente d'importer un module comme vous nous l'avez appris, seulement l'import semble bloquer /figer. 
J'ai constaté que vous aviez créé des statuts supplémentaires pour gérer les imports. Notamment "En cours d'import". Mon import reste bloqué à cet état là depuis une 20taine de minutes. 
J'ai ajouté une date d'effet  au cas où. Rien n'a changé.

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and those are the steps to reproduce it:*

1. Faire un import via le bouton "import XML"
![image|690x304](upload://y4fw5wGSlIawbqRUxodc8t2y5tR.png)

2. Drag/Drop un fichier précédemment exporté de type ZIP
3.  
![image|690x121](upload://qMmYFwWgNsFeeXfWr0Waz6hXCa6.png)

(J'ai refait la manip deux fois au cas où).

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.2
BuiltOn=2022-04-29 15:38
Git=5.2/a2c69b2ee78658770a248e617730e607252990ca
Encoding=UTF-8
EndpointIP=10.201.58.66
EndpointURL=http://siparex-simplicite-dev-777bcd4cfc-dqxdr:8080
TimeZone=Europe/Paris
SystemDate=2022-05-06 10:41:32
```
[/details]

[details="Simplicité logs"]
```text
RAS dans les logs
```
[/details]

[details="Browser logs"]
```text
RAS dans les logs browser
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonjour Ophélie, 

Un "Import XML" n'est pas un import de module. 
Pour importer un module il faut aller dans Adminsitration > Module, choisir le module que tu souhaites importer (ou le créer s'il n'existe pas). Déposer le fichier (ZIP ou XML) dans le champ Fichier et cliquer sur "Importer" 

![Capture d’écran 2022-05-06 à 10.45.29|690x396](upload://2TMnXbJg1isWoGa3YeGx6Qf31ah.png)
