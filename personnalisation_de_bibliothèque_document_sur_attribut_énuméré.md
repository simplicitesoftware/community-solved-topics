# Personnalisation de bibliothèque document sur attribut énuméré

**URL:** https://community.simplicite.io/t/8412

## Question
### Request description


Bonjour, j'aimerais avoir un retour sur la meilleure façon d'implémenter ma fonctionnalité :

J'ai un objet "LegalText" avec un attribut de type Document (qui permet à l'utilisateur d'importer des documents de type .rtf) et un autre attribut de type énuméré avec une liste de valeurs à 3 choix (Master, Adaptation, Template).

![Capture d’écran 2024-06-26 144323|690x222](upload://1NNcicAWdtCVs3zxlXYqyxhOIWE.png)


Nous voulons contraindre l'utilisateur à l'import de 5 documents lorsque le choix est "Master" et à 1 lorsque le choix est "Adaptation". 
J'ai d'abord commencé par créer une bibliothèque liée à cet attribut pour limiter à 5 documents maximum et cela fonctionne :) .

![Capture d’écran 2024-06-26 144701|690x144](upload://uW2Z2k3Ufczbe3PhQgLMso0vf6w.png)


Mais dans le cas où nous voulons une personnalisation sur la liste même des valeurs énumérées ( dans mon cas en fonction du code MASTER/ADAPTATION/TEMPLATE), y a-t-il un standard Simplicité ( Sur l'attribut, l'attribut d'objet ou une seconde bibliothèque) ou bien dois-je passer par le code Java de mon objet ?

En attente de votre retour, à bientôt !

### Steps to reproduce

*This request concerns an **up-to-date** Simplicité instance
and these are the steps to reproduce it:*

1.
2.
3. 

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=6.0.14
BuiltOn=2024-06-24 16:23
Git=6.0/29f59bbf1de2a4950b4a895775bf235e3f36d888
Encoding=UTF-8
EndpointIP=100.88.199.126
EndpointURL=http://lbc-77449-app-647dc4cf68-fj4tk:8080
TimeZone=Europe/Paris
SystemDate=2024-06-26 14:53:41

[Healthcheck]
Date=2024-06-26 14:53:41
ElapsedTime=11
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
Bonjour Hamza, 

C'est là qu'intervient la limite de la solution proposée, tu auras forcément une colonne par document. 

A ma connaissance, il n'y a donc pas d'autre possibilité que de vérifier au `postValidate` le nombre de documents dans le champ.

Par exemple : 

```java
@Override
public List<String> postValidate() {
	List<String> msgs = new ArrayList<>();
	
	ObjectField f = getField("myDocField");
	DocumentDB docs = f.getDocument();
	List<DocumentDB> list = docs.getDocuments();
	
	if (list.size() > 2) {
		msgs.add(Message.formatError("Trop de documents", null, "myDocField"));
	}
	
	return msgs;
}
```
