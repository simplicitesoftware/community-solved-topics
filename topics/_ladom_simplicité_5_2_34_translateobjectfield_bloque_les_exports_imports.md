# [LADOM] [Simplicité 5.2.34] TranslateObjectField bloque les exports/imports

**URL:** https://community.simplicite.io/t/6598

## Question
Bonjour, 

cela fait aujourd'hui 2 semaines que je fais face à un problème récurrent et bloquant. Nous travaillons sur plusieurs versions selon les livraisons: entre une 2.3.* et une 2.4.* Il m'arrive souvent de basculer d'une version à une autre. Dans la 2.4 je crée un objet Facture qui réfère un autre objet, cela se passe bien. Cepndant quand je passe sur une 2.3.* (l'objet Facture n'existe pas dans ce contexte), je fais mes développements, j'exporte le module en tar.gz et lors de l'import j'ai des erreurs avec l'objet `TranslateObjectField`, cette erreur semble se produire sur des champs sur lesquels je travaille en 2.4. mais cela se produit lorsque je suis en 2.3. J'ai bien sûr vidé tous les caches, Simplicité + navigateur mais rien n'y fait. La seule option pour moi est de supprimer les containers et les image, faire une commande Docker type `docker rm $(docker ps -a -q)` (notre instance locale provient d'une image) et de tout réinstaller et réimporter toutes les données, ce qui fait perdre énormément de temps et d'énergie. Je vous ai laissé les logs en PJ afin de laisser le post visualisable. 
[flow_20230627_141947.log|attachment](upload://1Qg0iUJeYfslLIkl7AolE3rpWiq.log) (7.6 MB)
Je vous remercie

## Answer
Dans votre cas nous vous **recommandons fortement**  de travailler sur **deux instances distinctes**. 
Une avec votre module en 2.3 et l'autre avec votre module en 2.4.
