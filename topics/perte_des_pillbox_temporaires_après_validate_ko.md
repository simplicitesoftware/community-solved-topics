# Perte des pillbox temporaires après validate KO

**URL:** https://community.simplicite.io/t/10926

## Question
### Request description

Bonjour,
J'ai l'impression qu'on perd les pillbox temporaires en cas d'erreur au Create.

- Faire Create sur un objet comportant des pillbox
- Sélectionner au moins une valeur dans la pillbox
- Laisser un champ obligatoire vide
- Faire Save
-> les pillbox semblent avoir disparu

Merci d'avance !
Emmanuelle

[Platform]
Status=OK
Version=6.2.17
BuiltOn=2025-10-02 18:05

## Answer
Oui nous avons eu le même soucis. 
Quand le formulaire se recharge le tmppb est perdu.

Ca sera corrigé avec l'évolution sur la copie.
