# Reset Field de type Document après échec du preValidate

**URL:** https://community.simplicite.io/t/4043

## Question
Bonjour,

J'ai un comportement que je n'arrive pas à comprendre ni à expliquer, malgré mes recherches :

J'ai un objet avec 61 ObjectFields. J'ai commenté tout le code java de l'objet pour être certain que le problème ne vienne pas de celui-ci : il ne me reste qu'un initUpdate dans lequel je rend obligatoire deux champs : un champ numérique (achNumSibo), et un champ de type Document (achJustifCommande).

Lorsque je prend un objet existant et que j'ouvre son formulaire, j'efface le contenu du champ achNumSibo, et je renseigne le champ achJustifCommande :
![image|690x147](upload://mQpQjGGoLcV2cknbCxH0btbpvxU.png)

A l'enregistrement, j'ai alors un message d'erreur me demandant de renseigner le champ achNumSibo, ce qui est normal car ce champ est obligatoire. Notez que le champ achJustifCommande est bien renseigné :
![image|690x261](upload://qawqasVQRPCwsXyz6kVnEWzHOUG.png)

Je renseigne alors le champ achNumSibo, puis je réenregistre. L'objet est bien enregistré, mais le champ achJustifCommande a été réinitialisé (1/ si le champ est vide, tout en étant obligatoire, je ne comprends pas comment l'objet a pu passer le validate() avec succès ; 2/ le champ n'aurait pas du être vide, car avant que je clique sur enregistrer, le champ était bien renseigné) :
![image|690x217](upload://aMI0aokcPWykEZNQFtHs3VFzXBE.png)

Quelques informations supplémentaires :
- J'ai parfois le message d'erreur : "WARN|designer|com.simplicite.util.engine.ObjectManager|historize||Evénement: Empty path for document 0" dans les logs lorsque j'enregistre pour la 2e fois (une fois que je renseigne le champ achNumSibo).
- A cause du message d'erreur ci-dessus, j'ai essayé de désactiver l'historique de l'objet, puis d'effacer l'objet historique correspondant et de le regénérer, mais ces deux manipulations n'ont rien donné. (le message d'erreur disparait néanmoins).
- Lorsque j'essaie sur un objet "plus petit" (= moins de 10 champs), j'arrive bien à sauvegarder mon objet, et le fichier est conservé lors du 2e appui sur le bouton "Enregistrer". De même, sur la démo, sur un objet "plus petit" (= moins de 10 champs), le fichier est conservé lors du 2e appui sur le bouton "Enregistrer". Les objets sur lesquels j'effectue les tests m'ont l'air identique (hormis le nombre de champs) et les champs sont paramétrés de la même manière.
- Lors de certains cas de tests, j'ai l'impression que le fichier est bien conservé (sur mon objet "Achat" de départ). Mais je n'arrive pas à reproduire ce phénomène de façon récurrente (j'ai réussi 2 fois, sur des dizaines et dizaines de tests...)
- J'ai essayé d'effacer/recréer le Field et l'ObjectField achJustifCommande, sans résultats...
- Ce ne serait pas une solution, j'en suis conscient, mais : j'ai essayé de sauvegarder le fichier dans le prevalidate dans le répertoire temporaire pour conserver le fichier en cas d'erreur (champs obligatoires non renseignés par exemple ?), dans le cadre de mes tests, mais cela n'a pas abouti...

Le problème viendrait-il du fait que le fichier n'est pas conservé assez longtemps ? Auriez-vous des idées d'où pourait venir ce phénomène ? Ou bien des pistes que je pourrais explorer afin de résoudre ce problème ? J'ai l'impression d'avoir regardé partout...

Merci d'avance pour votre aide,

Alexandre

![image|690x64](upload://onmbsd9VXmTmaf3SgAFt123w4MU.png)

## Answer
Bonsoir, 

Merci pour les réponses. On a mis à jour avec la dernière release, et j'ai toujours le problème, sur l'instance de démo, avec la même manipulation.

nb : @François, une petite nuance avec votre vidéo : je ne dis pas que les champs de type document sont vidés s'ils étaient renseignés avant l'enregistrement - le cas que vous montrez. Je dis que si on part d'un formulaire avec un champ document vide, qu'on le renseigne, qu'on fait échouer le validate avec un premier enregistrement, puis qu'on réenregistre cette fois-ci avec succès, alors le document est perdu, comme dans la vidéo suivante : [Echec validate.zip|attachment](upload://Ao2HGOaikMQNxPpwvQDEsFZjsUo.zip) (5.0 MB)
De plus, si le champ document est obligatoire, mon objet est sauvegardé malgré tout...

Peut-être avez vous également testé mon cas, mais que vous ne reproduisez pas non plus, mais ce n'est pas grave, j'ai enlevé les contraintes de type back que j'avais sur l'objet, je rajouterai si besoin le code correspondant directement dans le prevalidate : ça marche bien comme ça !

Merci encore ! :slight_smile:
