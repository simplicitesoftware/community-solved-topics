# Accès au profil utilisateur via le login en haut à droite de l’instance

**URL:** https://community.simplicite.io/t/9926

## Question
### Request description

Bonjour,

Nous souhaitons gérer plus finement le comportement par défaut de l'UI Simplicité lorsqu’un utilisateur clique sur son profil en haut à droite de l’interface.

![Capture d'écran 2025-05-13 102433|690x305, 75%](upload://5aO3aOZvSq70TOtbu6JpuoZHjVN.png)


###  **Contexte :**

Quand un utilisateur clique sur son nom ou avatar (menu utilisateur), il est redirigé automatiquement vers sa fiche utilisateur.
Ce comportement cause parfois des lenteurs (chargement infini dans certains cas, et n'est pas pertinent dans notre configuration actuelle).

### **Comportement souhaité :**

Nous aimerions pouvoir :

* Soit désactiver complètement cet accès au formulaire utilisateur via le menu,
* Soit rediriger vers un objet spécifique.( paramétrer la classe de l'objet accessible par ce menu).

### **Questions :**

1. Peut-on désactiver ce lien ou le rediriger vers une autre classe ?
2. Y a-t-il une configuration UI ou un paramètre système à modifier ?
3. Si une surcharge est nécessaire côté code, quelle méthode permet de gérer cette redirection ou désactivation ?

Merci d’avance pour votre aide !
Bonne journée, 

### Technical information

[details="Instance /health"]
```text
---paste the content of your-instance.com/health---
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

Le paramètre `OBJECT_MANAGEMENT_USER` est prévu à cet effet :
- Il vaut `User` par défaut,
- peut être remplacé par un autre objet métier de gestion du User,
- ou désactivé via `none`

https://docs.simplicite.io/docs/core/system-parameters-list#object_management_user

On peut changer ce paramètre dans le hook `postLoadGrant` à l'ouverture de session, si on veut l'autoriser pour certains profils uniquement.
