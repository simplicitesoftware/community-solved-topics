# Attribut "Document" en clé fonctionnelle

**URL:** https://community.simplicite.io/t/11040

## Question
Bonjour,

Je n’arrive plus à paramétrer en “clé fonctionnelle” un attribut de type “Document” alors que j’y arrivais en 4.0

J’obtiens ce message dans le formulaire : “This field type cannot be used as functional-key due to index size limitation.”

Est-ce une limitation de la 6.2 ?

## Answer
Bonjour,

Cette limitation fait partie des breaking changes de la 5.3 : https://docs.simplicite.io/versions/release-notes/v5-3/#no-more-user-key-on-huge-fields
