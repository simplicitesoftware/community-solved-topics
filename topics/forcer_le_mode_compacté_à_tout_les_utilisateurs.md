# Forcer le mode compacté à tout les utilisateurs

**URL:** https://community.simplicite.io/t/6004

## Question
Bonjour, 

Nous avons rencontré un problème lors de nos développement au niveau d'une icone cliquable. 

Le comportement que nous avons remarqué est un "scintillement" au dessus de cette icône. 
L'icône en question : 
![image|556x205](upload://2YI1UnqZLca79siSQTmiHxm26fX.png)
Ce que nous entendons par "scintillement" est le fait que lors du survol de l'icone la tooltip et le curseur oscille rapidement entre plusieurs mode d'affichage ce qui rend complexe le clique sur cet icone. 
![image|330x159](upload://rZeKZLce2rTyI89olXN1rGqEm76.png)
voici une capture d'écran essayant d'imager le problème  qui est compliqué a montrer en une unique  image. 

Apres quelques recherches de notre coté nous nous sommes rendu compte que ce "scintillement" n'apparaissait plus lorsque l'on passe notre interface en mode compacté et le problème interviens de nouveau lorsque nous remettons l'interface en mode étendu. 
![image|452x223](upload://9ylbCJDsYD7uCBI9bYTj7WhxQEj.png)

Ne sachant pas ce qu'implique les deux modes d'affichages (étendu et compacté) nous souhaiterions savoir s'il existait un moyen de forcer l'affichage en mode compacté à tout les utilisateurs de notre application pour éviter ce scintillement au niveau de notre icone? Et ainsi rendre plus accessible le clique sur cette dernière.


Cordialement, 
Mathilde

## Answer
Ca avait été backporté dans le cadre de la 5.1.58 releasée le 12/03

Mais de toute façon la  révision actuelle est la 5.1.59 releasée le 24/03 (et une 5.1.60 va arriver bientôt pour un fix de sécurité).
