# Problème de perte de données lors s'appel API

**URL:** https://community.simplicite.io/t/5193

## Question
Bonjour,
On utilise les API (com.simplicite.webapp.services.RESTMappedObjectsExternalObject) pour exposer nos données à l'un de connexe.
Il a un job qui tourne chaque jour pour récupérer toutes nos données modifiées à partir d'une certaine date, lors de la récupération de données il parcourt page par page  (on a mis en place une pagination)
Le problème qu'on a : c'est que lors de l'appel on a des traitement qui tournent au même temps et qui augmente le  count  et on a remarqué qu'on procédant de cette manière notre connexe perd de la donnée.
On aimerait savoir s'il y a une manière pour garder le même count récupéré au premier appel ( une sorte de cache) .

Je vous remercie d'avance.

Cdt,
Laila

[Platform]
Status=OK
Version=5.1.44
BuiltOn=2022-05-10 18:36
Git=5.1/a51516647c95b8cab51e136ca72a2a5e5c30e27c
Encoding=UTF-8
EndpointIP=172.20.179.40
EndpointURL=http://mla-api-57bcd487f-lf27l:8080
TimeZone=Europe/Paris
SystemDate=2022-08-26 06:28:59

## Answer
On parle de quelles APIs ?

Des API standards REST (c'est de celles là dont je parle dans ma réponse) ou d'API mappées à la mode Renault ?
