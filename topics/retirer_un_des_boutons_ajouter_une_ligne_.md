# Retirer un des boutons "ajouter une ligne"

**URL:** https://community.simplicite.io/t/7055

## Question
Bonjour,

Nous souhaitons retirer l'un des boutons "Ajouter une ligne" sur l'IHM. Il a t'il une faisabilité pour le retirer ?
Le bouton a retiré serait celui d'en bas (voir IMG)

![image|690x126](upload://c3rQp7IfpagU3NY0WaZ1HaxT6T1.png)

Merci.

## Answer
Bonjour, 

Ce bouton est visible lorsque vous êtes en mode "Modifier la liste" uniquement. 
Il apparait deux fois afin de le rendre disponible au cas où celui en en-tête de liste n'apparait plus à l'écran (liste avec beaucoup d'éléments).
Il n'y a pas de façon de paramétrer son affichage.

Vous pouvez tout de même surcharger le CSS de l'objet dans une ressource :
```css
tfoot{
	.btn-addrow{
		display:none;
	}
}
```

Si vous souhaitez modifier les façons dont une liste est modifiable, vous pouvez modifier le champ "Liste éditable" au niveau du paramétrage de votre objet :
![image|690x415](upload://78Vwsg6wAQXnCcOcWkcDojwMtFd.png)
