# Ajout d'une page d'accueil et d'une page de conclusion dans un processus métier

**URL:** https://community.simplicite.io/t/7708

## Question
### Request description

Bonjour,

Je suis actuellement en train de travailler sur la configuration d'un processus métier dans Simplicité, et j'aimerais inclure à la fois une sorte de page d'accueil et une page de conclusion pour améliorer l'expérience utilisateur.

Pour commencer, je souhaiterais ajouter une étape "d'accueil" qui s'afficherait lorsque l'utilisateur lance le processus. L'idée est d'avoir cette étape pour présenter brièvement le but du processus métier à l'utilisateur avec un message, par exemple : "Vous vous apprêtez à créer une fiche en tant que sous-traitant. Assurez-vous de bien suivre les instructions fournies pour garantir la qualité et l'efficacité du processus.", avec un bouton "Suivant" en bas de la page pour lancer la première activité.

Ensuite, j'aimerais également intégrer une page de conclusion à la fin du processus. Cette page devrait offrir des instructions ou des prochaines étapes à suivre pour l'utilisateur une fois le processus terminé. Par exemple, un message du type : "Vous venez de terminer le processus de création de la fiche. Souhaitez-vous faire évoluer son état ?"

Pourriez-vous me guider sur la meilleure façon de mettre en œuvre ces fonctionnalités dans Simplicité ? J'apprécierais toute assistance que vous pourriez fournir, que ce soit des conseils sur la configuration ou des ressources pertinentes que je pourrais consulter.

Je vous remercie par avance pour votre aide et votre expertise.

Cordialement,
Elyass


### Technical information

[Platform]
Status=OK
Version=5.3.27
BuiltOn=2024-01-31 11:28
Git=5.3/0666d5e9ba5ff03705a1491771d7c40b3e049660
Encoding=UTF-8
EndpointIP=149.202.171.75
EndpointURL=http://renault.simplicite.io:10488
TimeZone=Europe/Paris
SystemDate=2024-02-09 15:15:01

## Answer
Bonjour Elyass, 

La méthode doit retourner un String  contenant le HTML. 
Pour qu'elle soit appelée, elle doit être directement dans le paramétrage de ta donnée d'activité
![image|690x175](upload://hy862UeMgHg9XN4qFZebtQ9KZRw.png)


Exemple 
````java
public String displayTest(Processus p, ActivityFile context, ObjectContextWeb ctx, Grant g) {
		return "<h1>Hello world!</h1>";
	}
```
