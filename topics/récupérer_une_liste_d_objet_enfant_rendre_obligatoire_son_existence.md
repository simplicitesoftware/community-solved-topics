# Récupérer une liste d'objet enfant + rendre obligatoire son existence

**URL:** https://community.simplicite.io/t/4528

## Question
Bonjour,

J'ai le formulaire suivant : 
![image|690x353](upload://cn73oTPOY0ianzIdRSjpc9Rsm7q.png)

J'aimerais faire 2 choses :
* Rendre obligatoire le fait d'avoir au moins un élément dans la table pouvoir d'une AG (c'est la table entouré en rouge dans la capture d'écran ci-dessus)
* Dans le code récupérer sous forme de `liste d'ObjectDB` toutes les lignes de la table pouvoir (1 ligne dans la table pouvoir = 1 ObjectDB)

**Auriez-vous des solutions pour réaliser ces 2 demandes ?**

Voici le MCD concernant ces 2 tables :
![image|690x471](upload://1SkUucPWMpZ6GScWXEKkZAFYUUa.png)

## Answer
Bonjour Corentin,

---

### Objet référençant (Pouvoir) obligatoire

Deux approches:

1. Diagramme d'état sur l'AG avec un état "brouillon", et une vérification ("possède au moins un pouvoir") sur la transition à l'état suivant, permettant d'afficher un message d'erreur approprié. 
2. **[déconseillé]** Sur l'AG, ajouter des champs non persistants (*pas de nom physique*), visibles et obligatoires uniquement en création, reprenant les champs du Pouvoir, et création de ce premier pouvoir obligatoire par code dans la `postCreate` de l'AG.

*La première approche, plus dans l'"esprit Simplicité", est largement préférable et bien plus intuitive en termes d'UX. Les champs qui disparaissent c'est toujours troublant, et d'expérience c'est un nid de problèmes et de cas non prévus à maintenir.* 

---

### Liste d' `ObjectDB`

Tu peux aller (re)lire [la leçon sur les instances](https://docs2.simplicite.io/lesson/tutorial/development/instances), il y a un exemple de recherche par code (cherche `product.search()`). Le search retourne un tableau de valeurs, ce qui consomme bien moins de mémoire et d'instances d'objets que la liste d'ObjectDB que tu demandes. Relis bien attentivement, ta question montre que cette leçon n'a pas été correctement assimilée (*si après ça tu penses que je suis dans l'erreur et que la liste d'ObjectDB se justifie, ou que tu ne comprends pas en quoi ça peut poser problème, on en reparle bien évidemment*).

---

Bonne journée à toi :wink:
