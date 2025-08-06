# Retirer possibilité changement de langue dans le panel utilisateur

**URL:** https://community.simplicite.io/t/7048

## Question
Bonjour,

Nous souhaitons retirer la possibilité aux utilisateurs de changer la langue de l'application et rester par défaut en Français. C'est une opération qui est possible sur Simplicité ?

![image|296x186](upload://hGqVE5iq75jsPCJmaKMqrzWLO47.png)

Merci

## Answer
Bonjour,  
Vous pouvez implémenter ce besoin dans  le preLoadGrant des PlatformHooks:
En définissant la liste des langues disponible lors de la connexion.

```java
@Override
public void preLoadGrant(Grant g) {
		List<String> langs = new ArrayList<>();
		langs.add("FRA");
		g.setLanguages(langs);//Langue disponible
		g.setLang("FRA");//Langue active
}
```
