# Bouton Modifier en liste - erreur à la création d'un deuxième élément

**URL:** https://community.simplicite.io/t/5426

## Question
### Request description

Bonjour, 
nous avons testé la fonctionnalité "Modifier en liste" sur nos objets liés mais dès qu'on ajoute une deuxième ligne, nous vons une erreur sur le champ obligatoire (alors que nous sommes sur la fiche de l'Entretien, donc il devrait être automatiquement relié à son objectif)
![image|690x197](upload://1RCRhUmNB3zFroQ14mkxzkeT2Jc.png)

Nous arrivons à reproduire cette erreur également lorsque dans l'objet, nous groupons les valeurs par collaborateur. 

Nous avons testé en commentant nos hook dans le code source. Et en tentant de répliquer le problème sur le module démo. 
Je n'arrive pas à reproduire le problème sur le module Demo, en revanche lorsque j'incorpore la vue des Produits fournisseurs dans le formulaire du Fournisseur puis que je tente d'insérer une première ligne le bouton "Ajouter une ligne" est complétement bloqué (ce qui n'arrive pas dans notre cas d'usage). En revanche je n'arrive pas à répliquer l'erreur d'ajout de plusieurs lignes..

une idée ? 


### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1. Activer la fonctionnalité "Créer+Modifier+Supprimer" sur l'objet 
2. Sur un objet parent, cliquer sur "Modifier la liste" (la vue de l'objet fille doit être incorporé dans le formulaire de la vue parent).
3.  Ajouter 2 élements, cliquer sur Enregistrer. L'erreur apparaît.

### Technical information

[details="Instance /health"]
```text

[Platform]
Status=OK
Version=5.2.20
BuiltOn=2022-10-23 23:06
TimeZone=Europe/Paris
```
[/details]

[details="Simplicité logs"]
```text
RAS dans les logs
```
[/details]

[details="Browser logs"]
```text
RAS 
```
[/details]

[details="Other relevant information"]
*----E.g. type of deployment, browser vendor and version, etc.----*
[/details]

## Answer
Bonsoir,

Non reproduit sur un panel embarqué dans le formulaire.
Vous devez avoir du code back ou front qui supprime le contexte du parent object dans l'objet fils.
Le bouton ""ajouter une ligne" clone le même enregistrement en front, en contexte création avec la clé étrangère au parent renseignée.

Ajoutez des traces dans le preValidate du fils (l'objectif) pour voir si getParentObject est toujours présent et ce que contient le field de clé étrangère.

Sinon essayez de le forcer s'il est vide et que le parent object est non null (entretien)
du style :

```java
// preValidate workaround to set the parent foreign-key
if (isNew() && getParentObject()!=null && getField("champEntretienId").isEmpty())
  setFieldValue("champEntretienId", getParentObject().getRowId());
```
