# CSVLineBasedAdaptateur : Des sauts de lignes présents dans certaines valeurs cassent mon import

**URL:** https://community.simplicite.io/t/9598

## Question
Bonjour, 

Je suis en train de créer un adaptateur CSV. (je suis obligé car un fichier va créer plusieurs objets et les lier entre eux).
Mon fichier CSV a pour séparateur la virgule et pour quote ". Je les ai bien paramétré avec setSeparator(',') et setQuote(' " ').
Cependant, certaines valeurs, du texte entre quote, contiennent des sauts de lignes. Ils devraient être ignoré car entre quote mais ce n'est pas le cas. Lorsque je log chaque ligne avec :
 appendLog("Processing line " + n + " = " + String.join(String.valueOf(getSeparator()), values));

Je vois bien que chaque retour à la ligne dans la valeur appel une nouvelle fois processValues.

Comment remédier à cela ?

## Answer
J'ai trouvé la solution tout seul, il ne faut pas utiliser cette classe mais plutôt ApacheCommonsCSVAdapter. Ce parser gère les sauts de ligne au sein d'un record et le fonctionnement reste le même je traite ligne par ligne.
