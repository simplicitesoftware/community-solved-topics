# Peut-on utiliser "initRefSelect" en front

**URL:** https://community.simplicite.io/t/4471

## Question
Bonjour,

Je souhaite mettre en place un filtre, de manière dynamique, sur une liste d’une instance Panel, en fonction d’un attribut dans le formulaire de l’objet parent.

C’est-à-dire, si je change la valeur de l’attribut, le nouveau filtre s’applique aussitôt au niveau de la liste panel, sans que j’aie besoin d’enregistrer l’objet parent.

Actuellement, j’utilise le hook « initRefSelect », mais il ne tient compte que des valeurs enregistrées de l’attribut, et non pas d’une nouvelle valeur saisie dans l’attribut (sans enregistrer le formulaire).

Je ne sais pas si le besoin est clair.

Est-ce qu’il y a un moyen d’avoir ce filtre « dynamique » ?

Merci d’avance

Abed.

## Answer
Bonjour Abed, 

Désolé que tu sois bloqué... Si j'avais à le faire, je m'appuierais sur :

* La [jsdoc v5](https://docs.simplicite.io/5/jsdoc/)
* [js] object hooks (voir exemple [chartjs](https://community.simplicite.io/t/chart-usage-example/919))
* [js] [Simplicite.Ajax.BusinessObject.html#setParameter](https://docs.simplicite.io/5/jsdoc/Simplicite.Ajax.BusinessObject.html#setParameter)
* [js] [Simplicite.UI.Engine.html#displayList](https://docs.simplicite.io/5/jsdoc/Simplicite.UI.Engine.html#displayList)
* [java] [ObjectDB.getParameter](https://docs.simplicite.io/5/javadoc/com/simplicite/util/ObjectCore.html#getParameter(java.lang.String))
* [java] [ce tips & tricks](https://community.simplicite.io/t/how-to-make-an-optional-initrefselect/1374) sur un cas particulier d'initRefSelect

Malheureusement je n'ai pas d'exemple sur étagère à ce jour, et la construction d'une solution sur mesure relève du support personnalisé, que nous fournissons volontiers via des tickets de support.
