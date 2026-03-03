# Le Guide Recorder génère des sélecteurs incorrects pour les éléments de menu

**URL:** https://community.simplicite.io/t/11700

## Question
### Request description

Bonjour,

Nous utilisons actuellement la fonctionnalité Recorder et avons identifié un comportement qui pourrait devenir un point de frustration majeur pour nos utilisateurs métiers.

Nous avons constaté que le Recorder ne génère pas les sélecteurs corrects pour les éléments de menu. Il produit systématiquement un sélecteur du type `#menu [data-path='undefined']`.

Bien qu'il soit possible de corriger manuellement ces sélecteurs dans l'éditeur de Tour, notre objectif est de permettre à des utilisateurs non techniques (profils métiers) d'utiliser le Recorder de manière autonome. Cette nécessité de correction manuelle contredit cet objectif.

Serait-il possible d'examiner ce point afin que le Recorder puisse générer les sélecteurs appropriés pour les éléments de menu ? Cela améliorerait grandement l'expérience utilisateur pour nos équipes. 

[Platform]
Status=OK
Version=6.3.5
BuiltOn=2026-02-20 11:40

## Answer
Bonjour, 

Les éléments de menu sont composés de plusieurs éléments :
```html
<li>
    <a href="" class="js-searchable" data-obj="Dataset" data-path="DomainProject.Dataset">
        <div class="ico"></div>
        <span class="text">Datasets</span>
    </a>
</li>
```
En l'état, lors de la sélection d'étape de guide, si vous faites un click droit sur l'**icone** ou le **texte** de l'élément, la plateforme produit effectivement un sélecteur undefined : `#menu [data-path='undefined']`.
Si vous faites un click droit ailleurs : à droite du libellé par exemple, le sélecteur généré contient le bon `data-path`

Nous avons rendu le sélecteur plus robuste afin de ne pas devoir cliquer de façon précise pour générer un sélecteur correct.
