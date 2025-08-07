# Instance merge persistante sur vue avec onglets

**URL:** https://community.simplicite.io/t/6409

## Question
### Request description

Bonjour,

J'ai une vue présentant plusieurs Recherches sous forme d'onglets.

![image|690x322](upload://thYsJbMk5RrlbCcBiXEZU7Zx92x.png)

Si j'affiche la vue Merge sur un de ces onglets puis que je Cancel, j'ai l'impression que cela bloque l'instance l'instance de la vue sur celle du Merge. 

![image|690x168](upload://gpdXm2nwnaiXZTs7ZfuQHFoc7yf.png)

Une des conséquences est que je ne parviens plus à supprimer les filtres appliqués.
![image|657x500](upload://hFdJhyG99vLn9vLCSSMPhsV1ae5.png)

Le clic sur les croix de suppression de filtre ne fonctionne plus
![image|690x256](upload://tfcTJl1FtajkoGKchCVhV5NXiZw.png)

Instance Merge
![image|690x130](upload://xaMJ5uMadQzihYPKGLQCoqoJt20.png)

Merci d'avance pour votre aide !
Emmanuelle

### Technical information

[details="Instance /health"]
```text
Version=5.2.39
BuiltOn=2023-05-02 12:08
```
[/details]

## Answer
Ok corrigé.
Le pb était que le formulaire de merge s'affichait dans la div du panel embedded de la vue, et non pas en pleine page / empilée dans la nav. Il y a avait aussi le problème sur l'action "Copy" qui restait dans le panel pour la même raison.

Quand on veut afficher un truc en pleine page dans la div de navigation courante, il faut utiliser la méthode getNavContainer :

> let ctn = $ui.getNavContainer(element);
> $ui.displayForm(ctn, ....)

Car on peut avoir plusieurs nav, par exemple pour comparer via split d'écran des objets avec 2 navbar = 2 containers. On peut aussi prévoir d'utiliser ce mécanisme pour avoir plusieurs nav via onglets...
