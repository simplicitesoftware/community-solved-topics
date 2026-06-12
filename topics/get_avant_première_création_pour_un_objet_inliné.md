# Get avant première création pour un objet inliné

**URL:** https://community.simplicite.io/t/12472

## Question
### Request description

Bonjour,
Je constate une différence de comportement entre la 6.3.9 et la 6.3.10 : lors de la création d'un objet inliné, on passe dans le get avant que celui ci ne soit effectivement créé.

Mode opératoire :
- avoir un objet A avec un objet B inliné
- surcharger le getTargetObject de B et mettre un log
- créer une instance de A
-> dans getTargetObject, on constate qu'on passe avant la création de B. Le rowId de B = 0 et ses valeurs sont nulles.

J'ai contourné en testant le rowId avant de faire la suite du getTargetObject, mais le problème s'est déplacé dans isUpdateEnable, puis dans un autre hook non identifié car pas surchargé chez moi.
Dans tous les cas, la création finit en erreur.

Si je refais le même test, je n'ai plus le souci.

Merci d'avance pour votre aide !
Emmanuelle

## Answer
J'ai trouvé la cause du problème, c'était moi :grin:

J'avais mis la clé vers le père en lecture seule pour éviter que les utilisateurs puissent le modifier en Edit list. Je ne sais pas pourquoi ça ne posait problème qu'à la première création, j'ai sûrement quelque chose qui le remet en édition par la suite.
En tout cas c'est ce qui faisait faire n'importe quoi à mes hooks derrière.

Je m'auto solutionne, toutes mes excuses pour le dérangement !

Emmanuelle
