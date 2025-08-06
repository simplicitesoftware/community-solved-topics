# Problème champ rapporté (UI)

**URL:** https://community.simplicite.io/t/4779

## Question
Bonjour, 
J'ai actuellement un problème d'affichage d'un champ sur une UI en particulier. 

Constat : dans la définition de l'object, dans le cas qui fonctionne, il y a bien les champs rapportés (165, 166 et 167) et donc ces trois champs sont bien visible dans l'IHM

---
![SCREEN 1|690x222](upload://zucui63GUOqsnjjg1TIerDpiwSQ.png)


et dans le cas qui pose problème il y a 2 champs rapportés mais indirectement (162 et 163) :

---
![SCREEN 2|690x192](upload://1kojyu3UTbf63EiZwZEaHm9MY8z.png)


Parmi ces deux champs ramenés indirectement, seul le champ 163 s'affiche correctement (présent dans le template editor) mais pas le 162. 

Avez-vous une idée du pourquoi ce champ ne s'affiche pas ?
Merci d'avance pour votre aide !

Cordialement, 
Elyass

## Answer
On me souffle que c'est peut être un pb d'ordre des attributs:

![image|690x192](upload://7rgrRXiVvXOCm9G7EDoFKkIMHFE.png)

Pour les attributs ramenés plusieurs fois à N niveaux l'ordre des FK ramenées est déterminant pour constituer le "chemin" (full input) par lequel l'attribut est ramené.
