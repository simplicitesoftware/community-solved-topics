# Problème avec un objet select

**URL:** https://community.simplicite.io/t/7219

## Question
Nous sommes en train de créer un objet select, pour pouvoir récupérer la donnée depuis deux tables différentes.  

Nous avons essayé de suivre les conseils qu'on a pu trouver sur le forum, et donc on a réussi à afficher les données dans les 4 colonnes (3 qui vient d'une table et 1 d'une deuxième)

Au moment qu'on ajoute une 3ème colonne de la première table en tant qu'objet field, sur l'affichage de l'objet on a une table vide. ( même si la requête sur DB marche bien )

### Steps to reproduce

1. Create an object select and add the filter :
```sql
SELECT co.code AS bur_brand_code
     , co.name AS NAME
     , co.org_code AS org_code
	 , cp.bur_programm AS bur_programm
	 , co.org_name AS org_name
FROM bur_cataloguedoffer co 
JOIN bur_cataloguedproduct cp 
	ON cp.bur_projet_genre_fg = co.bur_projet_genre_fg
GROUP BY co.code, co.name, co.org_code, cp.bur_programm, co.org_name
```
2. Création des object fields brand code / org code / programm / projet genre
3. Affichage de donnée sur la vue
4. Ajout d'une nouvelle colonne (org name par ex), pas de donnée affiché sur la table

On aimerait savoir si vous avez de la documentation à ce sujet, pour savoir ce qu'il nous manque pour que ca marche correctement ?

### Technical information

Status=OK
Version=5.2.50
BuiltOn=2023-10-06 15:27
Git=5.2/2f28e6eac516aa8133f23896ce1c9ad76ec756ed
Encoding=UTF-8
EndpointIP=172.17.0.4
EndpointURL=http://fa66fdde7cae:8080
TimeZone=Europe/Paris
SystemDate=2023-11-23 16:08:19

## Answer
Bonjour, 

Après avoir refait des tests avec les objets select, je n'arrive toujours pas à reproduire votre cas. J'ai un peu renforcé la [documentation sur le sujet](https://docs.simplicite.io/docs/core/objects/select-objects), mais je ne suis pas sûr de comprendre cette question : 

[quote="Laura, post:16, topic:7219"]
est-ce que l’objet doit avoir un identifiant ?
[/quote]

Si vous parlez d'un identifiant technique de type `row_id`, alors non, il n'en faut pas. Ci-dessous un screenshot de l'exemple d'objet select présent dans le module **SimFeatures** (AppStore > Tools)


[details="Voir l'image"]
![Simplicité|690x417](upload://3T4SucpWoDBFFXanTuyneLtpj3k.jpeg)
[/details]
