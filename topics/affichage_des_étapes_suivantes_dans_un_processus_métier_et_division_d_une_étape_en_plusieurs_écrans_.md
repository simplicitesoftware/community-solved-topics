# Affichage des étapes suivantes dans un processus métier et division d'une étape en plusieurs écrans avec le fil d'ariane inchangé

**URL:** https://community.simplicite.io/t/6941

## Question
### Request description

Bonjour,

Je travail actuellement sur la gestion de nos processus métier, et je me heurte à deux questions importantes. J'aimerais solliciter votre expertise pour trouver les meilleures solutions :

1. Affichage des étapes suivantes dans le fil d'ariane :

Actuellement, le fil d'ariane de mon processus affiche l'étape actuelle et l'étape précédente, mais il ne montre pas les étapes suivantes. J'aimerais que l'utilisateur puisse visualiser toutes les étapes de son processus métier, y compris les étapes suivantes, en grisées par exemple pour indiquer qu'il n'est pas encore arrivé à cet endroit. Cela permettrait à l'utilisateur de mieux comprendre où il en est et ce qui l'attend.

2. Division d'une étape en plusieurs écrans tout en maintenant le fil d'ariane inchangé :

Dans certains cas, une étape peut contenir un grand nombre de champs en raison de réponses qui déclenchent elles-mêmes l'ouverture de nouveaux champs. Pour améliorer l'expérience utilisateur, je voudrais diviser cette étape en plusieurs écrans, mais sans changer l'affichage du fil d'ariane. En d'autres termes, je veux que l'utilisateur se sente toujours dans la même étape, même s'il navigue entre différents écrans pour remplir les champs supplémentaires.


Je suis ouvert à toutes les suggestions et astuces pour améliorer l'expérience utilisateur. Merci d'avance pour votre aide !

Cordialement,
Elyass

### Technical information

[Platform]
Status=OK
Version=5.3.15
BuiltOn=2023-09-22 16:53
Git=5.3/662de91d19355d80e24aa899086313aba4159d89
Encoding=UTF-8
EndpointIP=149.202.171.75
EndpointURL=http://renault.simplicite.io:10488
TimeZone=Europe/Paris
SystemDate=2023-09-27 12:13:57

## Answer
Bonjour,

Le chemin / fil d'ariane d'un processus métier n'est pas forcement linéaire, il peut y avoir des branchements conditionnels, des split/join d'activités lors d'un processus long... donc seul le passé est une liste chainée / pas le futur...

Nous avons déjà, dans la roadmap produit, un besoin de pouvoir modéliser dans un processus au niveau des activités :
- un chemin nominal / critique = présentable comme tu l'indiques (activités suivantes grisées)
- des activités optionnelles (affichées que si parcourus)
- des activités transitoires (non affichées, ce qui revient à ton "groupement")
- des chemins d'erreur (affiché en rouge ou pas) 
- ou de compensation (retour arrière spécial pour défaire ce qui a été fait)

Certains métiers veulent aussi voir "tout" le processus, avec des carrés/flèches, les branches conditionnelles... des activités coloriées au fur et à mesure, ou avec des dates prévues/réalisés... Bref le fil d'ariane devient un widget complexe.

Dans un premier temps, 

1) On peut ajouter un hook front sur le fil d'ariane d'un processus

2) si le processus est "linéaire", on pourrait prévoir une évolution simple pour afficher en grisé les activités suivantes (enfin jusqu'à l'étape conditionnelle qui ferait une boucle/split par exemple)

3) on s'oriente aussi vers du CSS avec des classes liées aux étapes et un SVG "libre" représentant le processus mais balisé des classes CSS qui s'appliqueront pour chaque étape. 

Ce sera à horizon de la v6. 
En attendant, on peut agir sur le CSS et masquer certaine étapes, ou insérer du contenu élémentaire sur le dernier item  :

```css
#wkf_MyProcess .act-road>li:nth-child(2) {
  display: none; /* hide activity 2 */
}
#wkf_MyProcess.activity-MyActivity3 .act-road>li:last-child::after {
  content: "Next activity 4...";
  display: block;
  margin-top: 1rem;
  color: #777;
}
```

on pourrait aussi tout masquer, et insérer un SVG à chaque étape qui remplace tout avec un
`content: url('.../myprocess_step2.svg')`

mais bon ça fait beaucoup de boulot.
