# Paramètre importé par deux modules

**URL:** https://community.simplicite.io/t/2997

## Question
Bonjour,
Est-il possible qu'un paramètre système soit importé avec deux modules différents ?
Exemple: un paramètre TESTING défini a la fois dans un module A et un module B mais ayant des valeurs différentes dans chacun.
Dans ce genre de situation, comment définir lequel utiliser ?

Merci d'avance !

## Answer
Bonjour Gireg,

Si un paramètre système est défini par plusieurs modules, le dernier module importé écrase le paramètre système. 

La solution à cette problématique est généralement :

* de préfixer les noms de paramètres avec le préfixe du module afin d'assurer une certaine unicité
* de définir les paramètres de l'application dans un module à part (par exemple AppConfig), et d'introduire une dépendance de modules afin que le modules applicatifs ne puisse pas s'installer sans le module de paramétrage. si tous les paramètres systèmes d'une instance sont dans un même module, le risque n'existe pas, et ça facilite la création de fichiers de configuration pour vos différents environnements (dev, recette, etc)
