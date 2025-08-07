# *EASY* by Paramètres système (module System)

**URL:** https://community.simplicite.io/t/7540

## Question
Bonjour la team Simplicité,

Lors d’une montée de version du socle 4 à 5.3, nous n'avons retrouvé les paramètres système (module System) suivant :

* EASYMODE
* EASYMODE_CLEARCACHE
* EASYMODE_DEFAULTAPPCODE
* EASYMODE_DEFAULTDOMAINNAME
* EASYMODE_DEFAULTGROUPNAME
* EASYMODE_DEFAULTMODULENAME
* EASYMODE_PATCHES

Pourriez-vous nous confirmer qu'il s'agit bien d’une évolution de votre part ?
Quels sont les impacts et comment gérer-vous désormais ces fonctionnalités ?

Merci d’avance,

![easy|690x231](upload://yQSHVRTh6CDjWbIxEjVBr54QSlP.png)

## Answer
Bonjour Bertrand,

Effectivement le EASYMODE disparaît est remplacé :

* `EASYMODE` -> n'a plus lieu d'être depuis que le template editor facilite les process facilités par EASYMODE
* `EASYMODE_CLEARCACHE` -> c'est désormais le comportement par défaut de la plateforme
* `EASYMODE_DEFAULTDOMAINNAME` -> remplacé par de la sélection explicite d'un domain des modules visibles
* `EASYMODE_DEFAULTGROUPNAME` -> remplacé par de la sélection explicite d'un domain des groupes visibles
* `EASYMODE_DEFAULTMODULENAME` -> remplacé par les notions de module visible et module par défaut, sélectionnables via le raccourci "module selector" 

![visible|623x455](upload://yAnjTkdp2U8vIhnSxRYLg091Vei.png)
