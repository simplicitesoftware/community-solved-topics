# Champ forbidden exportable

**URL:** https://community.simplicite.io/t/6430

## Question
### Problem description

Les attributs d'objet forbidden sont exportables.

### Steps to reproduce

1. Paramétrer un attribut d'objet en forbidden
2. Faire un export excel, l'attribut est exporté

### Technical information

Simplicité version 5.3.3
Built on 2023-05-15 21:17

## Answer
La notion de visibilité ne s'applique pas aux exports de données, c'est comme un attribut masqué côté UI, il faut parfois l'exporter pour un usage externe (un salaire par exemple pour la RH).

C'est la notion "exportable" qui s'applique.
Field.isExportable / setExportable...
