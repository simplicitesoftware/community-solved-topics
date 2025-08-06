# Nom des enregistrements paramétrage : Template editor

**URL:** https://community.simplicite.io/t/3665

## Question
Bonjour, 
Comment est paramétré le nom des enregistrements créés (en haut de chaque page) : ![image|434x88](upload://z5YF0QK4rFDrx4e22g0HgqbRirg.png)
J'ai besoin de configurer ces noms correctement selon les clés fonctionnelles de l'objet concerné. Ici, ce sont des champs ramenés (certes définis en tant que clés fonctionnelles sur leur table primaire, mais pas sur les tables où nous avons rapatrié le champ). 

Merci pour votre aide, 
Ophélie

## Answer
Le libellé du titre d'un formulaire est constitué, par défaut, de la concaténation des attributs clés fonctionnelles, ce qui n'est pas forcément toujours idéal.

Il y a donc un hook qui permet de surcharger ce titre avec ce que l'on veut: `getUserKeyLabel`.

Exemple (tiré de la démo sur le client = plutôt que d'afficher le code du client - ce qui n'est pas très user-friendly - on affiche son prénom + nom):

```java
@Override
public String getUserKeyLabel(String[] row) {
	return getFieldValue("demoCliFirstname", row) + " " + getFieldValue("demoCliLastname", row);
}
```
