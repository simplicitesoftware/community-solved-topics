# Lien entre applicatif et le serveur physique

**URL:** https://community.simplicite.io/t/10357

## Question
Bonjour, 
Je souhaiterais savoir si il est possible via l'applicatif de lancer un script .sh situé sur le même serveur ? 
Dans l'optique de pouvoir lancer des dumps de donné juste en lançant une procédure via le front applicatif.
J'ai cherché via les cron mais j'ai pas trouvé de moyen de lancé un script.
Je suis en version 5.3.53.

Merci d'avance

## Answer
Bonjour,

Il est **fortement déconseillé** de réaliser des dump sans arrêter le serveur car cela peut facilement mener à des erreurs d'intégrité de vos données (modification de données pendant la réalisation du dump), et l'**exécution de scripts par l'applicatif est contraire aux bonnes pratiques**.

Si on parle de réaliser des sauvegardes, comme pour l'immense majorité des besoins nécessitant un script externe, la préconisation est de faire lancer ces scripts par le planificateur CRON du système, et non par Simplicité. 

Quel est exactement votre besoin?

*Pour répondre tout de même à la question, cela est possible en pratique, via la mise en place d'une tâche cron Simplicité, appelant une action, appelant elle-même une méthode Java exécutant une commande shell.* 

> PS: Votre révision 5.3.53 de la v5 date d’il y a 9 mois (octobre 2024) et est en retard de 20 révisions et d’environs 400 commits vs la révision de maintenance actuelle de la v5 (5.3.73 de fin juin 2025). Nous ne pouvons pas assurer de support correctement si vous ne vous maintenez pas à jour plus régulièrement
