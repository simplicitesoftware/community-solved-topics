# Attribut d'action avec référence vers un objet

**URL:** https://community.simplicite.io/t/6222

## Question
### Request description

Bonjour,

Désolée pour les nombreux tickets :grimacing:
J'essaie de configurer un attribut d'action avec une référence. Le champ ne fait pas partie de mon objet, mais je voudrais pouvoir aller chercher les valeurs possibles par loupe (c'est une liste de pays que je vais utiliser pour créer des données filles de mon objet)

J'arrive à obtenir la loupe, mais quand je sélectionne une valeur le champ reste vide.
Auriez vous des exemples de configuration ?

Merci pour votre aide !
Emmanuelle

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

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
Test fait en ajoutant une référence vers un Utilisateur sur l'action de la démo qui incrémente le stock d'un produit :

![image|690x308](upload://t1bDo23BcBt2KK39nbbsjl8U6d4.png)

Ce qui donne :

![image|681x433](upload://hFNo0sDcoa5kA4hZjx3H57iv9eG.png)

Code back pour récupérer les 2 champs :

```java
/** Action: increase stock */
@BusinessObjectAction
public String increaseStock(Action action) {
	String lang = getGrant().getLang();
	ObjectField userId = action.getConfirmField(lang, "obu_user_id");
	AppLog.info("user Id = " + userId.getValue(), null);
	ObjectField userLogin = action.getConfirmField(lang, "usr_login");
	AppLog.info("user login = " + userLogin.getValue(), null);
	//...
}
```
