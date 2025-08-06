# Problème sauvegarde avec une action

**URL:** https://community.simplicite.io/t/4395

## Question
Bonjour,

J'ai une action qui sert de transition d'état entre l'état 1 et 2.
Lorsque je clique dessus, j'affiche dans les logs les valeurs contenues dans les champs de mon formulaire, mais le problème, c'est que même si je rentre des valeurs et que j'appuie sur l'action, la valeur affichée dans les logs est vide.

1) Je renseigne mon champ
![image|690x48](upload://v2qBOpmdoBTboiPLFlJDbCu57R6.png)

2) Je clique sur mon action
![image|343x44](upload://sPkFpnLVVQ9WN9yJ1hUmsEwiFhh.png)

3) J'affiche la valeur de mon champ dans les logs pour vérifier si l'action prend bien en compte mon formulaire
![image|556x19](upload://tMKd9fNlXUt7Khxt2oe1erZPZ8E.png)
![image|356x40](upload://m335gD3KPLIpxbzGv7BHqvuBuDB.png)

C'est vide et aucune valeur n'est affichée. J'ai l'impression que mon action prend en compte uniquement la valeur enregistrer dans le champ mais pas la valeur actuelle (celle qui n'a pas encore été enregistrer). La preuve est que si je sauvegarde mon formulaire avant d'appuyer sur l'action, ma valeur est bien prise en compte. Mais si j'essaye de la modifier par une autre valeur et que j'appuie sur l'action avant de cliquer sur le bouton "Enregistrer", j'ai toujours l'ancienne valeur, mais pas la nouvelle.

Je voudrais vraiment ne pas avoir à cliquer sur "enregistrer" avant de cliquer sur mon action et que ce soit l'action qui enregistre pour moi. Avez-vous une idée ?

## Answer
Vérifiez que vous n'avez pas du JS ou un nom de méthode résiduel en la repassant temporairement  en "Front" puis "Back"

Un action de transition d'état nominale est nécessairement de type "Aucun" sans méthode ou traitement JS.

Ensuite, vous avez peut être des contraintes ou du code qui rend votre attribut non modifiable à un "mauvais" moment = trop tôt (un attribut non modifiable au moment de l'enregistrement n'est - légitimement - pas pris en compte à l'enregistrement). Dans ce cas essayez d'inhiber votre code (en le mettant en commentaires) et/ou vos contraintes (avec un ordre négatif) pour cerner ce qui pose pb.
