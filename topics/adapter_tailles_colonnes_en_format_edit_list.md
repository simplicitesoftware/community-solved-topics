# Adapter tailles colonnes en format edit List

**URL:** https://community.simplicite.io/t/8514

## Question
### Version

v5.3.28

### Description

Bonjour,

J'ai développé une action de liste qui dès lors qu'elle est exécutée suite au click sur le bouton, m'ouvre une liste en format editable en cachant certains champs et en n'en montrant que 2. Etant donné qu'il n'y a que 2 champs, je me retrouve avec des colonnes très étirées (Voir ci-dessous). 

![image|690x319](upload://fKTl6n8goyPfFHECDcAItiogSFv.png)

J'aimerais remédier à tout ça et avoir ma liste au milieu de l'écran avec des colonnes moins larges. J'ai vu un autre post à ce sujet qui date de quelques années et vous suggériez d'ajouter une ressource CSS à notre objet avec le code suivant pour réduire la taille d'une colonne : 
```
.objlist.object-MyObject .form-group {
  min-width: auto !important; 
}
.objlist.object-MyObject [data-group="forexEcoValuesValueDate"] input{
	width: 60px;
}
```
Je l'ai fait pour une colonne mais rien ne se passe.Savez-vous comment dois-je procéder ? 

Merci d'avance.

## Answer
[quote="mndiaye, post:8, topic:8514"]
Qu’est ce que je fais qui fait que ça ne fonctionne pas ?
[/quote]

- le code de la resource est-il bien `STYLES` ?
- la resource est-elle configurée sur l'objet métier en question ?
- avez-vous vidé le cache navigateur ?
