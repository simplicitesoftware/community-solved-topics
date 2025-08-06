# Contrainte Front affichage valeur d'attribut en fonction d'un attribut ramené

**URL:** https://community.simplicite.io/t/5413

## Question
### Request description

Bonjour,
nous souhaitons afficher la valeur d'un champ uniquement lorsque la valeur d'un attribut ramené est égale à une valeur. 
Voici la contrainte que nous avons faite : 
![image|690x207](upload://A5Gmf5oj4Uek1wzPnoBmdYXZK7m.png)

Si notre etat est à "BR" alors le champ "Required Level" doit être masqué 


### Steps to reproduce

N/A
 

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.2.20
BuiltOn=2022-10-23 23:06
Git=5.2/6548a50464cfa68801d29f775d9882f53ce8926b
Encoding=UTF-8
EndpointIP=10.201.101.249
EndpointURL=http://siparex-simplicite-dev-546fddd684-vhb82:8080
TimeZone=Europe/Paris
SystemDate=2022-10-25 16:00:15
```
[/details]

[details="Simplicité logs"]
```text
N/A
```
[/details]

[details="Browser logs"]
```text
N/A
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
[quote="Alistair, post:5, topic:5413"]
e montrer la configuration de la contrainte ?
[/quote]

Alistair, on a comparé avec Démo, et modifier la contrainte en Back End. 

Elle s'exécute bien pour faire disparaître le champ niveau requis mais il ne réapparait pas pour les Etat en statut autre que BR. 
On investigue
