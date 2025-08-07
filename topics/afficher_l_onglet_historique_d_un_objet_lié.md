# Afficher l'onglet historique d'un objet lié

**URL:** https://community.simplicite.io/t/4435

## Question
Bonjour,

J'ai un objet Flux historisé qui référence un objet Application. Je voudrais voir, pour chaque Application, l'historique de ses flux. J'ai bien mon FluxHist dans les links de l'objet application, avec visible = yes. Mais l'onglet n'est pas visible et en mettant une trace dans le CanReference je vois que ce lien n'est pas testé.

Est-ce qu'il y a un moyen de faire apparaître cet onglet ?

Merci !
Emmanuelle

Version=4.0.P25
BuiltOn=2021-12-22 23:20 (revision f67a357ce5c6322b35b751aab7d68c776dbefbe1)

## Answer
Il doit manquer un droit en lecture sur FluxHist pour le groupe habilité à Application ?
canReference est appelé depuis Application si l'utilisateur est au moins habilité en lecture à l'objet lié.
