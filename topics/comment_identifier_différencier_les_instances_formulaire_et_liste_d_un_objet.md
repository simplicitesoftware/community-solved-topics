# Comment identifier/différencier les instances formulaire et liste d'un objet

**URL:** https://community.simplicite.io/t/5255

## Question
Bonjour,

Je voudrais personnaliser l’affichage (ou non) des listes filles quand je suis sur un formulaire d’un objet A. Pour cela, j’utilise **canReference** qui fait très bien l’affaire, mais qui prend un peu de temps, ce qui est normal vue le nombre de contrôle que je fais.

Or, cette contrainte (canReference), se lance même quand je suis sur la liste principale de l’objet A, et donc cela prend un temps encore plus important.

Je souhaite donc ajouter un contrôle dans ce canReference pour ne l’exécuter que si je suis sur un formulaire A et non pas sur la liste A.

Comment puis-je différencier l’instance du formulaire de celle de la liste ? (L’utilisation de isMainInstance me rend le même résultat que cela soit un formulaire ou une liste.)

Merci d’avance.

Abed.

[Platform]
Status=OK
Version=5.2.14
BuiltOn=2022-09-09 19:11
Git=5.2/c59be7fc25acb41d6994979998cfb42547c6e188
Encoding=UTF-8
EndpointIP=149.202.173.228
EndpointURL=http://e3m.simplicite.io:10118
TimeZone=Europe/Paris
SystemDate=2022-09-12 12:01:05

## Answer
Si tu ne veux exécuter tes test uniquement lorsque tu es sur le formulaire de l'objet, tu peux tester : `getContext().isUpdate()`
