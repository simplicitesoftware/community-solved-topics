# Problème de visibilité de transition d'état selon un attribut de l'objet

**URL:** https://community.simplicite.io/t/8817

## Question
### Request description

Bonjour, nous travaillons sur les transitions d'état lié à un objet, nous rencontrons actuellement  le problème suivant :

Nous avons un objet qui avec un attribut `LegalTextDocumentType` peut être de deux types : Master ou Adaptation. Lorsque l'objet est créé, il commence toujours dans l'état "Brouillon" (Draft). 

Selon son type, la transition d'état est différente :

* Pour le type Adaptation, les transitions possibles sont : Brouillon → Validé →Publié→ Archivé.
* Pour le type Master, les transitions possibles sont : Brouillon → Publié→ Archivé.

Nous utilisons le hook `isActionEnable` pour déterminer si l'utilisateur peut ou non effectuer une action, en fonction du type de l'objet et de son état. Cependant, je me retrouve dans une situation où l'utilisateur ne peut pas effectuer l'action (ce qui est correct), mais cette action reste visible dans l'interface (bien qu'elle soit désactivée). 


Exemple avec le screen suivant dans une adaptation en draft, l'utilisateur peut la valider mais ne peut pas la rendre disponible ( logique lié au type master) il ne peut pas cliquer mais peut le voir
![Capture d'écran 2024-09-30 111534|690x65, 75%](upload://yAvjySQzSQBkaTfVZRFnKczfn0p.png)


Meme chose dans un objet de type master qui peut rendre Disponible sans pouvoir valider ( car non adaptation mais l'action reste visible)
![Capture d'écran 2024-09-30 111641|690x77, 75%](upload://mikGqpJ03XS4fSflHxYAaZACE77.png)

Est-il normal que l'action soit visible même si elle n'est pas réalisable ? Et Quelle serait la meilleure façon de cacher complètement les actions que l'utilisateur ne peut pas exécuter, afin de rendre l'interface plus propre ?

Merci d'avance pour vos conseils et votre aide :slight_smile: 

### Technical information

[details="Instance /health"]
```text
Status=OK
Version=6.1.6
BuiltOn=2024-09-13 16:21
Git=6.1/dfa6a2c301a0b79b7667cb2f921b3c5a38f0d51c
Encoding=UTF-8
EndpointIP=100.88.204.156
EndpointURL=http://lbc-77449-app-846c7ffb59-g486c:8080
TimeZone=Europe/Paris
SystemDate=2024-09-30 11:25:27

[Application]
ApplicationVersion=1.0.0
ContextPath=
ContextURL=https://lbc-app.ext.gke2.dev.gcp.renault.com
ActiveSessions=0
TotalUsers=302
EnabledUsers=21
LastLoginDate=2024-09-30 11:00:03```
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

Une transition n'est pas une "vraie" Action spécifique et n'utilise donc pas les mêmes hooks. Le bouton de transition est juste un moyen rapide de faire la mise à jour du statut + save.

Il existe un hook dédié `isStateTransitionEnable` pour les transitions qui devrait répondre à votre besoin, par exemple :

```java
public boolean isStateTransitionEnable(String fromStatus, String toStatus) {
  if ("ADAPT".getFieldValue("myType") 
   && "DRAFT".equals(fromStatus)
   && "VALID".equals(toStatus))
    return false;
  return super.isStateTransitionEnable(fromStatus, toStatus);
}

```
