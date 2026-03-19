# Correction visibilité sur contrainte en liste

**URL:** https://community.simplicite.io/t/11808

## Question
### Request description

Bonjour,

Je viens d'installer la 6.3.6 et j'ai toujours le problème de visibilité en liste mentionné ici https://community.simplicite.io/t/contrainte-de-visibilite-en-liste/11771/10

Dernière ligne ne valide pas la contrainte : colonne cachée
![image|534x500, 75%](upload://gL7KVJY7LIweAN3EEHFQ2RPWw0P.png)

Dernière ligne valide la contrainte : colonne affichée

![image|690x383, 75%](upload://v4CsSE3G8lQOZTLoYj1ONTKqqYl.png)

Merci d'avance pour votre aide !
Emmanuelle

[Platform]
Status=OK
Version=6.3.6
Variant=full
BuiltOn=2026-03-12 16:20

## Answer
Voilà une solution qui fonctionne :

Les meta-data de l'objet, lors du search, évaluent d'autres contraintes pour savoir si l'utilisateur peut créer/copier un record. Donc une solution simple est d'ajouter une contrainte en contexte CREATE qui passera après ta contrainte `true` qui s'applique tout le temps :

Contrainte C1:  
- `Front + Back`, ordre `10`, expression = `true`
- Impact Field `demoSupPhone` visible = `[VALUE:demoSupName].equals("SUP")`

Contrainte C2:  
- `Back`, ordre `20`, expression = `[CONTEXT:CREATE]`
- Impact Field `demoSupPhone` visible = `true`
