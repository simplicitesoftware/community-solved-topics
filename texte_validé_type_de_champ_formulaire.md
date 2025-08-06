# Texte Validé : type de champ Formulaire

**URL:** https://community.simplicite.io/t/3602

## Question
A quoi sert les champs de type "Texte validé". 
Impossible de tester car on me demande de renseigner un "Type validé" dans le formulaire de création, que je ne trouve pas.

## Answer
Ce genre de champ est utilisé pour créer des types d'attributs "custom".

Admettons que tu as un attribut qui doit suivre la syntaxe "XXX-YYY", soit trois caractères alphabétiques, un tiret, puis à nouveau trois caractères alphabétiques. 
Tu vas donc définir un champ type "Texte validé" et sélectionner la regex - ou la créer - à appliquer pour ce champ. Soit la regex `^[a-zA-Z]{3}-[a-zA-Z]{3}$`

Le paramétrage de ton attribut sera donc :
![Capture d’écran 2021-07-30 à 10.00.53|690x275](upload://shLqGbKdkwB2qzYIcj1gaUR9KPw.png)


Et le type d'attribut :
![Capture d’écran 2021-07-30 à 10.04.57|690x215](upload://2gRtPHgZ0BjR6AFXILjwytq9vWA.png)


Sur le formulaire de l'objet, si la syntaxe n'est pas valide, tu auras donc un message :
![Capture d’écran 2021-07-30 à 10.06.24|690x257](upload://uwLl4DQjDhG0KJbR2hUf1DFquiF.png)
