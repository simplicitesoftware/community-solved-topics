# Personnaliser l'affichage d'un domaine dans le menu

**URL:** https://community.simplicite.io/t/9413

## Question
### Request description

Bonjour,

Nous avons un besoin spécifique concernant la personnalisation des domaines dans le menu left-sidebar. 

Pour un domaine précis, nous souhaitions afficher uniquement les objets qu'il contient, sans montrer le titre du domaine lui-même. De plus, empêcher l'utilisateur de replier/déplier ce domaine, tout en maintenant les sous-menus toujours visibles.

**Exemple vue démo_User :**
![image|309x500, 50%](upload://cMftw4u1P7h2set5f1b8UWWX2Ov.png)


### Steps to reproduce

Dans le module de démo, nous avons donc essayer de gèrer ce comportement dans le scriptUI via le code suivant et cela marche, nous n'avons plus le titre du domaine et toujours les objets,process.. du domaines visible : 
[details="Script UI"]

```
/* Specific client script */
(function($) {
    $(document).on("ui.ready", function() {
        
        let demoMenu = $("a[data-domain='DemoDomain']").parent();
        
        if (demoMenu.length > 0) {
            console.log("Élément 'Démo' trouvé :", demoMenu);

            demoMenu.children("a").hide();
            console.log("Titre 'Démo' caché.");

            let subMenu = demoMenu.find(".sub-menu");
            subMenu.css("display", "block");
            console.log("Sous-menu affiché en permanence.");

            demoMenu.off("click");
            console.log("Événement de clic supprimé.");
        } else {
            console.log("Élément 'Démo' non trouvé.");
        }
    });

    $(document).on("ui.beforeunload", function() {
  //      console.log("Déchargement de la fenêtre en cours...");
    });

    $(document).on("ui.unload", function() {
//        console.log("Fenêtre déchargée.");
    });

})(jQuery);

```
[/details]
**Vue Demo_User après :**

![image|280x500, 50%](upload://9rJsT40WXBU95UTvBVWLEaZNGUB.png)

Nous souhaitions savoir si c'était la meilleure manière de faire dans le cas ou ce besoin est réitéré sur d'autres projets. 
Ou bien d'autres facon de faire comme l'utilisation de hooks serveur ou d'autres mécanismes pour l'avoir en natifs de Simplicité ?

Merci d'avance pour vos retours et suggestions. :slight_smile:

## Answer
Bonjour, 

La manière de faire par paramétrage est de créer autant de domaines que d'objets. Un domaine qui ne possède qu'un seul objet affiche la traduction de l'objet dans le menu. Tout dépend donc du nombre d'objets. Si votre script permet d'adresser ce besoin, vous pouvez le mettre dans un module commun à toutes vos applications (parent des autres modules applicatifs).
