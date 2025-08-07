# Configuration External Object

**URL:** https://community.simplicite.io/t/8432

## Question
### Request description

Bonjour, 

Nous sommes passés de la version 5.2 à la 5.3. 
Avec cette montée en version je viens de constater qu'un external object que l'on avait configuré et placé dans un Domain ne fonctionne plus. Celui-ci avait pour but d'accéder rapidement à l'écran d'import XML. Je n'arrive pas à trouver la raison de pourquoi cela ne marche plus maintenant ? Est ce l'url que l'on avait configuré qui n'est plus d'actualité ? 

![image|690x273](upload://jzWwByAS3MyQXBKM9jM7IaNYXNz.png)

Merci d'avance.
Mathias.

## Answer
Bonjour Mathias,
Vous pouvez utiliser:
`javascript:$ui.displayImportXML()`
au lieu de:
`[EXPR:HTMLTool.getImportExportURL("action=import")]`
Candice
