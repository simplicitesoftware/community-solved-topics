# Déplacer le footer d'un processus metier vers le haut

**URL:** https://community.simplicite.io/t/8828

## Question
Bonjour,

Après avoir mis en place un processus métier sur mon référentiel, je souhaite remonter la bande de footer en haut. J'ai essayé d'y parvenir avec du code CSS, mais cela n'a pas fonctionné. Pourriez-vous me dire s'il existe une autre méthode pour le faire ou si j'ai peut-être raté une étape ? Merci d'avance !

![image|689x258](upload://yUaQ2Hq7wRrCianalsMX2b8z7JQ.png)

## Answer
Bonjour,

Il faudrait utiliser le debugger/inspector de votre navigateur pour vérifier/corriger votre CSS sur ces 3 éléments.

- si votre CSS est bien présent, où avez-vous déclaré le CSS custom ?
- si les selector sont corrects, `#pan_wkf_CreateEvaluation` existe dans la page ?

Par exemple en ajoutant à la ressource  `STYLES` de la disposition `responsive5`

```css
#pan_wkf_CreateUser > .card { display: flex; }
#pan_wkf_CreateUser > .card > .card-header { order: 1; }
#pan_wkf_CreateUser > .card > .card-body   { order: 3; }
#pan_wkf_CreateUser > .card > .card-footer { order: 2; }
```

On obtient à la création d'un User :

![image|690x346](upload://3Km1W7jQowHLIDJXV7z9LJvJW9c.png)
