# Contrainte de visibilité sur un attribut document multiple

**URL:** https://community.simplicite.io/t/3985

## Question
Bonjour,
lorsque j'utilise une contrainte sur un attribut avec une présentation "multidoc", la contrainte front ne s'applique pas. 

Ci-dessous la contrainte : 
![image|690x276](upload://cMYOBpSkdwZu5wIefepbgtXh3f5.png)

le paramétrage de l'attribut :
![image|690x423](upload://bOg3KMCW2jEcnYW8i6ganYowXx0.png)
le résultat : 
![image|690x108](upload://3d174yC3ysfEFfv1cvQwQhmlU5J.png)

Quand je repasse en présentation "Document simple avec une icone en liste", cela fonctionne : 
![image|690x62](upload://2cws9JAdwailuKgWi6SzDrE5UcZ.png)


merci pour votre aide, 

[Platform]
Status=OK
Version=5.1.9

## Answer
Il manquait un input caché à la zone en lecture, il a été ajouté en v5.1.10.
La contrainte devrait maintenant s'appliquer dans tous les cas pour ce type de champ.
