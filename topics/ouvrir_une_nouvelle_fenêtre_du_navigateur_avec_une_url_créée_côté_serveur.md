# Ouvrir une nouvelle fenêtre du navigateur avec une url créée côté serveur

**URL:** https://community.simplicite.io/t/5530

## Question
Bonjour,

Depuis un enregistrement, j'ai une action qui créé une url avec les données de l'enregistrement encodées Base64.

J'aimerai qu'une fois l'url créée, l'action se poursuive en ouvrant une nouvelle fenêtre avec cette url

Quels sont vos conseils sur la meilleure façon de faire?

Merci

Fabrice

## Answer
Bonjour, 

Dans le return de l'action vous pouvez appeler un bout de script js qui appelle l'ouverture d'un nouvel onglet. 

Par exemple : 

```
public String myAction(){
    ...
   String url = "https://my-url.ch";
   return sendJavaScript("window.open('"+url+"', '_blank')");
}
