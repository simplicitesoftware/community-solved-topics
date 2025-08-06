# Filtre / row_id rémanant lors de l'affichage en liste intégrant des pillbox

**URL:** https://community.simplicite.io/t/3811

## Question
Bonjour,
j'arrive après la bataille sur le post https://community.simplicite.io/t/export-csv-de-lensemble-des-lignes-ne-fonctionne-pas/3806/11?u=bmo
Cela ressemble à un problème que nous avons rencontré sur des objets présentant eux aussi des pillbox en liste : dans notre cas, l'affichage en liste se limitait à une seule ligne et nous avons en effet constaté qu'un filtre était positionné sur le row_id alors que ça n'avait a priori aucun sens métier. On a d'abord pensé à un effet de bord non maîtrisé de notre côté et mis en place un contournement dans les hook initList des objets concernés (resetFilter sur le champ row_id) en attendant de trouver le temps de comprendre (:sweat:).

Dans l'hypothèse où ce serait bien la même chose, si la résolution pouvait aussi couvrir le cas de l'initList ce serait super :slight_smile:

ps: nous sommes encore en Version=4.0.P25 BuiltOn=2021-07-16 10:19 mais on va se mettre à jour asap

## Answer
Après une descente archéologique dans le contexte d'une recherche en liste, une meilleur gestion de la concurrence d'accès entre toutes les pillboxes a été ajoutée dans toutes les versions. Le problème ne semble plus se produire sur nos cas de tests. Le "row_id" retrouve bien son filtre d'origine (% ou autre).

A tester dans une prochaine livraison sur votre instance.
