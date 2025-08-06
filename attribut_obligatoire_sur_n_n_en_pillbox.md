# Attribut obligatoire sur N,N en pillbox

**URL:** https://community.simplicite.io/t/7679

## Question
### Request description

Bonjour,

Je souhaiterais pouvoir proposer à l'utilisateur la saisie d'un attribut obligatoire de la N,N à la sélection d'un élément présenté en pillbox, comme c'est le cas pour le Associate sur les child lists.
Existe-t-il un hook front qui me permettrait de coder ceci ?

Merci d'avance,
Emmanuelle

## Answer
Oui ce composant fait une simple création de lien entre les 2 objets sans hook front.
Il n'y a pas que la création à concevoir, il faut aussi prévoir la modification (la criticité peut changer, erreur de saisie...).

- Il faudrait une évolution pour passer par le formulaire comme le fait l'action "associate" si l'objet contient plus de champs que les 2 foreign-keys
- Mais il faudra aussi pouvoir ouvrir la N,N pour modifier son contenu quelque part (qui peut être plus complexe qu'un simple booléen). Actuellement ça doit ouvrir l'objet lié et pas la N,N
