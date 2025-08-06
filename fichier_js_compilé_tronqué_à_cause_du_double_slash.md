# Fichier JS compilé tronqué à cause du double slash

**URL:** https://community.simplicite.io/t/8132

## Question
### Request description
Bonjour,
Lors de la compilation des ressources en JavaScript, j'ai remarqué un problème avec les chaînes de caractères `"//"`.
Les caractères `"//"` sont considérés comme des commentaires ce qui a pour effet de tronquer le fichier compilé.
Pour contourner ce comportement, nous sommes contraints de transformer les `"//"` en `"/"+"/"`.
Exemple : `http://blabla` => `http:/`+`/blabla`.

Avons-nous la possibilité de charger une ressource sans qu'elle soit compilée ?
Sinon 
Est-ce que ce comportement sera corrigé ?
Ou existe-il une autre solution à ce problème ?

### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.2.54
BuiltOn=2024-01-31 10:05
Git=5.2/4e6529843e4700856182bdf9cb4a4c01d4ad13ff
```
[/details]

## Answer
Le fichier est plutôt conséquent donc difficile à partager ici et je pense que la subtilité peut venir du fait que c'est un fichier js déjà minifié en amont en input de la compilation mais la solution de contournement mentionné ici [Est-il possible de récupérer une ressource JS non minifiée? - Support - Simplicité Software Community Forum (simplicite.io)](https://community.simplicite.io/t/est-il-possible-de-recuperer-une-ressource-js-non-minifiee/5161/2) fonctionne donc nous allons partir sur cette solution. Merci du support
