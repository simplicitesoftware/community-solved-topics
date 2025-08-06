# Action de liste qui agit differement lorsqu'elle est déclenchée depuis une vue

**URL:** https://community.simplicite.io/t/8502

## Question
### Request description

Action de liste qui agit differement sur le menu principal. 
This request concerns an Simplicité instance 5.3.28

### Steps to reproduce

Bonjour à tous,

J'ai configuré une action de liste sur l'un de mes objets, qui fonctionne parfaitement. Cette action a pour but de présenter à l'utilisateur un formulaire de saisie simplifié où il configure des paramètres. Ensuite, cela prégénère des enregistrements à compléter avant d'ouvrir la liste en mode édition pour que l'utilisateur puisse finaliser les détails.

Lorsque j'accède à cet objet via un domaine et que j'utilise le bouton d'action de liste, tout fonctionne correctement. Cependant, ce formulaire étant destiné à un utilisateur spécifique, j'ai créé un utilisateur dédié et j'aimerais lui présenter directement cette action de liste sur sa page principale.

Pour cela, j'ai configuré une vue qui est définie comme page principale. Cette vue affiche correctement la liste avec le bouton d'action de liste. Toutefois, lorsque j'essaie d'utiliser ce bouton via la vue, le comportement est différent : le formulaire s'affiche, mais une fois rempli, les enregistrements ne se créent pas comme habituellement et les filtres ne s'affichent pas non plus.

En revanche, si l'utilisateur accède directement à la liste et non via la vue de la page principale, l'action de liste fonctionne parfaitement.

Je suppose donc que le problème vient de ma configuration de la vue. Pourriez-vous m'aider à identifier ce qui ne va pas ?
![image|690x326](upload://cp7HaFlwQp65iZjQaTd8FJmlsiZ.png)


Merci d'avance pour votre aide !

## Answer
Bonjour Mathias, 

Vous n'êtes pas sur la même instance de l'objet sur une vue (home instance).
Sur l'objet principal vous êtes sur une main instance. 

https://docs.simplicite.io/tutorial/development/instances

Si `inst` n’est pas spécifié dans les paramètres du `displayList`, par défaut ce sera the_ajax_xxx = Main instance.  

Vous pouvez tester si vous êtes sur une Home instance de l'objet 
https://platform.simplicite.io/5.3/javadoc/com/simplicite/util/ObjectCore.html#isHomeInstance() et l'envoyer au displayList.
