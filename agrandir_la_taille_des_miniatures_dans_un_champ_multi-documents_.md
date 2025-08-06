# Agrandir la taille des miniatures dans un champ "Multi-Documents"

**URL:** https://community.simplicite.io/t/4254

## Question
Bonjour,

Je souhaite créer un attribut qui peut contenir plusieurs photos, j'ai donc choisi le "Multi-documents".
Quand je charge mes photos, elles s'affichent avec une taille correcte (visible) : 

![photos avants enregistrer|690x488](upload://2PJ8i6opYZZWxniucH2LMSD459X.png)

Or, quand j'enregistre mon formulaire, les miniatures sont toutes petites :
![photos après enregistrer|690x332](upload://xoHg6wXnwbfA55bsf1TqKSBjl3c.png)

Y-a-t 'il un moyen pour agrandir la taille des miniatures dans ce champ ? 
Merci d'avance.
Abed.

````
[Platform]
Status=OK
Version=5.1.21
BuiltOn=2021-12-23 12:45
Git=release/1e05783d2d3869696ea8a6f09d20660ee6eb88cc
Encoding=UTF-8
EndpointIP=149.202.173.228
EndpointURL=http://e3m.simplicite.io:10118
TimeZone=Europe/Paris
SystemDate=2021-12-27 16:46:55
````

## Answer
Après vérification, il est bien possible de préciser à la fois la dimension d'une image miniature et le taille max des fichiers dans un champ multi-documents.

Par exemple 
- sur un champ de type **Document** en rendering **Multi-documents boxes**
- avec une Précision égale à **w=200 max=1** 

Les thumbnails des images feront 200px 
et chaque fichier ne devra pas dépasser 1Mo.

Enfin pour préciser en plus :
- le nombre min et max de fichiers joints
- et les types de fichier (mime types / accept files)

Il faut le paramétrer au niveau du **Bookshelf** lié au champ.
