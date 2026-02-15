# Accès FORM sur un objet Select en page d'accueil

**URL:** https://community.simplicite.io/t/11564

## Question
### Request description

Bonjour,

J'ai un objet SELECT intégré à une vue sur ma page d'accueil.
Il s'affiche correctement en liste, mais quand je clique sur une ligne, le formulaire affiché est vide. L'ID du About n'apparaît pas.

![image|690x401, 50%](upload://r1rFuK558uDiYzv79cntASZBMLJ.png)

Si je fais la même chose à partir du menu de gauche en revanche, j'ai bien mon formulaire rempli et l'ID apparaît.

![image|690x271, 50%](upload://kFuekv112Gz1vIVz44lM3IBOMfM.png)

Et si je retourne ensuite sur la page d'accueil, cela fonctionne également.

Dans les logs je vois ceci juste après le GET qui ne fonctionne pas

```com.simplicite.util.engine.CoreCache|instantiateObject||Event: Instanciated implementation com.simplicite.objects.CDP.CdpProductView for object CdpProductView```

Dans Network, le GET envoie bien un row_id mais récupère des valeurs nulles.
![image|690x350](upload://zhUg38o55gg0PETjBqmVY0znhvc.png)

![image|621x500](upload://lzyYTROMCKLllvRRcg8gjHknCUx.png)

Mon paramétrage

![image|690x112](upload://pNzCZH5QgHNPTwlWPed8JOpr0Lu.png)

![image|690x356](upload://mu2Dk7otFxJPiYTQr05OLjpiVq6.png)

[EDIT] J'ai aussi testé avec un row_id logique cf [ce ticket](https://community.simplicite.io/t/referencer-un-objet-select/5914/11) apparemment ouvert par moi, mais sans succès

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.2
BuiltOn=2026-01-30 20:34

## Answer
Problème corrigé en 6.2.23 et 6.3.4, ce cas d'usage n'avait jamais existé.

L'instance `home` qui charge en mémoire la liste de l'objet `select`, ne la partage pas avec l'instance `main` qui sert à afficher le formulaire (sans faire de select en base mais en récupérant la ligne en mémoire de l'instance).

A l'ouverture du formulaire, le front rechargera la liste en mémoire back du l'objet main si ce n'était pas cette instance qui listait l'objet. Donc ça corrigera aussi le problème depuis l'instance `panel` de cet objet.
