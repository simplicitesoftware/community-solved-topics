# Peut-on créer un objet lié directement depuis la création de son objet parent?

**URL:** https://community.simplicite.io/t/5209

## Question
### Request description

Bonjour, 

Est-il possible dans le formulaire de création d'un objet parent de créer à l'enregistrement l'objet fils si tous les champs de sa clé fonctionnelle sont complétés ?

### Steps to reproduce

Pour l'exemple j'utilise le module de démo.

Dans le formulaire de création d'un produit, je peux choisir un fournisseur avec la loupe.
Je me rend compte que le fournisseur que je veux n'existe pas encore. 
Pour en créer un nouveau je dois donc soit le faire depuis la pop-up avec la liste des fournisseurs grâce au bouton "Créer" soit avec le bouton "Plus" qui va ouvrir une pop-up de création pour le fournisseur.

![image|690x176](upload://etAZoIRzd6ivROPhQ0ID4pWUJrI.png)

![image|690x153](upload://eBZ8iuWZXZnPi15TT6WgxFw8yER.png)

Est-il possible de créer mon fournisseur sans forcément passer par une pop-up, en faisant ça par exemple :

![image|690x241](upload://mxsoFjdsTZaeqEymGaQTvRYFPHn.png)

Je complète les champs de 1 à 5 et j'enregistre le nouveau produit.
A l'enregistrement, mon fournisseur serait automatiquement créé car le code et le nom du fournisseur sont non vides et car je n'ai pas sélectionné de fournisseur avec la loupe.

Dans une de nos applications, les utilisateurs ont du mal avec le concept de création des objets liés, notamment quand le modèle est un peu complexe et qu'ils doivent passer par 2 pop-up (ou plus) de création d'objets liés avant d'enregistrer la création du parent. Pour faciliter la création des différents objets nous aimerions donc que l'utilisateur puisse le faire de manière transparente en complétant les champs dans le formulaire du parent sans devoir passer par des créations intermédiaires dans des pop-up.

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.2.11
BuiltOn=2022-07-22 22:18
Git=5.2/bc1f6e720f5df119336af65fa1b502bd40ac47d4
Encoding=UTF-8
EndpointIP=
EndpointURL=
TimeZone=UTC
SystemDate=2022-08-30 09:36:54

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=
ActiveSessions=1
TotalUsers=7
EnabledUsers=5
LastLoginDate=2022-08-30 09:07:14

[Server]
ServerInfo=Apache Tomcat/9.0.65
ServerType=WEB
ServerActiveSessions=1
ServerSessionTimeout=30

[OS]
Name=Linux
Architecture=amd64
Version=5.4.0-125-generic
DockerImageName=centos7
SystemEncoding=UTF-8

[JavaVM]
Version=17.0.3
Vendor=Eclipse Adoptium
VMName=OpenJDK 64-Bit Server VM
VMVersion=17.0.3+7
ScriptEngine=rhino
ScriptEngineVersion=Rhino 1.7.13 2020 09 02
HeapFree=202191
HeapSize=399360
HeapMaxSize=2037760
TotalFreeSize=1840591

[Cache]
ObjectCache=233
ObjectCacheMax=10000
ObjectCacheRatio=2
ProcessCache=1
ProcessCacheMax=10000
ProcessCacheRatio=0
APIGrantCache=0
APIGrantCacheMax=1000
APIGrantRatio=0

[Database]
Vendor=3
ProductName=PostgreSQL
ProductVersion=11.16 (Debian 11.16-1.pgdg90+1)
DriverName=PostgreSQL JDBC Driver
DriverVersion=42.4.0
DBDate=2022-08-30 09:36:54
DBDateOffset=0
DBPatchLevel=5;P02;061b2c28d6156a42239626b53ced124f
UsingBLOBs=true

[Healthcheck]
Date=2022-08-30 09:36:54
ElapsedTime=249


```
[/details]

## Answer
Bonjour,

[quote="FlorentGN, post:1, topic:5209"]
passer par 2 pop-up (ou plus)
[/quote]

Vous avez un problème d'UX trop complexe. On ne crée jamais 20 entités dans 1 écran. On peut privilégier un screenflow d'étape par étape pour aider à créer un objet complexe et ses dépendances.

L'ergonomie que vous demandez n'est pas généralisable et va entrainer des complications.

Le problème avec ce genre d'UX est que l'utilisateur n'ira jamais chercher une référence (dans l'exemple un fournisseur) existant, devra saisir N caractères "en vue de créer" plutôt que de sélectionner une entité existante dans la base... Vous allez sûrement vous retrouver avec des doublons fonctionnels (erreur d'accent, espace, tiret...). Dans Simplicité, c'est bien de devoir "Créer" explicitement l'entité si on ne la trouve pas.

Quand on tape dans un champ d'objet lié indexable et indexé, un dropdown propose les entités par complétion (sans passer par un popup de recherche), si on ne trouve pas on peut utiliser le bouton [+] qui reste également un choix volontaire de l'utilisateur de créer un objet lié.

L'action de création d'un objet métier est rarement simple et il convient de passer par un écran pour valider les données, afficher les erreurs, les autres références vers d'autres objets, etc.

Pour un cas d'usage à priori simple de pouvoir créer un nouvel objet dans un référentiel (sans métier complexe comme une liste des Pays) qui s'auto-incrémenterait sans logique, il faut demander à vos utilisateurs l'intérêt de saisir N caractères ou N champs (en hypothèse forte de créer) plutôt que de sélectionner une entité, avec le risque de saisir des doublons par erreur de frappe, espaces, accents ou homonyme... (ce besoin semble plus exprimé au démarrage "base vide", mais une fois la liste des pays complétées, il perdrait son sens)

Une autre façon de raisonner plutôt que de faire créer commande > créer produit > créer fournisseur, est de suivre l'exemple de la démo en créant un Processus de type screenflow : sélection d'un fournisseur > sélection d'un produit > commande préremplie pour saisir la quantité.

Si l'objet lié est en relation 0,1 ou 1,1, ce cas est prévu et vous pouvez déjà "inliner" (dans la définition du link et en mettant la vue du link dans le formulaire) ses champs mono-valués dans le formulaire parent.

Enfin, vous pouvez interdire la création via référence. Une référentiel s'administre en général depuis un menu/domaine ad hoc. Ce n'est pas le même cas d'usage (gérer le référentiel des produits plus simple que créer une commande qui permettrait d'administrer le référentiel au passage...)
