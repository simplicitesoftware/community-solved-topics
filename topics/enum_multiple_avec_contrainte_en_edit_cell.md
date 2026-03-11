# Enum multiple avec contrainte en edit cell

**URL:** https://community.simplicite.io/t/11761

## Question
### Request description

Bonjour,

J'ai un champ 
- type énuméré multiple 
- edit cell autorisé
- propriété Updatable impactée par une contrainte (si NA est coché, updatable = false)

En liste, si l'impact de ma contrainte = false, le champ est grisé (résultat attendu)
![image|366x234](upload://zNXFXEFtKFM2U0qa0scgOhbkPBN.png)

Si l'impact = true, le champ est éditable mais les options sont grisées

![image|373x349](upload://98uzhpv8Uxk4lLjFaHOgYUubpKE.png)

Dans Network, je vois que le champ est indiqué Updatable mais pas les valeurs de la LOV.

![image|320x500](upload://yMduREOZawnzOurEu8F2fBX5GAq.png)

Merci d'avance pour votre aide !
Emmanuelle


Platform]
Status=OK
Version=6.3.4
BuiltOn=2026-02-16 12:31

## Answer
Les expressions Simplicité utilisent toujours la syntaxe Rhino, l'égalité stricte `===` ne fonctionnera pas côté back. 

Essaie plutôt avec : `[VALUE:myField] == false || [VALUE:myField] == ""`
