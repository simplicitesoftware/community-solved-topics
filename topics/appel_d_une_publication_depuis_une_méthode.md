# Appel d'une publication depuis une méthode

**URL:** https://community.simplicite.io/t/5286

## Question
Bonjour,

J'ai une méthode déclenchée par une action qui va demander une date à l'utilisateur puis créer un xml. A la fin la méthode appelle une publication :

avec : `return this.sendRedirect(HTMLTool.getPrintTemplateURL(this.getName(), this.getInstanceName(), "ParticipationPctMandatLettreMissionPDF"));`

le résultat s'affiche bien

avec `return this.javascript("$ui.displayPrint(null, 'ParticipationPctMandatLettreMissionPDF', '" + this.getName() + "', '" + this.getRowId() + "')");`

La publication n'est pas appelée.

> Simplicité version5.2.15
Built on2022-09-19 14:58

## Answer
Bonjour,

Je vais m'en inspirer.

Merci
