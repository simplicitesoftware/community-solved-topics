# Problèmes de copie d'objet inliné

**URL:** https://community.simplicite.io/t/11577

## Question
### Request description

Bonjour,
Je rencontre des soucis avec la copie d'un objet avec objet lié inliné (pour changer :slight_smile: ).
J'ai reproduit avec un paramétrage simple :
- créer un objet A
- créer un objet B lié à A en inliné, cardinalité 1,1 et cascade copy = true
- la clé fonctionnelle de B est sa foreign key vers A (je ne sais pas si c'est important)
- dans le template form de A, ajouter explicitement B comme area (sinon l'objet inlined n'apparaît ni à la copie ni à la création, ce qui est bizarre)

![image|690x257, 75%](upload://2Fu5pWMedw058SkVcltabWAxkut.png)

Créer une instance de A puis cliquer sur Copy et Save.
J'ai deux soucis :
- l'instance inlined n'est pas copiée, elle est créée vide
- on dirait qu'on passe deux fois dans le preValidate de B, la 2ème fois après qu'il ait été créé. Cela déclenche une erreur ERR_USERKEY.

[Platform] Status=OK Version=6.3.2 BuiltOn=2026-01-30 20:34

Merci d'avance pour votre aide !
Emmanuelle

## Answer
Le problème a été reproduit et corrigé. 

En fait ce n'était pas prévu pour le cas 1,1 mais juste pour le cas 0,1.
On a aligné les usages : la recopie du parent affichera également une copie du lien fils s'il existe.
Et on a aussi corrigé un pb indirect de recopie de champ multi-documents.

Ce sera livré en 6.2.23
