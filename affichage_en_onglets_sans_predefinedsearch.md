# Affichage en onglets sans PredefinedSearch

**URL:** https://community.simplicite.io/t/6502

## Question
### Request description

Bonjour,

J'ai paramétré un menu accessible à gauche qui fait apparaître plusieurs listes d'objets dans l'écran principal, sous forme d'onglets.

![image|690x127](upload://xYPffv31ef9Kzlafai4e41j4W53.png)

Pour cela j'ai ajouté une Home page visible comportant une PredefinedSearch par onglet avec filtre = {}.

Cela me pose problème car quand j'essaie d'appliquer des filtres par code sur une de ces listes dans le postLoad, la predefinedSearch les remet à vide.

Ma question est la suivante : y a-t-il un moyen d'afficher des objets métier sous forme d'onglets sans passer par une PredefinedSearch ?
Sinon, y a-t-il un moyen de faire en sorte qu'un filtre vide ne soit pas géré comme un resetFilters ?

Merci d'avance pour votre aide !
Emmanuelle

## Answer
C'est bien compliqué ton histoire. Pourquoi réinventer la roue ?

Depuis la 5.0, il est possible de définir N preset-search, et l'utilisateurs peut les sélectionner depuis la liste ou faire un reset.

![image|453x152](upload://lmCvhY4C3vm0QimCwQBB1TqAGzb.png)


Sinon il faut le faire à l'ancienne/V4 par des actions/boutons, les actions positionnent juste des paramètres de contexte setParameter("WhatsTheFilter", "blablah");

Et le preSearch, récupère les paramètres pour forcer/retirer des filtres,
le isActionEnable teste les paramètres, etc.
