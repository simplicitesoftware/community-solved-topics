# Problème de transition d'états et de sélection de références

**URL:** https://community.simplicite.io/t/4800

## Question
### Request description

Bonjour,

Depuis la mise à jour 5.2, nous avons remarqué plusieurs problèmes majeur :
* Les transitions d'état ne s'effectuent plus
* Les clefs techniques sont apparus dans les listes
![image|690x96](upload://zDbOJTHWBVLATc7xNS9hiPr4Jml.png)
* Nous n'arrivons plus à sélectionner un utilisateur (il n'y a pas la loupe). Je précise que nous sommes sur le compte Designer
![image|690x118](upload://AsXbtCFzDz0S7GZew8j4DGcYDZ3.png)

**Je suis sûr que le problème 1 est lié à la MAJ.** Pour les problèmes 2 et 3, pas sûr, mais j'ai un doute quand même.

**Problème 2 et 3 :**
ID technique :
![image|690x247](upload://vh9WpjD4WWRsIiia9oSRiXxaCyz.png)
Nom et prénom (champs ramenés grâce à la clef technique) :
![image|690x209](upload://4ljoV1bEY38GsvOTb7g1xkx2L0M.png)
![image|690x182](upload://kNGRDCy8JVsJYc9DhjPHDhv5ucD.png)

MCD :
![image|690x180](upload://zS9XpRfs0BPSBszXNVfON0ryTvG.png)


### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.2
BuiltOn=2022-04-29 15:38
Git=5.2/a2c69b2ee78658770a248e617730e607252990ca
Encoding=UTF-8
EndpointIP=10.201.58.85
EndpointURL=http://siparex-simplicite-dev-777bcd4cfc-dqxdr:8080
TimeZone=Europe/Paris
SystemDate=2022-05-02 16:15:27
```
[/details]

[details="Simplicité logs"]
```text
NA
```
[/details]

## Answer
Après analyse, de nombreux vieux paramétrages ont des clés étrangères incomplètes fonctionnellement (par exemple ne ramène que le nom, mais pas la clé complète nom/prenom/date naissance, car trop pensé pour un écran donné et non pas pour une API déterministe).

En 5.1 la UI était "compréhensive" et permettait d'avoir des clés techniques partiellement identifiées par quelques champs clés fonctionnelles ou des row_id. (si la clé est totallement absente, on ne peut rien faire comme ici sans usr_login)

Mais cela posait déjà des problèmes sur les autres interfaces d'import XML ou mise à jour par API (sans aucun row_id ou fk techniques car variables d'une base à l'autre). Une clé pas ou partiellement fournie ne permet pas de retrouver le row_id de l'objet (lié ou principal) de façon sûre et unique pour mise à jour.

La 5.2 ayant renforcé ce point, l'audit permet désormais de le signaler au niveau de la définition de l'objet. Mais comme peu de designers ont été sensibilisés à cela, on va ajouter à la prochaine livraison 5.2.3 un traitement qui ajoutera temporairement les champs manquants (en mémoire) avec des warnings dans les logs.

Cela reste un contournement à un défaut de paramétrage des objets déjà présent en 5.1 ou avant.
Une fois l'objet corrigé le warning disparaitra.
