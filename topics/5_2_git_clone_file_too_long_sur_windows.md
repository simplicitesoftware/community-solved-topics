# 5.2 GIT clone file too long sur Windows

**URL:** https://community.simplicite.io/t/5320

## Question
Bonjour,

nous sommes en phases de migration vers la 5.2.16 (nous sommes en 5.1.45). J'ai un problème avec les nouveautés git.
Lorsque je clone clone le repo sur mon PC (windows 10) j'ai les erreurs suivantes :

![image|690x318](upload://7hJ9P4oZucftBRfINRFqA95OU4a.png)

J'ai configuré le référentiel en indiquant localhost comme c'était en 5.1 comme valeur par défaut.
![image|690x303](upload://andjvox3JfyTveGcSrjLt78vZxV.png)

Merci de votre aide,
Thierry

## Answer
Oui comme déjà expliqué, l'export éclaté en JSON pose problème sous Windows qui bride la profondeur de l'arbre/path à 256 (pour compatibilité avec feu MSDOS).

Nous n'avons pas trouvé de solution simple/fiable pour lever cette contrainte sous Windows.
Ce sujet est en cours de dev et sera bien livré en 5.3. On verra pour backporter en 5.2 dans la foulée.

- L'export en fichiers JSON éclatés se fera dans les mêmes répertoires statiques que l'export XML éclaté
- Le diff par la UI entre un répertoire éclaté et une instance ne sera plus possible sous forme arborescente, ce qui sera un breaking change pour la 5.3 et une régression pour la 5.2. On verra pour parcourir l'arbre autrement si c'est possible plus tard.
